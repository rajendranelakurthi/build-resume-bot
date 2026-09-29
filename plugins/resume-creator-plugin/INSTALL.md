# Résumé Creator Plugin Setup (macOS)

All commands below run from the repository root and use relative paths. For an extracted standalone plugin, run from its directory and replace `plugins/resume-creator-plugin/scripts/` with `scripts/`.

## Requirements

- Python 3.10+ (use `python3.12` on this Mac)
- Chrome, Edge, or Chromium for PDF export
- Codex for using the plugin through natural-language requests

## Run without installation

```bash
python3.12 plugins/resume-creator-plugin/scripts/run_resume_request.py \
  --person Rajendra --domain aws-devops --level Aggressive \
  --jd-file plugins/resume-creator-plugin/assets/jds/aws-s3-stonebranch.txt \
  --output-name Rajendra-Lead-AWS-DevOps
```

The default output directory is `tailored_resume/rajendra-prasad-n/`. HTML, PDF, profile JSON, and manifest files are saved there; required image files are copied to its `assets/` directory. Manifest paths are relative to the command's working directory. Run from the repository root for repository-relative paths. Move the output directory together with its `assets/` folder to preserve image references.

Browser executables are located through `PATH` or platform-discovered application directories. The exporter resolves full filesystem paths internally only when invoking the browser; no user-specific machine paths are saved in the profile or manifest.

## First-time macOS installation

```bash
bash plugins/resume-creator-plugin/scripts/install_plugin.sh
```

The installer discovers the current user's home directory at runtime and installs the plugin into the user's plugin location. Restart Codex afterward. Installation changes global plugin files; it is not required for the direct script command above.

## Update an installed copy

```bash
bash plugins/resume-creator-plugin/scripts/update_plugin.sh
```

Follow the Codex plugin update/reinstall workflow for cache refresh, then start a new thread to load updated instructions. Branch-local edits do not update the installed cache automatically.

## Package the plugin

```bash
python3.12 plugins/resume-creator-plugin/scripts/package_plugin.py
```

The default versioned ZIP is placed under `plugins/dist/`.

## Windows compatibility

PowerShell scripts remain available with relative paths for users running Windows:

```powershell
powershell -ExecutionPolicy Bypass -File ./plugins/resume-creator-plugin/scripts/install_plugin.ps1
powershell -ExecutionPolicy Bypass -File ./plugins/resume-creator-plugin/scripts/update_plugin.ps1
```

No Windows drive is assumed. Browser discovery uses environment-provided application locations.
