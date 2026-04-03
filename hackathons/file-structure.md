# Hackathon Project File Structure

A recommended full-stack project structure for hackathons. This combines the "speed-first" backend principles with the scalable frontend structure. This assumes a **monolithic Next.js repository**, which is the fastest way to get a live URL and skip CORS/Vercel split-deployment headaches.

## The Structure (Next.js App Router)

```text
src/
├── app/                  # Routing layer (Frontend Pages & Backend API)
│   ├── (auth)/           # Route groups for UI layouts 
│   ├── api/              # Backend API Routes
│   │   └── [resource]/   # e.g., /api/projects/route.ts
│   ├── dashboard/        # Frontend feature routes
│   ├── layout.tsx        # Root layout
│   └── globals.css       # Global stylesheet
├── components/           # Shared UI components
│   ├── ui/               # Base design system (buttons, inputs, cards)
│   └── layout/           # Shared parts (navbar, footer, sidebar)
├── features/             # Domain-specific modules
│   └── projects/         # E.g., everything related to "Projects"
│       ├── components/   # UI logic specific only to this domain
│       ├── hooks/        # Data-fetching hooks (e.g., SWR / React Query)
│       └── utils/        # Domain-specific frontend helpers
├── lib/                  # Shared Utilities (Backend & Frontend)
│   ├── db/               # Database schemas and connection logic
│   ├── supabase/         # Supabase client singletons (browser & server)
│   └── utils.ts          # Generic helpers (like shadcn/ui class merging)
├── scripts/              # Useful runner scripts
│   └── seed.ts           # Script to quickly seed database with demo data
└── middleware.ts         # Centralized route protection (Auth)
```

## Why this structure wins at Hackathons:
1. **Single Monorepo:** Frontend and Backend live together. You avoid CORS entirely, you only deploy to Vercel once, and you don't need multiple `.env` files.
2. **Feature Co-location:** Multiple team members can work in `features/user` and `features/projects` concurrently. This minimizes merge conflicts in `components/` and `pages/`.
3. **Painless Scaling:** It starts fast, but the `features/` abstraction means you won't end up with a terrifying "junk drawer" component folder at 3:00 AM on Sunday.
4. **Demo Readiness:** Putting `scripts/seed.ts` at the root encourages early data seeding, which is critical for making sure the app actually looks good during the final pitch.
