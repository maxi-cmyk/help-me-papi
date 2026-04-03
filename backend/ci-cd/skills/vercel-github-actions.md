# CI/CD with Vercel + GitHub Actions

## What this covers
The full deployment pipeline for a startup: Vercel handles hosting and auto-deploys, GitHub Actions handles test/lint/type-check runs before code merges. Together they form a complete CI/CD system.

---

## How the pieces fit together

```
Developer pushes code
        │
        ▼
GitHub receives the push
        │
        ├──► GitHub Actions triggers (CI)
        │         - Install dependencies
        │         - Run linter
        │         - Run type checker
        │         - Run test suite
        │         - ✅ Pass or ❌ Fail
        │
        └──► Vercel triggers (CD)
                  - Detects the push
                  - Builds the app
                  - Deploys to preview URL (feature branches)
                  - Deploys to production (main branch only)
```

GitHub Actions and Vercel run **in parallel** — they're both triggered by the same push event. The key is using **branch protection rules** (see standards.md) to block merges to `main` unless GitHub Actions passes.

---

## Vercel Setup (one-time)

1. Go to vercel.com → New Project → Import Git Repository
2. Select your GitHub repo
3. Set the **root directory** if your frontend is in a subfolder (e.g. `frontend/`)
4. Set your **environment variables** (never hardcode secrets in code)
5. Click Deploy

After this, Vercel watches your repo automatically. No further config needed for basic deploys.

**What Vercel does on every push:**
- `feature/*` branch → builds and deploys to a unique preview URL like `your-app-git-feature-login.vercel.app`
- `main` branch → builds and deploys to your production URL

---

## GitHub Actions Setup

GitHub Actions is configured via YAML files in `.github/workflows/` at the root of your repo.

### File: `.github/workflows/ci.yml`

```yaml
name: CI

# When does this run?
on:
  push:
    branches: ["**"]        # All branches on push
  pull_request:
    branches: [main]        # PRs targeting main

jobs:
  test:
    name: Lint, Type Check, Test
    runs-on: ubuntu-latest  # The virtual machine this runs on (free)

    steps:
      # 1. Pull the code into the VM
      - name: Checkout code
        uses: actions/checkout@v4

      # 2. Set up Node.js
      - name: Set up Node.js
        uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: "npm"       # Caches node_modules between runs (faster)

      # 3. Install dependencies
      - name: Install dependencies
        run: npm ci           # Faster, stricter than npm install

      # 4. Run linter (ESLint)
      - name: Lint
        run: npm run lint

      # 5. Run type checker (TypeScript)
      - name: Type check
        run: npm run typecheck

      # 6. Run tests (Jest, Vitest, etc.)
      - name: Run tests
        run: npm test
```

Each `step` runs in sequence. If any step fails, the job fails and the PR is blocked from merging (if branch protection is set up).

---

## Understanding the YAML fields

| Field | What it means |
|---|---|
| `on: push` | Trigger when code is pushed |
| `on: pull_request` | Trigger when a PR is opened or updated |
| `runs-on: ubuntu-latest` | Use a fresh Ubuntu VM (GitHub provides this free) |
| `uses: actions/checkout@v4` | Built-in action to clone your repo into the VM |
| `run: npm ci` | Shell command to run in the VM |
| `cache: "npm"` | Reuse `node_modules` from previous runs to save time |

---

## Environment Variables

**In Vercel:** Go to Project Settings → Environment Variables. Add vars per environment (Production, Preview, Development). Vercel injects them at build time. For Next.js, prefix with `NEXT_PUBLIC_` if they need to be accessible in the browser.

**In GitHub Actions:** Go to repo Settings → Secrets and Variables → Actions → New repository secret. Reference them in your YAML with `${{ secrets.MY_SECRET }}`. Example for a DB connection during tests:

```yaml
- name: Run tests
  run: npm test
  env:
    DATABASE_URL: ${{ secrets.TEST_DATABASE_URL }}
```

---

## Common `package.json` scripts you'll need

```json
{
  "scripts": {
    "lint": "eslint . --ext .ts,.tsx",
    "typecheck": "tsc --noEmit",
    "test": "vitest run",
    "test:watch": "vitest"
  }
}
```

`tsc --noEmit` runs the TypeScript compiler to check for type errors without producing output files — exactly what you want in CI.

---

## Debugging failed runs

- Go to your GitHub repo → Actions tab → click the failed run
- Expand the failed step to see the full error log
- Common causes: missing env var, a test that only fails in clean environments, a type error that was ignored locally

---

## Monorepo note

If your repo has separate `frontend/` and `backend/` folders, you can scope workflows to only run when relevant files change:

```yaml
on:
  push:
    paths:
      - "frontend/**"   # Only trigger CI when frontend files change
```