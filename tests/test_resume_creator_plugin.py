from __future__ import annotations

import importlib.util
from pathlib import Path
import sys
import zipfile


PLUGIN_SCRIPTS = Path(__file__).resolve().parents[1] / "plugins" / "resume-creator-plugin" / "scripts"


def _load_module(module_name: str, filename: str):
    path = PLUGIN_SCRIPTS / filename
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec is not None and spec.loader is not None
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


def test_resolve_person_id_supports_expected_domains() -> None:
    module = _load_module("run_resume_request", "run_resume_request.py")

    assert module.resolve_person_id("Rajendra", "devops-cloud") == "rajendra-prasad-n"


def test_normalize_level_canonicalizes_values() -> None:
    module = _load_module("run_resume_request_levels", "run_resume_request.py")

    assert module.normalize_level("base") == "Base"
    assert module.normalize_level("Tailored") == "Tailored"
    assert module.normalize_level("OPTIMIZED") == "Optimized"
    assert module.normalize_level("aggressive") == "Aggressive"


def test_slugify_falls_back_for_empty_text() -> None:
    module = _load_module("run_resume_request_slug", "run_resume_request.py")

    assert module.slugify("!!!", fallback="sample") == "sample"


def test_package_plugin_creates_zip(tmp_path: Path) -> None:
    module = _load_module("package_plugin", "package_plugin.py")
    plugin_root = Path(__file__).resolve().parents[1] / "plugins" / "resume-creator-plugin"
    output_zip = tmp_path / "resume-creator-plugin.zip"

    created = module.package_plugin(plugin_root, output_zip)

    assert created == output_zip.resolve()
    assert output_zip.exists()
    with zipfile.ZipFile(output_zip) as archive:
        names = archive.namelist()
    assert any(name.endswith(".codex-plugin/plugin.json") for name in names)
    assert any(name.endswith("scripts/run_resume_request.py") for name in names)


def test_default_output_zip_includes_version() -> None:
    module = _load_module("package_plugin_default", "package_plugin.py")
    plugin_root = Path(__file__).resolve().parents[1] / "plugins" / "resume-creator-plugin"

    output = module.default_output_zip(plugin_root)

    assert output.name == "resume-creator-plugin-0.1.0.zip"


def test_browser_discovery_uses_platform_and_environment(tmp_path, monkeypatch) -> None:
    module = _load_module("portable_export", "export_html_to_pdf.py")
    monkeypatch.setattr(module.platform, "system", lambda: "Darwin")
    monkeypatch.setattr(module.Path, "home", lambda: tmp_path)
    candidates = module.browser_candidates()
    assert tmp_path / "Applications/Google Chrome.app/Contents/MacOS/Google Chrome" in candidates
    monkeypatch.setattr(module.platform, "system", lambda: "Windows")
    monkeypatch.setenv("PROGRAMFILES", str(tmp_path / "programs"))
    assert tmp_path / "programs/Google/Chrome/Application/chrome.exe" in module.browser_candidates()
    browser = tmp_path / "browser"
    monkeypatch.setattr(module.shutil, "which", lambda name: str(browser) if name == "chromium" else None)
    assert module.resolve_browser() == browser


def test_aws_aliases_levels_and_output_names(tmp_path, monkeypatch) -> None:
    import json
    import pytest
    module = _load_module("aws_runner", "run_resume_request.py")
    def export(html, pdf):
        assert html.is_file()
        pdf.write_bytes(b"%PDF-1.7\nmock")
    monkeypatch.setattr(module, "export_html_to_pdf", export)
    for domain in ("aws-devops", "AWS DevOps", "devops-cloud"):
        args = module.build_parser().parse_args(["--person", "Rajendra", "--domain", domain])
        assert args.domain == "aws-devops"
        for level in ("Base", "Tailored", "Optimized", "Aggressive"):
            result = module.render_request(module.ResumeRequest(
                "Rajendra", domain, level, "S3 VPC IAM Terraform", tmp_path / domain / level,
                PLUGIN_SCRIPTS.parent, "Rajendra-Lead-AWS-DevOps"))
            assert result["domain"] == "aws-devops"
            assert Path(result["pdf_path"]).name == "Rajendra-Lead-AWS-DevOps.pdf"
            profile = json.loads(Path(result["profile_path"]).read_text())
            assert profile["headline"].startswith("Lead AWS DevOps Engineer")
            assert "Amazon S3" in profile["summary_html"]
            if level != "Base":
                assert "s3" in result["matched_keywords"]
    for invalid in ("azure-devops", "gcp-devops", "../aws"):
        with pytest.raises(ValueError):
            module.normalize_domain(invalid)
    for invalid in ("../escape", "resume.pdf", "/tmp/resume", "", "a/b"):
        with pytest.raises(ValueError):
            module.validate_output_name(invalid)


def test_aws_tailoring_preserves_evidence_and_assets() -> None:
    import json
    from dataclasses import replace
    core = _load_module("aws_core", "plugin_core.py")
    root = PLUGIN_SCRIPTS.parent
    repo = PLUGIN_SCRIPTS.parents[2]
    raw = json.loads((root / "assets/people/rajendra-prasad-n.json").read_text())
    assert raw == json.loads((repo / "resume_data/people/rajendra-prasad-n.json").read_text())
    assert (root / "assets/templates/base_resume.html").read_text() == (repo / "templates/base_resume.html").read_text()
    profile = core.BundledJsonResumeStore(root / "assets/people", root / "assets/static").load_person("rajendra-prasad-n")
    profile = replace(profile, email="custom@example.com")
    for jd in ("AWS S3 VPC IAM", "Azure DevOps GitHub Actions Terraform", "GitLab unknown-security-tool"):
        result, _ = core.tailor_profile(profile, jd)
        assert result.email == profile.email
        assert result.headline == profile.headline
        assert result.summary_html == profile.summary_html
        assert result.certifications == profile.certifications
        for before, after in zip(profile.experience, result.experience):
            assert (before.company, before.title, before.date_range) == (after.company, after.title, after.date_range)
            assert set(before.impact) == set(after.impact)
    _, matched = core.tailor_profile(profile, "S3. Security. unknown-security-tool")
    assert "s3" in matched and "security" in matched and "unknown-security-tool" not in matched


def test_export_rejects_missing_source_and_preserves_previous_pdf(tmp_path, monkeypatch) -> None:
    import pytest
    module = _load_module("aws_export_checks", "export_html_to_pdf.py")
    source, output = tmp_path / "resume.html", tmp_path / "resume.pdf"
    output.write_bytes(b"%PDF-old")
    calls = []
    monkeypatch.setattr(module.subprocess, "run", lambda *args, **kwargs: calls.append(args))
    with pytest.raises(FileNotFoundError):
        module.export_html_to_pdf(source, output, browser_path=Path("browser"))
    assert not calls and output.read_bytes() == b"%PDF-old"
    source.write_text("<html>Resume</html>")
    with pytest.raises(RuntimeError, match="did not create"):
        module.export_html_to_pdf(source, output, browser_path=Path("browser"))
    assert output.read_bytes() == b"%PDF-old"
    def browser_run(command, **kwargs):
        target = Path(next(arg.split("=", 1)[1] for arg in command if arg.startswith("--print-to-pdf=")))
        target.write_bytes(b"%PDF-1.7\nnew")
    monkeypatch.setattr(module.subprocess, "run", browser_run)
    assert module.export_html_to_pdf(source, output, browser_path=Path("browser")) == output.resolve()
    assert output.read_bytes() == b"%PDF-1.7\nnew"
    assert not list(tmp_path.glob("resume-export-*"))


def test_saved_paths_are_relative_and_assets_move_with_output(tmp_path, monkeypatch) -> None:
    import json
    import shutil
    module = _load_module("portable_runner", "run_resume_request.py")
    monkeypatch.chdir(tmp_path)
    def export(html, pdf):
        pdf.write_bytes(b"%PDF-1.7\nmock")
    monkeypatch.setattr(module, "export_html_to_pdf", export)
    result = module.render_request(module.ResumeRequest(
        "Rajendra", "aws-devops", "Aggressive", "AWS S3 IAM", Path("output"),
        PLUGIN_SCRIPTS.parent, "Portable"))
    for key in ("html_path", "pdf_path", "profile_path", "manifest_path"):
        assert not Path(result[key]).is_absolute()
        assert Path(result[key]).exists()
    assert result["paths_relative_to"] == "invocation_directory"
    profile = json.loads(Path(result["profile_path"]).read_text())
    assert profile["certification_badges_image"].startswith("assets/")
    assert "file:///" not in json.dumps(profile)
    shutil.copytree("output", "moved")
    assert (Path("moved") / profile["certification_badges_image"]).is_file()
    manifest_text = Path(result["manifest_path"]).read_text()
    assert str(tmp_path) not in manifest_text


def test_explicit_profile_variant_preserves_default_base(tmp_path, monkeypatch) -> None:
    import json
    import pytest
    module = _load_module("variant_runner", "run_resume_request.py")
    root = PLUGIN_SCRIPTS.parent
    base = root / "assets/people/rajendra-prasad-n.json"
    original = base.read_bytes()
    variant = root / "assets/variants/rajendra-aws-python-kubernetes.json"
    monkeypatch.setattr(module, "export_html_to_pdf", lambda html, pdf: pdf.write_bytes(b"%PDF-mock"))
    request = module.ResumeRequest("Rajendra", "aws-devops", "Aggressive", "Python Kubernetes CI/CD", tmp_path,
                                   root, "Python-Resume", variant)
    result = module.render_request(request)
    data = json.loads(Path(result["profile_path"]).read_text())
    assert "Python, Kubernetes" in data["headline"]
    assert "13+ years" in data["summary_html"]
    assert data["experience"][-1]["project"] == "Expedia Travel Portal"
    assert "12+" not in data["summary_html"]
    assert base.read_bytes() == original
    wrong = json.loads(variant.read_text())
    wrong["person_id"] = "someone-else"
    incorrect = tmp_path / "incorrect.json"
    incorrect.write_text(json.dumps(wrong))
    request.profile_file = incorrect
    with pytest.raises(ValueError, match="requested person"):
        module.render_request(request)
