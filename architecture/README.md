# System Architecture Design

This directory serves as the high-level "Map of the World" for the entire system. While individual domains (Backend, Frontend, Hardware) handle their internal structures, this space is dedicated to **Cross-Functional Design**, **Integration Patterns**, and **Infrastructure Strategy**.

---

## Strategic Navigation

Use these links to jump between specific architectural layers:

- **[Backend Architecture](../backend/architecture/)**: Service layers, API envelopes, and database scaling.
- **[Frontend Architecture](../frontend/architecture/)**: Feature-Sliced Design (FSD), routing, and state management.
- **[Hardware Architecture](../hardware/architecture/)**: Firmware modules, communication protocols, and power management.

---

## System Design Standards

### 1. High-Level Modeling
We use the **C4 Model** (Context, Containers, Components, Code) to describe the system. Always ensure that the "System Context" diagram is up to date in the `diagrams/` folder.

### 2. Integration Patterns
- **API First**: All integrations between frontend and backend must be defined via Zod schemas or OpenAPI before implementation.
- **Event-Driven**: Heavily prioritize asynchronous communication for long-running hardware simulation tasks.

### 3. Core Decisions
Refer to **[decisions.md](./decisions.md)** for documented trade-offs regarding:
- Monolith vs. Microservices.
- SQL vs. NoSQL choices.
- Caching strategies (Edge vs. Origin).

---

## Architecture & Directory Structure

To maintain a high-level "Map of the World", we segment systemic design into:

- **[`diagrams/`](./diagrams/)**: [C4 Context](./diagrams/c4-context.mermaid) and system flows.
- **[`skills/`](./skills/)**: [System Design](./skills/system-design.md) and scalability playbooks.
- **[`resources/`](./resources/)**: Infrastructure templates and Cloudformation/Terraform.
- **[`ideas/`](./ideas/)**: Potential architectural pivots and R&D logs.
- **[`standards.md`](./standards.md)**: Global reliability and integration rules.
- **[`decisions.md`](./decisions.md)**: Immutable trade-off records.
