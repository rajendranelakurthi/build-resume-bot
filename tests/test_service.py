import tempfile
from pathlib import Path
import subprocess
import shutil

from resume_agents.cli import _branch_name
from resume_agents.service import ResumeAgentService
from resume_agents.tailor import extract_keywords, tailor_profile


def test_list_people() -> None:
    service = ResumeAgentService(Path("resume_data"))
    assert "vikram-bathala" in service.list_people()
    assert "rajendra-prasad-n" in service.list_people()


def test_tailor_request_routes_and_returns_agents() -> None:
    service = ResumeAgentService(Path("resume_data"))
    result = service.handle_request(
        "vikram-bathala",
        "Tailor my resume for a lead platform engineering role.",
    )
    assert result.route == "tailor"
    assert any(item.agent_name == "resume-tailor" for item in result.responses)


def test_render_html_uses_template() -> None:
    service = ResumeAgentService(Path("resume_data"))
    html = service.render_resume_html("vikram-bathala")
    assert "VIKRAM BATHALA" in html
    assert "Key Platform Achievements" in html


def test_render_html_supports_extended_contact_lines_and_optional_certifications() -> None:
    service = ResumeAgentService(Path("resume_data"))
    html = service.render_resume_html("rajendra-prasad-n")
    assert "linkedin.com/in/rajendranelakurthi" in html
    assert "rajendranelakurthi.github.io" in html
    assert "Certifications" in html
    assert "certifications-grid" in html
    assert "GitLab Certified Associate" in html
    assert "Project:</strong> CDO (Chief Data Office)" in html
    assert "Skills Used:</strong> AWS, AWS CodePipeline, PowerShell" in html
    assert "Directed end-to-end release management across multiple engineering teams by aligning schedules, dependencies, change windows, and risk mitigation plans." in html


def test_rajendra_experience_sections_have_between_10_and_15_points() -> None:
    service = ResumeAgentService(Path("resume_data"))
    profile = service.store.load_person("rajendra-prasad-n")
    counts = [len(job.impact) for job in profile.experience]
    assert counts == [15, 10, 15, 15, 15, 11]


def test_tailor_profile_matches_keywords() -> None:
    service = ResumeAgentService(Path("resume_data"))
    profile = service.store.load_person("vikram-bathala")
    tailored, matched = tailor_profile(profile, "Need Kubernetes Terraform Azure platform engineering leadership")
    assert "terraform" in tailored.summary_html.lower()
    assert "terraform" in matched


def test_tailor_resume_creates_branch_commit_and_html() -> None:
    with tempfile.TemporaryDirectory() as temp_dir:
        repo_root = Path(temp_dir)
        subprocess.run(["git", "init"], cwd=repo_root, check=True, capture_output=True)
        subprocess.run(["git", "config", "user.name", "Codex"], cwd=repo_root, check=True, capture_output=True)
        subprocess.run(["git", "config", "user.email", "codex@example.com"], cwd=repo_root, check=True, capture_output=True)

        source_root = Path.cwd()
        for folder in ["resume_data", "templates"]:
            shutil.copytree(source_root / folder, repo_root / folder)

        service = ResumeAgentService(repo_root / "resume_data", repo_root=repo_root)
        result = service.tailor_resume_to_jd(
            "vikram-bathala",
            "Need AKS Terraform Azure platform engineering",
            "codex/test-jd",
            push=False,
        )
        assert result.commit_sha
        assert Path(result.output_path).exists()
        assert "aks" in [item.lower() for item in result.matched_keywords]


def test_branch_name_prefers_company_name() -> None:
    jd = "Company: Aristek Consulting\nWe are seeking a highly motivated DevOps Engineer."
    assert _branch_name("vikram-bathala", jd) == "codex/vikram-bathala-aristek-consulting"


def test_branch_name_falls_back_to_role_name() -> None:
    jd = "We are seeking a highly motivated DevOps Engineer to help build and maintain scalable infrastructure."
    assert _branch_name("vikram-bathala", jd) == "codex/vikram-bathala-devops-engineer"
