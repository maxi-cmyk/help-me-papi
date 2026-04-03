# Hardware Documentation

This directory contains hardware-specific skills, resources, ideas, projects, and reference sheets. It is strictly engineered to act as a constraint system for AI interactions concerning embedded devices and signal processing.

## How to use this folder effectively

To get the most out of this structure when collaborating with an AI (or onboarding new developers), follow this workflow:

1. **Attach the Mastery Skill**: When starting a new embedded layout or project, always attach the [`skills/SKILLS.md`](./skills/SKILLS.md) outline. This teaches the AI exactly what hardware limits you face to prevent hallucinatory code output.
2. **Combine with Prompts**: Keep prompts localized by combining the general queries with specialized references found underneath this folder (e.g., adding `concepts-and-math.md` before asking the AI to script an FFT library). 
3. **Modify per Project**: The [`inventory.md`](./inventory.md) dictates exactly what equipment is currently valid. Constantly modify this list; it is the ultimate source of truth preventing the AI from recommending chips you do not possess.

## Architecture & Documentation Structure

- **[`skills/SKILLS.md`](./skills/SKILLS.md)**: The foundational constraint framework and self-improvement instructions for AI interaction in hardware contexts. 
- **[`inventory.md`](./inventory.md)**: User profile mapping existing platforms, confirmed used components, libraries, and a record of completed hardware projects.
- **[`optimisation-and-debugging.md`](./optimisation-and-debugging.md)**: Hardware optimisation reminders and a crucial debugging checklist for spotting I2C hanging or memory bounds hits. 
- **[`concepts-and-math.md`](./concepts-and-math.md)**: Quick reference sheet for bitmask logic, hardware-specific math (like Shannon entropy), and structural patterns.
- **[`components.md`](./components.md)**: A catalog of expected components with analogies to familiar parts for easy learning loops when asking the AI to expand contexts.
- **[`ideas/project_ideas.md`](./ideas/project_ideas.md)**: Scrappy thoughts, feature notes, and project experiments ordered by relevance to the existing skill set.

## Reference Resources
- ESP32 technical reference: https://docs.espressif.com/projects/esp-idf/en/latest/
- MAX7219 datasheet: https://datasheets.maximintegrated.com/en/ds/MAX7219-MAX7221.pdf
- Adafruit MPU6050: https://github.com/adafruit/Adafruit_MPU6050
- ArduinoFFT: https://github.com/kosme/arduinoFFT
- esp-dsp (hardware FFT): https://github.com/espressif/esp-dsp
