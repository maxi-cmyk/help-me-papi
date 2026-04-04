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
