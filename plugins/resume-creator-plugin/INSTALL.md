# Résumé Creator Plugin Install Guide

This plugin creates tailored DevOps / Cloud resumes for Rajendra and exports recruiter-ready HTML and PDF output.

## Inputs Supported

- `person`
  - `Rajendra`
- `domain`
  - `devops-cloud`
- `level`
  - `Base`
  - `Tailored`
  - `Optimized`
  - `Aggressive`
- `jd`
  - pasted text
  - or a text file path when running the script directly

## Requirements

- Codex
- Python 3
- a Chromium-based browser for PDF export
  - Google Chrome
  - Microsoft Edge
  - Chromium

## Windows Install

1. Extract the plugin folder so you have a local `resume-creator-plugin` directory.
2. Run:

```powershell
powershell -ExecutionPolicy Bypass -File C:\path\to\resume-creator-plugin\scripts\install_plugin.ps1
```

3. Restart Codex.

## Windows Update

When you receive a newer plugin bundle, extract it and run:

```powershell
powershell -ExecutionPolicy Bypass -File C:\path\to\resume-creator-plugin\scripts\update_plugin.ps1
```

Then restart Codex.

## macOS Install

1. Extract the plugin folder so you have a local `resume-creator-plugin` directory.
2. Run:

```bash
bash /path/to/resume-creator-plugin/scripts/install_plugin.sh
```

3. Restart Codex.

## macOS Update

When you receive a newer plugin bundle, extract it and run:

```bash
bash /path/to/resume-creator-plugin/scripts/update_plugin.sh
```

Then restart Codex.

## Create A Distributable Zip

From the source repo or plugin source folder:

```powershell
python C:\path\to\resume-creator-plugin\scripts\package_plugin.py
```

This creates a versioned zip such as:

- `resume-creator-plugin-0.1.0.zip`

## Direct Script Usage

You can also run the plugin directly without waiting for Codex discovery:

```powershell
python C:\path\to\resume-creator-plugin\scripts\run_resume_request.py `
  --person Rajendra `
  --domain devops-cloud `
  --level Aggressive `
  --jd-file C:\temp\jd.txt
```

Example for DevOps / Cloud:

```powershell
python C:\path\to\resume-creator-plugin\scripts\run_resume_request.py `
  --person Rajendra `
  --domain devops-cloud `
  --level Tailored `
  --jd-file C:\temp\jd.txt
```

## Output

The runner writes:

- HTML resume
- PDF exported from the HTML
- JSON manifest with output paths

The PDF path is the primary artifact.
