# Recommended Hackathon Project Structure

To maintain speed and clarity, follow this Next.js + Supabase structure for all hackathon projects.

---

### **Directory Structure**

```text
src/
 app/                  # Routing layer (Frontend Pages & Backend API)
    (auth)/           # Route groups for UI layouts 
    api/              # Backend API Routes
       [resource]/   # e.g., /api/projects/route.ts
    dashboard/        # Frontend feature routes
    layout.tsx        # Root layout
    globals.css       # Global stylesheet
 components/           # Shared UI components
    ui/               # Base design system (buttons, inputs, cards)
    layout/           # Shared parts (navbar, footer, sidebar)
 features/             # Domain-specific modules (Feature-based architecture)
    example-feature/  # Everything related to a specific domain
        components/   # UI logic specific only to this domain
        hooks/        # Data-fetching hooks (e.g., SWR / React Query)
        utils/        # Domain-specific helpers
 lib/                  # Shared Utilities (Backend & Frontend)
    db/               # Database schemas and connection logic
    supabase/         # Supabase client singletons
    utils.ts          # Generic helpers
 scripts/              # Useful runner scripts (Seeding, Migrations)
    seed.ts           # Script to quickly seed database with demo data
 docs/                 # Documentation (Source of Truth)
    Research.md       # Heavy research on the question/problem
    PRD.md            # Product Requirements & Iteration Notes
    techStack.md      # Tech Stack: What, How, Why
    design.md         # User Flows & Design Inspiration
    pitch/            # Slide outlines, demo scripts, and assets
 middleware.ts         # Centralized route protection (Auth)
```

### **Core Tenets**
1. **Docs as Code:** Keep your strategic foundation (`docs/`) inside the repo so the AI and team are always in sync.
2. **Feature-First:** Use the `features/` directory for anything beyond generic UI. It prevents the `components/` folder from becoming a graveyard.
3. **Seeding & Envs:** Always include a `seed.ts` script and a populated `.env.example`. You cannot waste time manually creating test data or debugging missing local secrets.

---

### **Sidenote: Why the `features/` folder?**
In high-speed development, the `features/` directory implements **Feature-Based Architecture**. This is superior to standard "Layer-Based" folders for three reasons:

*   **Logic Separation:** `components/` is for how things *look* (generic UI like Buttons/Cards). `features/` is for what they *do* (domain logic like `Leaderboard` or `ProjectSubmission`).
*   **AI Efficiency:** When an AI needs to update a specific flow, it only scans the relevant feature folder rather than hunting through global `hooks/`, `utils/`, and `components/` directories.
*   **Encapsulation:** It prevents the global `components/` folder from becoming a graveyard of one-off components. Everything related to a domain (types, hooks, UI) lives and dies together in its feature folder.
