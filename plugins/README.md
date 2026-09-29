# Plugins

This directory is reserved for Codex plugin packaging work.

Current branch intent:

- use the `plug-in` branch for plugin package development
- keep plugin manifests, packaged skills, marketplace metadata, and plugin-specific helper scripts/assets here
- do not update this directory from `main`, `resume-creator-skill`, or `codex/devops-cloud` unless those changes are intentionally being promoted across branches

Current target plugin:

- package/folder name: `resume-creator-plugin`
- user-facing display name: `Résumé Creator Plugin`
- keep filesystem names ASCII even when the display name contains accented characters

DevSecOps support is developed on `feature/rajendrapn-devsecops`. Use `--domain devsecops --level Aggressive` with `scripts/run_resume_request.py`; see the root README for the complete command. This variant does not overwrite the DevOps/Cloud or Azure DataOps bases.
