# Frontend Documentation

This directory contains our highly modular, domain-driven frontend documentation. It is designed to be highly AI-friendly and perfectly organized so you instantly know where to find rules, aesthetic inspirations, or architectural decisions.

## Hackathon Focus (Visual Wow & Speed)

When building for a hackathon, prioritize **The First Impression** and **Landing Page Polish**.

- **Aesthetics**: Use high-impact visual trends like **Glassmorphism**, **Smooth Gradients**, and **Dark mode** to wow judges instantly.
- **Components**: Use Radix UI, Shadcn/UI, or Headless UI to move fast without sacrificing quality. Avoid building complex UI from scratch.
- **State**: Use React Query (TanStack Query) for simple data fetching and local state (Zustand) over complex Redux. 
- **Micro-interactions**: Spend 15 minutes on smooth hover effects and transitions—it makes the app feel premium.
- **LLM Usage**: Attach `hackathon-frontend.md` and your aesthetic choice from `/design-inspos` to your prompt.

---

## Webdev Focus (Production Standards)

For standard production web applications, prioritize **Scalability** and **SEO**.

- **Architecture**: Use **Feature-Sliced Design (FSD)** to maintain a clean codebase as features grow.
- **Accessibility**: Strict **WCAG AA** compliance with semantic HTML and ARIA labels.
- **Search Engine Optimization**: Proper metadata tags, SSR/SSG, and fast Core Web Vitals (LCP, CLS).
- **Core Engineering**: 60fps rule for animations and absolute prevention of layout shifts.

---

## Startup Focus (Growth & Iteration)

For startups, prioritize **User Retention** and **Feedback Loops**.

- **Product Market Fit**: Simple, conversion-driven UX with high-performance landing pages.
- **Speed to Market**: Use reliable component libraries (Radix/Tailwind) to ship MVP fast but with a premium feel.
- **Analytics**: Deep integration for A/B testing and user behavior tracking. 
- **Optimistic UI**: Use loading states (Skeletons) and optimistic updates (React Query) to keep the app feeling lightning-fast.

---

## Philosophy: Clarity-First Design
Our frontend approach heavily prioritizes an **elegant, Apple-like, Clarity-First aesthetic**. The core foundation is built upon vanilla HTML, CSS, and JavaScript. 

- **HTML** must strictly be semantic.
- **CSS** should focus on minimalism, purposeful whitespace, and refined typography.
- **JavaScript** should be added purposefully to enhance interaction through micro-animations.

---

## How to use this folder effectively

To get the most out of this structure when collaborating with an AI, follow this workflow:

1. **Attach the Mastery Skill**: When starting a new feature, always attach the relevant file from [`/skills`](./skills) (e.g., `startup-frontend.md` or `hackathon-frontend.md`).
2. **Combine with Prompts**: Use the templates in [`PROMPTS.md`](./PROMPTS.md) or domain-specific `prompts/` folders.
3. **Modify per Project**: Use these as a baseline. For a specific theme (e.g., Cyberpunk), update the local definitions in `design-inspos/`.

---

## Architecture & Directory Structure

To prevent context fragmentation when using AI, every domain follow a strict modular structure:
`domain/`
├── `skills/` — Domain-specific fundamentals and best practices.
├── `prompts/` — Robust, token-efficient scaffolds for AI generation.
├── `resources/` — Curated links, libraries, and design inspiration.
├── `ideas/` — Scrappy thoughts and UI experiments.
├── `standards.md` — Hard rules for the domain (e.g., 60fps rule).
└── `decisions.md` — Architectural choices and justifications.

### Domains:
- **[`architecture/`](./architecture/)**: Routing logic, FSD structure, and backend integration.
- **[`design-inspos/`](./design-inspos/)**: Aesthetic source of truth (Glassmorphism, Typography, Themes).
- **[`performance/`](./performance/)**: Engineering standards to eliminate jank (60fps, CLS prevention).
- **[`ui-ux/`](./ui-ux/)**: UX heuristics, focal points, and accessibility rules.
- **[`tooling/`](./tooling/)**: Functional library choices (Radix, React Aria, Tailwind).
- **[`ideas/`](./ideas/)**: Cross-domain brainstorming and UI experiments.
- **[`PROMPTS.md`](./PROMPTS.md)**: Master prompt templates for consistent generation.
