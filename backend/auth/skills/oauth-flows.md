---
name: oauth-flows
description: Setting up OAuth and handling redirects.
---

# OAuth Flows

If integrating Google, GitHub, or other providers:

## Essential Steps
1. **Configuring the Provider:** You must register your application on the provider's developer console.
2. **Redirect URIs:** You must explicitly list all redirect URLs. 
   - Add `http://localhost:3000/api/auth/callback` for local development.
   - Add `https://your-domain.com/api/auth/callback` for production.
3. **Handling the Callback:** After login, the provider redirects back to your server with a code. Exchange that code for an auth token.

## Pitfalls
- **Missing Production Redirect URL:** Forgetting to update the OAuth provider settings with the Vercel production URL is a common cause of auth failure at launch.
- **Cross-site cookies:** Ensure cookies are set with `SameSite=Lax` and `Secure=true` in production to avoid login loops.
