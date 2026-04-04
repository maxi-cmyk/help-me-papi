---
name: embedded-cpp
description: Mastery skill triggered exclusively for embedded electronics, signal processing, hardware interactions, and firmware structuring in C++.
---

# Embedded Hardware Architecture 

This mastery skill encapsulates structural interactions when handling physical hardware configurations scaling across microcontrollers (e.g. Arduino / ESP32 interfaces). DO NOT deploy this documentation when managing pure web servers or general JS development.

**Rule One:** Ensure physical execution constraints are strictly honoured. Memory, floating pins, voltage bounds, and CPU blocking limits are primary considerations before any loop logic is structured.

**Rule Two:** Always explain a new physical component proposed to a user with an analogy mapped directly to logic they firmly possess (e.g., comparing an I2C multiplexer directly to a router switcher). 

---

## Navigating the Hardware Domains

For complex embedded systems, manually attach the following context files to your prompt to prevent hallucinatory or non-optimized code:

### 1. [Firmware Architecture](../architecture/skills/firmware-patterns.md)
**When to attach**: When structuring your `main.cpp` vs `web.cpp` logic partitions, preventing linker errors from double-includes, or implementing Flag Handshake protocols for multi-core ESP32 tasks.

### 2. [Performance and Optimization](../performance/skills/optimisation.md)
**When to attach**: For all display rendering, interrupt handling (`IRAM_ATTR`), or when timing is critical. Use this to ensure the AI swaps `delay()` for non-blocking timer loops.

### 3. [Math and Signal Processing](../math/skills/signal-processing.md)
**When to attach**: When implementing FFT calculations (e.g., `esp_dsp`), Hann windows, IMU filtering, or bitwise logic for high-speed LED arrays.

### 4. [Inventory and Components](../components/inventory.md)
**When to attach**: Always. This ensures the AI only recommends components, pins, and libraries that you actually have in your physical inventory.

---

## Execution Setup Check

When producing embedded code:
1. Is an ISR defined? If yes, confirm `IRAM_ATTR` and minimal logic hooks.
2. Are delays configured? Swap `delay()` globally for non-blocking timer loops or FreeRTOS `vTaskDelays`.
3. Does the system demand concurrent web telemetry arrays natively hosted on the ESP? Confirm softAP definitions using the `192.168.4.1` standard constraints mapped inside the architecture module.
