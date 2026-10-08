---
name: resume-creator
description: Create Rajendra AWS DevOps resumes on this AWS-only branch, emphasizing S3, VPC networking, IAM/security, infrastructure as code, workflow automation, and production operations. Use the packaged HTML/PDF workflow.
---

# AWS DevOps Resume Creator

1. Select `Rajendra` and `aws-devops`. Use AWS DevOps wording in user-facing commands. The legacy `devops-cloud` domain remains an AWS-only compatibility alias.
2. Use `Base`, `Tailored`, `Optimized`, or `Aggressive` as requested.
3. Use the bundled AWS profile and HTML template. Preserve employment history, contact details, education, and genuine certifications.
4. Write HTML, PDF, structured profile JSON, and manifest to `tailored_resume/rajendra-prasad-n/` unless the user requests another location.
5. Inspect PDF pages for clipping, missing text, and poor page breaks before delivery.

User command:

```text
Use the Résumé Creator Plugin to create an Aggressive AWS DevOps resume for Rajendra using this JD: <provide JD>
```

CLI (Python 3.10+; use 3.12 on this Mac):

```bash
python3.12 plugins/resume-creator-plugin/scripts/run_resume_request.py \
  --person Rajendra --domain aws-devops --level Aggressive \
  --jd-file plugins/resume-creator-plugin/assets/jds/aws-s3-stonebranch.txt \
  --output-name Rajendra-Lead-AWS-DevOps
```

Domains are case-insensitive; `AWS DevOps` and `devops-cloud` normalize to `aws-devops`. Azure and GCP domain requests are rejected on this branch. Canonical manifests and default filenames use `aws-devops`.

Base renders the AWS profile directly. Other levels share a JD ranking engine that reorders approved skills, highlights, and bullets without inventing experience. S3 is included in keyword matching despite its short name. Public documentation establishes product capabilities, not candidate experience: confirm Stonebranch usage, S3 zone ownership, specific security controls, regulatory claims, and measurable outcomes before adding them as employment history.

Maintain synchronized repository/bundled profiles and templates. The reference source is retained under `assets/reference/`. Keep original supplied JDs unchanged as source inputs. Use `--output-name` for a short filename without an extension. The exporter rejects missing HTML, uses a fresh temporary PDF, and replaces output only after successful validation.

Branch changes do not automatically update the globally installed plugin. Do not reinstall or overwrite global plugin assets as part of an ordinary résumé request.

For the enterprise Python / Kubernetes leadership JD, use `assets/variants/rajendra-aws-python-kubernetes.json` through `--profile-file`. The related JD is `assets/jds/aws-python-kubernetes.txt`. Keep the default AWS base intact. Use 10 years of experience for Rajendra and omit the removed early-career employer from every resume. Apply this to the base, reference sources, and profile variants; do not restore older history when tailoring. Do not add certifications merely because they are preferred by the JD.
