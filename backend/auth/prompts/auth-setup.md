# Auth Prompts

## Implement auth from scratch
```
I'm building a [Next.js / Express + React / other] app.
Auth requirements:
- [ ] Email + password login
- [ ] OAuth: [Google / GitHub / other]
- [ ] Magic link / passwordless
- [ ] MFA

I'm using [Supabase / NextAuth / Clerk / Lucia / rolling my own].
My database is [Postgres / SQLite / MongoDB].

Walk me through setting up auth end-to-end, including:
1. The schema/tables needed
2. The login and registration flow
3. How sessions/tokens are stored and validated
4. How to protect routes
5. How to access the current user in route handlers
```

## Design role-based authorization
```
I need to add authorization to my app.

Roles needed: [e.g. user, admin, moderator, or more complex]
Resources: [e.g. posts, comments, billing settings]
Rules: [e.g. users can only edit their own posts, admins can edit anything]

My tech stack: [framework + ORM]

Design:
1. The database schema for roles/permissions
2. Middleware or helper functions to check authorization
3. How to attach this to route handlers
4. How to handle row-level authorization (does this user own THIS resource?)
```

## Debug an OAuth flow
```
My OAuth flow is broken. Here's what's happening:

Provider: [Google / GitHub / etc]
Library: [NextAuth / Lucia / custom]
Error: [paste the error message or unexpected behavior]

My callback URL in the provider console: [paste]
My callback URL in code: [paste]
My environment variables (names only, not values): [paste]

What is wrong?
```

## Set up JWT + refresh token rotation
```
I need to implement a JWT access token + refresh token system.

Stack: [Node.js/Express or Next.js API routes]
Storage: [where you want to store refresh tokens — Postgres / Redis]

Implement:
1. Login endpoint that issues both tokens
2. Middleware to verify the access token on protected routes
3. Refresh endpoint that rotates the refresh token
4. Logout endpoint that revokes the refresh token
5. "Revoke all sessions" endpoint

Include security best practices (HttpOnly cookies, token rotation, etc).
```