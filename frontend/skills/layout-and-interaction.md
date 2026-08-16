# Layout, Interaction & Execution

## Layout & Spatial Principles

### Information Hierarchy
- Establish a clear visual reading order. On LTR interfaces: primary content top-left, actions top-right or bottom of content flow.
- Use **one** dominant focal point per viewport. If everything is bold, nothing is.
- Group related controls together and separate unrelated groups with whitespace  not lines or borders. Whitespace is the most elegant divider.

### The 80/20 Interface Rule
Design for the 80% use case. The interface should serve the most common user journey with zero friction. The remaining 20% of edge-case functionality should exist but never clutter the primary path. 

**Practical application:**
- Show 5 well-chosen options instead of 20 exhaustive ones.
- Default form fields to the most common value.
- Use progressive disclosure: "Show more options" beats a wall of controls.
- Collapse or tab secondary content rather than stacking it vertically.

### Whitespace as a Feature
Whitespace isn't empty space  it's **active design**. It gives content room to breathe, creates grouping, and signals hierarchy.
- Generous padding inside interactive elements (buttons, cards, inputs)  cramped tap targets feel broken.
- Consistent spacing scale (e.g., 4/8/12/16/24/32/48px) to create rhythm.
- Let key content areas have asymmetric breathing room  not everything needs to be edge-to-edge.

### Responsive Reduction
As viewport shrinks, **remove** rather than compress:
- **Desktop:** Full layout with all three tiers visible in appropriate weight.
- **Tablet:** Tier 3 collapses into menus; Tier 2 moves to secondary panels.
- **Mobile:** Tier 1 only in the main view; Tier 2 behind tabs or bottom sheets; Tier 3 behind settings.
> *Never shrink a desktop layout into mobile. Redesign the information flow for each breakpoint.*

---

## Terminal / CLI Aesthetic (NFC Portfolio Case Study)

Some products benefit from a deliberately constrained, retro-computing visual language (portfolio sites, developer tools, NFC-connected physical touchpoints). When the brand calls for it:

### Constraints as a Design Tool
A terminal aesthetic trades visual excess for **signal density**:
- Monospace body (`font-family: 'JetBrains Mono', 'SF Mono', 'Fira Code', monospace`).
- Near-black background (`#0a0a0a` or `#0d0d0d`), high-contrast text (`#e0e0e0`+).
- Minimal color: one accent for links/interactions, one dim for secondary, one bright for the cursor/command prompt.
- No hero images, no cards, no gradients. The content IS the interface.

### Animated Boot Sequence
A short, skippable terminal boot animation on first visit creates a memorable "arrival" moment:
- Render lines sequentially with a typewriter effect.
- End at a blinking cursor and a command prompt.
- Provide a visible "Skip animation" link — never trap the user.

### Command-Router UI
Treat the site like a CLI:
- A `whoami` command that prints identity + brief bio.
- A `help` command that lists available commands.
- `ls focus/` that lists current focus areas.
- `clear` to reset.
- Each "page" is a command output, not a route change. The URL can still be shareable via hash.

### Why It Works
- **Instant performance**: a terminal UI is lightweight by nature — no large assets, excellent Core Web Vitals on weak connections (common at events where someone taps an NFC card).
- **Memorable**: stands out from the generic SaaS aesthetic of every other portfolio.
- **Physical-digital coherence**: an NFC card that opens a terminal-styled site bridges the physical object and the digital experience with a consistent "hacker" sensibility.

### Pitfalls to Avoid
- Don't sacrifice readability for theme: monospace is fine, but body text still needs 16px+ and 1.5 line height.
- Don't make the user learn commands to find basic content — provide a visible nav alongside the terminal.
- Skip the animation on subsequent visits or when `prefers-reduced-motion` is set.

---

## Interaction Design

### Feedback & State
Every interactive element must have clearly distinct states:
- **Default:** Resting state, clearly interactive (affordance).
- **Hover:** Subtle acknowledgment (desktop only; never rely on hover for critical info).
- **Active/Pressed:** Immediate tactile feedback.
- **Disabled:** Visually muted AND communicates why (tooltip or adjacent text).
- **Loading:** Skeleton screens or inline spinners, never a blank void.
- **Success/Error:** Confirmation near the point of action, not in a disconnected banner.

### Empty States
An empty state is a **first impression, not a dead end**. Every empty state should:
- Explain what this area is for.
- Show one clear action to populate it.
- Optionally, show a helpful illustration or example.

### Navigation
- **Flat over deep:** Reduce nesting. If something is 3+ clicks deep, consider surfacing it.
- **Persistent orientation:** The user should always know where they are (breadcrumbs, highlighted nav items, descriptive page titles).
- **Predictable placement:** Primary nav at top or left. Actions contextual to content near that content  not in a distant toolbar.

## Typography & Readability
- **Body text:** 16px minimum for web, 1415px minimum for dense data UIs. Line height 1.41.6.
- **Heading hierarchy:** Limit to 3 levels in any single view. If you need a fourth level, the page is too complex  split it.
- **Contrast:** WCAG AA minimum (4.5:1 for body text, 3:1 for large text). This isn't optional  it's a legal and moral baseline.
- **Line length:** 5075 characters per line for body text. Wider than that and readability drops sharply.
- **Label everything:** Icons without labels are ambiguous. Use icon + text for primary nav. Icon-only is acceptable only for universally understood symbols (close [X], search [Search], menu [Menu]) or when a tooltip is provided.

## Color with Purpose
- **Semantic color:** Reserve specific colors for specific meanings. Red = destructive/error. Green = success/positive. Blue = interactive/informational. Yellow/amber = warning. Don't use red for a non-destructive primary button  it will trigger anxiety.
- **Limit the palette:** 1 primary brand color, 1 accent, neutrals for structure. Additional semantic colors as needed. That's it.
- **Accessible contrast:** Test every color combination. A beautiful palette that fails WCAG is a broken palette.
- **Dark mode considerations:** If supporting dark mode, design it intentionally  don't just invert colors. Reduce surface brightness, increase contrast for text, and ensure semantic colors remain distinguishable.

## Anti-Patterns to Actively Avoid

| Anti-Pattern | Why It's Harmful | What to Do Instead |
| :--- | :--- | :--- |
| **Card overload** | Every piece of content in its own card creates visual noise and false equivalence. | Use cards sparingly for distinct, actionable items. Use simple list rows or inline groups for related content. |
| **Button bloat** | 5+ buttons in a single view creates decision paralysis. | 1 primary CTA, 12 secondary actions, everything else in overflow. |
| **Settings on the surface** | Showing every toggle and option upfront overwhelms new users. | Smart defaults + "Customize" entry point for power users. |
| **Rainbow status indicators** | Using 5+ colors for different statuses creates cognitive overload. | Limit to 3 status colors; use text labels alongside color. |
| **Modal abuse** | Modals that spawn modals, or modals for non-critical info, feel like interruptions. | Reserve modals for confirmations and focused tasks. Use inline expansion or side panels for supplementary content. |
| **Icon-only navigation** | Users guess at meaning, increasing error rate and cognitive load. | Always label primary navigation. Icon-only is for toolbar-density UIs where users have learned the icons. |
| **Infinite scrolling without anchor** | Users lose their place and can't share or return to specific content. | Provide pagination, "back to top", or section anchors for long content. |
| **Decoration masquerading as UI** | Gradients, shapes, and illustrations that look interactive but aren't. | Every visual element should either communicate information or provide interaction. Decoration should never mimic affordance. |

## Implementation Checklist

Before considering any interface complete, verify:

- [ ] **Squint test:** Squint at the screen. Can you identify the primary action? If not, the hierarchy has failed.
- [ ] **5-second test:** Could a new user understand the purpose of this screen within 5 seconds?
- [ ] **Tier audit:** Is every visible element classified as Tier 1, 2, or 3? Is Tier 3 properly hidden?
- [ ] **Tap target check:** All interactive elements are at least 4444px (Apple) / 4848dp (Material).
- [ ] **State coverage:** Do all interactive elements have default, hover, active, disabled, loading, and error states?
- [ ] **Empty state:** Does every list, table, or dynamic area have a meaningful empty state?
- [ ] **Error recovery:** Can the user undo or recover from every destructive action?
- [ ] **Contrast check:** Does all text meet WCAG AA contrast ratios?
- [ ] **Responsive reduction:** Does the layout gracefully reduce (not just compress) on smaller viewports?
- [ ] **Cognitive load:** Count the number of decisions on screen. If it's more than 5, reduce.
