# Rajendra Azure DevOps Resume Creator

This branch generates Azure DevOps resumes for Rajendra, focused on software automation, CI/CD, AWS, Bicep, secure connectivity, and production support.

## First-time setup for Codex IDEs

1. Open this repository in a Codex-supported IDE, such as VS Code or Antigravity.
2. From the repository root, switch to the Azure branch:

```bash
git switch feature/rajendrapn-azure
```

3. Install the resume creator plugin:

```bash
bash plugins/resume-creator-plugin/scripts/install_plugin.sh
```

4. Restart the IDE so Codex can load the installed plugin.
5. In Codex, use this command format:

```text
Use the Résumé Creator Plugin to create an Aggressive Azure-devops resume for Rajendra using this JD: <provide JD>
```

## Azure DevOps command

```bash
python3.12 plugins/resume-creator-plugin/scripts/run_resume_request.py \
  --person Rajendra --domain azure-devops --level Aggressive \
  --jd-file plugins/resume-creator-plugin/assets/jds/azure-devops-developer.txt \
  --output-dir tailored_resume/rajendra-prasad-n
```

Replace the JD file with your own as needed. Requires Python 3.10+ and Chrome/Edge for PDF export. `Azure-devops` is case-insensitive; legacy `devops-cloud` is an Azure-led alias. Filenames and manifests use `azure-devops`. Other domains are rejected on this branch.

Outputs: HTML, PDF, structured profile JSON, and manifest. Base renders the authored Azure profile; Tailored, Optimized, and Aggressive rank approved content against the JD. They currently share the same ranking engine. Employment history and certifications are preserved. AWS, Bicep, certificate lifecycle management, and encrypted database connectivity are included following user confirmation.

Both `resume_data/people/rajendra-prasad-n.json` and the bundled profile contain the Azure branch content. The repository and packaged HTML templates use the same Azure visual style. The backend preserves the authored summary rather than presenting unsupported JD terms as candidate skills.

These are branch-local changes. Refresh the installed plugin separately when you want Codex's installed copy to use this version.

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
