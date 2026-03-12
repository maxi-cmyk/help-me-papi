---
name: hackathon-backend

description: Backend patterns for hackathons and small-scale apps. Use this skill when helping build backend logic for a hackathon project, small app, or prototype — including API routes, auth, database setup, and deployment. Trigger when the user mentions hackathon, prototype, MVP, demo, quick setup, or when the context is clearly small-scale (not enterprise). Covers Next.js (App Router), Python (Flask/FastAPI), Supabase, SQLite, and deployment to Vercel/Railway. This skill prioritizes speed and clarity over scalability. Also trigger when the user is debugging deployment issues, setting up auth quickly, or designing a database schema for a new project.
---

# Hackathon Backend Practices

Backend patterns optimized for speed, clarity, and demo-ability. Not enterprise architecture — just enough structure to ship something clean in 24–48 hours.

**Language default**: JavaScript. Only use TypeScript if the user explicitly asks for it or the project already uses it. When writing JS, keep it clean and readable — no type annotations, no generics, no Zod (use simple validation functions instead).

**When to use this skill**: Any hackathon project, prototype, MVP, or small app. If the user hasn't mentioned scale, assume small scale.

**When NOT to use this skill**: Production systems that serve real users at scale. Use the `nextjs-backend` skill instead for production Next.js patterns.

---

## Core Principles

1. **Ship working software, not perfect architecture.** A clean happy path that demos well beats a comprehensive system that's half-finished.

2. **Pick boring tools.** Use what the team already knows. A hackathon is not the time to learn a new framework unless the sponsor requires it.

3. **Deploy hour one, not hour last.** Get a live URL immediately. Every feature goes live as it's built. Deployment surprises at the end are project-killers.

4. **Fake what you can't build.** Hard-code responses, use mock data, seed the database. If a feature isn't essential to the demo, stub it. Judges evaluate what they see, not what you describe.

5. **One repo, one deployment.** Monorepo. No microservices. No separate frontend/backend deploys unless the stack absolutely requires it.

---

## Stack Decision Tree

Help the user pick the right stack quickly:

```
Is the frontend Next.js?
├── Yes → Next.js Route Handlers + Supabase + Vercel
└── No
    ├── Is it Python-based (ML, data, sponsor SDK)?
    │   ├── Need shared database? → FastAPI + Supabase + Railway
    │   └── Local/simple data? → Flask/FastAPI + SQLite + Railway
    └── Something else → Use whatever the sponsor provides or team knows
```

Don't let the user spend time choosing. If they're unsure, default to **Next.js + Supabase + Vercel**.

---

## API Design

### Next.js App Router

```
app/api/
├── [resource]/
│   ├── route.js          # GET (list), POST (create)
│   └── [id]/route.js     # GET (one), PATCH, DELETE
```

Every handler:
1. Validates input (simple check functions — no Zod unless using TypeScript)
2. Calls a service function (not raw DB queries in the handler)
3. Returns consistent `{ data }` or `{ error }` JSON

### Input validation (JS)

```javascript
function validateProject(body) {
  const errors = [];
  if (!body.name || typeof body.name !== 'string') errors.push('name is required');
  if (body.name && body.name.length > 100) errors.push('name too long');
  return errors;
}
```

### Error handler wrapper

```javascript
// lib/api-handler.js
export function withErrorHandler(handler) {
  return async (req) => {
    try {
      return await handler(req);
    } catch (error) {
      if (error.statusCode) {
        return NextResponse.json({ error: error.message }, { status: error.statusCode });
      }
      console.error('Unhandled:', error);
      return NextResponse.json({ error: 'Internal server error' }, { status: 500 });
    }
  };
}
```

### Python

- **Flask**: Quick, minimal. Use for simple APIs.
- **FastAPI**: Better for typed APIs, auto-generates docs at `/docs`. Prefer this if the team knows Python typing.

### What NOT to build at a hackathon

Skip: pagination, rate limiting, API versioning, GraphQL, microservices, WebSocket (unless real-time is the core feature).

Build: input validation, consistent errors, working auth on protected routes, one clean happy path.

---

## Auth

### Decision

```
Is auth essential to the demo?
├── No → Skip it entirely. Don't waste time.
└── Yes
    ├── Using Next.js + Supabase? → Supabase Auth (15 min setup)
    ├── Sponsor provides auth (Auth0, Clerk)? → Use it
    └── Python backend? → Simple JWT
```

### Supabase Auth essentials

- Server client with `@supabase/ssr`, created per-request
- Middleware to protect routes (redirect to /login if no user)
- Always use `getUser()` not `getSession()` for auth checks (getSession can be spoofed)
- Set OAuth redirect URLs for BOTH localhost AND production domain

### Pre-pitch auth checklist

- Can a fresh user sign up and use the app?
- Pre-seed a demo account so the pitch doesn't start with a signup form
- Test auth on the deployed URL, not localhost

---

## Database

### Decision

```
Using Supabase already?
├── Yes → Use Supabase Postgres (it's right there)
└── No
    ├── Deploying to Vercel? → Supabase (Vercel filesystem is ephemeral)
    ├── Deploying to Railway/Render? → SQLite or Railway Postgres
    └── Local only? → SQLite
```

### Schema rules for hackathons

- **2–3 tables max.** Users + main entity + maybe one join table.
- **Use UUID primary keys** (Supabase) or **TEXT IDs** (SQLite).
- **Use JSON columns** for flexible/uncertain data shapes.
- **Don't over-normalize.** A `status TEXT` column beats a separate statuses table.
- **Always add `created_at`.**
- **Enable RLS on Supabase.** At minimum: users can only see/edit their own data.

### Seeding

Always seed demo data. An empty app looks broken. Write a seed script or use the Supabase SQL editor.

---

## Deployment

### Decision

```
Next.js?
├── Yes → Vercel
└── No → Railway (or Render as backup)
```

### The rules

1. **Deploy in the first hour.** Push a hello world, get the URL, confirm it works.
2. **Set env vars before deploying.** A build with missing env vars breaks silently.
3. **Build locally first.** `npm run build` catches errors before the deploy does.
4. **Test the deployed version.** Demo from the production URL, not localhost.
5. **One person owns deployment.** They know the login, env vars, and how to roll back.

### Common Vercel failures

| Symptom | Likely cause | Fix |
|---------|-------------|-----|
| Works locally, blank in production | Missing env vars | Check Vercel dashboard |
| Middleware crashes | Node-only import in Edge runtime | Add `export const runtime = 'nodejs'` |
| Stale deploy | Build cache | Redeploy with cache OFF |
| API timeout | Function > 10s on free plan | Optimize or go Pro |
| OAuth redirect broken | Only localhost URL set | Add production URL to OAuth provider |

### Before the pitch

- [ ] Production URL works
- [ ] Demo account is seeded
- [ ] Full user flow works on deployed version
- [ ] Screen recording as backup if live demo fails
- [ ] Localhost running as fallback

---

## File Structure

When scaffolding a hackathon project, use this structure:

### Next.js

```
app/
├── api/
│   └── [resource]/route.js
├── (auth)/
│   └── dashboard/page.js
├── login/page.js
├── layout.js
└── page.js
lib/
├── supabase/
│   ├── server.js
│   └── browser.js
├── services/
│   └── [domain].js
├── validation.js
└── utils.js
middleware.js
scripts/
└── seed.js
```

### Python

```
app.py (or main.py)
routes/
├── auth.py
└── [resource].py
services/
└── [domain].py
db.py
models.py
requirements.txt
Procfile
```

Keep it flat. If you're creating more than 2 levels of nesting, you're over-engineering.