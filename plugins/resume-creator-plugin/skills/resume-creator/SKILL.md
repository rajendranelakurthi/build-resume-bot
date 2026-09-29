---
name: resume-creator
description: Create Rajendra Azure DevOps resumes on this Azure-led branch, emphasizing software automation, CI/CD, AWS, Bicep, secure connectivity, and production operations. Export recruiter-ready HTML/PDF through the packaged workflow.
---

# Azure DevOps Resume Creator

1. Select person `Rajendra` and domain `azure-devops`.
2. Select `Base`, `Tailored`, `Optimized`, or `Aggressive` from the user request.
3. Use the bundled Azure profile in `assets/people/rajendra-prasad-n.json` and packaged renderer.
4. Generate HTML, PDF, profile JSON, and manifest in `tailored_resume/rajendra-prasad-n/` unless the user specifies another location.
5. Inspect the PDF for readable text, clean pagination, and accurate contact/history details.

User command:

```text
Use the Résumé Creator Plugin to create an Aggressive Azure-devops resume for Rajendra using this JD: <provide JD>
```

CLI (Python 3.10+; use Python 3.12 on this Mac):

```bash
python3.12 plugins/resume-creator-plugin/scripts/run_resume_request.py \
  --person Rajendra --domain azure-devops --level Aggressive \
  --jd-file plugins/resume-creator-plugin/assets/jds/azure-devops-developer.txt \
  --output-dir tailored_resume/rajendra-prasad-n
```

`Azure-devops` is case-insensitive. `devops-cloud` remains a compatibility alias for `azure-devops`; it does not enable a separate multi-cloud route. Canonical filenames and manifests always use `azure-devops`. Unsupported domains are rejected.

`Base` renders the Azure profile. Other levels rank the profile's skills, highlights, and bullets against the JD using the shared tailoring engine; they do not invent experience. AWS and Bicep are included at user request; certificate lifecycle management and encrypted database connection experience were confirmed. Do not include SSIS in this profile. Preserve employer names, employment titles/dates, contact details, education, and all genuine certifications, including non-Azure credentials. Do not replace historical tools with Azure equivalents without evidence or invent regulatory certifications, quantified improvements, or on-call rotation history.

Keep the repository and bundled profile/template copies synchronized. Return the PDF as the primary artifact. Do not overwrite installed global plugin files or repeat installation steps for ordinary resume requests. Branch code changes do not automatically refresh the installed plugin cache.
