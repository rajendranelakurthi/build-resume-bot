from __future__ import annotations

from dataclasses import replace
from html import escape
import re

from resume_agents.models import Experience, PersonProfile

STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "build", "built", "by", "for", "from",
    "in", "into", "is", "of", "on", "or", "that", "the", "to", "using", "with",
    "your", "you", "our", "we", "will", "this", "role", "job", "work", "years",
    "year", "experience", "engineer", "senior", "need", "required", "requirements",
    "responsible", "preferred", "plus",
}


def tailor_profile(profile: PersonProfile, job_description: str) -> tuple[PersonProfile, list[str]]:
    keywords = extract_keywords(job_description)
    matched_keywords = [keyword for keyword in keywords if _profile_contains(profile, keyword)][:10]
    missing_keywords = [keyword for keyword in keywords if keyword not in matched_keywords][:6]

    tailored_summary = build_summary(profile, matched_keywords, missing_keywords)
    tailored_achievements = rank_tagged_items(profile.achievements, keywords) or profile.achievements
    tailored_skill_sections = rank_tagged_items(profile.skill_sections, keywords, content_key="content") or profile.skill_sections
    tailored_experience = [rank_experience(job, keywords) for job in profile.experience]

    tailored = replace(
        profile,
        summary_html=tailored_summary,
        achievements=tailored_achievements,
        skill_sections=tailored_skill_sections,
        experience=tailored_experience,
    )
    return tailored, matched_keywords


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
    matched_text = ", ".join(matched_keywords[:8]) if matched_keywords else "cloud engineering, DevOps automation, and platform reliability"
    summary = (
        f"<strong>{escape(profile.headline)}</strong> with a base resume tailored toward "
        f"<strong>{escape(matched_text)}</strong>. "
        f"Proven background across {escape(', '.join(profile.skills[:6]))} with emphasis on measurable platform, delivery, and infrastructure outcomes."
    )
    if missing_keywords:
        summary += (
            " <strong>Target emphasis:</strong> "
            f"{escape(', '.join(missing_keywords[:4]))}."
        )
    return summary


def rank_tagged_items(
    items: list[dict[str, str]],
    keywords: list[str],
    *,
    content_key: str = "text",
) -> list[dict[str, str]]:
    return sorted(
        items,
        key=lambda item: _score_text(f"{item.get('tag', '')} {item.get(content_key, '')}", keywords),
        reverse=True,
    )


def rank_experience(job: Experience, keywords: list[str]) -> Experience:
    ranked_impact = sorted(
        job.impact,
        key=lambda point: _score_text(_impact_text(point), keywords),
        reverse=True,
    )
    return replace(job, impact=ranked_impact)


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
