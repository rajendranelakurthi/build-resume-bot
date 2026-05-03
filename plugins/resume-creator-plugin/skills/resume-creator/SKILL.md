---
name: resume-creator
description: Create tailored resumes for Rajendra or Vikram from job descriptions and render recruiter-ready HTML or PDF output. Use when Codex needs to choose one of the packaged base resumes, apply a tailoring level such as Base, Tailored, Optimized, or Aggressive, rewrite the resume to match a JD, and regenerate output files.
---

# Resume Creator

Use the repo's packaged resume workflow.

1. Identify the person:
   - `Rajendra`
   - `Vikram`
2. Identify the tailoring level:
   - `Base`
   - `Tailored`
   - `Optimized`
   - `Aggressive`
3. Locate the base resume JSON in `resume_data/people/`.
4. Tailor the resume against the JD.
5. Regenerate HTML output.
6. Export PDF when requested.

Follow the repository rules in `C:\Data\ai_resume\instructions.md`:

- keep JSON as the source of truth
- create a local commit when files change
- ask before any push
- use internet research when adding new points

When packaging or maintaining this plugin:

- keep the plugin manifest in `.codex-plugin/plugin.json`
- keep the marketplace entry aligned with `.agents/plugins/marketplace.json`
- keep person-specific bundled assets under the appropriate plugin folders when they are added later
