---
name: owasp-top-10-for-startups
description: Essential security practices based on the OWASP Top 10.
---

# Security for Startups

Security can't be an afterthought. Focus on these heavily-exploited vectors first:

1. **Injection (SQL, NoSQL, ORM):** Never concatenate user input directly into queries. Always use parameterized queries or trusted ORMs (Prisma/Drizzle) for database access.
2. **Broken Authentication:** Implement rate limiting on login routes. Don't allow limitless password guessing. Ensure cookies are `HttpOnly` and `Secure`.
3. **Sensitive Data Exposure:** NEVER log API keys or user passwords. Bcrypt/Argon2 hash all passwords. Store infrastructure secrets in Vercel/GitHub secrets exclusively.
4. **Broken Access Control (IDOR):** Just because a user is authenticated, are they authorized to view *this specific* resource? Always check ownership (e.g., `WHERE user_id = ?`) before returning data based on a URL ID.
5. **Security Misconfiguration:** Disable directory listing, ensure default passwords are changed, and handle CORS properly—do not return `Access-Control-Allow-Origin: *` for authenticated API endpoints.
