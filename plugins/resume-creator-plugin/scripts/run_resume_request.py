from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
import re
import sys

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from export_html_to_pdf import export_html_to_pdf
from plugin_core import BundledHtmlResumeRenderer, BundledJsonResumeStore, tailor_profile


@dataclass(slots=True)
class ResumeRequest:
    person: str
    domain: str
    level: str
    jd: str
    output_dir: Path
    plugin_root: Path


def resolve_person_id(person: str, domain: str) -> str:
    normalized_person = person.strip().lower()
    normalized_domain = domain.strip().lower()
    mapping = {
        ("rajendra", "devops-cloud"): "rajendra-prasad-n",
        ("vikram", "devops-cloud"): "vikram-bathala",
        ("vikram", "mech"): "vikram-bathala-mech",
    }
    try:
        return mapping[(normalized_person, normalized_domain)]
    except KeyError as exc:
        raise ValueError(
            f"Unsupported person/domain combination: person={person!r}, domain={domain!r}"
        ) from exc


def normalize_level(level: str) -> str:
    normalized = level.strip().lower()
    allowed = {
        "base": "Base",
        "tailored": "Tailored",
        "optimized": "Optimized",
        "aggressive": "Aggressive",
    }
    try:
        return allowed[normalized]
    except KeyError as exc:
        raise ValueError(f"Unsupported level: {level!r}") from exc


def slugify(text: str, *, fallback: str = "request") -> str:
    tokens = re.findall(r"[A-Za-z0-9]+", text.lower())
    return "-".join(tokens[:8]) or fallback


def render_request(request: ResumeRequest) -> dict[str, object]:
    assets_root = request.plugin_root / "assets"
    store = BundledJsonResumeStore(assets_root / "people", assets_root / "static")
    renderer = BundledHtmlResumeRenderer(assets_root / "templates" / "base_resume.html")

    person_id = resolve_person_id(request.person, request.domain)
    level = normalize_level(request.level)

    profile = store.load_person(person_id)
    matched_keywords: list[str] = []
    if level == "Base":
        output_profile = profile
    else:
        output_profile, matched_keywords = tailor_profile(profile, request.jd)

    request_slug = slugify(request.jd, fallback=f"{request.person}-{request.domain}")
    output_dir = request.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    html_path = output_dir / f"{person_id}-{request.domain}-{level.lower()}-{request_slug}.html"
    pdf_path = html_path.with_suffix(".pdf")
    manifest_path = html_path.with_suffix(".json")

    html_path.write_text(renderer.render(output_profile), encoding="utf-8")
    export_html_to_pdf(html_path, pdf_path)

    manifest = {
        "person": request.person,
        "person_id": person_id,
        "domain": request.domain,
        "level": level,
        "matched_keywords": matched_keywords,
        "html_path": str(html_path),
        "pdf_path": str(pdf_path),
        "manifest_path": str(manifest_path),
    }
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    return manifest


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate HTML and PDF resume artifacts from plugin-style inputs.")
    parser.add_argument("--person", required=True, help="Person name, for example Rajendra or Vikram")
    parser.add_argument("--domain", required=True, choices=["mech", "devops-cloud"], help="Resume domain routing key")
    parser.add_argument("--level", default="Tailored", help="Tailoring level: Base, Tailored, Optimized, or Aggressive")
    parser.add_argument("--jd-text", help="Raw job description text")
    parser.add_argument("--jd-file", help="Path to a text file containing the job description")
    parser.add_argument(
        "--output-dir",
        default=str(Path.cwd() / "output"),
        help="Directory where HTML, PDF, and manifest files will be written",
    )
    parser.add_argument(
        "--plugin-root",
        default=str(Path(__file__).resolve().parents[1]),
        help="Plugin root containing bundled assets and metadata",
    )
    return parser


def resolve_jd_text(raw_text: str | None, jd_file: str | None) -> str:
    if raw_text:
        return raw_text
    if jd_file:
        return Path(jd_file).read_text(encoding="utf-8")
    raise ValueError("Provide either --jd-text or --jd-file.")


def main() -> None:
    args = build_parser().parse_args()
    request = ResumeRequest(
        person=args.person,
        domain=args.domain,
        level=args.level,
        jd=resolve_jd_text(args.jd_text, args.jd_file),
        output_dir=Path(args.output_dir),
        plugin_root=Path(args.plugin_root),
    )
    manifest = render_request(request)
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
