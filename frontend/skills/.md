# Clarity-First Design Principles

This skill is a **constraint layer** that works alongside the primary visual design. Where visual execution handles aesthetic direction, this skill governs **what to show, what to hide, and how to structure interaction** so that every element earns its place on screen. 

## Core Philosophy

Every interface built should feel like it respects the user's time and attention. The goal is not to impress with volume  it's to make the right action obvious and everything else invisible until needed. 

**Three questions to ask before adding ANY element:**
1. **Does the user need this to complete their primary task?** If no, remove it or hide it behind progressive disclosure.
2. **Can this be inferred or defaulted instead of asked?** Smart defaults reduce decisions.
3. **Would a first-time user understand this in under 3 seconds?** If not, simplify.

## Foundational Standards

This skill draws from three proven design systems. Do not copy them wholesale  synthesize their shared principles into a coherent approach for each project.

### Apple Human Interface Guidelines
- **Deference:** The UI stays out of the way of content. Chrome, borders, and decorative elements are minimized so the user's focus lands on what matters.
- **Clarity:** Text is legible at every size. Icons are precise and communicative. Every element serves a functional purpose.
- **Depth:** Use layering, translucency, and motion to convey hierarchy and context  not decoration.

### Material Design (Google)
- **Surface hierarchy:** Use elevation (shadows, layering) to signal importance and relationships between elements. Primary actions float above secondary content.
- **Intentional motion:** Transitions communicate cause-and-effect. An element doesn't just appear  it arrives from somewhere meaningful.
- **Density-appropriate design:** Comfortable touch targets (48dp minimum) for mobile, compact information density for desktop. Never apply the same density to both.

### Nielsen Norman Usability Heuristics
These 10 heuristics act as a **checklist**  run every interface through them before considering it complete:
1. **Visibility of system status**  Always show the user what's happening (loading states, progress indicators, confirmation feedback).
2. **Match between system and real world**  Use language and concepts the user already knows. No jargon unless the audience expects it.
3. **User control and freedom**  Provide clear undo, back, cancel, and escape routes. Never trap the user.
4. **Consistency and standards**  Follow platform conventions. A trash icon means delete everywhere, not archive.
5. **Error prevention**  Disable invalid actions. Use smart defaults. Constrain inputs to valid ranges.
6. **Recognition over recall**  Show options rather than requiring the user to remember them. Labels over icons-only.
7. **Flexibility and efficiency**  Support both novice flows (guided) and expert shortcuts (keyboard, batch actions) where appropriate.
8. **Aesthetic and minimalist design**  Every extra element competes with the relevant ones. Reduce to the essentials.
9. **Help users recognize and recover from errors**  Plain-language error messages that say what went wrong AND how to fix it.
10. **Help and documentation**  If the interface needs a manual, the interface has failed. But if help is needed, make it contextual and searchable.

## The Reduction Framework

Before laying out any interface, classify every potential element into one of three tiers:

### Tier 1  Core Actions (always visible)
These are the 13 things the user came here to do. They get primary visual weight, prominent placement, and the largest interactive targets. 
* **How to identify:** Ask "If this screen could only have one button, what would it be?" That's Tier 1. Then ask if there's a second action that 80%+ of users need on every visit. That might also be Tier 1. Rarely should more than 3 actions share this tier.

### Tier 2  Supporting Functions (visible but subdued)
Settings, filters, secondary navigation, metadata. These support the primary task but aren't the reason the user is here. 
* **Execution:** Use lighter visual weight  secondary buttons, smaller type, muted colors, or positioning in less prominent areas.

### Tier 3  Edge Cases (hidden until needed)
Advanced settings, bulk operations, export options, admin tools. These serve power users or infrequent tasks. 
* **Execution:** Hide them behind overflow menus (), expandable sections, "Advanced" toggles, or contextual menus. 

> **The Rule:** If you can't classify an element into one of these tiers, it probably doesn't belong on this screen at all.
