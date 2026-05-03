# Instructions

This file records the operating rules for this repository so future resume work stays consistent.

## Branch Model

- `main` is the source of truth for all shared code, templates, tests, stable resume data, and generated outputs that are intended to be reused.
- specialized branches inherit from `main`
- when shared code changes, update `main` first
- then merge `main` into the specialized branches

Current branch roles:

- `main`
  - shared repo baseline
  - shared renderer, models, storage, CLI, tests, templates
  - stable resume data and generated outputs

- `codex/mech-vikram`
  - branch for Vikram mechanical resume work
  - should carry branch-specific instructions for Vikram mechanical tailoring

- `codex/devops-cloud-aggressive`
  - branch for aggressive DevOps / Cloud resume generation
  - should carry branch-specific instructions for high-ATS aggressive tailoring

## Tailoring Levels

Use 4 levels:

1. `Base`
   - no real content change
   - render or lightly clean formatting only

2. `Tailored`
   - rewrite and reorder existing content for JD match
   - improve headline, summary, skills, and bullets
   - no invented experience

3. `Optimized`
   - aggressively reshape the base resume for ATS
   - allow stronger inferred framing from adjacent experience
   - still intended to stay broadly defensible

4. `Aggressive`
   - maximum modification level
   - full freedom to change bullets and add JD-aligned points
   - best for ATS/demo/testing
   - not constrained by strict real-resume truthfulness

Default:

- if the user says nothing, use `Tailored`
- if the user says `optimize`, use `Optimized`
- if the user says `aggressive`, use `Aggressive`

## Person Selection

When a JD is provided:

- if the user asks for `Vikram`, use Vikram’s base resume
- if the user asks for `Rajendra`, use Rajendra’s base resume

Do not assume the person when the user names one explicitly.

## Resume Workflow

1. identify the person
2. identify the tailoring level
3. update or generate the corresponding JSON
4. regenerate HTML
5. run tests when code or rendering behavior changes
6. keep branch-specific behavior recorded in that branch’s `instructions.md`
7. whenever new resume points are created, research realistic production-style patterns before writing them
8. create a local git commit whenever changes are made
9. ask for user permission before any `git push`

## Repo Rules

- JSON is the source of truth
- HTML is generated output
- keep non-interactive git workflows
- avoid destructive git commands unless explicitly requested
- keep branch-specific policy documented in `instructions.md` on that branch
- maintain `main` as the shared source of truth
- update the corresponding branches from `main` when shared rules or shared code change

## Research Rules For New Points

- this rule applies at every tailoring level whenever a new point is added
- use internet research to make new points realistic, practical, and production-like
- prefer official documentation, architecture guides, platform best practices, customer stories, and strong public resume-writing guidance
- synthesize original bullet points from that research
- do not copy someone else’s resume text verbatim
- keep the final points strong, JD-aligned, and believable for the selected tailoring level

## Git Workflow Rules

- whenever changes are made, create a local git commit
- before any `git push`, stop and ask the user for permission
- take responsibility for keeping `main` updated with shared changes
- take responsibility for updating the corresponding specialized branches locally after `main` changes
