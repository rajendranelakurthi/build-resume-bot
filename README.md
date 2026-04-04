# Multi-Person Resume Agents

Repository foundation for managing resume content for multiple people and rendering each resume into a shared HTML layout.

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
.venv\Scripts\activate
pip install -e .
python -m resume_agents.cli list-people
python -m resume_agents.cli render-html --person vikram-bathala --output examples/vikram-bathala.html
python -m resume_agents.cli request --person vikram-bathala --message "Tailor my resume for a lead platform engineering role"
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
