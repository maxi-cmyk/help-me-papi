---
name: hackathon-frontend
description: Frontend patterns for hackathons and prototypes. Prioritizes velocity, the "WOW demo", and zero-friction deployments.
---

# Hackathon Frontend Practices

Frontend patterns optimized for absolute speed, clarity, and demo-ability. Not enterprise architecture — just enough structure to win the pitch and prevent deployment disasters at 3:00 AM.

**Language Default**: JavaScript or TypeScript with `any`. Do not waste an hour fighting TypeScript utility types or generic inference constraints. 

**When to use this skill**: Weekend hackathons, temporary prototypes, MVPs built specifically to pitch to investors.
**When NOT to use this skill**: Any project that expects to be maintained for longer than 3 months. Use `startup-frontend` instead.

---

## Core Principles

1. **Velocity over Purity.** Code quality tradeoffs are acceptable as long as they don't block the visual pitch. Inline Tailwind heavily instead of trying to abstract every single layout wrapper.
2. **The "Hero Focus".** Spend 70% of your frontend effort on the first viewport the user sees (The Hero Section). This wins hackathons. Secondary pages can use absolute defaults.
3. **Monolithic Repo.** Keep the frontend and backend in a single Next.js project. You completely bypass CORS issues, split-deployment headaches, and sync issues.
4. **Use Pre-Built Primitives.** Copying Shadcn UI components is mandatory. Do not bespoke style a dropdown menu or modal from scratch.
5. **Fake Data Early.** Create beautiful UI states utilizing hardcoded JSON objects, then swap in the real API connection once it's completely ready. Don't let UI development block on a broken backend.

---

## Stack Decision Tree

```
Are we building for a hackathon?
├── Yes → Next.js App Router + Tailwind + Shadcn UI (Hosted on Vercel)
└── (There is no 'No'. This is the fastest stack to ship full-stack features).
```

---

## State Management Shortcut

- Do not set up complex Context providers or Redux sagas.
- Pass props manually down the tree if it's only 2 levels deep.
- If it's a global app state (like auth, or a shared map), throw it into a simple un-optimized `Zustand` store for instant access anywhere.

---

## Navigating the Domains

Even at a hackathon, respect the aesthetic. Pull from specific project docs when generating:

- **[Clarity-First Rules](../ui-ux/skills/clarity-first.md)**: Keep the interface ruthlessly simple to prevent cognitive overload during your 2-minute pitch.
- **[Design Inspirations](../design-inspos/decisions.md)**: Pick a distinct alternative style (like Synthwave or Neo-Brutalism) to stand out, and execute it using the CSS constraints defined.
- **[Component Patterns](../architecture/skills/component-patterns.md)**: Only read the "Hero Sections (Best Practices)" section to ensure the hero layout maps perfectly to user eyetracking (Headline -> Subheadline -> Single CTA).

---

## Deploy Early Checkout

1. Deploy the empty scaffolding to Vercel in Hour 1 to guarantee environment variables are configured.
2. Ensure the core "WOW" feature works perfectly on the live URL.
3. Have a fallback screen recording ready in case the venue Wi-Fi drops during the demo.
