# Auth Decisions

## Use an auth library over rolling your own
Auth has too many edge cases to implement from scratch: timing attacks, session fixation, token rotation, PKCE for OAuth, secure cookie handling. Libraries encode years of security lessons. Only write custom auth if you have a very specific requirement no library covers.

## Supabase Auth as the default for Supabase projects
Supabase Auth handles OAuth providers, magic links, OTP, JWT issuance, and session management out of the box. It integrates with Supabase's row-level security (RLS), which lets you enforce authorization at the database level.

## NextAuth (Auth.js) for Next.js without Supabase
Best-in-class Next.js integration, large provider ecosystem, supports both JWT and database session strategies. Use the database session strategy in production  it enables instant revocation.

## Clerk for hackathons and fast MVPs
Best developer experience of any auth library. Pre-built UI components mean you can have login/signup working in under an hour. Cost becomes significant at scale (pricing is per monthly active user), so evaluate before committing to it for production.

## Hybrid access + refresh token pattern over pure JWT
Pure JWTs with long expiry can't be revoked. Pure sessions require a DB hit on every request. The hybrid approach (short-lived JWT access token + DB-backed refresh token) gives fast per-request verification with revocability.

## HttpOnly cookies over localStorage for refresh tokens
localStorage is readable by any JavaScript on the page. An XSS vulnerability anywhere on your site can steal tokens from localStorage. HttpOnly cookies are invisible to JavaScript entirely. The slight added complexity of handling cookie credentials is worth the security gain.

## argon2id over bcrypt
argon2id is the current recommendation from OWASP. It's memory-hard, making it more resistant to GPU-based brute force attacks than bcrypt. Use bcrypt only if your runtime/library doesn't support argon2.