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

    for domain in ("platform-engineer", "Platform-Engineer", "platform engineer", "platform_engineer", "devops-cloud", "devops-sre"):
        assert module.resolve_person_id("Rajendra", domain) == "rajendra-prasad-n"
        assert module.normalize_domain(domain) == "platform-engineer"


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


def test_rajendra_header_survives_all_tailoring_routes() -> None:
    from dataclasses import replace

    core = _load_module("plugin_core_header_test", "plugin_core.py")
    assets = PLUGIN_SCRIPTS.parent / "assets"
    profile = core.BundledJsonResumeStore(assets / "people", assets / "static").load_person("rajendra-prasad-n")
    assert profile.headline == "Lead Platform Engineer | Developer Experience | Cloud Infrastructure"
    for jd in (
        "CloudBees Jenkins Python AWS",
        "GitLab CI Terraform",
        "lead aws devops engineer codepipeline cloudformation",
        "release engineering branching strategies jenkins",
        "observability gpu hpc",
        "azure devops github actions terraform",
    ):
        tailored, _ = core.tailor_profile(profile, jd)
        assert tailored.headline == profile.headline
        assert tailored.page_title == profile.page_title
    explicitly_changed = replace(profile, headline="User-approved new designation")
    tailored, _ = core.tailor_profile(explicitly_changed, "GitLab")
    assert tailored.headline == explicitly_changed.headline


def test_platform_request_defaults_and_preserves_summary_history(tmp_path):
    from unittest.mock import patch
    import json
    module = _load_module("run_platform_request", "run_resume_request.py")
    args = module.build_parser().parse_args(["--person", "Rajendra", "--jd-text", "GitLab Terraform Kubernetes"])
    assert args.domain == "platform-engineer"
    core = _load_module("platform_core_test", "plugin_core.py")
    assets = PLUGIN_SCRIPTS.parent / "assets"
    profile = core.BundledJsonResumeStore(assets / "people", assets / "static").load_person("rajendra-prasad-n")
    for jd in ("GitLab", "lead aws devops engineer codepipeline cloudformation", "release engineering branching strategies jenkins", "observability gpu hpc", "azure devops github actions terraform"):
        tailored, _ = core.tailor_profile(profile, jd)
        assert tailored.summary_html == profile.summary_html
        assert [(j.title, len(j.impact)) for j in tailored.experience] == [(j.title, len(j.impact)) for j in profile.experience]
    with patch.object(module, "export_html_to_pdf"):
        result = module.render_request(module.ResumeRequest("Rajendra", "Platform-Engineer", "Aggressive", "Terraform Kubernetes", tmp_path, assets.parent))
    assert result["domain"] == "platform-engineer"
    assert "platform-engineer" in Path(result["html_path"]).name
    assert json.loads(Path(result["profile_path"]).read_text())["headline"] == profile.headline


def test_project_minimum_rejects_short_variants():
    from dataclasses import replace
    import pytest
    module = _load_module("run_min_project_test", "run_resume_request.py")
    core = _load_module("core_min_project_test", "plugin_core.py")
    assets = PLUGIN_SCRIPTS.parent / "assets"
    profile = core.BundledJsonResumeStore(assets / "people", assets / "static").load_person("rajendra-prasad-n")
    module.validate_project_bullets(profile)
    short = replace(profile, experience=[replace(profile.experience[0], impact=profile.experience[0].impact[:9])])
    with pytest.raises(ValueError, match="at least 10"):
        module.validate_project_bullets(short)
