# Design System

The single source of truth for execution. This document dictates how components should be built, the CSS tokens that style them, and the strict accessibility requirements they must follow.

---

## Part 1: Component Patterns
Reusable approaches for component APIs, composition, and system consistency.

### API Design
- **Boolean States First:** Use `isPrimary` over `variant="primary"`.
- **Prop Primitives:** Try to export native primitives via HTML attributes (`...rest`) without blocking or overriding them with custom names.
- **Strict Typing (TypeScript):** Always define prop interfaces explicitly.

### Composition
- **Inversion of Control:** Use the `children` or slot patterns rather than passing enormous configuration objects to the component.
- **Example:**
```jsx
// Bad (Prop drilling)
<Card title="Hello" subtitle="World" icon={<Icon />} primaryAction={() => {}} />

// Good (Composition)
<Card>
  <Card.Header>
    <Card.Title>Hello</Card.Title>
    <Card.Subtitle>World</Card.Subtitle>
    <Icon />
  </Card.Header>
  <Card.Footer>
    <Button onClick={() => {}}>Action</Button>
  </Card.Footer>
</Card>
```

### Hero Sections (Best Practices)
Best practices for the most critical user real estate on any page:
- **The "H1" Rule:** Every hero MUST have exactly one `<h1>`. It should clearly state the unique value proposition in under 6 words.
- **Hierarchy Mapping:** Eyetracking studies show users read: Headline -> Subheadline -> Primary CTA. Do not break this visual flow.
- **Singular Focus:** Limit the hero to ONE primary action (Tier 1). If there must be a secondary action (Tier 2), design it as a subtle outline button or a bare text link (e.g., "Read Documentation").
- **Asset / Media:** If using an image, 3D element, or video, ensure it adds context rather than just decoration. Aggressively optimize it and use `aspect-ratio` to avoid layout shifts (CLS) when the media loads.
- **Immediate Social Proof:** Including micro-elements like tiny customer avatars, star ratings, or trusted company logos right below the CTA drastically improves conversion.

### When NOT to use a component 
- Doing a one-off layout element.
- When the prop list exceeds 7-10 props (this hints that it's handling too many responsibilities).
- When it requires extensive CSS overrides to use it.

---

## Part 2: Styling Tokens (Apple-Like Default)

We heavily restrict our color palette to enforce a "Clarity-First" aesthetic.

### 1. Colors & Contrast
- A UI should be fundamentally monochrome (whites, soft grays, off-blacks) with a **single vibrant accent color** (e.g., `#007AFF`) used purely for interaction feedback.
- Dark mode is NOT an inversion. It requires distinct tokens.

### 2. Glassmorphism & Translucency
To achieve macOS/iOS layered depth, avoid heavy borders and hard drop-shadows on modal surfaces. Use blurred, translucent backgrounds.
```css
/* Token example: --surface-glass */
.surface-glass {
  background-color: rgba(255, 255, 255, 0.7); /* translucent white */
  backdrop-filter: blur(20px) saturate(180%);
  border: 1px solid rgba(255, 255, 255, 0.3); /* subtle micro border */
}
```

### 3. Soft Elevation (Shadows)
Shadows should never look black or muddy. They should be heavily diffused with a slight color tint.
```css
/* Token example: --shadow-elevation-high */
.shadow-high {
  box-shadow: 
    0 10px 40px -10px rgba(0, 0, 0, 0.08),  /* ambient glow */
    0 1px 3px rgba(0, 0, 0, 0.04);          /* sharp edge definition */
}
```

### 4. Typography Scale
Prioritize tight letter-spacing on massive display fonts, and looser tracking on small body text.
- **Display:** (48px+) `letter-spacing: -0.04em; font-weight: 600;`
- **Heading:** (24px - 40px) `letter-spacing: -0.02em; font-weight: 600;`
- **Body:** (16px) `letter-spacing: 0; font-weight: 400; line-height: 1.5;`

---

## Part 3: Alternative Styling Frameworks
If the project strays from the main aesthetic, utilize these token frameworks:

### 1. Arcade / 8-Bit Pixel Art
- **Colors:** Vibrant neon rgb (`#00FFFF`, `#FF00FF`) on pure `#000`.
- **Borders:** Thick, 4px solid borders with `border-radius: 0`.
- **Typography:** Blocky pixel fonts without antialiasing (`-webkit-font-smoothing: none;`).

### 2. Synthwave / Cyberpunk
- **Glow Effects:** Stacked `box-shadow` to simulate neon tubes (e.g., `box-shadow: 0 0 5px #fff, 0 0 20px #ff00de;`).
- **Textures:** Subtle animated CRT scanlines or film grain overlays.

### 3. Swiss / International Style (Bauhaus)
- **Grid Systems:** Aggressive multi-column asymmetric grid. No gradients.
- **Typography:** Gigantic, extra-bold sans-serifs (80px+) set flush-left.

### 4. Skeuomorphism / Y2K Aero
- **Textures:** Multi-stop linear gradients to simulate glossy plastic.
- **Lighting:** Inset shadows highlighting the top edge (`box-shadow: inset 0 2px 4px rgba(255,255,255,0.7)`).
- **Physics:** Buttons physically depress `2px` via `transform: translateY()`.

### 5. Brutalism & Neo-Brutalism
- **Borders & Shadows:** Raw 4px black borders with harsh, un-blurred offset shadows (e.g., `box-shadow: 8px 8px 0px #000;`).
- **Typography:** Chaotic, mixing monospace with heavy sans-serifs.

### 6. Neumorphism (Soft UI)
- **Lighting:** Paired light and dark drop-shadows on a monochromatic canvas to simulate plastic extrusion.

### 7. Hyper-Playful (Gen-Z Aesthetic)
- **Surfaces:** Floating bubbly objects (`border-radius: 999px`) with clashing pastel gradients.

### 8. Data-Dense / Bloomberg Aesthetic
- **Layout:** Terminal density. Minimal 2px padding, stark amber/green on black. Monospaced tabular datasets.

---

## Part 4: Accessibility

Guidance for semantic markup, keyboard support, multimodal interaction design, and inclusive engineering.

### Multimodal Accessibility (Beyond Screen Readers)
1. **ADHD & Cognitive Load:** Keep the interface minimalist. Heavy borders and unnecessary moving backgrounds actively distract users. Ensure the Tier 1 action is obvious.
2. **Vestibular Disorders:** Honor `prefers-reduced-motion: reduce`. Replace sweeping slide animations with cross-fades. Never flash content.
3. **Motor Impairments:** Use generous padding and minimum `48px` tap targets. Avoid deep, nested hover menus that require high cursor precision.
4. **Visual Sensitivities:** Avoid pure black (`#000`) on pure white (`#FFF`) to prevent halation.

### HTML Semantics & Keyboard
- Use standard HTML elements (`<nav>`, `<article>`, `<dialog>`). Supply `role` and `aria-*` tags if building custom headless components.
- **Focus Indicators:** NEVER remove the native outline (`outline: none`) without providing a visible `:focus-visible` alternative.
- **Trap Focus:** Modals and dialogs MUST trap keyboard focus.
