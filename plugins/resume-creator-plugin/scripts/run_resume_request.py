from __future__ import annotations

import argparse
import json
import os
import shutil
from dataclasses import asdict, dataclass
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
    output_name: str | None = None
    profile_file: Path | None = None


def normalize_domain(domain: str) -> str:
    normalized = re.sub(r"[ _]+", "-", domain.strip().lower())
    if normalized in {"aws-devops", "devops-cloud"}:
        return "aws-devops"
    raise ValueError(f"Unsupported domain {domain!r}; this branch supports aws-devops only.")


def resolve_person_id(person: str, domain: str) -> str:
    normalize_domain(domain)
    if person.strip().lower() == "rajendra":
        return "rajendra-prasad-n"
    raise ValueError(f"Unsupported person: {person!r}")


def validate_output_name(name: str) -> str:
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]{0,119}", name):
        raise ValueError("Output name must be a filename stem using letters, numbers, hyphens, or underscores.")
    return name


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

    domain = normalize_domain(request.domain)
    person_id = resolve_person_id(request.person, domain)
    level = normalize_level(request.level)

    if request.profile_file is not None:
        profile_source = request.profile_file
        variant_store = BundledJsonResumeStore(profile_source.parent, assets_root / "static")
        profile = variant_store.load_person(profile_source.stem)
        if profile.person_id != person_id:
            raise ValueError("Selected profile does not belong to the requested person.")
    else:
        profile = store.load_person(person_id)
    matched_keywords: list[str] = []
    if level == "Base":
        output_profile = profile
    else:
        output_profile, matched_keywords = tailor_profile(profile, request.jd)

    request_slug = slugify(request.jd, fallback=f"{request.person}-{domain}")
    output_name = validate_output_name(request.output_name) if request.output_name else f"{person_id}-{domain}-{level.lower()}-{request_slug}"
    output_dir = request.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    html_path = output_dir / f"{output_name}.html"
    pdf_path = html_path.with_suffix(".pdf")
    manifest_path = html_path.with_suffix(".json")

    profile_path = html_path.with_suffix(".profile.json")
    profile_path.write_text(json.dumps(asdict(output_profile), indent=2) + "\n", encoding="utf-8")
    # Keep emitted HTML/profile asset references portable alongside the output.
    references = [output_profile.certification_badges_image] + [item.logo_image for item in output_profile.education]
    for reference in references:
        if not reference.startswith("assets/"):
            continue
        source = assets_root / "static" / Path(reference).name
        target = output_dir / reference
        if source.is_file() and source.resolve() != target.resolve():
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
    html_path.write_text(renderer.render(output_profile), encoding="utf-8")
    export_html_to_pdf(html_path, pdf_path)

    manifest = {
        "person": request.person,
        "person_id": person_id,
        "domain": domain,
        "level": level,
        "matched_keywords": matched_keywords,
        "paths_relative_to": "invocation_directory",
        "profile_path": Path(os.path.relpath(profile_path, Path.cwd())).as_posix(),
        "html_path": Path(os.path.relpath(html_path, Path.cwd())).as_posix(),
        "pdf_path": Path(os.path.relpath(pdf_path, Path.cwd())).as_posix(),
        "manifest_path": Path(os.path.relpath(manifest_path, Path.cwd())).as_posix(),
    }
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    return manifest


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate HTML and PDF resume artifacts from plugin-style inputs.")
    parser.add_argument("--person", required=True, help="Person name, for example Rajendra")
    parser.add_argument("--domain", required=True, type=normalize_domain, choices=["aws-devops"], help="AWS DevOps; devops-cloud is an AWS-only alias")
    parser.add_argument("--level", default="Tailored", help="Tailoring level: Base, Tailored, Optimized, or Aggressive")
    parser.add_argument("--jd-text", help="Raw job description text")
    parser.add_argument("--jd-file", help="Path to a text file containing the job description")
    parser.add_argument(
        "--output-dir",
        default="tailored_resume/rajendra-prasad-n",
        help="Directory where HTML, PDF, and manifest files will be written",
    )
    parser.add_argument("--profile-file", type=Path, help="Optional approved structured profile variant; preserves the default base")
    parser.add_argument("--output-name", type=validate_output_name, help="Optional readable filename stem, without extension")
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
        output_name=args.output_name,
        profile_file=args.profile_file,
    )
    manifest = render_request(request)
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
