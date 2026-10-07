---
name: resume-creator
description: Create Rajendra Azure DevOps resumes on this Azure-led branch, emphasizing software automation, CI/CD, AWS, Bicep, secure connectivity, and production operations. Export recruiter-ready HTML/PDF through the packaged workflow.
---

# Azure DevOps Resume Creator

## Required branch and request check

Before every resume task, including follow-up edits:

1. Run `git branch --show-current` and read the current checkout's `instructions.md`, README command, and packaged resume-creator skill.
2. Read the user's current command for person, domain, and tailoring level. Do not infer the domain from prior conversation.
3. Apply current explicit user instructions first, then the active branch's rules. Reuse earlier preferences only when their branch/domain scope matches the current task. A branch switch requires re-reading these rules.
4. On `feature/rajendrapn-azure` with `Azure-devops`, use header `Lead Azure DevOps Engineer | AI | K8s` and latest AT&T title `Lead Azure DevOps Engineer`. Do not import the AWS branch's `Lead SRE` designation.
5. Before rendering and again before delivery, verify that the selected profile, header, latest AT&T designation, domain, and output manifest agree with the active branch and current command.
6. If the command conflicts with the active branch's supported domain, identify the mismatch before changing defaults or switching branches. Do not silently reuse another branch's profile or designation.

This check applies to Base, Tailored, Optimized, and Aggressive. A designation described as "standard" is scoped to its branch/domain unless the user explicitly makes it global. Never modify another branch to enforce a current branch's preference.

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

For a JD-specific profile, pass `--profile-file assets/variants/<profile>.json` to the packaged CLI; preserve the person ID and use the bundled template/static assets. This leaves the branch default in place. For the AKS Kubernetes role, use `assets/variants/rajendra-aks-kubernetes.json`. The latest AT&T designation on this Azure branch is `Lead Azure DevOps Engineer`. Preserve the branch header `Lead Azure DevOps Engineer | AI | K8s`; do not carry AWS SRE designation rules into this branch. GKE, Prisma/Twistlock, Dynatrace, and direct vendor engagement remain evaluation targets until confirmed.

- Kubernetes profile clarification: show GKE as platform knowledge in skills only; do not claim GKE work experience.
