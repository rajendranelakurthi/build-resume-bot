from __future__ import annotations

import argparse
from pathlib import Path
import re

from resume_agents.service import ResumeAgentService


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Multi-person resume agent CLI")
    parser.add_argument(
        "--data-root",
        default=str(Path.cwd() / "resume_data"),
        help="Path to the resume data directory",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("list-people", help="List known people")

    request_parser = subparsers.add_parser("request", help="Run an agent request for one person")
    request_parser.add_argument("--person", required=True, help="Person identifier")
    request_parser.add_argument("--message", required=True, help="Natural language request")

    render_parser = subparsers.add_parser("render-html", help="Render HTML resume for one person")
    render_parser.add_argument("--person", required=True, help="Person identifier")
    render_parser.add_argument("--output", required=True, help="Output HTML file path")

    tailor_parser = subparsers.add_parser("tailor-jd", help="Tailor a resume to a job description and commit it on a branch")
    tailor_parser.add_argument("--person", required=True, help="Person identifier")
    tailor_parser.add_argument("--jd-text", help="Raw job description text")
    tailor_parser.add_argument("--jd-file", help="Path to a text file containing the job description")
    tailor_parser.add_argument("--branch", help="Target branch name")
    tailor_parser.add_argument("--push", action="store_true", help="Push branch to origin after commit")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    service = ResumeAgentService(Path(args.data_root))

    if args.command == "list-people":
        for person_id in service.list_people():
            print(person_id)
        return

    if args.command == "render-html":
        html = service.render_resume_html(args.person)
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(html, encoding="utf-8")
        print(output_path)
        return

    if args.command == "tailor-jd":
        job_description = _resolve_job_description(args.jd_text, args.jd_file)
        branch_name = args.branch or _branch_name(args.person, job_description)
        result = service.tailor_resume_to_jd(
            args.person,
            job_description,
            branch_name,
            push=args.push,
        )
        print(f"person_id: {result.person_id}")
        print(f"branch: {result.branch_name}")
        print(f"output: {result.output_path}")
        print(f"commit: {result.commit_sha}")
        print(f"pushed: {result.pushed}")
        print(f"matched_keywords: {', '.join(result.matched_keywords)}")
        return

    result = service.handle_request(args.person, args.message)
    print(f"person_id: {result.person_id}")
    print(f"route: {result.route}")
    print(f"request: {result.user_request}")
    print("")
    for response in result.responses:
        print(f"[{response.agent_name}]")
        print(response.content)
        print("")

def _resolve_job_description(jd_text: str | None, jd_file: str | None) -> str:
    if jd_text:
        return jd_text
    if jd_file:
        return Path(jd_file).read_text(encoding="utf-8")
    raise ValueError("Provide either --jd-text or --jd-file.")


def _branch_name(person_id: str, job_description: str) -> str:
    company = _extract_company_name(job_description)
    if company:
        return f"codex/{person_id}-{_slugify(company)}"

    role = _extract_role_name(job_description)
    if role:
        return f"codex/{person_id}-{_slugify(role)}"

    return f"codex/{person_id}-job-description"


def _extract_company_name(job_description: str) -> str | None:
    patterns = [
        r"(?im)^\s*company\s*:\s*(.+)$",
        r"(?im)^\s*client\s*:\s*(.+)$",
        r"(?im)^\s*employer\s*:\s*(.+)$",
    ]
    for pattern in patterns:
        match = re.search(pattern, job_description)
        if match:
            return match.group(1).strip()
    return None


def _extract_role_name(job_description: str) -> str | None:
    match = re.search(
        r"(?i)seeking\s+(?:a|an)\s+(?:highly\s+motivated\s+|experienced\s+|skilled\s+)?([a-z0-9 /&-]{3,80}?)(?:\s+to|\s+who|\s*\.)",
        job_description,
    )
    if match:
        return match.group(1).strip()

    match = re.search(r"(?im)^\s*title\s*:\s*(.+)$", job_description)
    if match:
        return match.group(1).strip()
    return None


def _slugify(value: str) -> str:
    return "-".join(re.findall(r"[A-Za-z0-9]+", value.lower()))


if __name__ == "__main__":
    main()
