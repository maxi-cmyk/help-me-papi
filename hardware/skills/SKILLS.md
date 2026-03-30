---
name: mini-electronics-hardware
description: >
  ONLY trigger this skill when the conversation explicitly involves hardware —
  components, microcontrollers, sensors, actuators, firmware, embedded code,
  signal processing, or physical electronics builds. Do NOT trigger for pure
  software, web dev, general coding, or any topic with no hardware context.
  When hardware IS mentioned, always: (1) prefer components the user already
  knows before suggesting new ones, (2) explain any new component with an
  analogy to a familiar one, (3) proactively flag relevant optimisation
  techniques from the optimisation table, (4) update completed projects and
  learned components when confirmed by the user.
---

# Mini Electronics Hardware Skill

---

## 🔧 Self-Improvement Instructions
> Claude must follow these rules to keep this skill current and useful.

- **New component acquired/used** → move it from Anticipated to Confirmed Used table in `inventory.md` (and remove from `components.md`). Ask user to confirm before moving.
- **Project completed** → add to Completed Projects table in `inventory.md`. Ask user to confirm before adding.
- **New optimisation technique discovered** → add to Optimisation Reminders table with a "When to Apply" condition in `optimisation-and-debugging.md`.
- **New library or software used** → add to Software / Libraries table in `inventory.md`.
- **Wiring details are NOT stored here** — Claude should reason from datasheets and fundamentals, not recall from this file.
- **Always check the Optimisation Reminders table** at the start of every hardware response (see `optimisation-and-debugging.md`) and flag any that apply to the current project.

---

## Hardware Documentation References

This file serves as the main entry point for the AI. For specific details on user preferences, debugging, and mathematics, refer to the following files in this domain:

- **[`../inventory.md`](../inventory.md)**: User profile mapping existing platforms, confirmed used components, libraries, and completed projects.
- **[`../optimisation-and-debugging.md`](../optimisation-and-debugging.md)**: Hardware optimisation reminders and the debugging checklist. 
- **[`../concepts-and-math.md`](../concepts-and-math.md)**: Quick reference sheet for bitmask logic, hardware specific math (like Shannon entropy), and structural patterns.
- **[`../components.md`](../components.md)**: A catalog of anticipated components with analogies to familiar components.
- **[`../ideas/project_ideas.md`](../ideas/project_ideas.md)**: Project experiments ordered by relevance to the existing skill set.