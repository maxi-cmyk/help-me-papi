---
name: monorepo-workflow
description: Configures GitHub action workflows for monorepos by using path filters to save resources.
---

# Monorepo CI Scoping

To avoid running backend tests when only frontend code changes (and vice versa), configure path scoping in GitHub Actions.

```yaml
on:
  push:
    paths:
      - 'backend/**'
```

If multiple workflows exist, be careful: path filtering combined with Branch Protection can block PRs forever if a required check is skipped. Use a tool like "paths-filter" action or configure skipped workflows to return a 'success' status automatically.
