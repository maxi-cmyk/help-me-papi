<!-- @maxi-cmyk -->
# Deployment

Get your app live and demoable. The goal is: a working URL that you can open on the projector during your pitch. Everything else is secondary.

## Decision: Where to Deploy?

| Stack | Deploy to | Why |
|-------|-----------|-----|
| Next.js | Vercel | Zero config, automatic preview deploys, built for Next.js |
| Python (Flask/FastAPI) | Railway or Render | Free tier, git push to deploy, no Docker needed |
| Static site / frontend only | Vercel or Netlify | Instant, free |
| Need a database too | Railway (app + Postgres in one place) | Simpler than managing separate services |
| Sponsor gives credits | Use the sponsor's platform | Judges notice |

Default to Vercel for Next.js. Default to Railway for everything else. Don't overthink it.

## Vercel (Next.js)

### First deploy (5 minutes)

```bash
npm i -g vercel
vercel          # follow the prompts, link to your repo
```

Or just connect your GitHub repo at vercel.com — every push to main auto-deploys.

### Environment variables

```bash
# Set via CLI
vercel env add NEXT_PUBLIC_SUPABASE_URL
vercel env add SUPABASE_SERVICE_ROLE_KEY

# Or set in dashboard: Settings > Environment Variables
```

Rules:
- `NEXT_PUBLIC_` prefix = visible in browser. Only for truly public values.
- Everything else is server-only.
- Set env vars **before** deploying, not after. A deploy without env vars will build with empty values and break silently.

### Common Vercel gotchas

**"It works locally but not on Vercel"** — 90% of the time it's one of these:

1. **Missing env vars.** Check the Vercel dashboard. Env vars are scoped per environment (Production, Preview, Development) — make sure yours are set for Production.

2. **Edge runtime incompatibility.** Middleware runs on Edge by default. If you import something Node-only (like `better-sqlite3`, `fs`, or `sharp`), it'll fail silently. Fix: add `export const runtime = 'nodejs'` to the route, or move the logic out of middleware.

3. **Build cache.** If a deploy is stale, go to Deployments > three-dot menu > Redeploy, and check "Redeploy with existing Build Cache" OFF.

4. **API routes timing out.** Vercel's serverless functions have a 10-second timeout on the free plan (can increase on Pro). If your route does heavy processing, it'll die. Fix: keep API routes fast, do heavy work async.

5. **OAuth redirect URL.** You set `http://localhost:3000/auth/callback` during dev and forgot to add the production URL. Add both in your OAuth provider's settings.

### Pre-pitch deploy checklist

```bash
# Build locally first — catch errors before Vercel does
npm run build

# Check your env vars are set
vercel env ls

# Deploy
vercel --prod
```

## Railway (Python / Any Backend)

### First deploy

1. Push your code to GitHub
2. Go to railway.app, create a new project, connect your repo
3. Railway auto-detects Python (looks for `requirements.txt`) or Node (looks for `package.json`)
4. Set environment variables in the Railway dashboard
5. It deploys. You get a URL.

### Procfile (tell Railway how to start your app)

```
# Procfile
web: gunicorn app:app          # Flask
web: uvicorn main:app --host 0.0.0.0 --port $PORT   # FastAPI
```

### Railway + Database

Railway can spin up a Postgres database in the same project. Click "New" > "Database" > "PostgreSQL". It auto-injects `DATABASE_URL` into your app's environment.

```python
import os
DATABASE_URL = os.environ['DATABASE_URL']
```

No separate Supabase setup needed for hackathons that don't require Supabase-specific features.

## Render (Alternative)

Similar to Railway. Free tier is slower (spins down after inactivity, ~30s cold start). Fine for a hackathon if Railway isn't available.

```yaml
# render.yaml (optional, for auto-config)
services:
  - type: web
    name: my-app
    runtime: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn app:app
```

## Universal Deployment Rules

### 1. Deploy early, deploy often

Don't save deployment for the last hour. Deploy a "hello world" version on day one, hour one. Then every feature goes live as it's built. This catches deployment issues when you still have time to fix them.

### 2. Have a deploy buddy

One person on the team owns deployment. They know the dashboard login, the env vars, and how to roll back. If everyone owns it, nobody owns it.

### 3. Seed your demo data

Judges see an empty app and think it's broken. Before the pitch:

```javascript
// scripts/seed.js — run this before the demo
async function seed() {
  await db.createUser({ email: 'demo@example.com', name: 'Demo User' });
  await db.createProject({ name: 'Sample Project', userId: demoUser.id });
  // add enough data that the app looks alive
}

seed().then(() => console.log('seeded')).catch(console.error);
```

For Supabase, you can also seed via the SQL editor in the dashboard.

### 4. Test the deployed version

Your demo should use the production URL, not localhost. Test the full flow:
- Fresh browser (no cached auth)
- Sign up / log in
- The core feature
- Any integrations (do they work with production keys?)

### 5. Have a fallback

If live demo fails during the pitch:
- Record a screen capture of the working demo beforehand
- Have screenshots ready
- Keep localhost running as backup

The best teams rehearse the demo on the deployed version at least once before pitching.

## DNS / Custom Domain (Optional)

If the hackathon gives you a domain or you want to look polished:

```bash
# Vercel
vercel domains add myproject.dev

# Or in dashboard: Settings > Domains
```

Usually not worth the time at a hackathon unless the custom domain is part of the brand/pitch.

## Quick Reference

```bash
# Vercel
vercel                  # deploy preview
vercel --prod           # deploy production
vercel env ls           # check env vars
vercel logs             # debug production issues

# Railway
railway login
railway up              # deploy
railway logs            # debug
railway variables       # check env vars
```