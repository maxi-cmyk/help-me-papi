# API Design Prompts

*Note: These are scaffold prompts. Always provide the AI with the suggested context files to ensure accurate results and save token usage.*

## Design endpoints for a feature
```text
Task: Design consistent REST API endpoints including methods, paths, request bodies, responses, and status codes.
Context to provide: 
- `backend/standards.md`
- `backend/decisions.md`

Input:
[Describe your feature and main entities]
```

## Design error handling system
```text
Task: Implement a global error handler and shared ApiError class with consistent error codes and production-safe logs.
Context to provide: 
- `backend/standards.md`
- `backend/decisions.md`
- `backend/security/standards.md`

Input:
[Describe your framework and specify unique requirements]
```

## Review an existing API
```text
Task: Review routes for naming, status codes, missing validation, security issues, and performance problems.
Context to provide: 
- `backend/standards.md`
- `backend/security/standards.md`
- `backend/performance/standards.md`

Input:
[Paste your routes or controller code]
```

## Set up tRPC in Next.js
```text
Task: Full tRPC setup including router, procedures, client-side provider, auth protection, and user context.
Context to provide: 
- `backend/standards.md`
- `backend/decisions.md`

Input:
[Describe your framework version, database choice, and auth provider]
```

## Add rate limiting
```text
Task: Implement rate limiting middleware with proper store selection and 429 Retry-After headers.
Context to provide: 
- `backend/security/standards.md`
- `backend/security/decisions.md`

Input:
[Describe framework, specify limits per endpoint, and storage choice]
```