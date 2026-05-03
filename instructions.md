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

- `resume-creator-skill`
  - branch for Codex skill packaging work only
  - should contain the skill package directory, skill-specific instructions, and any helper assets/scripts used to distribute or install skills
  - should not be used for general resume tailoring changes unless those changes are required by the skill package itself

- `plug-in`
  - branch for Codex plugin packaging work only
  - should contain plugin manifests, packaged skills/apps, marketplace metadata, and any helper assets/scripts needed for plugin distribution
  - should not be used for general resume tailoring or generic skill-authoring changes unless those changes are required by the plugin package itself
  - current target plugin package name: `resume-creator-plugin`
  - current target plugin display name: `Résumé Creator Plugin`

- `codex/mech-vikram`
  - branch for Vikram mechanical resume work
  - should carry branch-specific instructions for Vikram mechanical tailoring

- `codex/devops-cloud`
  - branch for DevOps / Cloud resume generation
  - supports all four tailoring levels through user input

## Branch And Level Rules

- do not create separate branches for each tailoring level
- use the same functional branch and select the tailoring level from the user request
- branch purpose should be domain-specific, not level-specific
- tailoring level must be passed as input or inferred from the user request

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

Level meaning for users:

- `Base`
  - minimal change
  - use when the user wants the base resume with little or no rewriting

- `Tailored`
  - moderate JD matching
  - use when the user wants better alignment without changing the whole resume

- `Optimized`
  - stronger ATS-oriented rewriting
  - use when the user wants a more aggressive match but still not a full rewrite

- `Aggressive`
  - maximum JD matching
  - use when the user wants the resume rewritten as much as needed for the strongest ATS alignment

## Person Selection

When a JD is provided:

- if the user asks for `Vikram`, use Vikram’s base resume
- if the user asks for `Rajendra`, use Rajendra’s base resume

Do not assume the person when the user names one explicitly.

## Required User Input

When creating a resume from a JD, the request should clearly identify:

1. the person
   - `Vikram`
   - `Rajendra`

2. the tailoring level
   - `Base`
   - `Tailored`
   - `Optimized`
   - `Aggressive`

3. the job description
   - raw text
   - pasted JD
   - or a file containing the JD

Good request examples:

- `Create a Tailored resume for Vikram using this JD: ...`
- `Create an Aggressive resume for Rajendra for this role: ...`
- `Optimize Vikram's resume for this JD`

If the user does not name a level:

- default to `Tailored`

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
- keep skill packaging files and experiments on the `resume-creator-skill` branch unless they are intentionally promoted into `main`
- keep plugin packaging files and experiments on the `plug-in` branch unless they are intentionally promoted into `main`

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
