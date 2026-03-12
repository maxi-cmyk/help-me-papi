<!-- @maxi-cmyk -->
# Auth

Get authentication working fast without building it from scratch. The goal at a hackathon is: users can sign up, log in, and protected routes stay protected. Nothing more.

## Decision: Which Auth?

| Situation | Use | Why |
|-----------|-----|-----|
| Next.js app, need it in 15 min | Supabase Auth | Drop-in, handles OAuth, email/password, sessions — zero backend code |
| Sponsor provides auth (e.g. Auth0, Clerk) | Sponsor's tool | Judges notice when you use sponsor tech |
| Python backend, no sponsor preference | Flask-Login or FastAPI + JWT | Simple, no external dependency |
| Quick prototype, auth isn't the point | Hardcoded user / skip auth entirely | Don't waste time on auth if the demo doesn't need it |

Be honest about whether your demo actually needs auth. If you're showing a data visualization tool and there's no concept of "my data vs your data," skip it and spend that time on the core feature.

## Supabase Auth (Fastest Path)

### Setup (5 minutes)

```bash
npm install @supabase/supabase-js @supabase/ssr
```

```env
# .env.local
NEXT_PUBLIC_SUPABASE_URL=https://xxx.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=eyJ...
```

Enable your auth providers in the Supabase dashboard (Email, Google, GitHub — whatever makes sense for the demo).

### Server client

```javascript
// lib/supabase/server.js
import { createServerClient } from '@supabase/ssr';
import { cookies } from 'next/headers';

export async function createClient() {
  const cookieStore = await cookies();

  return createServerClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL,
    process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY,
    {
      cookies: {
        getAll() { return cookieStore.getAll(); },
        setAll(cookiesToSet) {
          cookiesToSet.forEach(({ name, value, options }) =>
            cookieStore.set(name, value, options)
          );
        },
      },
    }
  );
}
```

### Protect a route (middleware)

```javascript
// middleware.js
import { createServerClient } from '@supabase/ssr';
import { NextResponse } from 'next/server';

export async function middleware(request) {
  let response = NextResponse.next({ request });

  const supabase = createServerClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL,
    process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY,
    {
      cookies: {
        getAll() { return request.cookies.getAll(); },
        setAll(cookiesToSet) {
          cookiesToSet.forEach(({ name, value }) =>
            request.cookies.set(name, value)
          );
          response = NextResponse.next({ request });
          cookiesToSet.forEach(({ name, value, options }) =>
            response.cookies.set(name, value, options)
          );
        },
      },
    }
  );

  const { data: { user } } = await supabase.auth.getUser();

  if (!user && request.nextUrl.pathname.startsWith('/dashboard')) {
    return NextResponse.redirect(new URL('/login', request.url));
  }

  return response;
}

export const config = {
  matcher: ['/dashboard/:path*', '/api/:path*'],
};
```

### Get the current user anywhere (server-side)

```javascript
const supabase = await createClient();
const { data: { user } } = await supabase.auth.getUser();
// user.id, user.email — that's usually all you need
```

### Sign in / sign up (client-side)

```javascript
'use client';
import { createBrowserClient } from '@supabase/ssr';

const supabase = createBrowserClient(
  process.env.NEXT_PUBLIC_SUPABASE_URL,
  process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY
);

// Email + password
await supabase.auth.signUp({ email, password });
await supabase.auth.signInWithPassword({ email, password });

// OAuth (Google, GitHub, etc.)
await supabase.auth.signInWithOAuth({
  provider: 'google',
  options: { redirectTo: `${window.location.origin}/auth/callback` }
});

// Sign out
await supabase.auth.signOut();
```

### Critical: getUser() not getSession()

Always use `getUser()` for server-side auth checks. `getSession()` reads from the cookie without verifying it — it can be spoofed. `getUser()` validates the JWT against Supabase.

## Python (JWT, Simple)

For Flask or FastAPI when you don't need a full auth provider:

```python
# Simple JWT pattern
import jwt
from functools import wraps

SECRET = os.environ['JWT_SECRET']

def create_token(user_id):
    return jwt.encode({'user_id': user_id, 'exp': datetime.utcnow() + timedelta(hours=24)}, SECRET)

def require_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization', '').replace('Bearer ', '')
        try:
            payload = jwt.decode(token, SECRET, algorithms=['HS256'])
            request.user_id = payload['user_id']
        except jwt.InvalidTokenError:
            return jsonify({'error': 'Unauthorized'}), 401
        return f(*args, **kwargs)
    return decorated

@app.route('/api/protected')
@require_auth
def protected_route():
    return jsonify({'user': request.user_id})
```

Good enough for a hackathon. Not good enough for production — but that's not what we're doing.

## Hackathon Auth Checklist

- [ ] Can a user sign up and log in?
- [ ] Are protected pages/routes actually protected?
- [ ] Does the demo flow work for a fresh user? (judges won't have accounts)
- [ ] If using OAuth, is the redirect URL set correctly for the deployed domain?
- [ ] Is there a way to quickly create a demo account for the pitch? (pre-seed one if needed)