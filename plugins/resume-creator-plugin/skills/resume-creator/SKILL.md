---
name: resume-creator
description: Tailor Rajendra DevOps / Cloud and DevSecOps resumes to a JD and generate recruiter-ready HTML/PDF output. Prefer the packaged plugin workflow and avoid re-running setup steps unless installing or updating the plugin.
---

# Resume Creator

Use the packaged workflow. Keep this short and deterministic:

1. Select person: `Rajendra`
2. Select domain: `devops-cloud` or `devsecops` (use `devsecops` for DevSecOps Lead requests)
3. Select level: `Base`, `Tailored`, `Optimized`, or `Aggressive`
4. Read the JD and route to the matching person/domain resume profile
5. Tailor the structured profile to the JD
6. Render HTML and, if requested, export PDF

Canonical execution:

```bash
python3.12 plugins/resume-creator-plugin/scripts/run_resume_request.py \
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

## DevSecOps command

```text
Use the Résumé Creator Plugin to create an Aggressive DevSecOps resume for Rajendra using this JD: <paste JD>
```

```bash
python3.12 plugins/resume-creator-plugin/scripts/run_resume_request.py \
  --person Rajendra --domain devsecops --level Aggressive \
  --jd-file /path/to/jd.txt --output-dir tailored_resume/rajendra-prasad-n
```

- The `devsecops` domain selects `assets/variants/rajendra-devsecops.json`, including at Base level. Other levels tailor this variant. DevSecOps JDs also route here through `devops-cloud`.
- Cover code/dependency security, application release validation, infrastructure controls, secrets/access, environment coordination, and production operations.
- Preserve employer names, employment titles/dates, contact details, education, and certifications. Keep other domain bases unchanged.
- Public documentation establishes tool capabilities, not candidate experience. Ask before adding unconfirmed tool usage, regulatory compliance, sole environment-booking ownership, refresh arbitration, or quantified outcomes. Keep proposed additions separate from the résumé.
