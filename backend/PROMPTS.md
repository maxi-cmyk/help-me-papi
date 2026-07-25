# Backend Agentic Macro Library

> [!IMPORTANT]
> **HOW TO USE THIS LIBRARY**
> 1. **Context First**: Always provide `skills/SKILLS.md` and your current `docs/techStack.md` as context before running these macros.
> 2. **Chained Development**: Use the output of `ARCHITECT_DATABASE` to feed into `SCAFFOLD_API_ROUTE`.
> 3. **Validation**: Every macro includes a mandatory "Verification" step to ensure runtime stability.

---

### **Stage 1: Foundation & Schema**

#### **Macro: ARCHITECT_DATABASE**
```markdown
[ROLE] You are a Senior Database Architect.
[CONTEXT] Analyze the `docs/PRD.md` and `docs/techStack.md`.
[TASK] Design a scalable, performant database schema for the project's core entities.

[CONSTRAINTS]
- Database: Supabase (PostgreSQL).
- Keep the schema flat where possible.
- Use JSON columns for flexible/extensible data.
- Max 3-5 tables for the MVP.

[OUTPUT]
1. SQL Schema: `CREATE TABLE` statements with proper indexing.
2. RLS POLICIES: Row Level Security rules for each table.
3. SEED SCRIPT: A robust `seed.sql` with realistic demo data.
4. DIAGRAM: A mermaid.js ERD for visualization.
```

---

### **Stage 2: API & Logic**

#### **Macro: SCAFFOLD_API_ROUTE**
```markdown
[ROLE] You are a Backend Engineer.
[CONTEXT] Analyze the Database Schema and the `features/` directory structure.
[TASK] Scaffold a new API route for a specific resource.

[INPUT]
- Resource: [e.g. projects, tasks]
- Operations: [e.g. GET, POST, DELETE]
- Auth Required: [Yes/No]

[STEPS]
1. SCHEMA VALIDATION: Use `zod` or equivalent for input validation.
2. SERVICE LAYER: Write the query functions in a separate service file.
3. HANDLER: Implement the route handler with proper error status codes.
4. AUTH: Implement user-ID filtering if the route is protected.

[OUTPUT]
Return the code for the handler, service, and a `curl` test command.
```

#### **Macro: AUTH_INTEGRATION**
```markdown
[ROLE] You are a Security Engineer.
[CONTEXT] Analyze the existing middleware and auth client setup.
[TASK] Wire authentication into a new or existing module.

[PREFERRED STACK]
- Managed auth (Clerk-style) or Supabase Auth over hand-rolled JWT unless there's a hard reason not to.
- Passkeys (WebAuthn) as the default first-factor where the provider supports it; fall back to OAuth 2.1 (with PKCE, mandatory for public clients) for social login.
- Short-lived access tokens + rotating refresh tokens; never long-lived tokens in localStorage.

[OUTPUT]
1. AUTH CLIENT: Setup code for the chosen provider (Clerk/Supabase Auth/custom JWT).
2. PASSKEY/OAUTH FLOW: Registration + login wiring, including PKCE for OAuth 2.1 and WebAuthn ceremony for passkeys.
3. MIDDLEWARE: Route protection logic with redirect handling.
4. HOOKS: A `useAuth` or `getServerUser` helper for session access.
5. SIGNUP/LOGIN: Production-ready forms and state handling, including passkey enrollment prompts.
```

#### **Macro: OBSERVABILITY_SETUP**
```markdown
[ROLE] You are a Site Reliability Engineer.
[CONTEXT] Analyze the service entrypoints (API routes, background jobs, cron handlers).
[TASK] Instrument the service with structured logging, tracing, and rate limiting so incidents are diagnosable in production.

[CHECKLIST]
1. STRUCTURED LOGGING: JSON logs (e.g. Pino) with request ID, user ID (if authed), route, latency, and status on every request.
2. TRACING: Propagate a `trace_id`/`request_id` across service boundaries (DB calls, external APIs, queues); wire OpenTelemetry if the stack supports it.
3. ERROR ENVELOPE: All errors follow the shared `{ "error": { "code", "message", "details" } }` shape (see `docs/api-standards.md`)  never leak stack traces to clients.
4. RATE LIMITING: Apply per-IP/per-user limits at the edge or middleware layer; return `Retry-After` on 429s.
5. ALERTING: Define the SLO (e.g. p99 latency, error rate) and the alert threshold that pages someone.

[OUTPUT] Instrumented code + a short runbook: "if X metric fires, check Y first."
```

---

### **Stage 3: Diagnostics & Optimization**

#### **Macro: DEBUG_RUNTIME_ERROR**
```markdown
[ROLE] You are a Debugging Specialist (SRE).
[CONTEXT] Paste the error logs (Vercel/Terminal) and the failing code block.
[TASK] Perform a root-cause analysis and provide a fix.

[DIAGNOSTIC CHECKLIST]
1. ENV VARS: Check for missing secrets in the current scope.
2. RUNTIME: Check for Edge vs Node mismatch.
3. NETWORK: Inspect for hardcoded localhost URLs or CORS issues.
4. DATABASE: Check RLS policy violations or connection timeouts.

[OUTPUT] A step-by-step fix and a `console.log` strategy to prevent recurrence.
```

#### **Macro: OPTIMIZE_PERFORMANCE**
```markdown
[ROLE] You are a Performance Engineer.
[CONTEXT] Paste the slow query or handler code.
[TASK] Reduce latency and improve throughput.

[CHECKLIST]
1. INDEXING: Suggest missing Postgres indexes.
2. CACHING: Implement Vercel Data Cache or Redis.
3. FETCHING: Fix N+1 query problems.
4. PAYLOAD: Minimize JSON response sizes.

[OUTPUT] Refactored code + a "Before vs After" latency estimate.
```
