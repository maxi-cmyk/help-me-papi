# Styling Tokens (Apple-Like Default)

We heavily restrict our color palette to enforce a "Clarity-First" aesthetic.

## 1. Colors & Contrast
- A UI should be fundamentally monochrome (whites, soft grays, off-blacks) with a **single vibrant accent color** (e.g., `#007AFF`) used purely for interaction feedback.
- Dark mode is NOT an inversion. It requires distinct tokens.

## 2. Glassmorphism & Translucency
To achieve macOS/iOS layered depth, avoid heavy borders and hard drop-shadows on modal surfaces. Use blurred, translucent backgrounds.
```css
/* Token example: --surface-glass */
.surface-glass {
  background-color: rgba(255, 255, 255, 0.7); /* translucent white */
  backdrop-filter: blur(20px) saturate(180%);
  border: 1px solid rgba(255, 255, 255, 0.3); /* subtle micro border */
}
```

## 3. Soft Elevation (Shadows)
Shadows should never look black or muddy. They should be heavily diffused with a slight color tint.
```css
/* Token example: --shadow-elevation-high */
.shadow-high {
  box-shadow: 
    0 10px 40px -10px rgba(0, 0, 0, 0.08),  /* ambient glow */
    0 1px 3px rgba(0, 0, 0, 0.04);          /* sharp edge definition */
}
```

## 4. Typography Scale
Prioritize tight letter-spacing on massive display fonts, and looser tracking on small body text.
- **Display:** (48px+) `letter-spacing: -0.04em; font-weight: 600;`
- **Heading:** (24px - 40px) `letter-spacing: -0.02em; font-weight: 600;`
- **Body:** (16px) `letter-spacing: 0; font-weight: 400; line-height: 1.5;`

---

## 5. Retro-Tech Palette (NFC Portfolio Variant)

For projects with a deliberately retro/computing identity (portfolio, NFC-linked experiences, developer tools), a separate palette is appropriate:

- **Base:** warm cream/off-white (`#f5f0e8`)
- **Text:** deep navy (`#1a1a40`)
- **Commands/interactive:** brownish-gold (`#b8860b` / `#d4a017`)
- **Traffic-light status:** red `#dc3545`, yellow `#ffc107`, green `#28a745`
- **Retro graphics:** restrained — pixel art, scanline effects, blinking cursor

This is intentionally NOT the Apple-like default. The brand calls for it; the tokens encode it. One palette per project.

---

## 6. Shared Design Tokens in a Multi-Frontend Monorepo

When two or more frontends (e.g., patient + nurse) share one backend:

- Create a **shared tokens module** (`frontend/shared/tokens/`) that exports colors, spacing, typography, elevation as CSS custom properties or JS tokens.
- Both apps import from the shared module. Never duplicate tokens.
- The tokens module is the **single source of truth**. Changing a token in one place updates both apps.
- This module should contain **presentation primitives only** — no business logic, no backend calls. Safe to import anywhere.
