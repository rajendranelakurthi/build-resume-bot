# Instructions

This file records the operating rules for this repository so future resume work stays consistent.

## Required branch and request check

Before every resume task, including follow-up edits:

1. Run `git branch --show-current` and read the current checkout's `instructions.md`, README command, and packaged resume-creator skill.
2. Read the user's current command for person, domain, and tailoring level. Do not infer the domain from prior conversation.
3. Apply current explicit user instructions first, then the active branch's rules. Reuse earlier preferences only when their branch/domain scope matches the current task. A branch switch requires re-reading these rules.
4. On `feature/rajendrapn-azure` with `Azure-devops`, use header `Lead Azure DevOps Engineer | AI | K8s` and latest AT&T title `Lead Azure DevOps Engineer`. Do not import the AWS branch's `Lead SRE` designation.
5. Before rendering and again before delivery, verify that the selected profile, header, latest AT&T designation, domain, and output manifest agree with the active branch and current command.
6. If the command conflicts with the active branch's supported domain, identify the mismatch before changing defaults or switching branches. Do not silently reuse another branch's profile or designation.

This check applies to Base, Tailored, Optimized, and Aggressive. A designation described as "standard" is scoped to its branch/domain unless the user explicitly makes it global. Never modify another branch to enforce a current branch's preference.

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
  - plugin requests should support the `devops-cloud` domain input
  - current target plugin display name: `Résumé Creator Plugin`

- `codex/devops-cloud`
  - branch for Rajendra DevOps / Cloud resume generation
  - supports all four tailoring levels through user input

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

- if the user asks for `Rajendra`, use Rajendra’s base resume

Do not assume the person when the user names one explicitly.

## Required User Input

When creating a resume from a JD, the request should clearly identify:

1. the person
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

- `Create a Tailored resume for Rajendra using this JD: ...`
- `Create an Aggressive resume for Rajendra for this role: ...`
- `Optimize Rajendra's resume for this JD`

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

## Persistent Rajendra preferences (updated 2026-09-30)
- Display name in every future resume and template-generated output: **Rajendra P N**. Retain internal person ID for compatibility.
- Azure resume header: **Lead Azure DevOps Engineer | AI | K8s**.
- Keep **10+ years** experience wording.
- On the Azure branch, focus exclusively on deep Azure DevOps and Kubernetes platform engineering. Omit multi-cloud wording, AWS technologies, and AWS certification from the displayed resume.
- Emphasize Bitrise builds, signing, provisioning, packaging, Google Play and App Store publishing, and embedded software build/release workflows. Bitrise belongs under the latest three employers per user instruction.
- Keep AI usage modest and tied to reviewed, tested automation and documentation.
- Synchronize reusable profile data in resume_data/people and plugin assets/people. Templates render the display name from full_name; do not hardcode another name.
- The user will commit changes; leave this work uncommitted.

- Every employer/project must contain at least nine distinct, substantive experience bullets in the standard base and all future resumes; preserve the requested domain focus and avoid repetitive filler.

## Current Kubernetes request (2026-10-07)

- Latest AT&T designation on this Azure branch is `Lead Azure DevOps Engineer`. AWS SRE designation rules are scoped to the AWS SRE branch.
- Use the separate `rajendra-aks-kubernetes.json` variant for the AKS role; the branch default uses Kubernetes-focused content.
- The user requested AKS, GPU nodes, Milvus/Qdrant, FastAPI/microservices and upgrade planning. GKE, Prisma/Twistlock, Dynatrace and vendor engagement remain evaluation targets per the user.

- Kubernetes profile clarification: show GKE as platform knowledge in skills only; do not claim GKE work experience.
