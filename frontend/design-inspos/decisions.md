# Design System Decisions & Alternative Frameworks

If the project strays from the main Apple-like aesthetic, utilize these token frameworks and their implementation decisions. See `resources/inspirations.md` for visual references.

## 1. Arcade / 8-Bit Pixel Art
- **Colors:** Vibrant neon rgb (`#00FFFF`, `#FF00FF`) on pure `#000`.
- **Borders:** Thick, 4px solid borders with `border-radius: 0`.
- **Typography:** Blocky pixel fonts without antialiasing (`-webkit-font-smoothing: none;`).

## 2. Synthwave / Cyberpunk
- **Glow Effects:** Stacked `box-shadow` to simulate neon tubes (e.g., `box-shadow: 0 0 5px #fff, 0 0 20px #ff00de;`).
- **Textures:** Subtle animated CRT scanlines or film grain overlays.

## 3. Swiss / International Style (Bauhaus)
- **Grid Systems:** Aggressive multi-column asymmetric grid. No gradients.
- **Typography:** Gigantic, extra-bold sans-serifs (80px+) set flush-left.

## 4. Skeuomorphism / Y2K Aero
- **Textures:** Multi-stop linear gradients to simulate glossy plastic.
- **Lighting:** Inset shadows highlighting the top edge (`box-shadow: inset 0 2px 4px rgba(255,255,255,0.7)`).
- **Physics:** Buttons physically depress `2px` via `transform: translateY()`.

## 5. Brutalism & Neo-Brutalism
- **Borders & Shadows:** Raw 4px black borders with harsh, un-blurred offset shadows (e.g., `box-shadow: 8px 8px 0px #000;`).
- **Typography:** Chaotic, mixing monospace with heavy sans-serifs.

## 6. Neumorphism (Soft UI)
- **Lighting:** Paired light and dark drop-shadows on a monochromatic canvas to simulate plastic extrusion.

## 7. Hyper-Playful (Gen-Z Aesthetic)
- **Surfaces:** Floating bubbly objects (`border-radius: 999px`) with clashing pastel gradients.

## 8. Data-Dense / Bloomberg Aesthetic
- **Layout:** Terminal density. Minimal 2px padding, stark amber/green on black. Monospaced tabular datasets.
