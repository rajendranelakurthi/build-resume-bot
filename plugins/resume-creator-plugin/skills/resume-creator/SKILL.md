---
name: resume-creator
description: Create tailored mechanical or DevOps/Cloud resumes for Rajendra or Vikram from job descriptions and render recruiter-ready HTML or PDF output. Use when Codex needs to choose one of the packaged base resumes, choose a domain such as mech or devops-cloud, apply a tailoring level such as Base, Tailored, Optimized, or Aggressive, rewrite the resume to match a JD, and regenerate output files.
---

# Resume Creator

Use the repo's packaged resume workflow.

1. Identify the person:
   - `Rajendra`
   - `Vikram`
2. Identify the domain:
   - `mech`
   - `devops-cloud`
3. Identify the tailoring level:
   - `Base`
   - `Tailored`
   - `Optimized`
   - `Aggressive`
4. Locate the base resume JSON in `resume_data/people/`.
5. Route to the appropriate resume variant for the selected domain.
6. Tailor the resume against the JD.
7. Regenerate HTML output.
8. Export PDF when requested.

Treat the expected plugin input contract as:

- `person`
- `domain`
- `level`
- `jd`

Return the exported PDF path as the primary output artifact when PDF generation is requested.

Follow the repository rules in `C:\Data\ai_resume\instructions.md`:

- keep JSON as the source of truth
- create a local commit when files change
- ask before any push
- use internet research when adding new points

When packaging or maintaining this plugin:

- keep the plugin manifest in `.codex-plugin/plugin.json`
- keep the marketplace entry aligned with `.agents/plugins/marketplace.json`
- keep person-specific bundled assets under the appropriate plugin folders when they are added later
