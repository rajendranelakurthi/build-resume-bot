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
    assert module.resolve_person_id("Vikram", "devops-cloud") == "vikram-bathala"
    assert module.resolve_person_id("Vikram", "mech") == "vikram-bathala-mech"


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
