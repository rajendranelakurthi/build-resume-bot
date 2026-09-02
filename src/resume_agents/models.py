from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Experience:
    title: str
    company: str
    impact: list[dict[str, str] | str] = field(default_factory=list)
    date_range: str = ""
    project: str = ""
    client: str = ""
    skills_used: list[str] = field(default_factory=list)


@dataclass
class Education:
    school: str
    degree: str
    logo_image: str = ""
    logo_alt: str = ""


@dataclass
class ResumeEntry:
    title: str
    organization: str = ""
    date_range: str = ""
    bullets: list[str] = field(default_factory=list)


@dataclass
class ResumeSection:
    title: str
    entries: list[ResumeEntry] = field(default_factory=list)


@dataclass
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


@dataclass
class AgentResponse:
    agent_name: str
    intent: str
    content: str


@dataclass
class OrchestrationResult:
    person_id: str
    user_request: str
    route: str
    responses: list[AgentResponse]


@dataclass
class TailoredResumeResult:
    person_id: str
    branch_name: str
    output_path: str
    commit_sha: str | None
    pushed: bool
    matched_keywords: list[str] = field(default_factory=list)
