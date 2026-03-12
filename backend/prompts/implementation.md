<!-- @maxi-cmyk -->
# Backend Implementation Prompts

Copy-paste prompts for building backend features fast. Fill in the brackets, paste into Claude, and get working code back.

---

## Scaffold a New API Route

```
Create a new API route for my app.

**Stack:** [e.g. Next.js App Router / Flask / FastAPI]
**Language:** JavaScript (unless I say otherwise)
**Resource:** [e.g. projects, tasks, submissions]
**Operations needed:** [e.g. list all, get one, create, update, delete — pick what you need]

**Fields:**
- [field name] — [type and any constraints, e.g. "name — string, required, max 100 chars"]
- [field name] — [type, e.g. "status — one of: draft, active, done"]
- [field name] — [type, e.g. "data — flexible JSON object"]

**Auth:** [is this route protected? should it filter by the logged-in user?]
**Database:** [Supabase / SQLite / other]

Give me:
1. The route handler file(s) with input validation
2. The service/query functions (keep DB logic separate from the handler)
3. The database table schema (SQL)
4. A quick test I can run with curl or the browser to verify it works

Keep it simple. No pagination, no rate limiting, no middleware unless I ask. JavaScript, not TypeScript.
```

---

## Add Auth to an Existing App

```
I need to add authentication to my app.

**Stack:** [e.g. Next.js + Supabase / Flask + JWT]
**What exists already:** [describe what's built — routes, pages, database tables]
**Auth requirements:**
- Sign up method: [email+password / OAuth (Google, GitHub) / both]
- What needs protecting: [which routes or pages need login]
- User data needed: [just email? also name/avatar? role-based access?]

**Current file structure (relevant bits):**
[paste or list the key files]

Give me:
1. Auth client setup (server + browser if Next.js)
2. Sign up and login functions
3. Middleware or route protection
4. A profiles table schema if needed
5. How to get the current user in any route/page

Wire it into my existing code — don't give me a standalone example. Show me what to add and where.
```

---

## Set Up the Database

```
I need to set up the database for my project.

**Database:** [Supabase / SQLite / Railway Postgres]
**What the app does:** [one sentence — e.g. "users submit projects and vote on them"]
**Main entities:** [e.g. users, projects, votes]

**For each entity, what I know so far:**
- [entity]: [fields and relationships, even if rough — e.g. "project has a name, description, belongs to a user, has many votes"]

**Auth:** [using Supabase Auth? if so, users table is handled — just need profiles]
**Deployment:** [Vercel / Railway / local only — affects SQLite viability]

Give me:
1. The full SQL schema (CREATE TABLE statements)
2. RLS policies if using Supabase
3. The query functions I'll need (list, get, create, update, delete for each entity)
4. A seed script with realistic demo data (at least 3-5 rows per table)
5. Any indexes worth adding

Keep the schema flat. Use JSON columns for anything flexible. 2-3 tables max unless I really need more.
```

---

## Build a Specific Feature

```
I need to build a specific backend feature.

**Stack:** [e.g. Next.js + Supabase + Vercel]
**Language:** JavaScript
**Feature:** [describe what it does — e.g. "users can upload a CSV and see it parsed into a table"]

**How it should work:**
1. [step 1 — what the user does]
2. [step 2 — what happens on the backend]
3. [step 3 — what the user sees]

**What exists already:**
- [relevant existing routes, tables, components — paste code if helpful]

**Constraints:**
- [time limit, e.g. "I have 2 hours to build this"]
- [tech constraints, e.g. "must use the sponsor's API", "no external libraries"]

Give me the implementation in order of what to build first. If something is risky or time-consuming, flag it and suggest a simpler alternative. If part of this can be faked or hardcoded for the demo, tell me.
```

---

## Connect to an External API / Sponsor SDK

```
I need to integrate an external API into my backend.

**The API:** [name, e.g. "OpenAI API", "Twilio", "a sponsor's custom SDK"]
**API docs URL:** [paste link if you have it]
**What I need it to do:** [e.g. "send a prompt and get a response", "send an SMS", "fetch user data"]

**My stack:** [e.g. Next.js route handler / Flask endpoint]
**Language:** JavaScript

**API key / auth:** [do I have it? where is it stored? .env.local?]

Give me:
1. A service function that wraps the API call (lib/services/[name].js)
2. A route handler that exposes it to my frontend
3. Error handling for common failures (rate limit, bad key, timeout)
4. How to keep the API key server-side only (never exposed to browser)

Keep the wrapper simple — one function per action, no abstraction layers.
```

---

## Deploy and Go Live

```
I need to deploy my app and make sure it works in production.

**Stack:** [e.g. Next.js + Supabase + Vercel / Flask + SQLite + Railway]
**Current state:** [works locally? partially deployed? first deploy?]
**Repo:** [GitHub? linked to deployment platform yet?]

**Environment variables I need:**
- [list them, e.g. NEXT_PUBLIC_SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY, etc.]

**Concerns:**
- [anything specific — e.g. "OAuth redirect URLs", "SQLite persistence", "demo is in 2 hours"]

Walk me through deployment step by step:
1. Pre-deploy checks (build locally, verify env vars)
2. Platform setup (connect repo, set env vars)
3. First deploy and verification
4. Seed the demo data on the production database
5. Test the full user flow on the production URL
6. Fallback plan if the live demo breaks

Give me the exact commands to run, not just descriptions.
```

---

## Refactor Messy Code (Hackathon Cleanup)

```
This code works but it's messy. Help me clean it up without breaking anything.

**What it does:** [one sentence]
**Why it's messy:** [e.g. "everything is in one file", "copy-pasted the same logic 3 times", "no error handling"]

**The code:**
[paste the messy code]

Clean it up:
1. Extract repeated logic into reusable functions
2. Add basic error handling where it's missing
3. Separate concerns if everything is crammed in one file
4. Name things clearly

Don't over-engineer it. Don't add TypeScript. Don't restructure the whole project. Just make this specific code clean enough that I won't be embarrassed showing it to a judge who reads the repo.
```

---

## Tips

- **Paste your existing code.** "I have a projects table" is vague. Pasting the actual schema or route gives Claude the full picture and it'll wire into what you already have.
- **State your time constraint.** "I have 2 hours" changes the answer from "here's the proper way" to "here's what to build and what to fake."
- **Say JavaScript.** Claude defaults to TypeScript for Next.js unless you tell it not to. Mention JS explicitly.
- **One feature per prompt.** Don't ask for auth + database + deployment in one message. Chain them: get auth working, then database, then deploy.
