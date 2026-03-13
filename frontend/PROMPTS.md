# AI Prompts

Copy-paste templates for implementing frontend work or reviewing code with AI. Make sure `skills/SKILLS.md` is provided as system context before using these.

---

## 1. AI Component Generation Template
Use this when asking an AI to scaffold a new UI component:

```text
Please build a [Component Name] component using vanilla HTML, CSS, and JS (or your current framework).

Constraint Checklist (Strictly Follow):
1. Aesthetic: Apple-style elegance. Rely on whitespace, fluid scale padding, and subtle borders/shadows over solid colors.
2. Structure: Use strictly semantic HTML5 tags (nav, section, main, article, button).
3. Theming: Use CSS custom properties for spacing and colors to allow easy theming. No hard-coded hex colors unless explicitly asked.
4. Typography: Use native system fonts or 'Inter' with a defined, readable scale and 1.5 line height.
5. Micro-interactions: Include default, hover, active, and disabled states. Add a subtle, 200ms easing transition to all state changes.
6. Responsive: Scale constraints down fluidly for mobile. Do NOT simply stack items; re-evaluate the layout for the breakpoint.

Provide the HTML structure first, followed by scoped CSS, and finally any necessary vanilla JS for interactivity.
```

---

## 2. Accessibility Audit Prompt
Use this to rigorously check DOM output:

```text
Act as a strict WCAG 2.2 auditor. Review the following code snippet for accessibility issues. 

Specifically look for:
- Missing ARIA labels or incorrect roles.
- Improper keyboard focus management (is the focus ring visible? does focus get trapped in modals?).
- Semantic failures (using <div> instead of <button>).
- Multimodal considerations (can flashing animations be disabled? is contrast AA+ compliant?).

Output a bulleted list of violations and the direct code fix for each.
```

---

## 3. UX & Aesthetic Review Prompt
Use this when reviewing a new UI implementation (via images, PR, or code). Note: It relies on Nielsen's Heuristics.

```text
Review this UI component or view. Evaluate it strictly against the "Clarity-First" design philosophy and Nielsen's 10 Usability Heuristics. 

Checklist for Review:
1. Nielsen's Heuristics check (especially: Visibility of system status, Match between system and real world, Consistency and standards).
2. The 5-second rule: Can a user immediately identify the primary Tier 1 action?
3. Visual Weight: Are secondary actions properly subdued without failing contrast checks?
4. Whitespace: Is there enough breathing room around interactive targets (min 48px)? Are groups logically separated by space rather than heavy borders?
5. State Coverage: Does the CSS handle hover, focus-visible, target, active, and disabled states transparently?

Provide a list of "Must Fix", "Should Fix", and "Nitpicks". 
```

---

### Reference: Nielsen's 10 Usability Heuristics
When the AI generates reviews or UX plans based on the prompt above, it is evaluating against these definitions:

1. **Visibility of system status:** Always keep users informed about what is going on.
2. **Match between system and the real world:** Speak the users' language, with words, phrases, and concepts familiar to the user.
3. **User control and freedom:** Provide "emergency exits" (undo/redo, clear cancel buttons).
4. **Consistency and standards:** Users should not have to wonder whether different words, situations, or actions mean the same thing.
5. **Error prevention:** Eliminate error-prone conditions or check for them and present users with a confirmation option.
6. **Recognition rather than recall:** Minimize the user's memory load by making objects, actions, and options visible.
7. **Flexibility and efficiency of use:** Accelerators (keyboard shortcuts) to speed up expert users.
8. **Aesthetic and minimalist design:** Interfaces should not contain information that is irrelevant or rarely needed.
9. **Help users recognize, diagnose, and recover from errors:** Error messages should be in plain language and offer a solution.
10. **Help and documentation:** Provide contextual, easily searchable help focused on the user's task.
