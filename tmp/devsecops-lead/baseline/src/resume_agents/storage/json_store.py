from __future__ import annotations

import json
from pathlib import Path

from resume_agents.models import Education, Experience, PersonProfile, ResumeEntry, ResumeSection


class JsonResumeStore:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.people_dir = self.root / "people"

    def list_people(self) -> list[str]:
        return sorted(path.stem for path in self.people_dir.glob("*.json"))

    def load_person(self, person_id: str) -> PersonProfile:
        path = self.people_dir / f"{person_id}.json"
        if not path.exists():
            raise FileNotFoundError(f"Unknown person_id: {person_id}")

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
            certification_badges_image=raw.get("certification_badges_image", ""),
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
                    logo_image=item.get("logo_image", ""),
                    logo_alt=item.get("logo_alt", ""),
                )
                for item in raw.get("education", [])
            ],
            education_before_experience=raw.get("education_before_experience", False),
            certifications=raw.get("certifications", []),
            notes=raw.get("notes", []),
        )
