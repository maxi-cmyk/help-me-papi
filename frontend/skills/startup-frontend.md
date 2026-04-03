---
name: startup-frontend
description: Frontend patterns for scalable, production-ready React/Next.js applications. Emphasizes feature-sliced design, tight component boundaries, and optimized Web Vitals.
---

# Startup / WebDev Frontend Practices

Frontend patterns optimized for maintainability, clean collaboration across developer teams, and long-term scaling. 

**Language Default**: TypeScript. In production apps, the cost of debugging runtime `undefined` errors drastically outweighs the time spent setting up `interface` shapes. Use Zod for runtime boundary validation.

**When to use this skill**: Web development for startups, enterprise software, applications expected to live for years, or any project facing real users.
**When NOT to use this skill**: Weekend hackathons, temporary disposable prototypes. Use `hackathon-frontend` instead.

---

## Core Principles

1. **Feature-Sliced Architecture.** Do not dump 100 components into `/components`. Co-locate domain logic inside `features/`.
2. **Generic UI Isolation.** Keep generic UI components (`Button`, `Modal`) entirely ignorant of your business logic. They should receive primitive props (`isOpen`) rather than full data objects.
3. **Strict Web Vitals.** Adhere rigorously to the 60fps rule and layout shift prevention. If a component causes jank, it is fundamentally broken.
4. **State Locality.** Global state is a last resort. If data only matters to a specific feature, keep it in that feature's specific hook or local component state. Server state belongs in data-fetching hooks (React Query/SWR/TRPC), not manual global state syncs.
5. **Accessibility is Non-Negotiable.** WCAG AA contrast rules and full keyboard navigation for trapped-focus elements must be tested before merging.

---

## Stack Decision Tree

```
Are we building an SEO-sensitive application or a full-stack monolithic app?
├── Yes → Next.js App Router + Tailwind + Shadcn UI
└── No (It's a pure single page application behind a login wall)
    ├── Does it require crazy client-side performance? → Vite + React + Tailwind
    └── Something else → Evaluate based on team familiarity (Remix, Astro)
```

---

## Navigating the Frontend Domains

When executing tasks, refer directly to the localized domain documentation to ensure you follow project-specific constraints:

### 1. [Architecture & Patterns](../architecture/skills/component-patterns.md)
Refer to the `architecture/` directory for determining when to build a component, how to use Inversion of Control with the `children` prop, and how to structure the `features/` directory properly.

### 2. [UI/UX & Clarity-First Rules](../ui-ux/skills/clarity-first.md)
Before putting any button or card on the screen, run it through the "Clarity-First" reduction framework found in `ui-ux/skills/clarity-first.md` and `layout-and-interaction.md`. Ensure empty states and error recovery are handled.

### 3. [Performance Vitals](../performance/skills/rendering-and-loading.md)
Before adding any animation or loading custom fonts, consult the `performance/` directory to ensure layout shifts (CLS) are prevented and CSS animations only manipulate GPU-accelerated properties (`transform` and `opacity`).

### 4. [Design Inspirations & Aesthetics](../design-inspos/decisions.md)
Consult the `design-inspos/` directory to ensure you are accurately replicating the project's visual constraints, whether it's an Apple-like translucent glassmorphism look, or alternative aesthetics like Neo-Brutalism or Y2K Aero.

### 5. [Tooling & Libraries](../tooling/resources/libraries.md)
Never install a heavy UI kit (like Material-UI or Bootstrap) without explicitly confirming. Stick to unstyled headless primitives (Radix, React Aria) styled with Tailwind or Vanilla CSS.

---

## Execution Workflow

1. Discuss state boundaries with the user before generating large blocks of code.
2. Build generic UI components into `components/ui/` purely using styling tokens.
3. Build the actual business view inside `features/[domain]/components/`.
4. Ensure the visual aesthetic maps correctly to the constraints in `design-inspos/`.
