from __future__ import annotations

from dataclasses import dataclass, field, replace
from html import escape
import json
from pathlib import Path
import re


@dataclass(slots=True)
class Experience:
    title: str
    company: str
    impact: list[dict[str, str] | str] = field(default_factory=list)
    date_range: str = ""
    project: str = ""
    client: str = ""
    skills_used: list[str] = field(default_factory=list)


@dataclass(slots=True)
class Education:
    school: str
    degree: str
    logo_image: str = ""
    logo_alt: str = ""


@dataclass(slots=True)
class ResumeEntry:
    title: str
    organization: str = ""
    date_range: str = ""
    bullets: list[str] = field(default_factory=list)


@dataclass(slots=True)
class ResumeSection:
    title: str
    entries: list[ResumeEntry] = field(default_factory=list)


@dataclass(slots=True)
class PersonProfile:
    person_id: str
    full_name: str
    headline: str
    location: str
    email: str
    page_title: str = ""
    summary_html: str = ""
    achievements_title: str = "Key Platform Achievements"
    contact_lines_html: list[str] = field(default_factory=list)
    certification_badges_image: str = ""
    certification_badges_alt: str = ""
    skills: list[str] = field(default_factory=list)
    skill_sections: list[dict[str, str]] = field(default_factory=list)
    achievements: list[dict[str, str]] = field(default_factory=list)
    experience: list[Experience] = field(default_factory=list)
    additional_sections: list[ResumeSection] = field(default_factory=list)
    education: list[Education] = field(default_factory=list)
    education_before_experience: bool = False
    certifications: list[str] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)


STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "build", "built", "by", "for", "from",
    "in", "into", "is", "of", "on", "or", "that", "the", "to", "using", "with",
    "your", "you", "our", "we", "will", "this", "role", "job", "work", "years",
    "year", "experience", "engineer", "senior", "need", "required", "requirements",
    "responsible", "preferred", "plus",
}


class BundledJsonResumeStore:
    def __init__(self, people_dir: Path, static_dir: Path) -> None:
        self.people_dir = people_dir
        self.static_dir = static_dir

    def load_person(self, person_id: str) -> PersonProfile:
        path = self.people_dir / f"{person_id}.json"
        raw = json.loads(path.read_text(encoding="utf-8"))
        return PersonProfile(
            person_id=raw["person_id"],
            full_name=raw["full_name"],
            headline=raw["headline"],
            location=raw["location"],
            email=raw["email"],
            page_title=raw.get("page_title", raw["full_name"]),
            summary_html=raw.get("summary_html", ""),
            achievements_title=raw.get("achievements_title", "Key Platform Achievements"),
            contact_lines_html=raw.get("contact_lines_html", []),
            certification_badges_image=self._resolve_asset(raw.get("certification_badges_image", "")),
            certification_badges_alt=raw.get("certification_badges_alt", ""),
            skills=raw.get("skills", []),
            skill_sections=raw.get("skill_sections", []),
            achievements=raw.get("achievements", []),
            experience=[
                Experience(
                    title=item["title"],
                    company=item["company"],
                    date_range=item.get("date_range", ""),
                    project=item.get("project", ""),
                    client=item.get("client", ""),
                    skills_used=item.get("skills_used", []),
                    impact=item.get("impact", []),
                )
                for item in raw.get("experience", [])
            ],
            additional_sections=[
                ResumeSection(
                    title=section["title"],
                    entries=[
                        ResumeEntry(
                            title=entry["title"],
                            organization=entry.get("organization", ""),
                            date_range=entry.get("date_range", ""),
                            bullets=entry.get("bullets", []),
                        )
                        for entry in section.get("entries", [])
                    ],
                )
                for section in raw.get("additional_sections", [])
            ],
            education=[
                Education(
                    school=item["school"],
                    degree=item["degree"],
                    logo_image=self._resolve_asset(item.get("logo_image", "")),
                    logo_alt=item.get("logo_alt", ""),
                )
                for item in raw.get("education", [])
            ],
            education_before_experience=raw.get("education_before_experience", False),
            certifications=raw.get("certifications", []),
            notes=raw.get("notes", []),
        )

    def _resolve_asset(self, asset_reference: str) -> str:
        if not asset_reference:
            return ""
        candidate = self.static_dir / Path(asset_reference).name
        if candidate.exists():
            return candidate.resolve().as_uri()
        return asset_reference


class BundledHtmlResumeRenderer:
    def __init__(self, template_path: Path) -> None:
        self.template_path = template_path

    def render(self, profile: PersonProfile) -> str:
        template = self.template_path.read_text(encoding="utf-8")
        payload = {
            "__PAGE_TITLE__": escape(profile.page_title or profile.full_name),
            "__FULL_NAME__": escape(profile.full_name.upper()),
            "__HEADLINE__": escape(profile.headline),
            "__CONTACT_LINES_HTML__": self._render_contact_lines(profile),
            "__SUMMARY_HTML__": profile.summary_html,
            "__TOP_CERTIFICATIONS_SECTION_HTML__": self._render_top_certifications_section(profile),
            "__ACHIEVEMENTS_TITLE__": escape(profile.achievements_title or "Key Platform Achievements"),
            "__ACHIEVEMENTS_HTML__": self._render_achievements(profile),
            "__SKILLS_CARDS_HTML__": self._render_skill_sections(profile),
            "__BODY_SECTIONS_HTML__": self._render_body_sections(profile),
        }
        for token, value in payload.items():
            template = template.replace(token, value)
        return template

    def _render_contact_lines(self, profile: PersonProfile) -> str:
        if profile.contact_lines_html:
            return "\n".join(f"<div>{line}</div>" for line in profile.contact_lines_html)
        return "\n".join([f"<div>{escape(profile.email)}</div>", f"<div>{escape(profile.location)}</div>"])

    def _render_achievements(self, profile: PersonProfile) -> str:
        return "\n".join(
            f'<li><span class="tag">{escape(item["tag"])}</span> {escape(item["text"])}</li>'
            for item in profile.achievements
        )

    def _render_skill_sections(self, profile: PersonProfile) -> str:
        return "\n".join(
            "\n".join(
                [
                    '<div class="skill-card">',
                    f"<h3>{escape(item['title'])}</h3>",
                    f"<p>{escape(item['content'])}</p>",
                    "</div>",
                ]
            )
            for item in profile.skill_sections
        )

    def _render_experience(self, profile: PersonProfile) -> str:
        blocks: list[str] = []
        for job in profile.experience:
            details = self._render_job_details(job.client, job.skills_used)
            impacts = "\n".join(
                f'<li><span class="tag">{escape(point["tag"])}</span> {escape(point["text"])}</li>'
                if isinstance(point, dict)
                else f"<li>{escape(point)}</li>"
                for point in job.impact
            )
            blocks.extend(
                [
                    '<div class="job-block">',
                    '<div class="job-header">',
                    f'<div><span class="job-title">{escape(job.title)}</span> | <span class="company-name">{escape(job.company)}</span></div>',
                    f'<span class="job-meta">{escape(job.date_range)}</span>',
                    "</div>",
                    details,
                    "<ul>",
                    impacts,
                    "</ul>",
                    "</div>",
                ]
            )
        return "\n".join(blocks)

    def _render_job_details(self, client: str, skills_used: list[str]) -> str:
        lines: list[str] = []
        if client:
            lines.append(f"<div><strong>Client:</strong> {escape(client)}</div>")
        if skills_used:
            lines.append(f"<div><strong>Skills Used:</strong> {escape(', '.join(skills_used))}</div>")
        if not lines:
            return ""
        return "\n".join(['<div class="job-details">', *lines, "</div>"])

    def _render_education(self, profile: PersonProfile) -> str:
        return "\n".join(
            "\n".join(
                [
                    '<div class="education-card">',
                    '<div class="education-row">',
                    self._render_education_logo(item.logo_image, item.logo_alt, item.school),
                    '<div class="education-copy">',
                    f"<strong>{escape(item.degree)}</strong>",
                    f"<div>{escape(item.school)}</div>",
                    "</div>",
                    "</div>",
                    "</div>",
                ]
            )
            for item in profile.education
        )

    def _render_education_logo(self, logo_image: str, logo_alt: str, school: str) -> str:
        if not logo_image:
            return ""
        return f'<img class="education-logo" src="{escape(logo_image)}" alt="{escape(logo_alt or f"{school} logo")}">'

    def _render_body_sections(self, profile: PersonProfile) -> str:
        sections: list[str] = []
        education_section = self._render_education_section(profile)
        experience_section = self._render_experience_section(profile)
        additional_sections = self._render_additional_sections(profile)
        if profile.education_before_experience:
            sections.extend([item for item in [education_section, experience_section, additional_sections] if item])
        else:
            sections.extend([item for item in [experience_section, additional_sections, education_section] if item])
        return "\n".join(sections)

    def _render_experience_section(self, profile: PersonProfile) -> str:
        experience_html = self._render_experience(profile)
        if not experience_html:
            return ""
        return "\n".join(['<h2 class="section-title">Professional Experience</h2>', experience_html])

    def _render_education_section(self, profile: PersonProfile) -> str:
        education_html = self._render_education(profile)
        if not education_html:
            return ""
        return "\n".join(['<h2 class="section-title">Education</h2>', '<div class="education-grid">', education_html, "</div>"])

    def _render_additional_sections(self, profile: PersonProfile) -> str:
        sections: list[str] = []
        for section in profile.additional_sections:
            sections.extend([f'<h2 class="section-title">{escape(section.title)}</h2>', self._render_additional_entries(section)])
        return "\n".join(item for item in sections if item)

    def _render_additional_entries(self, section: ResumeSection) -> str:
        blocks: list[str] = []
        for entry in section.entries:
            bullets = "\n".join(f"<li>{escape(bullet)}</li>" for bullet in entry.bullets)
            header_right = f'<span class="job-meta">{escape(entry.date_range)}</span>' if entry.date_range else ""
            organization_html = f' | <span class="company-name">{escape(entry.organization)}</span>' if entry.organization else ""
            blocks.extend(
                [
                    '<div class="job-block">',
                    '<div class="job-header">',
                    f'<div><span class="job-title">{escape(entry.title)}</span>{organization_html}</div>',
                    header_right,
                    "</div>",
                    "<ul>",
                    bullets,
                    "</ul>",
                    "</div>",
                ]
            )
        return "\n".join(blocks)

    def _render_top_certifications_section(self, profile: PersonProfile) -> str:
        if not profile.certifications:
            return ""
        items = "\n".join(self._render_certification_badge(item) for item in profile.certifications)
        return "\n".join(['<h2 class="section-title">Certifications</h2>', '<div class="certifications-grid">', items, "</div>"])

    def _render_certification_badge(self, certification: str) -> str:
        label = escape(certification)
        key = certification.lower()
        if "gitlab" in key:
            badge = self._gitlab_badge_svg()
        elif "azure fundamentals" in key:
            badge = self._azure_fundamentals_badge_svg()
        elif "azure devops engineer" in key:
            badge = self._azure_devops_badge_svg()
        elif "aws certified solutions architect" in key:
            badge = self._aws_badge_svg()
        elif "mulesoft" in key:
            badge = self._mulesoft_badge_svg()
        else:
            badge = self._generic_badge_svg()
        return "\n".join(['<div class="cert-card">', badge, f'<div class="cert-label">{label}</div>', "</div>"])

    def _gitlab_badge_svg(self) -> str:
        return '<svg class="cert-badge-svg" viewBox="0 0 180 180" aria-hidden="true"><circle cx="90" cy="90" r="82" fill="#ffffff" stroke="#3b296e" stroke-width="5"/><circle cx="90" cy="90" r="72" fill="none" stroke="#d7d0ea" stroke-width="3"/><text x="90" y="42" text-anchor="middle" font-size="16" font-weight="700" fill="#2c235d">GITLAB</text><text x="90" y="61" text-anchor="middle" font-size="16" font-weight="700" fill="#2c235d">CERTIFIED</text><path d="M76 82 90 112 104 82 114 114 90 140 66 114Z" fill="#f36f21"/><path d="M76 82 90 112 104 82" fill="none" stroke="#2c235d" stroke-width="4" stroke-linejoin="round"/><text x="90" y="157" text-anchor="middle" font-size="13" font-weight="700" fill="#2c235d">ASSOCIATE</text></svg>'

    def _azure_fundamentals_badge_svg(self) -> str:
        return '<svg class="cert-badge-svg" viewBox="0 0 180 180" aria-hidden="true"><path d="M90 12 150 32 150 120Q150 162 90 178Q30 162 30 120V32Z" fill="#0c62b7" stroke="#123a7a" stroke-width="5"/><path d="M12 78Q90 60 168 78L160 124Q90 139 20 124Z" fill="#f7f7f7" stroke="#7a7a7a" stroke-width="3"/><text x="90" y="42" text-anchor="middle" font-size="16" font-weight="700" fill="#1e225f">Microsoft</text><text x="90" y="58" text-anchor="middle" font-size="10" font-weight="700" letter-spacing="2" fill="#555">CERTIFIED</text><text x="90" y="96" text-anchor="middle" font-size="18" font-weight="700" fill="#202020">AZURE</text><text x="90" y="118" text-anchor="middle" font-size="15" font-weight="700" fill="#202020">FUNDAMENTALS</text><path d="M90 133 96 150 114 150 99 160 105 176 90 166 75 176 81 160 66 150 84 150Z" fill="#ffffff"/></svg>'

    def _azure_devops_badge_svg(self) -> str:
        return '<svg class="cert-badge-svg" viewBox="0 0 180 180" aria-hidden="true"><path d="M90 12 150 32 150 120Q150 162 90 178Q30 162 30 120V32Z" fill="#0a3d86" stroke="#123a7a" stroke-width="5"/><path d="M12 78Q90 60 168 78L160 124Q90 139 20 124Z" fill="#f7f7f7" stroke="#7a7a7a" stroke-width="3"/><text x="90" y="42" text-anchor="middle" font-size="16" font-weight="700" fill="#ffffff">Microsoft</text><text x="90" y="58" text-anchor="middle" font-size="10" font-weight="700" letter-spacing="2" fill="#d9e2f7">CERTIFIED</text><text x="90" y="94" text-anchor="middle" font-size="17" font-weight="700" fill="#202020">AZURE</text><text x="90" y="116" text-anchor="middle" font-size="13" font-weight="700" fill="#202020">DEVOPS ENGINEER</text><text x="90" y="145" text-anchor="middle" font-size="14" font-weight="700" fill="#ffffff">EXPERT</text><circle cx="68" cy="160" r="7" fill="#ffffff"/><circle cx="90" cy="160" r="7" fill="#ffffff"/><circle cx="112" cy="160" r="7" fill="#ffffff"/></svg>'

    def _aws_badge_svg(self) -> str:
        return '<svg class="cert-badge-svg" viewBox="0 0 180 180" aria-hidden="true"><path d="M90 12 162 54V126L90 168 18 126V54Z" fill="#3136f0" stroke="#4fb0ff" stroke-width="5"/><text x="90" y="44" text-anchor="middle" font-size="16" font-weight="700" fill="#ffffff">aws</text><text x="90" y="63" text-anchor="middle" font-size="13" font-weight="700" fill="#ffffff">certified</text><line x1="48" y1="78" x2="132" y2="78" stroke="#9bb8ff" stroke-width="2"/><text x="90" y="104" text-anchor="middle" font-size="18" font-weight="700" fill="#ffffff">Solutions</text><text x="90" y="126" text-anchor="middle" font-size="18" font-weight="700" fill="#ffffff">Architect</text><text x="90" y="148" text-anchor="middle" font-size="12" font-weight="700" letter-spacing="2" fill="#ffffff">ASSOCIATE</text></svg>'

    def _mulesoft_badge_svg(self) -> str:
        return '<svg class="cert-badge-svg" viewBox="0 0 180 180" aria-hidden="true"><path d="M50 14H130L166 52V124L90 168 14 124V52Z" fill="#4f26c8" stroke="#7f63ff" stroke-width="5"/><circle cx="90" cy="38" r="16" fill="#ffffff"/><circle cx="90" cy="38" r="10" fill="none" stroke="#0096d6" stroke-width="4"/><text x="90" y="92" text-anchor="middle" font-size="16" font-weight="700" fill="#ffffff">CERTIFIED</text><text x="90" y="118" text-anchor="middle" font-size="16" font-weight="700" fill="#ffffff">MuleSoft</text><text x="90" y="138" text-anchor="middle" font-size="13" font-weight="700" fill="#ffffff">Developer</text><text x="90" y="156" text-anchor="middle" font-size="12" font-weight="700" fill="#ffffff">LEVEL 1</text></svg>'

    def _generic_badge_svg(self) -> str:
        return '<svg class="cert-badge-svg" viewBox="0 0 180 180" aria-hidden="true"><circle cx="90" cy="90" r="76" fill="#174a8b" stroke="#0f3970" stroke-width="6"/><text x="90" y="98" text-anchor="middle" font-size="18" font-weight="700" fill="#ffffff">CERT</text></svg>'


def tailor_profile(profile: PersonProfile, job_description: str) -> tuple[PersonProfile, list[str]]:
    keywords = extract_keywords(job_description)
    matched_keywords = [keyword for keyword in keywords if _profile_contains(profile, keyword)][:10]
    missing_keywords = [keyword for keyword in keywords if keyword not in matched_keywords][:6]
    lowered_jd = job_description.lower()
    if "azure devops" in lowered_jd and "github actions" in lowered_jd and "terraform" in lowered_jd:
        return build_azure_devops_profile(profile), matched_keywords
    headline = profile.headline
    if "gitlab" in keywords:
        headline = "Lead GitLab & DevOps Engineer | CI/CD, DevSecOps, Terraform & Kubernetes"
    tailored = replace(
        profile,
        headline=headline,
        summary_html=build_summary(profile, matched_keywords, missing_keywords),
        achievements=rank_tagged_items(profile.achievements, keywords) or profile.achievements,
        skill_sections=rank_tagged_items(profile.skill_sections, keywords, content_key="content") or profile.skill_sections,
        experience=[rank_experience(job, keywords) for job in profile.experience],
    )
    return tailored, matched_keywords


def build_azure_devops_profile(profile: PersonProfile) -> PersonProfile:
    achievements = [
        {"tag": "Azure DevOps Engineering", "text": "Designed governed Azure DevOps delivery platforms with reusable YAML pipelines, service connections, environments, approvals, artifacts, and deployment controls."},
        {"tag": "Terraform Module Engineering", "text": "Built and maintained reusable, versioned Terraform modules for repeatable Azure infrastructure deployments across multiple environments."},
        {"tag": "GitHub Actions", "text": "Authored reusable GitHub Actions workflows for Terraform validation, planning, security checks, approvals, deployment, and post-deployment verification."},
        {"tag": "Azure Cloud Automation", "text": "Automated Azure networking, identity, compute, storage, secrets, monitoring, and container-platform provisioning through infrastructure as code."},
        {"tag": "AI-Accelerated Delivery", "text": "Applied AI tools and coding agents to accelerate module development, workflow authoring, test generation, troubleshooting, documentation, and peer review."},
    ]
    skill_sections = [
        {"title": "Azure DevOps", "content": "Azure DevOps, Azure Pipelines, Azure Repos, Azure Artifacts, Boards, YAML pipelines, environments, approvals, service connections"},
        {"title": "GitHub Automation", "content": "GitHub Actions, reusable workflows, composite actions, workflow_call, environments, branch protection, pull requests, OIDC"},
        {"title": "Terraform", "content": "Reusable modules, module versioning, remote state, state locking, workspaces, providers, variables, outputs, plan/apply governance"},
        {"title": "Microsoft Azure", "content": "Azure Resource Manager, Virtual Networks, Private Endpoints, Entra ID, Managed Identities, Key Vault, Storage, AKS, Azure Monitor"},
        {"title": "AI Engineering", "content": "GitHub Copilot, AI coding agents, prompt engineering, code generation, test generation, troubleshooting, documentation automation"},
        {"title": "DevSecOps", "content": "Terraform validation, Checkov, tfsec, SonarQube, Fortify, Black Duck, secrets management, policy gates, least privilege"},
        {"title": "Scripting", "content": "PowerShell, Bash, Python, Azure CLI, JSON, YAML"},
        {"title": "Containers", "content": "Docker, Kubernetes, AKS, Helm, container registries"},
        {"title": "Source Control", "content": "Git, GitHub, Azure Repos, trunk-based development, GitFlow, pull requests, code reviews"},
        {"title": "Observability", "content": "Azure Monitor, Log Analytics, Application Insights, Grafana, Prometheus, pipeline telemetry"},
    ]
    job_specs = [
        ("Lead Azure DevOps Engineer", ["Azure", "Azure DevOps", "Azure Pipelines", "GitHub Actions", "Terraform", "PowerShell", "Python", "Docker", "AKS", "AI Coding Agents"], [
            "Designed and maintained reusable Terraform modules for Azure networking, identity, compute, storage, Key Vault, monitoring, and container-platform services, with versioned interfaces and clear consumer documentation.",
            "Built reusable GitHub Actions workflows that executed Terraform formatting, validation, security scanning, plan generation, approval, apply, and post-deployment verification across controlled Azure environments.",
            "Implemented secure GitHub-to-Azure authentication using OpenID Connect and workload identity federation, eliminating long-lived cloud credentials from deployment workflows.",
            "Engineered multi-stage Azure DevOps YAML pipelines with templates, variable groups, service connections, artifacts, environment checks, manual approvals, and release promotion controls.",
            "Standardized Terraform engineering practices covering remote state, state locking, provider constraints, module versioning, input validation, outputs, plan review, and environment isolation.",
            "Used GitHub Copilot and AI coding agents to accelerate Terraform module scaffolding, workflow development, validation testing, troubleshooting, refactoring, and technical documentation.",
            "Established human-review and security guardrails for AI-generated infrastructure code, requiring peer approval, static analysis, policy validation, and controlled execution before deployment.",
            "Created automated quality gates for Terraform and pipeline code using linting, security scanning, pull-request checks, branch protection, and evidence-producing deployment approvals.",
            "Automated Azure platform administration and deployment support with PowerShell, Python, Azure CLI, YAML, and JSON, reducing manual configuration and improving repeatability.",
            "Worked independently with application, security, and infrastructure teams to resolve Azure DevOps pipeline, Terraform state, service-connection, permission, and deployment issues.",
        ]),
        ("Senior Azure DevOps Engineer", ["Azure DevOps", "Azure Pipelines", "GitHub Actions", "Terraform", "Git", "PowerShell", "Docker"], [
            "Developed Azure DevOps YAML templates and GitHub Actions reusable workflows to standardize application and Terraform delivery across engineering teams.",
            "Created and maintained Terraform modules with consistent variables, outputs, naming, tagging, security defaults, and semantic versioning.",
            "Configured hosted and self-hosted build agents, workload-specific pools, pipeline permissions, caching, artifacts, and execution policies for reliable delivery.",
            "Implemented Git branching, pull-request, code-review, approval, and protected-branch standards across Azure Repos and GitHub repositories.",
            "Troubleshot pipeline, Terraform, authentication, artifact, and deployment failures and documented repeatable remediation procedures.",
        ]),
        ("Senior DevOps Engineer - Azure Automation", ["Azure", "GitHub Actions", "Terraform", "PowerShell", "Python", "Docker", "Kubernetes"], [
            "Authored and maintained GitHub Actions workflows for continuous integration, infrastructure validation, artifact management, and controlled cloud deployments.",
            "Provisioned cloud environments with reusable Terraform modules and pipeline-driven infrastructure-as-code patterns.",
            "Developed PowerShell and Python automation for environment configuration, operational checks, deployment support, and recovery workflows.",
            "Built delivery dashboards and pipeline telemetry to improve visibility into workflow health, failures, approvals, and release readiness.",
            "Resolved complex build and deployment issues across distributed engineering teams while maintaining clear operational documentation.",
        ]),
        ("Senior DevOps / Site Reliability Engineer", ["Azure", "GitHub Actions", "Terraform", "Python", "Kubernetes", "Prometheus", "Grafana"], [
            "Standardized GitHub Actions workflow patterns to reduce pipeline drift and accelerate software and infrastructure delivery.",
            "Designed reusable Terraform solutions for repeatable platform provisioning and environment promotion.",
            "Integrated security, quality, and observability controls into CI/CD workflows to improve deployment confidence and operational readiness.",
            "Automated reliability checks, monitoring, and incident diagnostics with Python, Prometheus, and Grafana.",
        ]),
        ("Senior Azure DevOps Engineer", ["Azure DevOps", "Azure Pipelines", "Git", "PowerShell", "Terraform", "Docker", "Helm"], [
            "Built continuous-delivery pipelines for multi-environment application releases using reusable templates and governed promotion controls.",
            "Automated infrastructure configuration with Terraform and PowerShell to improve auditability and repeatability.",
            "Implemented source-control, branching, artifact-versioning, and release-governance practices for application teams.",
            "Created deployment guides and runbooks and supported production releases across complex enterprise environments.",
        ]),
        ("Azure DevOps Engineer", ["Azure DevOps", "Terraform", "Git", "PowerShell", "Python", "YAML", "JSON"], [
            "Authored and maintained reusable Terraform modules and executed infrastructure changes through automated CI/CD workflows.",
            "Built YAML-based build and release pipelines with event-driven triggers, artifact promotion, environment selection, and deployment controls.",
            "Developed branching strategies and pull-request standards to improve release governance and code promotion.",
            "Automated configuration and deployment activities with PowerShell and Python and maintained shared operational scripts.",
            "Supported self-hosted build agents and diagnosed pipeline execution, dependency, and environment issues.",
        ]),
    ]
    azure_jobs = [replace(job, title=title, skills_used=skills, impact=impact) for job, (title, skills, impact) in zip(profile.experience, job_specs)]
    return replace(
        profile,
        page_title="Rajendra Prasad N - Lead Azure DevOps Engineer",
        headline="Lead Azure DevOps Engineer | Terraform, GitHub Actions & AI Automation",
        summary_html=(
            "<strong>Lead Azure DevOps Engineer with more than a decade of enterprise CI/CD, cloud automation, infrastructure-as-code, and release engineering experience</strong>. "
            "Deep hands-on expertise building and maintaining <strong>reusable Terraform modules</strong>, authoring new and supporting existing <strong>GitHub Actions workflows</strong>, "
            "and designing governed Azure DevOps YAML pipelines for secure, repeatable cloud deployments. Strong Azure delivery background spanning identity, networking, secrets, compute, "
            "storage, monitoring, containers, and deployment governance. Proficient with AI tools and coding agents for module development, workflow authoring, test generation, troubleshooting, "
            "refactoring, and documentation, with human-review and DevSecOps controls applied to AI-generated changes."
        ),
        achievements_title="Azure DevOps & Automation Highlights",
        achievements=achievements,
        skill_sections=skill_sections,
        experience=azure_jobs,
        certifications=profile.certifications,
    )


def extract_keywords(job_description: str) -> list[str]:
    tokens = re.findall(r"[A-Za-z][A-Za-z0-9+.#/-]*", job_description.lower())
    seen: set[str] = set()
    keywords: list[str] = []
    for token in tokens:
        if len(token) < 3 or token in STOPWORDS:
            continue
        if token not in seen:
            seen.add(token)
            keywords.append(token)
    return keywords


def build_summary(profile: PersonProfile, matched_keywords: list[str], missing_keywords: list[str]) -> str:
    # Keep the candidate-facing summary polished and evidence-based. Keyword lists
    # are useful for ranking, but exposing them verbatim produces recruiter-hostile
    # prose and can accidentally present unsupported JD terms as candidate skills.
    if "gitlab" in matched_keywords:
        return (
            "<strong>Lead GitLab and DevOps Engineer with more than a decade of enterprise platform, "
            "release engineering, cloud infrastructure, and production operations experience</strong>. "
            "Hands-on expertise administering GitLab delivery workflows, migrating Azure DevOps and "
            "Jenkins pipelines to GitLab CI/CD, operating self-hosted and autoscaling runners, building reusable pipeline "
            "templates, and enforcing branch protection, merge, approval, artifact, and repository "
            "governance standards. Experienced implementing <strong>GitLab Duo</strong> for AI-assisted "
            "development with security, review, and adoption guardrails. Deep strength in <strong>Linux, shell automation, Terraform, AWS, "
            "Azure, Docker, Kubernetes, EKS, OpenShift, and DevSecOps controls</strong>, with experience "
            "supporting GPU-enabled and vector-search platforms for AI-oriented workloads. Proven record "
            "improving pipeline security, reliability, scalability, and developer delivery efficiency."
        )
    return (
        "<strong>Lead DevOps Engineer with more than a decade of enterprise delivery, "
        "release engineering, cloud infrastructure, and production operations experience</strong> "
        "across Linux and Unix environments. Deep hands-on strength in <strong>shell scripting, "
        "CI/CD pipeline engineering, infrastructure as code, build and deployment automation, "
        "and container orchestration</strong> using Jenkins, GitHub Actions, GitLab CI, Terraform, "
        "CloudFormation, Ansible, Bash, Python, Docker, Kubernetes, EKS, and OpenShift. Proven "
        "record modernizing application platforms, troubleshooting complex releases, integrating "
        "monitoring and security controls, and improving the reliability and repeatability of "
        "mission-critical delivery workflows."
    )


def rank_tagged_items(items: list[dict[str, str]], keywords: list[str], *, content_key: str = "text") -> list[dict[str, str]]:
    return sorted(items, key=lambda item: _score_text(f"{item.get('tag', '')} {item.get(content_key, '')}", keywords), reverse=True)


def rank_experience(job: Experience, keywords: list[str]) -> Experience:
    return replace(job, impact=sorted(job.impact, key=lambda point: _score_text(_impact_text(point), keywords), reverse=True))


def _impact_text(point: dict[str, str] | str) -> str:
    if isinstance(point, dict):
        return f"{point.get('tag', '')} {point.get('text', '')}"
    return point


def _score_text(text: str, keywords: list[str]) -> int:
    lowered = text.lower()
    return sum(1 for keyword in keywords if keyword in lowered)


def _profile_contains(profile: PersonProfile, keyword: str) -> bool:
    haystacks = [
        profile.headline,
        profile.summary_html,
        " ".join(profile.skills),
        " ".join(item.get("title", "") for item in profile.skill_sections),
        " ".join(item.get("content", "") for item in profile.skill_sections),
        " ".join(item.get("text", "") for item in profile.achievements),
        " ".join(_impact_text(point) for job in profile.experience for point in job.impact),
        " ".join(
            " ".join([section.title, entry.title, entry.organization, " ".join(entry.bullets)])
            for section in profile.additional_sections
            for entry in section.entries
        ),
    ]
    return any(keyword in haystack.lower() for haystack in haystacks)
