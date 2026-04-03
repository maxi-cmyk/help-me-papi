# Authentication & Authorization

## The core concepts (don't confuse these)

**Authentication (authn):** Who are you? (login, verify identity)
**Authorization (authz):** What are you allowed to do? (permissions, roles)

Most bugs in auth come from conflating the two. A user can be authenticated (logged in) but not authorized (not allowed to access that resource).

---

## Sessions vs JWTs — the most important decision

This is the decision you'll make on every project. Here's the honest breakdown.

### Sessions (stateful)

When a user logs in, the server:
1. Creates a session record in the database (or Redis)
2. Sends the session ID to the browser as an **HTTP-only cookie**
3. On every request, the browser sends the cookie automatically
4. The server looks up the session ID → finds the user

```
Login:
  POST /auth/login
  Server creates: sessions table → { id: "abc123", user_id: 42, expires_at: ... }
  Server sets:    Set-Cookie: session=abc123; HttpOnly; Secure; SameSite=Lax

Every request:
  Cookie: session=abc123   (browser sends automatically)
  Server: SELECT * FROM sessions WHERE id = 'abc123'  → finds user 42
```

**Pros:**
- Instant revocation — delete the session row, user is logged out immediately
- Simple mental model
- Cookie is automatic — no JS needed to attach it to requests
- HttpOnly cookie = JS can't read it = XSS-proof

**Cons:**
- Requires DB lookup on every request (mitigated by Redis)
- Harder with multiple servers unless you use a shared session store (Redis solves this)
- Doesn't work natively for mobile apps (cookies are a browser concept)

**Best for:** traditional web apps, anything where you need instant logout, B2B products where "revoke all sessions" matters.

---

### JWTs — JSON Web Tokens (stateless)

When a user logs in, the server:
1. Creates a signed token containing the user's data
2. Sends it to the client (usually in the response body, stored in memory or localStorage)
3. Client attaches it to every request as `Authorization: Bearer <token>`
4. Server verifies the signature — **no DB lookup needed**

```
Login:
  POST /auth/login
  Server creates: JWT { user_id: 42, role: "admin", exp: 1234567890 }
  Server signs it with a secret key → eyJhbGci...
  Response body: { token: "eyJhbGci..." }

Every request:
  Authorization: Bearer eyJhbGci...
  Server: verify signature → decode payload → user is 42, role is admin
  No database hit needed
```

**Pros:**
- Stateless — no DB lookup per request, scales horizontally trivially
- Works for mobile apps, SPAs, and third-party API consumers
- Self-contained — the token carries the data

**Cons:**
- **Cannot be revoked before expiry.** This is the big one. If a user's token is stolen or you need to log them out immediately, you can't — the token is valid until it expires. Workarounds exist (blocklists) but they require DB lookups, defeating the point.
- Storing JWTs in localStorage exposes them to XSS attacks
- Storing JWTs in cookies makes them session-like anyway

**Best for:** APIs consumed by mobile apps or third parties, microservices (service-to-service auth), situations where stateless scaling matters more than instant revocation.

---

### The hybrid approach (what most production apps use)

Short-lived **access token** (JWT, 15 min expiry) + long-lived **refresh token** (opaque, stored in DB or Redis).

```
Login:
  → access_token: JWT, expires in 15 min   (stored in memory/cookie)
  → refresh_token: random string, expires in 30 days   (stored in HttpOnly cookie)

Every API call:
  → Send access_token in Authorization header
  → Server verifies JWT signature → no DB hit, fast

When access_token expires:
  → Client sends refresh_token to POST /auth/refresh
  → Server looks up refresh_token in DB, verifies it's valid
  → Issues new access_token (and optionally rotates refresh_token)

Logout / revoke:
  → Delete refresh_token from DB
  → At worst, the access_token is valid for 15 more minutes — acceptable tradeoff
```

This is what Supabase, Auth0, and most auth libraries implement under the hood.

---

## OAuth 2.0 — "Sign in with Google/GitHub"

OAuth lets your app delegate authentication to a third party (Google, GitHub, etc.). You never see the user's password.

### The flow

```
1. User clicks "Sign in with Google"

2. You redirect them to Google:
   https://accounts.google.com/o/oauth2/v2/auth
     ?client_id=YOUR_CLIENT_ID
     &redirect_uri=https://yourapp.com/auth/callback
     &scope=openid email profile
     &response_type=code
     &state=RANDOM_STRING   ← CSRF protection

3. Google shows their login page, user logs in

4. Google redirects back to your callback URL:
   https://yourapp.com/auth/callback?code=4/0AX4XfW...&state=RANDOM_STRING

5. Your server exchanges the code for tokens:
   POST https://oauth2.googleapis.com/token
     code=4/0AX4XfW...
     client_id=...
     client_secret=...    ← never exposed to browser
     redirect_uri=...
     grant_type=authorization_code

6. Google returns:
   { access_token, id_token (JWT with user info), refresh_token }

7. You decode the id_token to get the user's email, name, Google ID
   → Create or find the user in your DB
   → Issue your own session/JWT
```

**The `state` parameter** — a random string you generate before the redirect and verify when Google redirects back. Prevents CSRF attacks where an attacker tricks a user into connecting their account to the attacker's OAuth session.

**The `code` (authorization code)** is short-lived and single-use. It's exchanged server-side, not in the browser, so the actual tokens never appear in the URL or browser history.

### OAuth vs OpenID Connect (OIDC)

OAuth 2.0 is for authorization ("can this app access your Google Drive?").
OIDC (OpenID Connect) is OAuth 2.0 + an identity layer. The `id_token` is the OIDC addition — it's a JWT with the user's identity info. When you "Sign in with Google", you're using OIDC.

---

## Authorization — roles and permissions

Once you know *who* the user is, you need to control *what they can do*.

### Simple role-based (RBAC)

```sql
-- users table
ALTER TABLE users ADD COLUMN role TEXT DEFAULT 'user';
-- roles: 'user', 'admin', 'moderator'
```

```typescript
// Middleware
function requireRole(role: string) {
  return (req, res, next) => {
    if (req.user.role !== role) {
      return res.status(403).json({ error: 'Forbidden' });
    }
    next();
  };
}

// Route
app.delete('/posts/:id', requireAuth, requireRole('admin'), deletePost);
```

### Resource-based (is this user allowed on THIS resource?)

```typescript
// Not just "is the user an admin" but "does this user own this post?"
async function canEditPost(userId: string, postId: string): Promise<boolean> {
  const post = await db.post.findUnique({ where: { id: postId } });
  return post?.authorId === userId || user.role === 'admin';
}
```

---

## Using an auth library vs rolling your own

**Don't roll your own for production.** Auth has too many edge cases (timing attacks, token rotation, PKCE, session fixation). Use a library.

### Options

| Library | Best for | Notes |
|---|---|---|
| **Supabase Auth** | Full-stack apps already on Supabase | Batteries-included: OAuth, magic links, MFA |
| **NextAuth / Auth.js** | Next.js specifically | Easy OAuth setup, session or JWT mode |
| **Lucia** | When you want full control but not raw crypto | Lightweight, framework-agnostic |
| **Clerk** | Best DX, fastest to ship | Expensive at scale, but great for hackathons/MVPs |
| **Auth0** | Enterprise, need MFA/SSO/compliance | Pricey, but very feature complete |
| **Better Auth** | Newer, TypeScript-first, open source | Growing fast, good alternative to Lucia |

For most startups: **Supabase Auth** if on Supabase, **NextAuth** if Next.js without Supabase, **Clerk** if you want to move fastest and cost isn't a concern yet.

---

## Common vulnerabilities to avoid

### Store tokens correctly
- HttpOnly cookie: JS can't read it → safe from XSS
- `localStorage`: JS can read it → stolen by any XSS attack
- Rule: **put session IDs and refresh tokens in HttpOnly cookies. Access tokens in memory (JS variable), not localStorage.**

### Always set cookie flags
```
Set-Cookie: session=abc; HttpOnly; Secure; SameSite=Lax; Path=/
```
- `HttpOnly` — JS can't access it
- `Secure` — only sent over HTTPS
- `SameSite=Lax` — protects against CSRF (cross-site request forgery)

### Rate limit login endpoints
Without rate limiting, an attacker can try millions of passwords. Add rate limiting to `POST /auth/login` and `POST /auth/register`.

### Use constant-time comparison for tokens
When comparing tokens (e.g. password reset tokens), use a timing-safe comparison. Regular string equality (`===`) leaks timing information.

```typescript
import { timingSafeEqual } from 'crypto';
// Use this instead of token === storedToken
```

### Don't leak user existence
`"No account with that email"` tells an attacker which emails are registered. Return `"Invalid email or password"` for both wrong email and wrong password.