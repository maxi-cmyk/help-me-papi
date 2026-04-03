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
