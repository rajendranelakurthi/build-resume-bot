---
name: resume-creator
description: Create tailored mechanical or DevOps/Cloud resumes for Rajendra or Vikram from job descriptions and render recruiter-ready HTML or PDF output. Use when Codex needs to choose one of the packaged base resumes, choose a domain such as mech or devops-cloud, apply a tailoring level such as Base, Tailored, Optimized, or Aggressive, rewrite the resume to match a JD, and regenerate output files.
---

# Resume Creator

Use the packaged plugin workflow.

1. Identify the person:
   - `Rajendra`
   - `Vikram`
2. Identify the domain:
   - `mech`
   - `devops-cloud`
3. Identify the tailoring level:
   - `Base`
   - `Tailored`
   - `Optimized`
   - `Aggressive`
4. Load the bundled base resume JSON from the plugin assets.
5. Route to the appropriate resume variant for the selected domain.
6. Tailor the resume against the JD.
7. Regenerate HTML output.
8. Export PDF when requested.

Treat the expected plugin input contract as:

- `person`
- `domain`
- `level`
- `jd`

Return the exported PDF path as the primary output artifact when PDF generation is requested.

Use the packaged scripts for deterministic execution:

- `plugins/resume-creator-plugin/scripts/run_resume_request.py`
- `plugins/resume-creator-plugin/scripts/export_html_to_pdf.py`
- `plugins/resume-creator-plugin/scripts/install_plugin.ps1`
- `plugins/resume-creator-plugin/scripts/package_plugin.py`

Example:

```powershell
python plugins/resume-creator-plugin/scripts/run_resume_request.py `
  --person Rajendra `
  --domain devops-cloud `
  --level Aggressive `
  --jd-file C:\temp\jd.txt
```

Current level behavior in this packaged baseline:

- `Base` keeps the original resume content and renders HTML/PDF directly
- `Tailored`, `Optimized`, and `Aggressive` all use the current repo tailoring engine
- deeper differentiation between those three levels should be added in later revisions

When packaging or maintaining this plugin:

- keep the plugin manifest in `.codex-plugin/plugin.json`
- keep the marketplace entry aligned with `.agents/plugins/marketplace.json`
- keep person-specific bundled assets under `assets/people/`, `assets/static/`, and `assets/templates/`
- use `install_plugin.ps1` to install into a user's home-local plugin directory
- use `package_plugin.py` to create a zip that another user can copy and install without the full repo
