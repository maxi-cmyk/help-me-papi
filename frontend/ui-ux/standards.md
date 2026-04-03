# UX/UI Accessibility Standards

Guidance for semantic markup, keyboard support, multimodal interaction design, and inclusive engineering.

## Multimodal Accessibility (Beyond Screen Readers)
1. **ADHD & Cognitive Load:** Keep the interface minimalist. Heavy borders and unnecessary moving backgrounds actively distract users. Ensure the Tier 1 action is obvious.
2. **Vestibular Disorders:** Honor `prefers-reduced-motion: reduce`. Replace sweeping slide animations with cross-fades. Never flash content.
3. **Motor Impairments:** Use generous padding and minimum `48px` tap targets. Avoid deep, nested hover menus that require high cursor precision.
4. **Visual Sensitivities:** Avoid pure black (`#000`) on pure white (`#FFF`) to prevent halation.

## HTML Semantics & Keyboard
- Use standard HTML elements (`<nav>`, `<article>`, `<dialog>`). Supply `role` and `aria-*` tags if building custom headless components.
- **Focus Indicators:** NEVER remove the native outline (`outline: none`) without providing a visible `:focus-visible` alternative.
- **Trap Focus:** Modals and dialogs MUST trap keyboard focus.
