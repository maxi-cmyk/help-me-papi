# Frontend Libraries

We prioritize **unstyled, accessible primitives** and **performant state** over heavy, opinionated UI kits.

## Functional / Unstyled Primitives
- **Radix UI:** The gold-standard for robust React components (Dropdowns, Dialogs, Popovers) with zero styles.
- **React Aria (Adobe):** Excellent hooks for deeply accessible headless states.
- **Tailwind CSS / Vanilla Extract:** For type-safe or utility-first styling bound by strict semantic tokens.

## Animation & Motion
- **Framer Motion:** Absolutely essential for React to achieve that physics-based iOS spring feel.

## Apple-Specific UI Kits (Pre-Styled)
If you do not want to build from scratch with headless primitives, use these:
- **Radix Themes:** Phenomenal spatial scaling right out of the box.
- **Geist UI / Vercel Design System:** Peak modern, minimal, high-contrast developer tools design.
- **Shadcn UI:** Copy-paste components featuring the subtle micro-borders and blur backgrounds typical of macOS.

*(Note: Avoid Bootstrap, Material-UI, or Ant Design if building a consumer-facing app. They carry heavy bundle bloat and require massive overrides).*

## AI Design-Quality Tooling
- **[Impeccable](./impeccable-skill.md)**: Third-party `/impeccable` Claude Code skill (also works with Cursor, Codex, Gemini CLI, etc.) that enforces a stronger design vocabulary and actively rejects overused AI-generated design tells (Inter/DM Sans everywhere, purple gradients, cards-in-cards). Pairs with the `AUDIT_UI_CLARITY` macro in [`PROMPTS.md`](../PROMPTS.md). See [github.com/pbakaus/impeccable](https://github.com/pbakaus/impeccable) / [impeccable.style](https://impeccable.style/).
- **[Taste Skill](./taste-skill.md)**: [leonxlnx/taste-skill](https://github.com/leonxlnx/taste-skill) — a popular third-party skill that gives the agent stronger design taste. Multiple variants (minimalist, brutalist, soft, editorial), image-generation skills, and three tunable dials (VARIANCE / MOTION / DENSITY). Pairs with `/impeccable`: taste generates, impeccable audits. See [tasteskill.dev](https://tasteskill.dev/).
