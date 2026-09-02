# Resume Workflow Playbook

This file is the working memory for resume generation, resume tailoring, HTML rendering, and recruiter-style review in this repository.

It is intended to be updated over time as new patterns, constraints, and quality checks are learned.

## Scope

This repo currently supports:

- base resume data stored as JSON
- HTML rendering from structured resume data
- tailored resume variants for specific job descriptions
- reusable additional sections such as Research Experience and Academic Projects
- print-friendly A4 output
- recruiter-style and ATS-style review passes

Primary example profile:

- `C:\Data\ai_resume\resume_data\people\rajendra-prasad-n.json`

Locked DevOps / Cloud base profile:

- `C:\Data\ai_resume\resume_data\people\rajendra-prasad-n.json`
- Use this as the default source profile for Rajendra P N DevOps / Cloud job tailoring requests.
- Do not overwrite it with JD-specific wording; generate tailored variants from it.

Primary tailored example:

- `C:\Data\ai_resume\tailored_resumes\rajendra-prasad-n\insight-global-mid-cloud-engineer.json`

## Core Files

- Base template: `C:\Data\ai_resume\templates\base_resume.html`
- HTML renderer: `C:\Data\ai_resume\src\resume_agents\renderers\html_resume.py`
- Models: `C:\Data\ai_resume\src\resume_agents\models.py`
- JSON store: `C:\Data\ai_resume\src\resume_agents\storage\json_store.py`
- Base example output: `C:\Data\ai_resume\examples\rajendra-prasad-n.html`
- Tailored example output: `C:\Data\ai_resume\tailored_resumes\rajendra-prasad-n\insight-global-mid-cloud-engineer.html`

## Standard Workflow

1. Extract resume content from the source file into structured JSON.
2. Preserve real meaning from the source resume instead of aggressively compressing it.
3. Render a first HTML version using the shared template.
4. Restore anything important that was omitted.
5. Rewrite wording to sound more senior, cleaner, and ATS-friendly.
6. Tailor for the target JD without echoing the JD too literally.
7. Regenerate HTML.
8. Run validation.
9. Run an independent recruiter-style review pass before finalizing.

## Resume Quality Rules

- Preserve the actual meaning of the candidate's experience.
- Do not invent federal, compliance, or domain experience unless explicitly supported.
- Prefer stronger wording, but do not turn bullets into generic buzzword statements.
- Use AWS-first wording when the user asks for AWS emphasis, but keep the original intent truthful.
- Avoid obvious JD mirroring.
- Make the resume sound like a strong, credible, hands-on engineer.
- Keep the final language recruiter-readable, not just ATS-readable.

## Rajendra-Specific Learned Rules

- Certifications should appear near the top of the HTML resume.
- Certification badges must render cleanly and not depend on broken external paths.
- A4 print layout needs explicit print rules; web breakpoints alone are not enough.
- Inline label bullets like `Migration Delivery Supported...` look awkward in print without better separation.
- Avoid redundant bullets in the same role, especially around:
  - architecture diagrams
  - IAM mappings
  - logging standards
  - runbooks
  - workshops / alignment sessions
- DevSecOps should be visible in both:
  - recent experience bullets
  - top highlights / summary sections

## Tailoring Rules For JD Alignment

When tailoring for a job description:

- Make at least 5 to 6 points align strongly to the role.
- Do not reuse the employer's phrasing too directly.
- Spread relevance across summary, highlights, skills, and recent roles.
- Use natural language substitutions instead of JD repetition.

Examples:

- Prefer `deployment tooling` instead of repeating `system agents` everywhere.
- Prefer `operational telemetry` instead of repeating `logging configurations` in every section.
- Prefer `access model differences` or `target-state access patterns` instead of repeating only `IAM roles`.

## Strong Resume Signals To Prefer

- migration ownership
- reusable Terraform / CloudFormation modules
- CI/CD modernization
- multi-account AWS environments
- EKS platform engineering
- observability and production support
- IAM and secure network design
- documentation that supports implementation and operations
- cross-team technical alignment
- DevSecOps controls inside delivery workflows

## DevSecOps Coverage Checklist

When a user asks to strengthen DevSecOps, look for opportunities to add credible details such as:

- secure runner standards
- branch protections
- secrets handling
- SAST
- DAST
- artifact scanning
- image validation
- policy checks
- Terraform validation
- gated approvals
- software supply chain controls

Do not add all of them blindly. Use only what fits the candidate's background and role context.

## Reviewer Pass Requirement

Before considering a tailored resume finished:

1. Run an independent reviewer or subagent pass.
2. Ask the reviewer to judge the resume like the recruiter who posted the role.
3. Validate these points:
   - Does it sound like a strong senior engineer?
   - Are at least 5 to 6 bullets strongly aligned to the JD?
   - Does it avoid sounding like it was copied from the JD?
4. Apply any realism-focused rewrites.

If the subagent limit is reached, reuse an existing reviewer agent instead of skipping this step.

## Bullet Management Rules

- Respect repo tests that expect specific bullet counts where applicable.
- If new emphasis needs to be added, first try folding it into existing bullets instead of always increasing counts.
- Remove overlap before adding more bullets.
- Prefer distinct bullet jobs:
  - delivery
  - architecture
  - automation
  - security
  - observability
  - stakeholder alignment

## Rendering Notes

- JSON is the source of truth.
- Regenerate HTML after JSON changes.
- Base and tailored versions may diverge intentionally.
- `Project:` lines should not be rendered in experience sections.
- `Client:` and `Skills Used:` can remain when they add value.
- Use `additional_sections` when a resume has important content that should not be collapsed into professional experience, such as research roles, publications, or academic project portfolios.
- For Rajendra DevOps tailoring, start from `rajendra-prasad-n` rather than the existing DevOps/cloud Rajendra profile.

## Validation

Run:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
python -m resume_agents.cli list-people
python -m resume_agents.cli render-html --person rajendra-prasad-n --output examples/rajendra-prasad-n.html
python -m resume_agents.cli request --person rajendra-prasad-n --message "Tailor my resume for a lead cloud storage engineering role"
```

Expected current baseline:

- all tests passing

## Regeneration Pattern

Use the shared renderer with `PersonProfile`, `Experience`, and `Education` objects loaded from JSON, then write the rendered HTML back to the appropriate output file.

Common outputs:

- `C:\Data\ai_resume\examples\rajendra-prasad-n.html`
- `C:\Data\ai_resume\tailored_resumes\rajendra-prasad-n\insight-global-mid-cloud-engineer.html`

## Finish Criteria

A resume is ready when:

- the content is truthful
- the wording is strong and professional
- the role alignment is clear
- the language does not look copied from the JD
- DevSecOps, cloud, and delivery themes are visible where relevant
- the HTML renders correctly on web and print
- tests pass
- a reviewer-style pass does not flag obvious realism problems

## Maintenance Note

This document should be updated whenever a new lesson is learned about:

- ATS alignment
- recruiter perception
- JD tailoring
- print layout issues
- bullet quality
- repetition and realism
- rendering behavior
