from __future__ import annotations

from pathlib import Path

from resume_agents.agents.router import detect_route, run_agents
from resume_agents.git_ops import commit_file, ensure_branch, has_remote, push_branch
from resume_agents.models import OrchestrationResult, TailoredResumeResult
from resume_agents.renderers.html_resume import HtmlResumeRenderer
from resume_agents.storage.json_store import JsonResumeStore
from resume_agents.tailor import tailor_profile


class ResumeAgentService:
    def __init__(self, data_root: Path, repo_root: Path | None = None) -> None:
        self.store = JsonResumeStore(data_root)
        self.repo_root = repo_root or Path(__file__).resolve().parents[2]
        self.renderer = HtmlResumeRenderer(self.repo_root / "templates" / "base_resume.html")

    def list_people(self) -> list[str]:
        return self.store.list_people()

    def handle_request(self, person_id: str, user_request: str) -> OrchestrationResult:
        profile = self.store.load_person(person_id)
        route = detect_route(user_request)
        responses = run_agents(profile, user_request, route)
        return OrchestrationResult(
            person_id=person_id,
            user_request=user_request,
            route=route,
            responses=responses,
        )

    def render_resume_html(self, person_id: str) -> str:
        profile = self.store.load_person(person_id)
        return self.renderer.render(profile)

    def tailor_resume_to_jd(
        self,
        person_id: str,
        job_description: str,
        branch_name: str,
        *,
        push: bool = False,
    ) -> TailoredResumeResult:
        profile = self.store.load_person(person_id)
        tailored_profile, matched_keywords = tailor_profile(profile, job_description)

        ensure_branch(self.repo_root, branch_name)

        output_dir = self.repo_root / "tailored_resumes" / person_id
        output_dir.mkdir(parents=True, exist_ok=True)
        output_path = output_dir / f"{branch_name.replace('/', '_')}.html"
        output_path.write_text(self.renderer.render(tailored_profile), encoding="utf-8")

        commit_sha = commit_file(
            self.repo_root,
            output_path,
            f"Tailor {person_id} resume for JD on {branch_name}",
        )

        pushed = False
        if push:
            if not has_remote(self.repo_root):
                raise RuntimeError("Cannot push because no Git remote is configured.")
            push_branch(self.repo_root, branch_name)
            pushed = True

        return TailoredResumeResult(
            person_id=person_id,
            branch_name=branch_name,
            output_path=str(output_path),
            commit_sha=commit_sha,
            pushed=pushed,
            matched_keywords=matched_keywords,
        )
