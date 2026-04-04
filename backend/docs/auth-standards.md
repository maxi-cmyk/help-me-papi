# Auth Standards

## Passwords
- Never store plaintext passwords  always hash with bcrypt (cost factor 12) or argon2id
- Minimum password length: 8 characters. Don't impose maximum below 64.
- Check against known breached password lists if possible (HaveIBeenPwned API)

## Tokens
- Access tokens: short-lived (15 min), JWT, stored in memory (not localStorage)
- Refresh tokens: long-lived (30 days), opaque random string, stored in HttpOnly cookie, stored as hash in DB
- Session IDs: cryptographically random (32+ bytes), stored in HttpOnly cookie

## Cookies
- All auth cookies must have: `HttpOnly; Secure; SameSite=Lax`
- Use `SameSite=None; Secure` only if you explicitly need cross-site cookie (e.g. embedded widget)

## OAuth
- Always validate the `state` parameter on the callback to prevent CSRF
- Exchange authorization codes server-side only  never in the browser
- Store client secrets in environment variables, never in code

## Endpoints
- Rate limit all auth endpoints: login, register, password reset, token refresh
- Use constant-time comparison for all token/secret comparisons
- Return generic errors for login failure  never reveal whether email exists

## Sessions
- Regenerate session ID after login (session fixation prevention)
- Set a sensible session expiry (e.g. 30 days idle, 90 days absolute)
- Provide "log out all devices" functionality for security-sensitive products

## Authorization
- Check authorization at the resource level, not just the route level
- Never trust user-supplied IDs without verifying ownership
- Log authorization failures  repeated 403s on a resource can indicate enumeration