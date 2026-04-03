# Recommended File Structure

A scalable, feature-based file structure for modern frontend applications (e.g. Next.js or React):

```text
src/
├── app/                  # Routing layer (Pages, Layouts)
│   ├── (auth)/           # Route groups (shared layouts without URL segments)
│   ├── dashboard/        # Standard feature routes
│   ├── globals.css       # Global stylesheet (minimal)
│   └── layout.tsx        # Root layout (providers, fonts)
├── components/           # Shared, generic UI components
│   ├── ui/               # Base design system elements (buttons, inputs, modals)
│   └── layout/           # Cross-page structural parts (Navbar, Sidebar, Footer)
├── features/             # Domain-specific modules (Feature Sliced Design approach)
│   ├── projects/         # E.g., everything related to "Projects" lives here
│   │   ├── components/   # UI logic specific only to projects
│   │   ├── hooks/        # Data-fetching hooks for projects
│   │   └── utils/        # Domain-specific helpers
├── lib/                  # Generic utilities, API clients, third-party wrappers
│   ├── api.ts            # Axios/Fetch wrapper
│   └── utils.ts          # Generic helpers (e.g., date formatting, class merging)
├── hooks/                # Global React hooks (e.g., useWindowSize, useTheme)
├── stores/               # Global state management (Zustand, Redux)
└── types/                # Global TypeScript definitions
```

## Why this structure works:
- **Feature Co-location:** By grouping components, hooks, and helpers by **domain** (in the `features/` directory), you avoid the "junk drawer" problem where the root `components/` folder bloats to hundreds of files.
- **Clear UI Separation:** The `components/ui/` directory stays completely ignorant of your business logic. It just receives props and renders UI.
- **Predictability:** Onboarding new developers is faster because the boundaries between routing (`app/`), generic UI (`components/`), and business logic (`features/`) are strictly enforced.
