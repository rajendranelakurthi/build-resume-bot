from __future__ import annotations

import argparse
import shutil
import subprocess
from pathlib import Path


BROWSER_CANDIDATES = [
    Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"),
    Path(r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"),
    Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe"),
    Path(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"),
]


def resolve_browser() -> Path:
    for candidate in BROWSER_CANDIDATES:
        if candidate.exists():
            return candidate

    for command_name in ("msedge", "chrome", "chromium"):
        resolved = shutil.which(command_name)
        if resolved:
            return Path(resolved)

    raise FileNotFoundError(
        "Could not find a Chromium-based browser for PDF export. "
        "Install Microsoft Edge or Google Chrome, or add one to PATH."
    )


def export_html_to_pdf(html_path: Path, pdf_path: Path, *, browser_path: Path | None = None) -> Path:
    html_path = html_path.resolve()
    pdf_path = pdf_path.resolve()
    pdf_path.parent.mkdir(parents=True, exist_ok=True)

    browser = browser_path or resolve_browser()
    command = [
        str(browser),
        "--headless=new",
        "--disable-gpu",
        "--allow-file-access-from-files",
        f"--print-to-pdf={pdf_path}",
        html_path.as_uri(),
    ]
    subprocess.run(command, check=True)
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
