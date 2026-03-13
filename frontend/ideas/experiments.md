# Frontend Experiments

UI, interaction, and product ideas worth trying. 

Use this document to propose micro-interactions or aesthetic concepts that push the boundary of our "Clarity-First" design without cluttering the primary user flows.

## Concept Template

### [Experiment Name]
**Context:** What problem does this solve or what delight does it add?
**Hypothesis:** If we implement X, users will experience Y (e.g., better spatial awareness, clearer feedback).
**Execution/Inspiration:** 
- How does the interaction feel? (e.g., spring physics, blur transitions).
- Links to references or CodePens.

---

## Active Experiments

### 1. Dynamic Island Context
**Context:** Modals and snackbars often feel disconnected from the action that triggered them.
**Hypothesis:** Expanding a floating pill from the exact point of interaction will provide better spatial context.
**Execution:** A pill element with `position: fixed` or `absolute` that uses spring animations to morph into a detailed card layout, maintaining a blurred backdrop filter (`backdrop-filter: blur(20px)`).

### 2. Fluid Typography Scale
**Context:** Granular media queries for text sizes are brittle and lead to jarring jumps on resize.
**Hypothesis:** Using CSS `clamp()` combined with `vw` units will create a perfectly smooth reading experience on any device width.
**Execution:** Example formula: `font-size: clamp(1rem, 0.8rem + 1vw, 1.5rem);`
