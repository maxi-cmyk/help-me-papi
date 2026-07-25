# Rendering and Loading Performance

Patterns for rendering performance, loading strategy, and perceived responsiveness. Nothing ruins a premium aesthetic faster than jank.

## 1. The 60fps Rule (Rendering)
- **CSS Animations:** ONLY animate `transform` (translate, scale, rotate) and `opacity`. These are GPU accelerated.
- **NEVER animate:** `width`, `height`, `top`, `left`, `margin`, `padding`, or `box-shadow`. This triggers expensive reflows (layout recalculations) and repaints, destroying battery life and dropping frames.

## 2. Layout Shift Prevention (CLS)
- Pre-allocate space for dynamic elements. If an image is loading asynchronously, define its `width` and `height` explicitly or use `aspect-ratio` on the container so the DOM doesn't jump aggressively when the asset arrives.

## 3. Font Loading
Premium typography requires massive font files. To prevent FOIT (Flash of Invisible Text) or jarring FOUT (Flash of Unstyled Text):
- Always request `font-display: swap` for non-critical fonts.
- Preload the absolute minimum critical `.woff2` files in the `<head>` to speed up the First Contentful Paint.
- Use system fonts (`font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto...`) where custom type isn't strictly necessary. It guarantees a fast, native look.

## 4. Perceived Performance
- **Optimistic UI updates are mandatory.** If a user clicks a toggle or a heart icon, update the local state immediately, fire the API request in the background, and silently revert/error *only* if the request fails. Don't make them wait 500ms for a spinner on a simple boolean interaction.

## 5. Performance Budgets (Core Web Vitals)
Treat these as hard budgets, not aspirational targets  check them before merging, not after a Lighthouse regression report:
- **LCP (Largest Contentful Paint):** < 2.5s. Preload the LCP image/font; never lazy-load above-the-fold hero media.
- **INP (Interaction to Next Paint):** < 200ms. Replaced FID as the responsiveness metric  break up long JS tasks and defer non-critical work off the main thread.
- **CLS (Cumulative Layout Shift):** < 0.1. Covered by the layout-shift rules above, but also applies to injected banners/ads/cookie notices  reserve their space up front.
- Ship a Lighthouse CI or `web-vitals` RUM check in the pipeline so budgets are enforced automatically, not just eyeballed locally.
