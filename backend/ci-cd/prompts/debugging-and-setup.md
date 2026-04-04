# CI/CD Prompts

*Note: These are scaffold prompts. Always provide the AI with the suggested context files to ensure accurate results and save token usage.*

## Debug a failing GitHub Actions run
```text
Task: Identify and fix a failing GitHub Actions CI pipeline.
Context to provide: 
- `.github/workflows/ci.yml`
- `package.json`

Input:
[Paste your error logs and failing scripts here]
```

## Write a CI workflow from scratch
```text
Task: Write a complete GitHub Actions CI workflow with caching, linting, type-checking, and tests.
Context to provide: 
- `package.json`

Input:
[Describe your framework, testing tools, and target Node version]
```

## Branch protection rules
```text
Task: Explain step by step how to set up GitHub branch protection rules to block unverified unmerges.
Context to provide: 
- Internal project standards (if any)

Input:
[Specify repo and job names]
```

## Debug a Vercel build failure
```text
Task: Identify and fix a Vercel build failure.
Context to provide: 
- Project structure
- `package.json`

Input:
[Paste Vercel logs and root directory setting]
```

## Add a new environment variable
```text
Task: Full guide for adding a new variable across environments with reference code.
Context to provide: 
- `backend/security/standards.md`

Input:
[Specify variable name, scope (secret/public), and framework/hosting]
```