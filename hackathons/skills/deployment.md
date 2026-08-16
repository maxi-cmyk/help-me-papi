# Deployment Skill — CLI Setup Guide

How to deploy backend, frontend, auth, and DB using only the CLI. This is the fastest path from "it works locally" to "judges can see it."

---

## The Golden Rules

1. **Deploy in the first hour.** Push a hello world, get the URL, confirm it works.
2. **Set env vars before deploying.** A build with missing env vars breaks silently.
3. **Build locally first.** `npm run build` catches errors before the deploy does.
4. **Test the deployed version.** Demo from the production URL, not localhost.
5. **One person owns deployment.** They know the login, env vars, and how to roll back.

---

## Frontend: Vercel (Next.js)

### Install CLI
```bash
npm i -g vercel
```

### Login
```bash
vercel login
```

### First deploy (from project root)
```bash
vercel                    # follow prompts: scope, project name, framework detection
vercel --prod             # deploy to production URL
```

### Set environment variables
```bash
vercel env add NEXT_PUBLIC_API_URL production
vercel env add NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY production
vercel env add CLERK_SECRET_KEY production
```

### Pull env vars locally (for `.env.local`)
```bash
vercel env pull .env.local
```

### Deploy existing project
```bash
vercel link                # link local dir to existing Vercel project
vercel --prod              # deploy
```

### Common Vercel failures

| Symptom | Likely cause | Fix |
|---|---|---|
| Works locally, blank in production | Missing env vars | Check Vercel dashboard → Settings → Environment Variables |
| Middleware crashes | Node-only import in Edge runtime | Add `export const runtime = 'nodejs'` |
| Stale deploy | Build cache | Redeploy with cache OFF (Settings → General) |
| API timeout | Function > 10s on free plan | Optimize or go Pro |
| OAuth redirect broken | Only localhost URL set | Add production URL to OAuth provider |

---

## Backend: Railway (FastAPI / Node)

### Install CLI
```bash
npm i -g @railway/cli
```

### Login
```bash
railway login
```

### Create a new project
```bash
railway init               # creates a new project, links current dir
```

### Add a service from GitHub
```bash
railway add --service my-backend --github --repo maxi-cmyk/my-repo --branch main
```

### Or deploy from local
```bash
railway up                 # deploy current directory
```

### Add a database
```bash
railway add --plugin postgres    # or --plugin redis, --plugin mysql
```

### Set environment variables
```bash
railway variables set OPENAI_API_KEY=sk-...
railway variables set FRONTEND_ORIGIN=https://your-vercel-domain.vercel.app
railway variables set CLERK_SECRET_KEY=sk_...
```

### View logs
```bash
railway logs               # tail production logs
```

### Open deployed URL
```bash
railway open               # opens the Railway domain in browser
```

### Common Railway failures

| Symptom | Likely cause | Fix |
|---|---|---|
| Build fails | Missing `requirements.txt` / `package.json` | Ensure manifest is in root or configured root dir |
| Worker won't start | Start command wrong | Check `railway.toml` or Settings → Deploy → Start Command |
| DB connection refused | Wrong connection string | Use `${{Postgres.DATABASE_URL}}` reference, not hardcoded |
| Out of memory | Worker too heavy | Reduce concurrency or upgrade plan |

---

## Auth: Clerk

### Install CLI (optional — most setup is dashboard)
```bash
npm install @clerk/clerk-sdk-node   # for backend verification
```

### Create a Clerk app (dashboard)
1. Go to [dashboard.clerk.com](https://dashboard.clerk.com)
2. Click **Add application**
3. Choose sign-in options (Email, Google, GitHub, etc.)
4. Copy **Publishable Key** (frontend) and **Secret Key** (backend)

### Configure redirect URLs
In Clerk Dashboard → **User & Authentication** → **Social Connections**:
- Add `http://localhost:3000` for development
- Add `https://your-production-domain.vercel.app` for production

### Protect routes (Next.js middleware)
```typescript
// middleware.ts
import { clerkMiddleware, createRouteMatcher } from '@clerk/nextjs/server'

const isProtectedRoute = createRouteMatcher(['/dashboard(.*)', '/api/protected(.*)'])

export default clerkMiddleware(async (auth, req) => {
  if (isProtectedRoute(req)) await auth.protect()
})

export const config = {
  matcher: ['/((?!.*\\..*|_next).*)', '/', '/(api|trpc)(.*)'],
}
```

### Protect backend routes (FastAPI)
```python
from clerk_backend_api import Clerk
import os

clerk = Clerk(bearer_auth=os.environ["CLERK_SECRET_KEY"])

@app.get("/api/protected")
async def protected(request: Request):
    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    try:
        session = clerk.verify_token(token)
        user_id = session["sub"]
    except:
        raise HTTPException(status_code=401, detail="Invalid token")
    return {"user_id": user_id}
```

---

## Database: Supabase

### Install CLI
```bash
npm i -g supabase
```

### Login
```bash
supabase login
```

### Link to a project
```bash
supabase link --project-ref YOUR_PROJECT_REF
```

### Create a new project (dashboard)
1. Go to [supabase.com/dashboard](https://supabase.com/dashboard)
2. Click **New project**
3. Set name, password, region
4. Wait ~2 minutes for provisioning

### Push schema
```bash
supabase db push            # push local migrations to remote
```

### Generate types
```bash
supabase gen types typescript --linked > types/database.ts
```

### Seed data
```bash
supabase db seed            # run supabase/seed.sql
```

### Row Level Security (RLS)
```sql
-- Enable RLS
alter table profiles enable row level security;

-- Users can only see their own profile
create policy "Users can view own profile"
  on profiles for select
  using (auth.uid() = id);

-- Users can only update their own profile
create policy "Users can update own profile"
  on profiles for update
  using (auth.uid() = id);
```

### Common Supabase failures

| Symptom | Likely cause | Fix |
|---|---|---|
| RLS blocks everything | No policy for the operation | Add explicit select/insert/update/delete policies |
| `getUser()` returns null | Token expired or wrong key | Use `CLERK_JWT_KEY` for networkless verification |
| Migration fails | Conflicting changes | Use `supabase db diff` to inspect before pushing |
| Connection refused | Wrong connection string | Use pooled connection (port 6543) for serverless |

---

## Full Deployment Checklist

### Before the pitch
- [ ] Production URL works
- [ ] Demo account is seeded
- [ ] Full user flow works on deployed version
- [ ] Screen recording as backup if live demo fails
- [ ] Localhost running as fallback
- [ ] All env vars set in Vercel AND Railway dashboards
- [ ] OAuth redirect URLs include production domain
- [ ] RLS policies enabled on all user-facing tables
- [ ] CORS configured: backend allows only the Vercel origin

### One-person deployment ownership
- One person has the Vercel + Railway + Clerk + Supabase logins
- They know how to roll back (Vercel: Deployments → Rollback; Railway: redeploy previous commit)
- They have a screen recording of the full demo as a last-resort fallback
