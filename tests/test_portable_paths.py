"""Keep machine-specific paths out of repository instructions and source files."""
from pathlib import Path
import re


def test_source_and_documentation_use_portable_paths() -> None:
    root = Path(__file__).resolve().parents[1]
    patterns = ("*.md", "src/**/*.py", "plugins/**/*.py", "plugins/**/*.md", "plugins/**/*.json", "tests/**/*.py")
    paths = {path for pattern in patterns for path in root.glob(pattern)}
    machine_path = re.compile(r"(?<![A-Za-z0-9])[A-Za-z]:[\\/]|/(?:Users|home)/[^/\s]+/")
    violations = []
    for path in sorted(paths):
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if machine_path.search(line):
                violations.append(f"{path.relative_to(root)}:{number}")
    assert not violations, "Machine-specific paths: " + ", ".join(violations)
