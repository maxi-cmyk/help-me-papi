# Auth Prompts

*Note: These are scaffold prompts. Always provide the AI with the suggested context files to ensure accurate results and save token usage.*

## Implement auth from scratch
```text
Task: Full end-to-end authentication setup including schema, flows, session validation, and route protection.
Context to provide: 
- `backend/security/standards.md`
- `backend/security/skills/security-fundamentals.md`
- `backend/standards.md`

Input:
[List requirements (Email, OAuth, MFA, etc.) and your tech stack]
```

## Design role-based authorization
```text
Task: Design RBAC database schema and middleware with row-level authorization logic.
Context to provide: 
- `backend/security/standards.md`
- `backend/security/skills/security-fundamentals.md`
- `backend/security/decisions.md`

Input:
[List requirements (Roles, permissions, resource ownership rules) and tech stack]
```

## Debug OAuth flow
```text
Task: Identify and fix broken OAuth flow based on provider and callback settings.
Context to provide: 
- `backend/security/standards.md`

Input:
[Paste error logs, provider settings, callback URLs, and environment variable names]
```

## Set up JWT + Refresh rotation
```text
Task: Implement a secure JWT access and refresh token system with rotation and revocation.
Context to provide: 
- `backend/security/standards.md`
- `backend/security/skills/security-fundamentals.md`
- `backend/security/decisions.md`

Input:
[Describe your stack and token storage choice (Redis or DB)]
```