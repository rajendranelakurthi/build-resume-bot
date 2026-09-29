# Rajendra AWS DevOps Resume Creator

This branch, `feature/rajendrapn-aws`, generates AWS DevOps resumes focused on Amazon S3, VPC networking, IAM/security, infrastructure automation, CI/CD, and production operations.

## Command in Codex

```text
Use the Résumé Creator Plugin to create an Aggressive AWS DevOps resume for Rajendra using this JD: <provide JD>
```

This command selects `aws-devops`. On this branch, `devops-cloud` is an alias for the AWS-only `aws-devops` domain. It does not switch to Azure or GCP based on JD keywords.

## Generate the résumé

From the repository root, with Python 3.10+ and Chrome or Edge installed (use Python 3.12 on this Mac):

```bash
git switch feature/rajendrapn-aws
python3.12 plugins/resume-creator-plugin/scripts/run_resume_request.py \
  --person Rajendra \
  --domain aws-devops \
  --level Aggressive \
  --jd-file plugins/resume-creator-plugin/assets/jds/aws-s3-stonebranch.txt \
  --output-name Rajendra-Lead-AWS-DevOps
```

Replace the JD file as needed. `--domain devops-cloud` produces the same AWS output. Domain matching is case-insensitive. Unsupported cloud domains are rejected.

Outputs are saved in `tailored_resume/rajendra-prasad-n/`:

- `Rajendra-Lead-AWS-DevOps.pdf`
- `Rajendra-Lead-AWS-DevOps.html`
- `Rajendra-Lead-AWS-DevOps.profile.json`
- `Rajendra-Lead-AWS-DevOps.json` (generation manifest)

Use `--output-dir` to choose another directory. `--output-name` accepts a simple filename stem without extension or directory separators; omit it for an automatic person/domain/level/JD filename. Reusing the same name replaces that generated résumé.

## AWS base and tailoring

- `resume_data/people/rajendra-prasad-n.json`: repository AWS base.
- `plugins/resume-creator-plugin/assets/people/rajendra-prasad-n.json`: identical packaged AWS base.
- `plugins/resume-creator-plugin/assets/reference/rajendra-aws-source.json`: original source retained for future tailoring.
- `templates/base_resume.html` and the packaged template: synchronized AWS visual style with print-safe geometry and pagination.
- `src/resume_agents/tailor.py` and packaged `plugin_core.py`: preserve authored summaries and career facts; rank approved content against the JD.

`Base` renders the profile directly. `Tailored`, `Optimized`, and `Aggressive` currently use the same ranking engine. An Aggressive request does not establish unconfirmed candidate experience. The supplied JD names Stonebranch and S3 landing/curated/archive zones; confirm hands-on responsibilities before adding them to employment history. Preserve real certifications, including non-AWS credentials.

## Verification

```bash
PYTHONPATH=src python3.12 -m pytest -q
```

Tests cover domain aliases, all four levels, keyword matching, identity/history preservation, synchronized assets, packaging, and export failure handling. The PDF exporter checks that the HTML exists, generates a fresh temporary file, validates its PDF signature, and only then replaces the output. Review rendered pages before sharing.

## Plugin installation

Branch-local changes do not refresh an already installed global plugin. For first-time setup, use the packaged installation workflow from this checkout. For installed-plugin maintenance, follow the plugin update workflow and start a new Codex thread after reinstalling. Ordinary résumé generation needs no reinstall.

## Portable paths

Run examples from the repository root. Documentation uses relative repository paths, generated manifest paths are relative to the invocation directory, and profile/HTML images use an adjacent `assets/` folder. No developer-specific drive or home directory is saved. Browser and installation locations are discovered at runtime; full paths are used internally only where operating-system tools require them.

## Python / Kubernetes leadership résumé

Use an approved profile variant without overwriting the AWS base:

```bash
python3.12 plugins/resume-creator-plugin/scripts/run_resume_request.py \
  --person Rajendra --domain aws-devops --level Aggressive \
  --jd-file plugins/resume-creator-plugin/assets/jds/aws-python-kubernetes.txt \
  --profile-file plugins/resume-creator-plugin/assets/variants/rajendra-aws-python-kubernetes.json \
  --output-name Rajendra-AWS-DevOps-Python-Kubernetes
```

`--profile-file` must identify the same person as `--person`. Repository source and documentation are checked for machine-specific paths by `tests/test_portable_paths.py`.
