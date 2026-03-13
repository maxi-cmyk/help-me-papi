# Architecture & API

The engineering rules. How we structure Next.js/Python routes, how we seed databases, our 2-3 table limit rule, and general architectural decisions.

---

## Part 1: Architectural Decisions
Record why backend resources, prompts, and skills exist and when to use them.

### The "Vanilla-First" Principle
- **Context:** Modern backend development often reaches for heavy framework abstractions immediately, leading to massive bloat and fragile dependencies.
- **Decision:** We prioritize standard, minimal JavaScript (or Python) and avoid heavy external libraries unless strictly necessary. Stay as close to the standard library/native request tools as possible.
- **Consequences:** Faster baseline performance, easier debugging, and reduced "magic" abstractions.

---

## Part 2: API Design (Next.js / Python)
Practical API patterns for hackathons and small apps. Not enterprise architecture — just enough structure to keep your routes clean, your errors helpful, and your frontend team (or future you) not confused.

### Next.js App Router (Route Handlers)
Use when your frontend is already Next.js. No separate server needed.

```javascript
app/api/
├── projects/
│   ├── route.js              # GET (list), POST (create)
│   └── [id]/
│       └── route.js          # GET (one), PATCH (update), DELETE
```

Each `route.js` exports functions named by HTTP method. Always validate input first:

```javascript
export async function POST(request) {
  const body = await request.json();

  if (!body.name || body.name.length === 0) {
    return NextResponse.json({ error: 'Name is required' }, { status: 400 });
  }

  const project = await createProject(body);
  return NextResponse.json(project, { status: 201 });
}
```

### Python (Flask / FastAPI)
Use when the hackathon needs Python (ML models, data processing, sponsor SDK is Python-only).

- **Flask:** Quick and minimal. `@app.route('/api/projects', methods=['POST'])`
- **FastAPI:** Better for typed APIs, auto-generates docs at `/docs`.

### Rules That Save Time

1. **Consistent response shape:** 
   - Success: `{ "data": { ... } }`
   - Error: `{ "error": "What went wrong", "details": { ... } }`
   - Never return a raw array. Never mix shapes.
2. **Validate at the edge:** Check input the moment it arrives using simple JS functions (or Zod if strictly using TypeScript).
3. **Use proper HTTP status codes:** `200` (Success), `201` (Created), `400` (Bad Input), `401` (Unauthorized), `404` (Not Found), `500` (Server Error).
4. **One error handler wrapper:** Use a Higher-Order Function to try/catch routes rather than scattering try/catches everywhere.
5. **Skip over-engineering:** Don't build pagination, rate limiting, or GraphQL unless absolutely necessary for the core demo.

---

## Part 3: Database

Pick the right database, set up a clean schema, and don't lose your demo data. 
- **Next.js app:** Default to Supabase (Postgres). Auth + database + realtime in one.
- **Python backend:** Default to SQLite for speed, assuming local or persistent disk (Railway/Render).

*(Warning: SQLite on Vercel doesn't persist because the filesystem is ephemeral).*

### Schema Rules for Hackathons
1. **Start with 2–3 tables max:** Users + main entity + maybe one join table.
2. **Don't normalize too early:** A `status` text column is fine. You don't need a separate `statuses` table.
3. **Use JSON/JSONB columns:** If different items have different shapes, store them as JSON (`data jsonb default '{}'`) rather than constantly altering the schema mid-hackathon.
4. **IDs & Timestamps:** Use `uuid` for IDs and always include a `created_at` timestamp.
5. **Row Level Security (RLS):** If using Supabase, ALWAYS enable RLS. At minimum, ensure users can only see/edit their own data.

### Seeding
Always seed demo data. An empty app looks broken during a pitch. Write a `scripts/seed.js` script or use the Supabase SQL editor to insert realistic demo data beforehand.
