from pathlib import Path
root=Path('plugins/resume-creator-plugin')
p=root/'scripts/plugin_core.py';s=p.read_text();a=s.index('def tailor_profile(');b=s.index('def extract_keywords(',a)
s=s[:a]+'''def tailor_profile(profile: PersonProfile, job_description: str) -> tuple[PersonProfile, list[str]]:
    """Rank the authored AWS profile without importing unrelated cloud claims."""
    keywords = extract_keywords(job_description)
    matched = [keyword for keyword in keywords if _profile_contains(profile, keyword)][:10]
    return replace(
        profile,
        achievements=rank_tagged_items(profile.achievements, keywords),
        skill_sections=rank_tagged_items(profile.skill_sections, keywords, content_key="content"),
        experience=[rank_experience(job, keywords) for job in profile.experience],
    ), matched


'''+s[b:];a=s.index('def build_summary(');b=s.index('def rank_tagged_items(',a);s=s[:a]+s[b:];s=s.replace('if len(token) < 3 or token in STOPWORDS:', 'if (len(token) < 3 and token not in {"s3"}) or token in STOPWORDS:');p.write_text(s)
p=Path('src/resume_agents/tailor.py');s=p.read_text();a=s.index('def build_summary(');b=s.index('def rank_tagged_items(',a);s=s[:a]+'''def build_summary(profile: PersonProfile, matched_keywords: list[str], missing_keywords: list[str]) -> str:
    # JD keywords rank approved experience; they are not evidence of new skills.
    return profile.summary_html or f"<strong>{escape(profile.headline)}</strong>"


'''+s[b:];s=s.replace('if len(token) < 3 or token in STOPWORDS:', 'if (len(token) < 3 and token not in {"s3"}) or token in STOPWORDS:');p.write_text(s)
p=root/'scripts/run_resume_request.py';s=p.read_text().replace('from dataclasses import dataclass','from dataclasses import asdict, dataclass').replace('    plugin_root: Path\n','    plugin_root: Path\n    output_name: str | None = None\n')
a=s.index('def resolve_person_id(');b=s.index('def normalize_level(',a);s=s[:a]+'''def normalize_domain(domain: str) -> str:
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


'''+s[b:]
s=s.replace('    person_id = resolve_person_id(request.person, request.domain)','    domain = normalize_domain(request.domain)\n    person_id = resolve_person_id(request.person, domain)')
s=s.replace('    request_slug = slugify(request.jd, fallback=f"{request.person}-{request.domain}")','    request_slug = slugify(request.jd, fallback=f"{request.person}-{domain}")\n    output_name = validate_output_name(request.output_name) if request.output_name else f"{person_id}-{domain}-{level.lower()}-{request_slug}"')
s=s.replace('f"{person_id}-{request.domain}-{level.lower()}-{request_slug}.html"','f"{output_name}.html"')
s=s.replace('    html_path.write_text(renderer.render(output_profile)', '    profile_path = html_path.with_suffix(".profile.json")\n    profile_path.write_text(json.dumps(asdict(output_profile), indent=2) + "\\n", encoding="utf-8")\n    html_path.write_text(renderer.render(output_profile)')
s=s.replace('"domain": request.domain','"domain": domain').replace('        "html_path": str(html_path),','        "profile_path": str(profile_path),\n        "html_path": str(html_path),')
s=s.replace('choices=["devops-cloud"], help="Resume domain routing key"','type=normalize_domain, choices=["aws-devops"], help="AWS DevOps; devops-cloud is an AWS-only alias"')
s=s.replace('default=str(Path.cwd() / "output")','default=str(Path.cwd() / "tailored_resume" / "rajendra-prasad-n")')
s=s.replace('    parser.add_argument(\n        "--plugin-root",','    parser.add_argument("--output-name", type=validate_output_name, help="Optional readable filename stem, without extension")\n    parser.add_argument(\n        "--plugin-root",')
s=s.replace('        plugin_root=Path(args.plugin_root),','        plugin_root=Path(args.plugin_root),\n        output_name=args.output_name,');p.write_text(s)
p=root/'scripts/export_html_to_pdf.py';s=p.read_text().replace('import subprocess','import subprocess\nimport tempfile');a=s.index('    pdf_path.parent.mkdir');b=s.index('\n\n\ndef build_parser',a)
s=s[:a]+'''    if not html_path.is_file():
        raise FileNotFoundError(f"Resume HTML does not exist: {html_path}")
    if html_path == pdf_path:
        raise ValueError("HTML input and PDF output must be different files.")
    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    browser = browser_path or resolve_browser()
    # Export to a fresh temporary file so a stale PDF cannot pass verification.
    with tempfile.TemporaryDirectory(prefix="resume-export-", dir=pdf_path.parent) as directory:
        candidate = Path(directory) / "resume.pdf"
        command = [
            str(browser), "--headless=new", "--disable-gpu",
            "--allow-file-access-from-files", "--no-pdf-header-footer",
            f"--print-to-pdf={candidate}", html_path.as_uri(),
        ]
        subprocess.run(command, check=True, timeout=120)
        if not candidate.is_file():
            raise RuntimeError("Browser did not create a PDF.")
        with candidate.open("rb") as stream:
            if stream.read(5) != b"%PDF-":
                raise RuntimeError("Browser output is not a valid PDF file.")
        candidate.replace(pdf_path)
    return pdf_path
'''+s[b:];p.write_text(s)
