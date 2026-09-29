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


def test_dataops_route_preserves_identity_and_azure_content() -> None:
    from dataclasses import replace
    core = _load_module("plugin_core_dataops", "plugin_core.py")
    assets = PLUGIN_SCRIPTS.parent / "assets"
    profile = core.BundledJsonResumeStore(assets / "people", assets / "static").load_person("rajendra-prasad-n")
    profile = replace(profile, email="contact@example.com", headline="Explicit title")
    result, _ = core.tailor_profile(profile, "Liquibase Snowflake GitHub Actions Azure DevOps Terraform")
    assert result.email == "contact@example.com"
    assert result.headline == "Explicit title"
    assert [e.date_range for e in result.experience] == [e.date_range for e in profile.experience]
    for job in result.experience:
        content = " ".join(job.impact)
        assert all(term in content for term in ("Azure", "Liquibase", "Snowflake"))
        assert "CloudWatch" not in content and "EKS" not in content


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
