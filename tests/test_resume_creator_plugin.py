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


def test_export_html_to_pdf_has_mac_browser_candidates() -> None:
    module = _load_module("export_html_to_pdf", "export_html_to_pdf.py")
    candidates = {str(path).replace("\\", "/") for path in module.BROWSER_CANDIDATES}

    assert "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" in candidates
    assert "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge" in candidates


def test_azure_route_preserves_confirmed_content_and_identity() -> None:
    from dataclasses import replace
    core = _load_module("plugin_core_azure", "plugin_core.py")
    assets = PLUGIN_SCRIPTS.parent / "assets"
    profile = core.BundledJsonResumeStore(assets / "people", assets / "static").load_person("rajendra-prasad-n")
    profile = replace(profile, email="contact@example.com", headline="Explicit title")
    for jd in ("AWS Python Bicep certificates", "AWS GCP GitLab", "Liquibase Snowflake GitHub Azure DevOps Terraform"):
        result, _ = core.tailor_profile(profile, jd)
        assert result.email == profile.email and result.headline == profile.headline
        assert result.summary_html == profile.summary_html
        assert result.certifications == profile.certifications
        for old, new in zip(profile.experience, result.experience):
            assert (new.company, new.title, new.date_range) == (old.company, old.title, old.date_range)
            assert set(new.impact) == set(old.impact)
            assert new.skills_used == old.skills_used
        assert "AWS" in result.summary_html and "GCP" not in result.summary_html
    _, matched = core.tailor_profile(profile, "AWS Python Bicep unverified-tool")
    assert all(term in matched for term in ("aws", "python", "bicep"))
    assert "unverified-tool" not in matched


def test_promote_profile_updates_both_bases(tmp_path: Path) -> None:
    import json
    module = _load_module("update_base_profile_test", "update_base_profile.py")
    source = PLUGIN_SCRIPTS.parent / "assets/variants/rajendra-azure-dataops.json"
    for parent in (tmp_path / "resume_data/people", tmp_path / "plugins/resume-creator-plugin/assets/people"):
        parent.mkdir(parents=True)
    module.update_base(source, tmp_path)
    primary = json.loads((tmp_path / "resume_data/people/rajendra-prasad-n.json").read_text())
    bundled = json.loads((tmp_path / "plugins/resume-creator-plugin/assets/people/rajendra-prasad-n.json").read_text())
    assert primary == bundled
    assert primary["email"] == "rajendran.scm@gmail.com"
    assert primary["certification_badges_image"] == "assets/rajendra-certifications.svg"


def test_azure_domain_and_legacy_alias_render_all_levels(tmp_path, monkeypatch) -> None:
    import json
    import pytest
    module = _load_module("run_resume_request_azure", "run_resume_request.py")
    def fake_export(html, pdf):
        assert html.exists()
        pdf.write_bytes(b"test-pdf")
    monkeypatch.setattr(module, "export_html_to_pdf", fake_export)
    for domain in ("Azure-devops", "azure-devops", "devops-cloud"):
        args = module.build_parser().parse_args(["--person", "Rajendra", "--domain", domain, "--jd-text", "AWS Bicep"])
        assert args.domain == "azure-devops"
        for level in ("Base", "Tailored", "Optimized", "Aggressive"):
            result = module.render_request(module.ResumeRequest("Rajendra", domain, level, "AWS Bicep Python", tmp_path / domain / level, PLUGIN_SCRIPTS.parent))
            assert result["domain"] == "azure-devops"
            assert "-azure-devops-" in result["pdf_path"]
            profile = json.loads(Path(result["profile_path"]).read_text())
            assert "Azure DevOps" in profile["headline"]
            assert "AWS" in profile["summary_html"] and "Bicep" in profile["summary_html"]
            assert Path(result["pdf_path"]).exists()
    with pytest.raises(ValueError):
        module.normalize_domain("aws-devops")
    with pytest.raises(SystemExit):
        module.build_parser().parse_args(["--person", "Rajendra", "--domain", "devsecops"])


def test_azure_sources_and_templates_are_synchronized() -> None:
    import json
    repo = PLUGIN_SCRIPTS.parents[2]
    bundled = json.loads((PLUGIN_SCRIPTS.parent / "assets/people/rajendra-prasad-n.json").read_text())
    primary = json.loads((repo / "resume_data/people/rajendra-prasad-n.json").read_text())
    assert bundled == primary
    assert (repo / "templates/base_resume.html").read_text() == (PLUGIN_SCRIPTS.parent / "assets/templates/base_resume.html").read_text()
    assert "AWS Certified Solutions Architect - Associate" in primary["certifications"]
    assert "AWS" in primary["experience"][0]["skills_used"]
    assert "SSIS" not in json.dumps({k: v for k, v in primary.items() if k != "notes"})
    assert primary["headline"] == "Lead Azure DevOps Engineer | AWS & Bicep"
