---
name: github-actions
description: Skill for setting up GitHub Actions workflows for testing, linting, and CI checks.
---

# GitHub Actions CI

Rules and structures for GitHub workflows.

## Essential CI Checks
All PRs targeting `main` must pass:
1. Lint (`npm run lint`)
2. Typecheck (`npm run typecheck` or `tsc --noEmit`)
3. Tests (`npm test`)

Use branch protection on GitHub to require these checks before merging.
