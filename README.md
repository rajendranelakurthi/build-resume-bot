# AWS SRE Resume Agents

Repository foundation for managing resume content for multiple people and rendering each resume into a shared HTML layout.

## First-time setup for Codex IDEs

1. Open this repository in a Codex-supported IDE, such as VS Code or Antigravity.
2. Switch to the plugin branch:

```bash
git switch feature/rajendrapn-aws-sre
```

3. Install the resume creator plugin:

```bash
bash plugins/resume-creator-plugin/scripts/install_plugin.sh
```

4. Restart the IDE so Codex can load the installed plugin.
5. In Codex, use this command format:

```text
Use the Résumé Creator Plugin to create an Aggressive aws-sre resume for Rajendra using this JD: <provide JD>
```

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
python -m resume_agents.cli request --person rajendra-prasad-n --message "Tailor my resume for a senior AWS SRE role"
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

## AWS SRE default

The repository and bundled plugin use the same AWS SRE base profile. The default domain is `aws-sre`; `devops-cloud` remains a compatibility alias. Use Python 3.12 on this Mac.

```bash
python3.12 plugins/resume-creator-plugin/scripts/run_resume_request.py --person Rajendra --level Base
```

See [AWS SRE role guide](docs/aws-sre-role-guide.md) for researched responsibilities, AWS references, and qualification validation. Historical tailored outputs and the explicit Azure DataOps variant remain separate from the default.
