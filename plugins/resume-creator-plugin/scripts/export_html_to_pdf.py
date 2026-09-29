from __future__ import annotations

import argparse
import os
import platform
import shutil
import subprocess
import tempfile
from pathlib import Path


def browser_candidates() -> list[Path]:
    """Discover platform locations without assuming a drive or username."""
    candidates: list[Path] = []
    if platform.system() == "Darwin":
        for applications in (Path(Path.home().anchor) / "Applications", Path.home() / "Applications"):
            for name, executable in (("Google Chrome", "Google Chrome"), ("Microsoft Edge", "Microsoft Edge"), ("Chromium", "Chromium")):
                candidates.append(applications / f"{name}.app" / "Contents" / "MacOS" / executable)
    elif platform.system() == "Windows":
        for variable in ("PROGRAMFILES", "PROGRAMFILES(X86)", "LOCALAPPDATA"):
            location = os.environ.get(variable)
            if location:
                base = Path(location)
                candidates.extend((base / "Google/Chrome/Application/chrome.exe",
                                   base / "Microsoft/Edge/Application/msedge.exe"))
    return candidates


def resolve_browser() -> Path:
    for command_name in ("google-chrome", "google-chrome-stable", "chromium", "chromium-browser", "msedge", "chrome"):
        resolved = shutil.which(command_name)
        if resolved:
            return Path(resolved)
    for candidate in browser_candidates():
        if candidate.is_file():
            return candidate
    raise FileNotFoundError(
        "Could not find a Chromium-based browser for PDF export. "
        "Install Chrome/Edge, add it to PATH, or pass --browser to the exporter."
    )


def export_html_to_pdf(html_path: Path, pdf_path: Path, *, browser_path: Path | None = None) -> Path:
    html_path = html_path.resolve()
    pdf_path = pdf_path.resolve()
    if not html_path.is_file():
        raise FileNotFoundError(f"Resume HTML does not exist: {html_path}")
    if html_path == pdf_path:
        raise ValueError("HTML input and PDF output must be different files.")
    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    browser = browser_path or resolve_browser()
    # Export to a fresh temporary file so a stale PDF cannot pass verification.
    with tempfile.TemporaryDirectory(prefix="resume-export-", dir=pdf_path.parent) as directory:
        candidate = Path(directory) / "resume.pdf"
        command = [
            str(browser), "--headless=new", "--disable-gpu",
            "--allow-file-access-from-files", "--no-pdf-header-footer",
            f"--print-to-pdf={candidate}", html_path.as_uri(),
        ]
        subprocess.run(command, check=True, timeout=120)
        if not candidate.is_file():
            raise RuntimeError("Browser did not create a PDF.")
        with candidate.open("rb") as stream:
            if stream.read(5) != b"%PDF-":
                raise RuntimeError("Browser output is not a valid PDF file.")
        candidate.replace(pdf_path)
    return pdf_path



def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Export a local HTML file to PDF using a Chromium-based browser.")
    parser.add_argument("--html", required=True, help="Path to the HTML input file")
    parser.add_argument("--pdf", required=True, help="Path to the PDF output file")
    parser.add_argument("--browser", help="Optional browser executable path override")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    browser_path = Path(args.browser) if args.browser else None
    output = export_html_to_pdf(Path(args.html), Path(args.pdf), browser_path=browser_path)
    print(output)


if __name__ == "__main__":
    main()
