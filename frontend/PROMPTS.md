# Frontend Agentic Macro Library

> [!IMPORTANT]
> **HOW TO USE THIS LIBRARY**
> 1. **Context First**: Always provide `skills/SKILLS.md` and the relevant `docs/design.md` as context before running these macros.
> 2. **Aesthetic Law**: All generations must adhere to the "Clarity-First" design philosophy (high whitespace, semantic HTML, fluid scale).
> 3. **Validation**: Use the `AUDIT_ACCESSIBILITY` macro on every component before finalization.

---

### **Stage 1: Component Scaffolding**

#### **Macro: SCAFFOLD_UI_COMPONENT**
```markdown
[ROLE] You are a Senior Frontend Engineer & UI/UX Specialist.
[CONTEXT] Analyze the `docs/design.md` and the existing `index.css` variables.
[PLATFORM] **Claude Code** (Primary execution CLI).
[PRE-REQUISITES] 
- Ensure **21st Dev MCP** is connected: `claude mcp add 21st-dev npx -y @21st-dev/mcp`
- Ensure **Stitch MCP** is connected: `claude mcp add stitch npx -y @_davideast/stitch-mcp proxy`
[TASK] Build a high-fidelity [Component Name] component

[TECHNICAL CONSTRAINTS]
- Aesthetic: Apple-style elegance (whitespace, fluid padding, subtle shadows).
- HTML: Strictly semantic (nav, section, main, article, button).
- CSS: Custom properties for all spacing/colors. No hard-coded hex.
- Typography: Inter/System fonts with 1.5 line height.
- Micro-interactions: 200ms easing transitions for hover/active/focus/disabled states.
- Responsive: Fluid scaling for mobile (evaluate layout, don't just stack).

[OUTPUT]
Return semantic HTML, scoped vanilla CSS, and the minimal JS required for interactivity.
```

---

### **Stage 2: Logic & State**

#### **Macro: IMPLEMENT_STATE_MANAGEMENT**
```markdown
[ROLE] You are a State Management Architect.
[CONTEXT] Paste the component code and the required data flow requirements.
[TASK] Implement a robust, predictable state management pattern for this feature.

[OUTPUT]
1. STATE DEFINITION: The core data structure.
2. ACTIONS/REDUCERS: Logic for state transitions.
3. HOOKS/SELECTORS: Clean API for components to consume state.
4. PERSISTENCE: (Optional) Logic for `localStorage` or DB syncing.
```

---

### **Stage 3: Review & Audit**

#### **Macro: AUDIT_ACCESSIBILITY**
```markdown
[ROLE] You are a strict WCAG 2.2 Auditor.
[CONTEXT] Paste the HTML/JS snippet of a component.
[TASK] Identify and fix all accessibility violations.

[CHECKLIST]
- ARIA: Missing labels or incorrect roles.
- FOCUS: Keyboard focus visibility and trap management (especially for modals).
- SEMANTICS: Incorrect tag usage (e.g., div instead of button).
- MULTIMODAL: Contrast (AA+) and animation reduction support.

[OUTPUT] A bulleted list of violations and the exact code refactor for each.
```

#### **Macro: SCAFFOLD_FEATURE**
```markdown
[ROLE] You are a Senior Fullstack Engineer.
[PLATFORM] **Claude Code** (Primary execution CLI).
[PRE-REQUISITES]
- `claude mcp add 21st-dev npx -y @21st-dev/mcp`
- `claude mcp add stitch npx -y @_davideast/stitch-mcp proxy`
[TASK] Scaffold a new feature or API integration into the `features/` directory.

[STEPS]
1. Create `features/[name]/types.ts` for domain interfaces.
2. Create `lib/[name]-client.ts` for the API singleton.
3. Implement `features/[name]/actions.ts` for server logic (Supabase, OpenAI, etc.).
4. Add demo-safe error handling (toasts, not crashes) tailored for a live demo.

[OUTPUT] Confirm the structure follows the "Feature-First" architecture.
```

#### **Macro: REVIEW_UX_HEURISTICS**
```markdown
[ROLE] You are a UX Strategist.
[CONTEXT] Analyze the UI implementation against Nielsen's 10 Heuristics.
[TASK] Provide a critique focused on "Clarity-First" and usability.

[REVIEW CRITERIA]
1. Visibility of system status (loading/success feedback).
2. The 5-second rule: Is the Tier 1 action immediately obvious?
3. Visual Weight: Are secondary actions properly subdued?
4. Breathing Room: Is there at least 48px of whitespace around interactive targets?
5. Run against Nielsen's heuristics.

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

[OUTPUT] Ranked list of "Must Fix", "Should Fix", and "Nitpicks".
```
