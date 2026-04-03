# The "Vanilla-First" Principle

## 1. The "Vanilla-First" Approach
- **Context:** Modern frontend development often reaches for heavy framework abstractions immediately, leading to massive bundle sizes and fragile dependencies.
- **Decision:** We prioritize standard HTML, CSS, and JavaScript. Frameworks (like React or Vue) are only adopted when the state complexity strictly demands them.
- **Consequences:** Faster baseline performance, closer adherence to web standards, and reduced "magic" abstractions hiding DOM flaws.

## 2. Spacing Context over Grid Rigidity
- **Context:** Strict 12-column grids often result in mechanical-looking layouts that don't respect the content's natural flow.
- **Decision:** We use a fluid, 4px-baseline scale (4, 8, 16, 24, 32, 48, etc.) using Flexbox/Grid implicitly based on the component's internal relationships rather than rigidly plotting items on a global 12-column grid.
- **Consequences:** More organic, "Apple-like" layouts where spacing acts as grouping boundaries (Whitespace as a Feature).
