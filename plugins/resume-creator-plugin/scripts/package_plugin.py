from __future__ import annotations

import argparse
from pathlib import Path
import zipfile


def package_plugin(plugin_root: Path, output_zip: Path) -> Path:
    plugin_root = plugin_root.resolve()
    output_zip = output_zip.resolve()
    output_zip.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output_zip, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in plugin_root.rglob("*"):
            if path.is_dir() or "__pycache__" in path.parts or path.suffix == ".pyc":
                continue
            archive.write(path, arcname=Path(plugin_root.name) / path.relative_to(plugin_root))
    return output_zip


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Create a distributable zip for the resume creator plugin.")
    parser.add_argument("--plugin-root", default=str(Path(__file__).resolve().parents[1]), help="Plugin root directory to package")
    parser.add_argument("--output", default=str(Path(__file__).resolve().parents[1].parent / "dist" / "resume-creator-plugin.zip"), help="Output zip file path")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    print(package_plugin(Path(args.plugin_root), Path(args.output)))


if __name__ == "__main__":
    main()
