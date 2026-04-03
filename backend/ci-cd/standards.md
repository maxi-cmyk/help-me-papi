# CI/CD Standards

## Branch strategy
- `main` is always production-ready and deployed live
- `feature/*` or `fix/*` branches for all work in progress
- Never push directly to `main` — always go through a PR

## Branch protection rules (set on GitHub)
Go to repo Settings → Branches → Add rule for `main`:
- Require status checks to pass before merging
  - Select your GitHub Actions job (e.g. `Lint, Type Check, Test`)
- Require pull request reviews before merging
- Require branches to be up to date before merging
- Do not allow bypassing the above settings

This means: if CI fails, the merge button is greyed out. No exceptions.

## Secrets
- Never commit API keys, database URLs, or tokens to the repo
- All secrets go in: Vercel (for runtime) and GitHub Secrets (for CI)
- Use `.env.local` locally, never `.env` committed to git
- `.env*.local` should always be in `.gitignore`

## What CI must always check
At minimum, every PR must pass:
1. Linting (no ESLint errors)
2. Type checking (no TypeScript errors)
3. Tests (all passing)

## Vercel deploy settings
- Production branch: `main`
- Preview branches: all others
- Build command: whatever your framework needs (Vercel usually auto-detects)
- Do not expose `NEXT_PUBLIC_` vars that should stay server-side