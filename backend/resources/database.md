<!-- @maxi-cmyk -->
# Database

Pick the right database, set up a clean schema, and don't lose your demo data. Hackathon-focused — just enough structure to not hate yourself at 3am.

## Decision: Which Database?

| Situation | Use | Why |
|-----------|-----|-----|
| Next.js app, need auth + database | Supabase (Postgres) | Auth + database + realtime in one, generous free tier |
| Python backend, need quick SQL | SQLite | Zero setup, single file, no server needed |
| Need a quick key-value store | Supabase or in-memory | Don't set up Redis for a hackathon |
| Sponsor provides a database | Use theirs | Judges notice |
| Storing files/images | Supabase Storage or Cloudinary | Don't put blobs in your database |

Default: Supabase if you're using Next.js. SQLite if you're using Python and the data doesn't need to be shared across deployments.

## Supabase (Postgres)

### Setup (5 minutes)

1. Create a project at supabase.com
2. Grab your URL and anon key from Settings > API
3. Create tables in the Table Editor or SQL Editor

### Schema design for hackathons

Keep it flat. You don't need a perfectly normalized schema for a demo — you need something that works and is easy to query.

```sql
-- Users come free with Supabase Auth (auth.users table)
-- Just create a profiles table for extra info

create table profiles (
  id uuid references auth.users primary key,
  name text,
  avatar_url text,
  created_at timestamptz default now()
);

-- Your main data table
create table projects (
  id uuid default gen_random_uuid() primary key,
  user_id uuid references profiles(id),
  name text not null,
  description text,
  status text default 'draft' check (status in ('draft', 'active', 'done')),
  data jsonb default '{}',
  created_at timestamptz default now(),
  updated_at timestamptz default now()
);
```

Tips:
- **Use `uuid` for IDs.** Auto-generated, no conflicts, works with Supabase Auth.
- **Use `jsonb` for flexible data.** If you're not sure what shape the data will be, throw it in a `jsonb` column. You can query into it later. Better than adding columns mid-hackathon.
- **Use `text` with `check` constraints for status fields.** Simpler than creating enum types.
- **Always add `created_at`.** You'll want to sort by it.

### Row Level Security (RLS)

Supabase exposes your database directly to the client via the anon key. Without RLS, anyone can read/write anything. Enable it:

```sql
-- Enable RLS
alter table projects enable row level security;

-- Users can only see their own projects
create policy "Users see own projects"
  on projects for select
  using (auth.uid() = user_id);

-- Users can only create their own projects
create policy "Users create own projects"
  on projects for insert
  with check (auth.uid() = user_id);

-- Users can only update their own projects
create policy "Users update own projects"
  on projects for update
  using (auth.uid() = user_id);
```

For a hackathon, at minimum enable RLS and add a "users see their own data" policy. Judges who know Supabase will check for this.

### Querying from Next.js

```javascript
const supabase = await createClient();

// List
const { data, error } = await supabase
  .from('projects')
  .select('*')
  .order('created_at', { ascending: false });

// Get one
const { data, error } = await supabase
  .from('projects')
  .select('*')
  .eq('id', projectId)
  .single();

// Create
const { data, error } = await supabase
  .from('projects')
  .insert({ name, description, user_id: user.id })
  .select()
  .single();

// Update
const { data, error } = await supabase
  .from('projects')
  .update({ status: 'active' })
  .eq('id', projectId)
  .select()
  .single();

// Delete
const { error } = await supabase
  .from('projects')
  .delete()
  .eq('id', projectId);
```

Always check `error`. Supabase doesn't throw — it returns `{ data, error }`.

## SQLite (Python)

### Setup (1 minute)

```python
import sqlite3

def get_db():
    db = sqlite3.connect('data/app.db')
    db.row_factory = sqlite3.Row  # return dicts, not tuples
    db.execute('PRAGMA journal_mode=WAL')
    db.execute('PRAGMA foreign_keys=ON')
    return db
```

### Schema

```python
def init_db():
    db = get_db()
    db.executescript('''
        CREATE TABLE IF NOT EXISTS users (
            id TEXT PRIMARY KEY,
            email TEXT UNIQUE NOT NULL,
            name TEXT,
            created_at TEXT DEFAULT (datetime('now'))
        );

        CREATE TABLE IF NOT EXISTS projects (
            id TEXT PRIMARY KEY,
            user_id TEXT REFERENCES users(id),
            name TEXT NOT NULL,
            description TEXT,
            status TEXT DEFAULT 'draft',
            data TEXT DEFAULT '{}',
            created_at TEXT DEFAULT (datetime('now'))
        );
    ''')
    db.commit()
```

Store JSON as text in SQLite, parse it in Python with `json.loads()`.

### Important: SQLite on Vercel doesn't persist

Vercel's serverless filesystem is ephemeral — your SQLite file resets on every deploy. SQLite only works for:
- Local development
- Railway / Render (persistent filesystem)
- Read-only data bundled at build time

If you need persistent data on Vercel, use Supabase.

## Schema Rules for Hackathons

1. **Start with 2–3 tables max.** Users + your main entity + maybe one join table. If you need a 4th table, think hard about whether you actually do.

2. **Don't normalize too early.** A `status` text column is fine. You don't need a separate `statuses` table with foreign keys for a demo.

3. **Use JSON columns for flexible data.** If different items have different shapes (settings, metadata, form responses), store them as JSON rather than creating columns you might not use.

4. **Seed your data.** An empty app looks broken. Write a seed script or use the Supabase SQL editor to insert demo data before your pitch.

5. **Name things clearly.** `user_id`, not `uid`. `created_at`, not `createdAt` or `timestamp`. Future-you (3am you) will thank present-you.