# Frontend Feature Notes

Feature-level thoughts, rough concepts, and UX questions.

When proposing a new feature to the frontend UI, run it through the **Reduction Framework** from our `SKILLS.md` guidelines before writing any code.

## Feature Proposal Template

### Feature: [Name of Feature]

**1. Motivation**
- What user problem does this solve? 
- Is this feature strictly necessary, or can it be inferred/defaulted?

**2. The Reduction Audit**
- **Tier 1 (Core Action - Always Visible):** Does this feature qualify as one of the top 3 reasons a user is on this page?
- **Tier 2 (Supporting Function - Subdued):** Is this a setting or filter? How will we visually de-prioritize it (e.g., smaller type, secondary colors)?
- **Tier 3 (Edge Case - Hidden):** Is this for power users? Where will it be nested (e.g., overflow menu, settings modal)?

**3. Interaction State Checklist**
- [ ] Default state is obvious.
- [ ] Loading state uses skeletons or polite spinners (no layout shifts).
- [ ] Empty state explains the missing data and provides a single CTA.
- [ ] Error states are handled gracefully and in plain English.

---

## Current Note Backlog

*(Add loose thoughts or rapid concepts here before turning them into formalized proposals)*
