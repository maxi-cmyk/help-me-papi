# CI/CD Decisions

## Vercel over Netlify or Railway for frontend hosting
Vercel has first-class Next.js support (same team), best DX for preview deployments, and the free tier is generous for startups. Railway is better for dedicated backend services (APIs, workers) that aren't serverless.

## GitHub Actions over CircleCI / Jenkins
GitHub Actions is free for public repos and has a generous free tier for private repos (2,000 min/month). It lives inside GitHub so there's no separate service to manage. CircleCI can be faster at scale, but that's a later problem.

## `npm ci` over `npm install` in CI
`npm ci` installs from `package-lock.json` exactly, without modifying it. This ensures CI uses the same versions as local development. `npm install` can silently update the lockfile, causing "works on my machine" bugs.

## `tsc --noEmit` for type checking in CI
Running the compiler without emitting files is the cleanest way to type-check in CI. It catches all type errors that might be suppressed by editor plugins or `any` casts. Keeps the build step separate from type checking.

## Parallel Vercel + GitHub Actions (not sequential)
Vercel and GitHub Actions both trigger on push and run independently. We don't block Vercel deploys on CI passing — preview URLs still generate even if tests fail. Only merges to `main` are blocked by branch protection. This lets you still share a preview URL for visual review even while debugging a test.