from __future__ import annotations

from html import escape
from pathlib import Path

from resume_agents.models import PersonProfile


class HtmlResumeRenderer:
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
            "__ACHIEVEMENTS_HTML__": self._render_achievements(profile),
            "__SKILLS_CARDS_HTML__": self._render_skill_sections(profile),
            "__EXPERIENCE_HTML__": self._render_experience(profile),
            "__EDUCATION_HTML__": self._render_education(profile),
        }
        for token, value in payload.items():
            template = template.replace(token, value)
        return template

    def _render_contact_lines(self, profile: PersonProfile) -> str:
        if profile.contact_lines_html:
            return "\n".join(f"<div>{line}</div>" for line in profile.contact_lines_html)

        return "\n".join(
            [
                f"<div>{escape(profile.email)}</div>",
                f"<div>{escape(profile.location)}</div>",
            ]
        )

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
            details = self._render_job_details(job.project, job.client, job.skills_used)
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
                    (
                        f'<div><span class="job-title">{escape(job.title)}</span> | '
                        f'<span class="company-name">{escape(job.company)}</span></div>'
                    ),
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

    def _render_job_details(self, project: str, client: str, skills_used: list[str]) -> str:
        lines: list[str] = []
        if project:
            lines.append(f"<div><strong>Project:</strong> {escape(project)}</div>")
        if client:
            lines.append(f"<div><strong>Client:</strong> {escape(client)}</div>")
        if skills_used:
            lines.append(
                f"<div><strong>Skills Used:</strong> {escape(', '.join(skills_used))}</div>"
            )

        if not lines:
            return ""

        return "\n".join(['<div class="job-details">', *lines, "</div>"])

    def _render_education(self, profile: PersonProfile) -> str:
        return "\n".join(
            "\n".join(
                [
                    "<div>",
                    f"<strong>{escape(item.degree)}</strong><br>",
                    escape(item.school),
                    "</div>",
                ]
            )
            for item in profile.education
        )

    def _render_top_certifications_section(self, profile: PersonProfile) -> str:
        if not profile.certifications:
            return ""

        items = "\n".join(
            self._render_certification_badge(item)
            for item in profile.certifications
        )
        return "\n".join(
            [
                '<h2 class="section-title">Certifications</h2>',
                '<div class="certifications-grid">',
                items,
                "</div>",
            ]
        )

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

        return "\n".join(
            [
                '<div class="cert-card">',
                badge,
                f'<div class="cert-label">{label}</div>',
                "</div>",
            ]
        )

    def _gitlab_badge_svg(self) -> str:
        return (
            '<svg class="cert-badge-svg" viewBox="0 0 180 180" aria-hidden="true">'
            '<circle cx="90" cy="90" r="82" fill="#ffffff" stroke="#3b296e" stroke-width="5"/>'
            '<circle cx="90" cy="90" r="72" fill="none" stroke="#d7d0ea" stroke-width="3"/>'
            '<text x="90" y="42" text-anchor="middle" font-size="16" font-weight="700" fill="#2c235d">GITLAB</text>'
            '<text x="90" y="61" text-anchor="middle" font-size="16" font-weight="700" fill="#2c235d">CERTIFIED</text>'
            '<path d="M76 82 90 112 104 82 114 114 90 140 66 114Z" fill="#f36f21"/>'
            '<path d="M76 82 90 112 104 82" fill="none" stroke="#2c235d" stroke-width="4" stroke-linejoin="round"/>'
            '<text x="90" y="157" text-anchor="middle" font-size="13" font-weight="700" fill="#2c235d">ASSOCIATE</text>'
            "</svg>"
        )

    def _azure_fundamentals_badge_svg(self) -> str:
        return (
            '<svg class="cert-badge-svg" viewBox="0 0 180 180" aria-hidden="true">'
            '<path d="M90 12 150 32 150 120Q150 162 90 178Q30 162 30 120V32Z" fill="#0c62b7" stroke="#123a7a" stroke-width="5"/>'
            '<path d="M12 78Q90 60 168 78L160 124Q90 139 20 124Z" fill="#f7f7f7" stroke="#7a7a7a" stroke-width="3"/>'
            '<text x="90" y="42" text-anchor="middle" font-size="16" font-weight="700" fill="#1e225f">Microsoft</text>'
            '<text x="90" y="58" text-anchor="middle" font-size="10" font-weight="700" letter-spacing="2" fill="#555">CERTIFIED</text>'
            '<text x="90" y="96" text-anchor="middle" font-size="18" font-weight="700" fill="#202020">AZURE</text>'
            '<text x="90" y="118" text-anchor="middle" font-size="15" font-weight="700" fill="#202020">FUNDAMENTALS</text>'
            '<path d="M90 133 96 150 114 150 99 160 105 176 90 166 75 176 81 160 66 150 84 150Z" fill="#ffffff"/>'
            "</svg>"
        )

    def _azure_devops_badge_svg(self) -> str:
        return (
            '<svg class="cert-badge-svg" viewBox="0 0 180 180" aria-hidden="true">'
            '<path d="M90 12 150 32 150 120Q150 162 90 178Q30 162 30 120V32Z" fill="#0a3d86" stroke="#123a7a" stroke-width="5"/>'
            '<path d="M12 78Q90 60 168 78L160 124Q90 139 20 124Z" fill="#f7f7f7" stroke="#7a7a7a" stroke-width="3"/>'
            '<text x="90" y="42" text-anchor="middle" font-size="16" font-weight="700" fill="#ffffff">Microsoft</text>'
            '<text x="90" y="58" text-anchor="middle" font-size="10" font-weight="700" letter-spacing="2" fill="#d9e2f7">CERTIFIED</text>'
            '<text x="90" y="94" text-anchor="middle" font-size="17" font-weight="700" fill="#202020">AZURE</text>'
            '<text x="90" y="116" text-anchor="middle" font-size="13" font-weight="700" fill="#202020">DEVOPS ENGINEER</text>'
            '<text x="90" y="145" text-anchor="middle" font-size="14" font-weight="700" fill="#ffffff">EXPERT</text>'
            '<circle cx="68" cy="160" r="7" fill="#ffffff"/><circle cx="90" cy="160" r="7" fill="#ffffff"/><circle cx="112" cy="160" r="7" fill="#ffffff"/>'
            "</svg>"
        )

    def _aws_badge_svg(self) -> str:
        return (
            '<svg class="cert-badge-svg" viewBox="0 0 180 180" aria-hidden="true">'
            '<path d="M90 12 162 54V126L90 168 18 126V54Z" fill="#3136f0" stroke="#4fb0ff" stroke-width="5"/>'
            '<text x="90" y="44" text-anchor="middle" font-size="16" font-weight="700" fill="#ffffff">aws</text>'
            '<text x="90" y="63" text-anchor="middle" font-size="13" font-weight="700" fill="#ffffff">certified</text>'
            '<line x1="48" y1="78" x2="132" y2="78" stroke="#9bb8ff" stroke-width="2"/>'
            '<text x="90" y="104" text-anchor="middle" font-size="18" font-weight="700" fill="#ffffff">Solutions</text>'
            '<text x="90" y="126" text-anchor="middle" font-size="18" font-weight="700" fill="#ffffff">Architect</text>'
            '<text x="90" y="148" text-anchor="middle" font-size="12" font-weight="700" letter-spacing="2" fill="#ffffff">ASSOCIATE</text>'
            "</svg>"
        )

    def _mulesoft_badge_svg(self) -> str:
        return (
            '<svg class="cert-badge-svg" viewBox="0 0 180 180" aria-hidden="true">'
            '<path d="M50 14H130L166 52V124L90 168 14 124V52Z" fill="#4f26c8" stroke="#7f63ff" stroke-width="5"/>'
            '<circle cx="90" cy="38" r="16" fill="#ffffff"/><circle cx="90" cy="38" r="10" fill="none" stroke="#0096d6" stroke-width="4"/>'
            '<text x="90" y="92" text-anchor="middle" font-size="16" font-weight="700" fill="#ffffff">CERTIFIED</text>'
            '<text x="90" y="118" text-anchor="middle" font-size="16" font-weight="700" fill="#ffffff">MuleSoft</text>'
            '<text x="90" y="138" text-anchor="middle" font-size="13" font-weight="700" fill="#ffffff">Developer</text>'
            '<text x="90" y="156" text-anchor="middle" font-size="12" font-weight="700" fill="#ffffff">LEVEL 1</text>'
            "</svg>"
        )

    def _generic_badge_svg(self) -> str:
        return (
            '<svg class="cert-badge-svg" viewBox="0 0 180 180" aria-hidden="true">'
            '<circle cx="90" cy="90" r="76" fill="#174a8b" stroke="#0f3970" stroke-width="6"/>'
            '<text x="90" y="98" text-anchor="middle" font-size="18" font-weight="700" fill="#ffffff">CERT</text>'
            "</svg>"
        )
