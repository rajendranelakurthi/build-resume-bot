from __future__ import annotations

import subprocess
from pathlib import Path


class GitError(RuntimeError):
    pass


def ensure_branch(repo_root: Path, branch_name: str) -> None:
    _run_git(repo_root, "checkout", "-B", branch_name)


def has_remote(repo_root: Path) -> bool:
    result = subprocess.run(
        ["git", "remote"],
        cwd=repo_root,
        capture_output=True,
        text=True,
        check=False,
    )
    return bool(result.stdout.strip())


def commit_file(repo_root: Path, file_path: Path, message: str) -> str:
    relative_path = file_path.relative_to(repo_root)
    _run_git(repo_root, "add", str(relative_path))
    _run_git(repo_root, "commit", "-m", message)
    return _run_git(repo_root, "rev-parse", "HEAD").stdout.strip()


def push_branch(repo_root: Path, branch_name: str) -> None:
    _run_git(repo_root, "push", "-u", "origin", branch_name)


def _run_git(repo_root: Path, *args: str) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(
        ["git", *args],
        cwd=repo_root,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        raise GitError(result.stderr.strip() or result.stdout.strip())
    return result
