---
name: resume-creator
description: Tailor Rajendra Platform Engineer resumes to a JD and generate recruiter-ready HTML/PDF output. Prefer the packaged plugin workflow and avoid re-running setup steps unless installing or updating the plugin.
---

# Resume Creator

Use the packaged workflow. Keep this short and deterministic:

1. Select person: `Rajendra`
2. Select domain: `platform-engineer`
3. Select level: `Base`, `Tailored`, `Optimized`, or `Aggressive`
4. Read the JD and route to the matching person/domain resume profile
5. Tailor the structured profile to the JD
6. Render HTML and, if requested, export PDF

Canonical execution:

```bash
python3 plugins/resume-creator-plugin/scripts/run_resume_request.py \
  --person Rajendra \
  --domain platform-engineer \
  --level Aggressive \
  --jd-file /path/to/jd.txt
```

Notes:
- This branch defaults to `platform-engineer`; `Platform-Engineer`, `platform engineer`, `devops-cloud`, and `devops-sre` normalize to it.
- Preserve the platform header, summary, historical job titles, and 10+ substantive bullets per project.
- Rewrite the structured profile against each supplied JD before rendering; the deterministic engine ranks content and does not perform a full semantic rewrite.
- `Base` keeps the base resume content and renders directly.
- `Tailored`, `Optimized`, and `Aggressive` all use the repo’s tailoring engine.
- Return the PDF path as the primary output artifact when a PDF is requested.
- Use the bundled plugin assets in `plugins/resume-creator-plugin/assets/` rather than rebuilding the resume from scratch.

When plugin install/update is needed only:
- use `install_plugin.sh` on macOS/Linux or `install_plugin.ps1` on Windows
- use `update_plugin.sh` / `update_plugin.ps1` to overwrite the installed local plugin copy
- keep `.codex-plugin/plugin.json` and `.agents/plugins/marketplace.json` aligned

Do not repeat setup, packaging, or reinstall instructions unless the user explicitly asks for plugin maintenance.

Latest project minimum: 15 distinct substantive bullets; all other projects minimum: 10. Hide MuleSoft certification badge in rendered resumes. Use four evenly aligned certification cards.

Before each task, verify `git branch --show-current`, the current command, and branch instructions. On this branch use Lead Platform Engineer | Cloud Infrastructure and latest AT&T title Lead Platform/DevOps Engineer. Azure experience only; GCP/GKE knowledge only for the current scope. For a JD-specific source, pass `--profile-file <structured-profile.json>` to the CLI without replacing the reusable base.

Global user preference: Never include Key Vault (including Azure Key Vault/KeyVault) in any project’s `Skills Used` list, on any branch or tailoring level. This restriction applies only to project technology lists; enforce it before rendering future resumes.

Platform profile: distribute Jenkins, SonarQube, JFrog Artifactory, OpenShift, Milvus and Qdrant across project Skills Used lists with corresponding substantive platform-engineering bullets. Keep Key Vault excluded.
