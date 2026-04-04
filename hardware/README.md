# Hardware Documentation

This directory contains hardware-specific skills, resources, ideas, projects, and reference sheets. It is strictly engineered to act as a constraint system for AI interactions concerning embedded devices and signal processing.

## How to use this folder effectively

To get the most out of this structure when collaborating with an AI (or onboarding new developers), follow this workflow:

1. **Attach the Mastery Skill**: When starting a new embedded layout or project, always attach the [`skills/SKILLS.md`](./skills/SKILLS.md) outline. This teaches the AI exactly what hardware limits you face to prevent hallucinatory code output.
2. **Combine with Prompts**: Keep prompts localized by combining the general queries with specialized references found underneath this folder (e.g., adding `concepts-and-math.md` before asking the AI to script an FFT library). 
3. **Modify per Project**: The [`inventory.md`](./inventory.md) dictates exactly what equipment is currently valid. Constantly modify this list; it is the ultimate source of truth preventing the AI from recommending chips you do not possess.

## Architecture & Documentation Structure

To prevent context fragmentation, the hardware domain is split into specialized modules:

- **[`architecture/`](./architecture/)**: [Skills](./architecture/skills/), [Resources](./architecture/resources/), [Ideas](./architecture/ideas/).
- **[`math/`](./math/)**: Signal processing, FFT logic, and bitmask standards.
- **[`components/`](./components/)**: Datasheets, pinouts, and physical component references.
- **[`performance/`](./performance/)**: Power management, memory bounds, and 60fps firmware rules.
- **[`skills/`](./skills/)**: Foundations, debugging checklists, and AI-interaction constraints.
- **[`ideas/`](./ideas/project_ideas.md)**: Scrappy thoughts and hardware experiments.
- **[`standards.md`](./standards.md)**: Global hardware engineering rules.
- **[`decisions.md`](./decisions.md)**: Hardware architectural choices.

## Reference Resources
- ESP32 technical reference: https://docs.espressif.com/projects/esp-idf/en/latest/
- MAX7219 datasheet: https://datasheets.maximintegrated.com/en/ds/MAX7219-MAX7221.pdf
- Adafruit MPU6050: https://github.com/adafruit/Adafruit_MPU6050
- ArduinoFFT: https://github.com/kosme/arduinoFFT
- esp-dsp (hardware FFT): https://github.com/espressif/esp-dsp
