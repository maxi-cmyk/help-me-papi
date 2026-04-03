# CI/CD Prompts

## Debug a failing GitHub Actions run
```
Here is the error output from a failed GitHub Actions CI run:

[paste the error log here]

My workflow file:
[paste .github/workflows/ci.yml]

My package.json scripts:
[paste scripts section]

What is failing and how do I fix it?
```

## Write a CI workflow from scratch
```
Write a GitHub Actions CI workflow for a [Next.js / React + Vite / Node.js Express] project.
It should run on every push and on PRs to main.
Steps needed: install dependencies, lint with ESLint, type-check with TypeScript, run tests with [Jest / Vitest].
The project uses npm. Node version: 20.
```

## Set up branch protection rules
```
Explain step by step how to set up GitHub branch protection rules for a repo called [repo name]
so that merges to main are blocked unless a GitHub Actions job called "[job name]" passes.
Include screenshots description or menu paths.
```

## Debug a Vercel build failure
```
My Vercel deployment is failing at build time. Here is the error:

[paste Vercel build log]

My project structure: [describe or paste directory tree]
Framework: [Next.js / Vite / etc]
Root directory setting in Vercel: [what you set]

What is wrong and how do I fix it?
```

## Add a new environment variable
```
I need to add a new environment variable called [VAR_NAME] to my project.
It is a [server-side secret / client-side public value].
I am using Next.js deployed on Vercel.
Explain where to add it in Vercel, how to reference it in code, and whether I need NEXT_PUBLIC_ prefix.
```