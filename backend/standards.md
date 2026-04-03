# Backend Core Standards

Cross-cutting rules that apply to the entire backend, regardless of domain.

## API Responses
- All APIs must return JSON with a consistent shape.
- Success: `{ "data": { ... } }`
- Error: `{ "error": "Message", "details": { ... } }`

## Secrets & Config
- All secrets go in environment variables (`.env.local`), never in code.
- `.env*.local` must always be in `.gitignore`.

## Database Access
- All DB queries should go through an ORM (Prisma/Drizzle) or query builder.
- No raw SQL in route handlers or controllers.

## Security
- Rate limit all public endpoints.
- Validate all incoming request payloads against a schema (e.g. Zod).
