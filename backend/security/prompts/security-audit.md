# Security Prompts

*Note: These are scaffold prompts. Always provide the AI with the suggested context files to ensure accurate results and save token usage.*

## Security audit of an existing API
```text
Task: Audit this API code for security vulnerabilities. Explain each issue, the attack scenario, and provide a fix.
Context to provide: 
- `backend/security/standards.md`
- `backend/security/skills/security-fundamentals.md`
- `backend/security/decisions.md`

Input:
[Paste your route handlers, middleware, or full file code]
```

## Implement rate limiting
```text
Task: Implement robust rate limiting with proper 429 responses, slow-down middleware, and Redis support where required.
Context to provide: 
- `backend/security/standards.md`
- `backend/security/skills/security-fundamentals.md`
- `backend/security/decisions.md`

Input:
[Describe endpoints, required limits, and deployment environment]
```

## Audit for IDOR vulnerabilities
```text
Task: Check every route for insecure direct object reference (IDOR) vulnerabilities and show corrected code.
Context to provide: 
- `backend/security/standards.md`
- `backend/security/skills/security-fundamentals.md`
- `backend/security/decisions.md`

Input:
[Paste your API route handlers]
```

## Set up security headers
```text
Task: Configure security headers using Helmet or platform-specific methods, including a tailored CSP.
Context to provide: 
- `backend/security/standards.md`
- `backend/security/skills/security-fundamentals.md`
- `backend/security/decisions.md`

Input:
[Describe your framework, deployment platform, and asset sources (fonts, APIs, etc.)]
```

## Review error handling for information leakage
```text
Task: Check for production information leakage (stack traces, DB errors, internal state) and suggest improvements.
Context to provide: 
- `backend/security/standards.md`
- `backend/security/skills/security-fundamentals.md`
- `backend/security/decisions.md`

Input:
[Paste your error handling middleware or code]
```

## Implement input validation with Zod
```text
Task: Define Zod schemas and add validation logic for body, params, and query objects.
Context to provide: 
- `backend/security/standards.md`
- `backend/security/skills/security-fundamentals.md`
- `backend/security/decisions.md`

Input:
[Paste your route handlers and specify validation requirements]
```