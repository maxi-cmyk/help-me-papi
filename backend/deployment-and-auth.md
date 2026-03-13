# Deployment & Auth

The DevOps rules. How to deploy to Vercel/Railway in hour one, set up basic authentication, and keep the application live.

---

## Part 1: Deployment

Get your app live and demoable. The goal is: a working URL that you can open on the projector during your pitch.

### Where to Deploy?
- **Next.js:** Vercel. Zero config, automatic preview deploys.
- **Python (Flask/FastAPI):** Railway or Render. Free tier, git push to deploy, native Postgres hosting.
- **Static Site:** Vercel or Netlify.

### Universal Deployment Rules
1. **Deploy in the first hour:** Push a hello world, get the URL, confirm it works. Every feature goes live as it's built to catch infra bugs early.
2. **Environment variables:** Set env vars in the dashboard **before** deploying. A build with missing keys fails silently.
3. **One person owns deployment:** They hold the Vercel/Railway login, manage the keys, and know how to rollback.
4. **Test the production URL:** Demo from the live URL, not localhost. Test the full user flow (Sign Up -> Core Feature) on the live site before pitching.
5. **Have a fallback:** Record a screen capture of the working demo beforehand. Keep localhost running as a backup.

### Common Vercel Gotchas
- **Missing Env Vars:** Check the Production vs Preview scopes in the Vercel Dashboard.
- **Edge Runtime Crashes:** If middleware imports a Node-only library (like `better-sqlite3`), it will fail silently. Move it out of middleware or add `export const runtime = 'nodejs'`.
- **Stale Builds:** Redeploy with "existing Build Cache" OFF.
- **API Timeouts:** Vercel free tier limits serverless functions to 10s. Do heavy work asynchronously.
- **OAuth Callbacks:** Don't forget to add your live `.vercel.app` domain to your Google/GitHub OAuth provider redirect URLs.

---

## Part 2: Authentication

Be honest: **Does your demo actually need auth?** If you are pitching a data visualization tool with no personalized data, skip it entirely and save the time.

If you DO need it:

### Supabase Auth (Next.js)
The fastest path. Handles OAuth, email/password, and sets server cookies in 15 minutes.
- Use `@supabase/ssr` to generate server clients.
- Use Next.js `middleware.js` to protect routes (e.g., redirect unauthenticated users away from `/dashboard`).
- **Critical Security:** Always use `getUser()` (which verifies the JWT with Supabase) instead of `getSession()` (which only reads the raw browser cookie and can be spoofed) for server-side checks.

### Simple JWT (Python)
If using Flask/FastAPI without a sponsor auth provider, build a simple JWT implementation:
- Use `jwt.encode` and `jwt.decode`.
- Create a `@require_auth` decorator that checks the `Authorization: Bearer <token>` header.
- This is fine for a hackathon, but not secure enough for production.

### Pre-Pitch Auth Checklist
- [ ] Can a fresh user sign up and use the app? (Judges won't have accounts).
- [ ] Pre-seed a demo account so your pitch doesn't start with you awkwardly filling out a signup form.
- [ ] Test auth on the deployed URL, checking for cookie cross-domain issues.

---

## Part 3: References
Reference material for backend design, runtime behavior, and system reliability.

- [Supabase SSR Subpackages (Auth)](https://supabase.com/docs/guides/auth/server-side/nextjs)
- [Vercel Deployment Limits & Edge Runtime](https://vercel.com/docs/functions/edge-functions/edge-runtime)
- [Next.js Route Handlers](https://nextjs.org/docs/app/building-your-application/routing/route-handlers)
