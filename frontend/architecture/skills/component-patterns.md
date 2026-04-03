# Component Patterns

Reusable approaches for component APIs, composition, and system consistency.

## Component Independence
- **Context:** Global CSS often bleeds into and breaks unrelated UI pieces.
- **Decision:** All components must be scoped (CSS Modules, Web Components, or strict BEM conventions if using vanilla CSS).
- **Consequences:** Components are truly droppable and reusable. Safe deletion without side effects.

## API Design
- **Boolean States First:** Use `isPrimary` over `variant="primary"`.
- **Prop Primitives:** Try to export native primitives via HTML attributes (`...rest`) without blocking or overriding them with custom names.
- **Strict Typing (TypeScript):** Always define prop interfaces explicitly.

## Composition
- **Inversion of Control:** Use the `children` or slot patterns rather than passing enormous configuration objects to the component.
- **Example:**
```jsx
// Bad (Prop drilling)
<Card title="Hello" subtitle="World" icon={<Icon />} primaryAction={() => {}} />

// Good (Composition)
<Card>
  <Card.Header>
    <Card.Title>Hello</Card.Title>
    <Card.Subtitle>World</Card.Subtitle>
    <Icon />
  </Card.Header>
  <Card.Footer>
    <Button onClick={() => {}}>Action</Button>
  </Card.Footer>
</Card>
```

## Hero Sections (Best Practices)
Best practices for the most critical user real estate on any page:
- **The "H1" Rule:** Every hero MUST have exactly one `<h1>`. It should clearly state the unique value proposition in under 6 words.
- **Hierarchy Mapping:** Eyetracking studies show users read: Headline -> Subheadline -> Primary CTA. Do not break this visual flow.
- **Singular Focus:** Limit the hero to ONE primary action (Tier 1). If there must be a secondary action (Tier 2), design it as a subtle outline button or a bare text link (e.g., "Read Documentation").
- **Asset / Media:** If using an image, 3D element, or video, ensure it adds context rather than just decoration. Aggressively optimize it and use `aspect-ratio` to avoid layout shifts (CLS) when the media loads.
- **Immediate Social Proof:** Including micro-elements like tiny customer avatars, star ratings, or trusted company logos right below the CTA drastically improves conversion.

## When NOT to use a component 
- Doing a one-off layout element.
- When the prop list exceeds 7-10 props (this hints that it's handling too many responsibilities).
- When it requires extensive CSS overrides to use it.
