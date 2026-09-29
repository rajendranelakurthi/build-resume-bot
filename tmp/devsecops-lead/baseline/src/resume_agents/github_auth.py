from __future__ import annotations

import subprocess
from dataclasses import dataclass


class GitHubAuthError(RuntimeError):
    pass


@dataclass(slots=True)
class GitHubAuthStatus:
    authenticated: bool
    hostname: str = "github.com"
    username: str | None = None
    raw_output: str = ""


def get_github_auth_status() -> GitHubAuthStatus:
    result = subprocess.run(
        ["gh", "auth", "status"],
        capture_output=True,
        text=True,
        check=False,
    )
    output = (result.stdout or "") + (result.stderr or "")
    if result.returncode != 0:
        lowered = output.lower()
        if "not logged into any github hosts" in lowered or "to log in, run: gh auth login" in lowered:
            return GitHubAuthStatus(authenticated=False, raw_output=output.strip())
        raise GitHubAuthError(output.strip() or "Unable to determine GitHub auth status.")

    username = _extract_username(output)
    hostname = _extract_hostname(output) or "github.com"
    return GitHubAuthStatus(
        authenticated=True,
        hostname=hostname,
        username=username,
        raw_output=output.strip(),
    )


def login_with_github_cli(*, web: bool = True, hostname: str = "github.com") -> None:
    command = ["gh", "auth", "login", "--hostname", hostname]
    if web:
        command.append("--web")

    result = subprocess.run(
        command,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        raise GitHubAuthError("GitHub CLI login failed.")


def _extract_username(output: str) -> str | None:
    for line in output.splitlines():
        if "Logged in to" in line and "account" in line:
            match = line.split("account", 1)[1].strip()
            username = match.split(" ", 1)[0].strip()
            if username:
                return username
    return None


def _extract_hostname(output: str) -> str | None:
    for line in output.splitlines():
        if "Logged in to " in line:
            fragment = line.split("Logged in to ", 1)[1]
            return fragment.split(" ", 1)[0].strip()
    return None
