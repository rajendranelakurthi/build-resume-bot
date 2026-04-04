from __future__ import annotations

from resume_agents.models import AgentResponse, PersonProfile


def detect_route(user_request: str) -> str:
    request = user_request.lower()
    if "review" in request or "gap" in request:
        return "review"
    if "summary" in request or "about me" in request:
        return "summary"
    if "tailor" in request or "target" in request or "for " in request:
        return "tailor"
    if "update" in request or "change" in request or "add" in request:
        return "update"
    return "general"


def run_agents(profile: PersonProfile, user_request: str, route: str) -> list[AgentResponse]:
    responses = [planner_agent(user_request, route)]

    if route == "summary":
        responses.append(summary_agent(profile))
    elif route == "review":
        responses.append(review_agent(profile, user_request))
    elif route == "tailor":
        responses.append(tailor_agent(profile, user_request))
        responses.append(review_agent(profile, user_request))
    elif route == "update":
        responses.append(update_agent(profile, user_request))
    else:
        responses.append(summary_agent(profile))
        responses.append(review_agent(profile, user_request))

    return responses


def planner_agent(user_request: str, route: str) -> AgentResponse:
    return AgentResponse(
        agent_name="planner",
        intent=route,
        content=f"Request classified as '{route}' based on: {user_request}",
    )


def summary_agent(profile: PersonProfile) -> AgentResponse:
    top_skills = ", ".join(profile.skills[:5])
    content = (
        f"{profile.full_name} is a {profile.headline} based in {profile.location}. "
        f"Core strengths include {top_skills}. "
        f"The profile shows experience translating work into measurable business outcomes."
    )
    return AgentResponse(agent_name="summary-writer", intent="summary", content=content)


def tailor_agent(profile: PersonProfile, user_request: str) -> AgentResponse:
    focus_area = _extract_focus_area(user_request)
    bullets: list[str] = []
    for role in profile.experience[:2]:
        if role.impact:
            first_point = role.impact[0]
            rendered_point = first_point["text"] if isinstance(first_point, dict) else first_point
            bullets.append(f"- {role.title}, {role.company}: {rendered_point}")

    content = "\n".join(
        [
            f"Tailored focus: {focus_area}",
            f"{profile.full_name} | {profile.headline}",
            "",
            "Priority skills:",
            ", ".join(profile.skills[:8]),
            "",
            "Selected impact highlights:",
            *bullets,
        ]
    )
    return AgentResponse(agent_name="resume-tailor", intent="tailor", content=content)


def review_agent(profile: PersonProfile, user_request: str) -> AgentResponse:
    findings: list[str] = []
    if len(profile.skills) < 6:
        findings.append("Add more role-relevant skills to improve keyword coverage.")
    if not profile.notes:
        findings.append("Add notes for target roles, industries, or preferences.")
    if not any(_mentions_leadership(impact) for job in profile.experience for impact in job.impact):
        findings.append("Leadership evidence is thin; add ownership or mentoring examples.")
    if not findings:
        findings.append("Current profile has enough structure for a first-pass tailored resume.")

    content = "\n".join(f"- {item}" for item in findings)
    return AgentResponse(agent_name="reviewer", intent="review", content=content)


def update_agent(profile: PersonProfile, user_request: str) -> AgentResponse:
    content = (
        "Suggested update workflow:\n"
        f"- Person: {profile.full_name}\n"
        f"- Requested change: {user_request}\n"
        "- Next step: capture the exact bullet, metric, or role emphasis to add to stored resume data."
    )
    return AgentResponse(agent_name="profile-updater", intent="update", content=content)


def _extract_focus_area(user_request: str) -> str:
    lowered = user_request.lower()
    marker = "for "
    if marker in lowered:
        return user_request[lowered.index(marker) + len(marker) :].strip().rstrip(".")
    return "the requested target role"


def _mentions_leadership(impact: dict[str, str] | str) -> bool:
    text = impact["text"] if isinstance(impact, dict) else impact
    lowered = text.lower()
    return "led" in lowered or "managed" in lowered

