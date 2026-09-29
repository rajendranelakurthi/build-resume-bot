# Multi-Person Resume Agents

Repository foundation for managing resume content for multiple people and rendering each resume into a shared HTML layout.

## First-time setup for Codex IDEs

1. Open this repository in a Codex-supported IDE, such as VS Code or Antigravity.
2. From the repository root, switch to the DevSecOps branch:

```bash
git switch feature/rajendrapn-devsecops
```

3. Install the resume creator plugin:

```bash
bash plugins/resume-creator-plugin/scripts/install_plugin.sh
```

4. Restart the IDE so Codex can load the installed plugin.
5. In Codex, use this DevSecOps command format:

```text
Use the Résumé Creator Plugin to create an Aggressive DevSecOps resume for Rajendra using this JD: <provide JD>
```

The explicit `DevSecOps` request selects `--domain devsecops`, even when the JD does not contain the word DevSecOps. With `devops-cloud`, automatic DevSecOps routing applies only to non-Base requests whose JD contains `DevSecOps`, `Dev Sec Ops`, or `Dev-Sec-Ops`.

## DevSecOps Lead on this branch

```text
Use the Résumé Creator Plugin to create an Aggressive DevSecOps resume for Rajendra using this JD: <paste JD>
```

From the repository root:

```bash
python3.12 plugins/resume-creator-plugin/scripts/run_resume_request.py \
  --person Rajendra \
  --domain devsecops \
  --level Aggressive \
  --jd-file plugins/resume-creator-plugin/assets/jds/devsecops-lead.txt \
  --output-dir tailored_resume/rajendra-prasad-n
```

Replace `--jd-file` with your own JD file as needed. The command writes HTML, PDF, structured profile, and a manifest. It requires Python 3.10+ and Chrome/Edge for PDF export.

The DevSecOps variant covers secure CI/CD, code and dependency checks, application validation, secrets/access, infrastructure controls, environment coordination, and production operations. `Base` renders the selected variant; Tailored, Optimized, and Aggressive use the shared tailoring engine. DevSecOps JDs also select this variant via `devops-cloud`; existing DataOps and Cloud routes remain available.

Source: `plugins/resume-creator-plugin/assets/variants/rajendra-devsecops.json`. Internet research must not be treated as proof of hands-on experience. Unconfirmed tools, compliance claims, and shared-environment booking/refresh ownership need confirmation before inclusion.

## What this repo does

- Stores structured resume data for multiple people in `resume_data/people/`
- Uses your HTML resume format as the base template
- Renders person-specific HTML resumes from JSON data
- Includes an agent orchestration layer that can later be connected to an LLM for request-based tailoring

## Repo layout

- `templates/base_resume.html`: base HTML resume template
- `src/resume_agents/models.py`: shared profile models
- `src/resume_agents/storage/json_store.py`: JSON-backed profile storage
- `src/resume_agents/renderers/html_resume.py`: HTML renderer for the base template
- `src/resume_agents/agents/router.py`: starter request routing
- `src/resume_agents/service.py`: orchestration and rendering service
- `src/resume_agents/cli.py`: command-line entrypoint
- `resume_data/people/`: per-person resume data
- `examples/`: generated HTML output

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
python -m resume_agents.cli list-people
python -m resume_agents.cli render-html --person rajendra-prasad-n --output examples/rajendra-prasad-n.html
python -m resume_agents.cli request --person rajendra-prasad-n --message "Tailor my resume for a lead platform engineering role"
```

## Current base format

The renderer is built around the HTML/CSS structure you provided:

- gradient header
- summary box
- achievement section
- two-column skill cards
- experience blocks
- education and certifications footer

## Recommended next steps

1. Add a write-back flow so agent requests can update stored JSON.
2. Plug in an LLM planner to rewrite summaries and bullets from user prompts.
3. Add multiple visual templates if you want different resume styles per customer.
4. Add a small web app so users can request role-specific resume variants.
