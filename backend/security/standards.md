# Security Standards

## Input validation
- All external input (req.body, req.params, req.query, headers) is validated with Zod before use
- Validation includes type, length limits, format, and allowed values (enum)
- Unknown fields are stripped from validated objects — never passed directly to DB queries
- Path parameter IDs are validated as the expected type (UUID, integer, etc.)

## Injection
- No raw SQL string interpolation — all queries use parameterized statements or an ORM
- If shell commands are ever necessary, use execFile with argument arrays, never exec with string concatenation

## Authentication and passwords
- All passwords hashed with argon2id or bcrypt (cost 12+)
- Rate limiting on all auth endpoints: 10 requests per 15 minutes per IP minimum
- Slow-down middleware applied before hard limit on login
- Timing-safe comparison for all token verification
- Generic error messages for auth failures — never reveal whether an email exists

## Authorization
- Every route that accesses a resource checks that the requesting user owns or is authorized for that specific resource
- No route passes req.body or req.params directly to DB queries without filtering (mass assignment prevention)
- 403 errors are logged with user ID, resource, and IP for security monitoring

## Cookies
- Session and refresh tokens: HttpOnly, Secure, SameSite=Lax
- No sensitive data in non-HttpOnly cookies

## Security headers
- Helmet applied to all routes
- CSP configured explicitly for the application's actual sources
- HSTS enabled in production

## Secrets and data
- No secrets in source code — all via environment variables
- .env*.local in .gitignore, environment variables set in platform (Vercel, Railway)
- API responses never include passwordHash, internal system fields, or full secrets
- Error responses in production never include stack traces

## Dependencies
- npm audit runs in CI and fails on high-severity vulnerabilities
- Lockfile committed and used in CI (npm ci)
- Dependencies reviewed before adding — avoid packages with low download counts or recent creation dates with wide permissions

## Logging
- Auth events (success and failure) logged with IP and timestamp
- Authorization failures logged with user ID, resource, and IP
- No passwords, tokens, or PII logged
- Structured JSON logs (Pino or Winston)

## Rate limiting
- General API: 100 requests per minute per IP
- Auth endpoints: 10 requests per 15 minutes per IP
- Password reset: 3 requests per hour per IP
- Rate limiter backed by Redis in multi-instance deployments