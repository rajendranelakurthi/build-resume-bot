"""Promote an explicitly approved structured resume to both repository bases."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from plugin_core import BundledJsonResumeStore


def update_base(source: Path, repo_root: Path) -> None:
    raw = json.loads(source.read_text(encoding="utf-8"))
    if raw.get("person_id") != "rajendra-prasad-n":
        raise ValueError("Only Rajendra's base is supported")
    # Validate the complete schema before writing either base.
    BundledJsonResumeStore(source.parent, repo_root / "plugins/resume-creator-plugin/assets/static").load_person(source.stem)
    raw["certification_badges_image"] = "assets/rajendra-certifications.svg"
    content = json.dumps(raw, indent=2) + "\n"
    for target in (repo_root / "resume_data/people/rajendra-prasad-n.json",
                   repo_root / "plugins/resume-creator-plugin/assets/people/rajendra-prasad-n.json"):
        target.write_text(content, encoding="utf-8")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", required=True, type=Path)
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[3])
    args = parser.parse_args()
    update_base(args.profile, args.repo_root)
