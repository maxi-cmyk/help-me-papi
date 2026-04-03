---
name: webdev-backend
description: Backend patterns for startups and scalable web applications. Prioritizes maintainability, strict typing, security, and robust architecture over immediate speed. Use this skill when building a production-ready web app.
---

# Startup / Web Dev Backend Practices

Patterns optimized for startups where code will live for years, teams will grow, and features will scale. Unlike hackathons, this focuses heavily on safety, CI/CD, and structured architecture.

**Language default**: TypeScript. Do not write raw JavaScript. Use strict mode, explicit interfaces for API contracts, and robust type inference (e.g., via Prisma or Drizzle).

**When to use this skill**: When building a production application, SaaS, or any project where you care about the codebase 6 months from now.

**When NOT to use this skill**: 24-hour hackathons, quick weekend prototypes, or throwaway scripts. Use `hackathon-backend` instead.

---

## Core Principles

1. **Maintainability over immediate speed.** Invest in CI/CD, strict typings, and tests up front. Setting up a staging environment and database migrations takes an extra day now but saves weeks later.
2. **Layered Architecture.** Never put raw business logic or database queries directly in the route handlers. Separate routing (controllers) from business logic (services/use-cases) and data access (repositories/DAOs).
3. **Defensive Programming.** Validate all inputs at the boundary using a schema library like Zod. Never trust client data, and never assume the database is perfectly clean.
4. **Secure by Default.** Employ Role-Based Access Control (RBAC), rate limiting, and parameterized queries. Store all secrets in a centralized vault or secure environment variables.

---

## Stack Decision Tree

Help the user architect the startup stack:

```
Is the frontend Next.js?
├── Yes
│   ├── Is it highly relational/structured data? → Next.js App Router + Postgres (Neon/Supabase) + Drizzle/Prisma + Vercel
│   └── Is it a purely real-time/sync heavy app? → Next.js + Convex or Supabase Realtime
└── No (e.g. React SPA, Mobile App, or Heavy background processing)
    ├── Does it require intensive background workers/AI? → Separate FastAPI/NodeJS Backend + Railway/Render + BullMQ/Celery
    └── Is it a standard CRUD / SaaS API? → NestJS or Express/Fastify + TypeScript + Postgres
```

---

## API Design

### Next.js App Router with Service Layer

```
app/api/
├── [resource]/
│   ├── route.ts          # Purely handles HTTP (req/res)
```

The route handler is intentionally "thin":

1. **Parse and Validate:** Validate `req.json()` using Zod.
2. **Auth Check:** Verify session and RBAC permissions.
3. **Call Service:** Pass the validated data to a service function.
4. **Return Response:** Return standard JSON or error.

### Zod Boundary Validation

```typescript
import { z } from "zod";

const CreateProjectSchema = z.object({
  name: z.string().min(3).max(100),
  description: z.string().optional(),
  ownerId: z.string().uuid()
});

// Inside route:
const data = CreateProjectSchema.parse(await request.json());
```

### Global Error Standard

Never let raw database errors leak to the client.

```typescript
export function apiResponse(data: any, status = 200) {
  return NextResponse.json({ data }, { status });
}

export function apiError(message: string, status = 400, details?: any) {
  return NextResponse.json({ error: message, details }, { status });
}
```

---

## Auth

### Decision

```
Do you want to own your auth data locally?
├── Yes (Need full control over DB users table) → Auth.js (NextAuth) or Lucia Auth
└── No (Happy to outsource to managed service)
    ├── Need enterprise features (SAML, B2B)? → Clerk or WorkOS
    └── Need deep Postgres integration with RLS? → Supabase Auth
```

### Production Auth Essentials

- **Session vs JWT:** Prefer secure HttpOnly cookies + Session storage (or short-lived secure JWTs with refresh token logic) over storing JWTs in `localStorage`.
- **RBAC (Role Based Access Control):** Always verify *authorization*, not just *authentication*. Checking if a user is logged in is not enough; check if they have permission to access the specific resource (e.g. `WHERE org_id = user.org_id`).
- **Audit Logs:** Log critical auth events (password changes, 2FA setup, dangerous deletions).

### Production Auth Checklist
- [ ] OAuth flow requires state/nonce validation (CSRF protection).
- [ ] Cookies are configured with `Secure`, `HttpOnly`, and `SameSite=Lax`.
- [ ] Rate limiting is applied to all `/login` and `/reset-password` routes to prevent brute force attacks.

---

## Database

### Decision

```
Are you using Postgres? (You should be.)
├── Need fully serverless + branch previews? → Neon
├── Need built-in Auth + Realtime + RLS? → Supabase
└── Need heavy analytics/reporting? → ClickHouse (Separate from Postgres)
```

### Schema Rules for Production

- **Migrations are mandatory.** Use Prisma Migrate or Drizzle Kit. Never manually `ALTER TABLE` in production.
- **Foreign Keys and Constraints:** Lean heavily on the database. Use `ON DELETE CASCADE` where appropriate, enforce `UNIQUE` constraints.
- **Indexing:** Add indexes on any column used frequently in `WHERE`, `JOIN`, or `ORDER BY` clauses.
- **Connection Pooling:** In serverless environments, always use a connection pooler (like PgBouncer or Supavisor) to avoid exhausting DB connections.
- **No N+1 Queries:** Always eager-load related data (e.g., Prisma `include`) to prevent database spam.

---

## Deployment & Infra

### CI/CD

Automation is mandatory. Use GitHub Actions for continuous integration.
- Code cannot be merged into `main` without passing:
  1. Linting (`eslint`)
  2. Type Checking (`tsc --noEmit`)
  3. Automated Tests (`vitest` / `jest`)

### Staging Environment

- Never deploy directly to production without testing.
- Utilize Vercel Preview deployments connected to a *development* or *branch* database (e.g. Neon branching).

### Common Production Failures

| Symptom | Likely cause | Fix |
|---------|-------------|-----|
| Sporadic 500s under load | Connection pool exhaustion | Implement PgBouncer / external pooler |
| Analytics query crashes app | Table locks on big reads | Move analytics to ClickHouse / read replica |
| Slow API response | Missing database index | Run `EXPLAIN ANALYZE` and add B-tree indexes |
| CI Type Check passes but build fails | Differing Node versions | Freeze version using `.nvmrc` and `npm ci` |

---

## File Structure

For a robust startup backend in Next.js, use a domain-driven or layered structure:

```
app/
├── api/
│   └── [domain]/route.ts       # Thin controllers
src/ (or lib/)
├── db/
│   ├── schema.ts               # Drizzle/Prisma schema
│   └── index.ts                # DB connection/pool
├── services/
│   └── [domain].ts             # Core business logic (e.g., paymentService.ts)
├── validation/
│   └── [domain].schema.ts      # Zod schemas
└── utils/
    ├── api-handler.ts          # Global error wrappers
    └── logger.ts               # Structured logging
```

Keep business logic completely decoupled from Next.js logic. You should be able to call a service function from an API route, a script, or a background cron job without modifying the service itself.
