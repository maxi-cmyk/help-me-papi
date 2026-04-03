---
name: jwt-vs-sessions
description: Trade-offs between JWT authentication and Session-based authentication.
---

# JWT vs Sessions

For standard applications, choose one of these models:

## Session Auth (Cookies)
- **Best for:** Most web applications.
- **Workflow:** Server generates a secure Session ID and sets it as an `HttpOnly` cookie. Server stores session data in DB/Redis.
- **Pros:** Can instantly revoke sessions, highly secure against XSS.

## JWT Auth
- **Best for:** Mobile apps or strictly decoupled APIs.
- **Workflow:** Server signs a payload and sends it to the client. Client sends it back in the `Authorization: Bearer <token>` header.
- **Pros:** Stateless (no DB lookup for auth).
- **Cons:** Cannot easily revoke a token before it expires without complex blocklists.

## Supabase Auth
If using Supabase, it seamlessly handles JWTs under the hood and provides server-side cookie utilities (`@supabase/ssr`). Just use `getUser()` for all server-side verifications.
