<!-- @maxi-cmyk -->
# Backend Debugging Prompts

Copy-paste prompts for when something's broken and you need to fix it fast. Paste the relevant template into Claude, fill in the brackets, and include any error messages or logs you have.

---

## "It works locally but not deployed"

```
Something works on localhost but is broken on the deployed version. Help me debug.

**Stack:** [e.g. Next.js + Supabase + Vercel]
**What works locally:** [describe the feature that works]
**What happens in production:** [blank page? error? wrong data? loading forever?]
**Deployed URL:** [url if you can share it]
**Error messages:** [paste any errors from browser console, Vercel logs, or network tab]

Check these in order and tell me which is most likely:
1. Missing or wrong environment variables
2. Edge runtime vs Node runtime mismatch
3. Hardcoded localhost URLs in the code
4. OAuth/redirect URL not set for production domain
5. CORS issues
6. Build-time vs runtime environment variable loading
7. API route timeout (serverless function limit)
8. Database connection rejected from deployment IP

For each one, tell me exactly what to check and where.
```

---

## "API route returns 500"

```
I'm getting a 500 error from an API route. Help me find the problem.

**Stack:** [e.g. Next.js App Router / Flask / FastAPI]
**Route:** [e.g. POST /api/projects]
**Request body I'm sending:** 
[paste the JSON or form data]

**What I expect to happen:** [describe expected behavior]
**What actually happens:** [500 error, and any message if shown]

**Server logs / error output:**
[paste whatever you see in terminal, Vercel logs, or Railway logs — even partial]

**The route handler code:**
[paste the full route handler]

**Any service/db functions it calls:**
[paste those too if you have them]

Walk through the code line by line and identify where it's most likely failing. If the logs don't show the exact error, add console.log statements and tell me where to put them to narrow it down.
```

---

## "Auth is broken"

```
Auth isn't working. Help me debug.

**Stack:** [e.g. Supabase Auth with Next.js / JWT with Flask]
**Auth provider:** [e.g. Supabase email+password, Google OAuth, custom JWT]
**What's broken:** [can't sign up? can't log in? session not persisting? redirect loop? 401 on protected routes?]

**Error messages:**
[paste any errors from console, network tab, or server logs]

**Relevant code:**
- Auth client setup: [paste]
- Login/signup function: [paste]
- Middleware or route protection: [paste]
- Auth callback route (if OAuth): [paste]

**Environment:**
- Running locally or deployed? [which one is broken, or both?]
- OAuth redirect URLs configured: [list them]

Check the most common auth failures:
1. getSession() used instead of getUser() for server-side checks
2. OAuth redirect URL doesn't match the current domain
3. Cookies not being set (wrong Supabase client setup)
4. Middleware not running on the right paths
5. NEXT_PUBLIC_ prefix missing on client-side env vars
6. Token expired and no refresh logic
```

---

## "Database query returns wrong or empty data"

```
A database query isn't returning what I expect. Help me debug.

**Database:** [Supabase Postgres / SQLite / other]
**What I'm querying:** [which table, what conditions]
**What I expect to get:** [describe expected result]
**What I actually get:** [empty array? null? wrong data? error?]

**The query code:**
[paste the full query — Supabase client call, raw SQL, or ORM call]

**The table schema:**
[paste the CREATE TABLE statement, or describe the columns]

**Sample data that should match:**
[paste a row or describe what's in the table]

**Error output (if any):**
[paste]

Check these in order:
1. Is the query actually hitting the right table?
2. Are the filter conditions correct? (wrong column name, wrong ID, case sensitivity)
3. Is RLS enabled and blocking the query? (Supabase — check policies)
4. Is the user authenticated when making the query? (RLS uses auth.uid())
5. Is the data actually in the table? (check via Supabase dashboard or SQL editor)
6. Is .single() being used when multiple rows exist (or vice versa)?
7. Am I checking the error? (Supabase returns { data, error } — log the error)
```

---

## "Frontend not showing data from API"

```
The API returns data correctly but the frontend isn't showing it. Help me debug.

**Stack:** [e.g. Next.js App Router / React + Flask]
**API endpoint:** [e.g. GET /api/projects]
**API response when tested directly:** [paste the JSON from browser/Postman/curl]

**Frontend code that fetches and displays:**
[paste the component or page]

**What I see in the browser:** [blank? loading forever? old data? error?]
**Browser console errors:** [paste any]
**Network tab:** [does the request show up? what status code? what response body?]

Check:
1. Is the fetch actually firing? (missing useEffect dependency, server component trying to use client fetch)
2. Is the response being parsed correctly? (await res.json() missing?)
3. Is the state being set? (useState not updating, or updating but not triggering re-render)
4. Is the data shape matching what the component expects? (data.projects vs data)
5. Is there a loading/error state hiding the content?
6. Is it a server component that needs to be async?
```

---

## "Everything is broken and I don't know where to start"

```
The app isn't working and I'm not sure where the problem is. Help me triage.

**Stack:** [list everything — framework, database, auth, deployment]
**What was the last thing that worked:** [describe the last known good state]
**What changed since then:** [new code? new deploy? env var change? dependency update?]
**Symptoms:** [describe what you see — errors, blank pages, wrong behavior]

**Any error messages from anywhere:**
[paste everything — browser console, terminal, deployment logs, even partial]

Don't try to fix everything at once. Instead:
1. Identify the single most likely point of failure based on what changed
2. Give me one thing to check first
3. Based on what I find, tell me what to check next

Let's work through this step by step.
```

---

## Tips for Effective Debugging with Claude

- **Paste actual error messages.** "It doesn't work" gives Claude nothing. The exact error text, even partial, narrows it down instantly.
- **Include the code.** Don't describe what the code does — paste it. Claude can spot bugs you'll talk around.
- **Say what changed.** "It was working, then I added X" is the most useful debugging sentence.
- **Check the network tab.** Before pasting a prompt, open browser DevTools > Network, reproduce the issue, and note: did the request fire? What status code? What response body? This saves a round trip.
- **Start with logs, not guesses.** Add `console.log` before and after the suspicious line. If the first one prints and the second doesn't, you've found the line that fails.
