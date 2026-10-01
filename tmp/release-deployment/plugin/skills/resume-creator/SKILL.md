---
name: resume-creator
description: Tailor Rajendra DevOps / Cloud resumes to a JD and generate recruiter-ready HTML/PDF output. Prefer the packaged plugin workflow and avoid re-running setup steps unless installing or updating the plugin.
---

# Resume Creator

Use the packaged workflow. Keep this short and deterministic:

1. Select person: `Rajendra`
2. Select domain: `devops-cloud`
3. Select level: `Base`, `Tailored`, `Optimized`, or `Aggressive`
4. Read the JD and route to the matching person/domain resume profile
5. Tailor the structured profile to the JD
6. Render HTML and, if requested, export PDF

Within `devops-cloud`, route strong role-specific requests to the packaged variants for Azure DevOps, GitLab, SRE/observability/GPU-HPC, or build and release engineering. The build/release variant must prioritize SCM and branching governance, reproducible builds, CI/CD, artifact and configuration management, release readiness, go/no-go decisions, deployment safety, automated status reporting, and release retrospectives across every project while retaining supporting DevOps and SRE context.

Canonical execution:

```bash
python3 plugins/resume-creator-plugin/scripts/run_resume_request.py \
  --person Rajendra \
  --domain devops-cloud \
  --level Aggressive \
  --jd-file /path/to/jd.txt \
  --output-dir tailored_resume/rajendra-prasad-n
```

Notes:
- For Rajendra, always write the final HTML, PDF, and manifest to `tailored_resume/rajendra-prasad-n/` unless the user explicitly requests a different output location. Do not substitute `output/` or `output/pdf/` for PDF verification workflows.
- `Base` keeps the base resume content and renders directly.
- `Tailored`, `Optimized`, and `Aggressive` all use the repo’s tailoring engine.
- Return the PDF path as the primary output artifact when a PDF is requested.
- Use the bundled plugin assets in `plugins/resume-creator-plugin/assets/` rather than rebuilding the resume from scratch.

When plugin install/update is needed only:
- use `install_plugin.sh` on macOS/Linux or `install_plugin.ps1` on Windows
- use `update_plugin.sh` / `update_plugin.ps1` to overwrite the installed local plugin copy
- keep `.codex-plugin/plugin.json` and `.agents/plugins/marketplace.json` aligned

Do not repeat setup, packaging, or reinstall instructions unless the user explicitly asks for plugin maintenance.
