# PROMPTS
Copy-paste templates to instruct LLMs on how to write code for your backend or debug complex runtime errors. Make sure `skills/SKILLS.md` is provided as system context before using these.

---

## AI Implementation Templates
Use these to generate feature code fast. Fill in the brackets before prompting.

### Scaffold a New API Route
```text
Create a new API route for my app.

**Stack:** [e.g. Next.js App Router / Flask / FastAPI]
**Language:** JavaScript (unless I say otherwise)
**Resource:** [e.g. projects, tasks, submissions]
**Operations needed:** [e.g. list all, get one, create, update, delete]

**Fields:**
- [field name] — [type and any constraints, e.g. "name — string, required"]

**Auth:** [is this route protected? should it filter by logged-in user?]
**Database:** [Supabase / SQLite / other]

Give me:
1. The route handler file(s) with input validation
2. The service/query functions (keep DB logic separate from handler)
3. The SQL schema
4. A quick curl test to verify

Keep it simple. No pagination, no rate limiting, no middleware. JavaScript, not TypeScript.
```

### Add Auth to an Existing App
```text
I need to add authentication to my app.

**Stack:** [e.g. Next.js + Supabase / Flask + JWT]
**What exists already:** [routes, pages, database tables]
**Auth requirements:**
- Sign up method: [email+password / OAuth]
- What needs protecting: [which routes need login]
- User data needed: [email, name, role?]

**Current file structure (relevant bits):**
[paste the key files]

Give me:
1. Auth client setup
2. Sign up / login functions
3. Middleware route protection
4. How to get the current user in any route

Wire it into my existing code — show me what to add and exactly where.
```

### Set Up the Database
```text
I need to set up the database for my project.

**Database:** [Supabase / SQLite]
**App purpose:** [e.g. users submit projects and vote]
**Main entities:** [users, projects, votes]

**For each entity, what I know so far:**
- [entity]: [fields and relationships]

Give me:
1. The full SQL schema (CREATE TABLE statements)
2. Supabase RLS policies (if applicable)
3. The query functions I'll need
4. A seed script with realistic demo data

Keep the schema flat. Use JSON columns for flexible data. 2-3 tables max.
```

---

## AI Debugging Templates
Use these when something is broken in production or local development.

### "Works locally but not deployed"
```text
Something works on localhost but is broken on the deployed version. Help me debug.

**Stack:** [e.g. Next.js + Supabase + Vercel]
**What works locally:** [describe the feature]
**What happens in production:** [blank page, error, 500, loading forever]
**Error messages:** [paste any Vercel logs, network tab outputs, etc.]

Check these in order and tell me which is most likely:
1. Missing environment variables in production scope
2. Edge runtime vs Node runtime mismatch
3. Hardcoded localhost URLs in the code
4. OAuth redirect URLs mismatching domains
5. API route timeout limits

Tell me exactly what to check and where.
```

### "API route returns 500 Error"
```text
I'm getting a 500 error from an API route. Help me find the problem.

**Stack:** [e.g. Next.js App Router]
**Route:** [e.g. POST /api/projects]
**Request body sent:** [paste JSON]
**What actually happens:** [500 error]

**Server logs / output:**
[paste terminal/Vercel logs]

**The route handler code:**
[paste the full route handler]

Walk through the code line by line and identify the failure. If logs are vague, tell me exactly where to add console.log statements to narrow it down.
```

### "Database query returns wrong data"
```text
A database query isn't returning what I expect. Help me debug.

**Database:** [Supabase Postgres / SQLite]
**What I'm querying:** [table, conditions]
**What I actually get:** [empty array, null, error]

**The query code:**
[paste Supabase client call or raw SQL]

**The table schema:**
[paste CREATE TABLE]

**Error output:** [paste any errors]

Check:
1. Is RLS enabled and blocking the query? (Are we passing `auth.uid()`?)
2. Are filter conditions missing case-sensitivity checks?
3. Am I using `.single()` when multiple rows exist?
4. Am I failing to check the `error` object?
```
