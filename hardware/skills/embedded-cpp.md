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

When executing complex sub-features for embedded logic systems, interact strictly against these isolated domains:

### 1. [Firmware Architecture](../architecture/skills/firmware-patterns.md)
Reference this directory prior to splitting a monolithic file. Outlines precise instructions on `main.cpp` / `web.cpp` logic partitions, preventing linker double-include faults, and correct Flag Handshake protocol logic preventing race conditions.

### 2. [Performance & Output Bounds](../performance/skills/optimisation.md)
Crucial limits for display renders and loop speed blocks. Defines exactly why `delay()` is fatally forbidden inside tasks, mandates hardware SPI, and demands `IRAM_ATTR` configurations for interrupts explicitly. Contains core debugging prompts.

### 3. [Math & Signal Limits](../math/skills/signal-processing.md)
Governs all computational outputs dictating how to map Hann windows mapped to `esp_dsp` FFT calculations, Complementary Filters for IMU datasets, and O(1) bitwise toroidal logic loops for structural LED calculations across memory bounds.

### 4. Physical Requirements
Check the local `inventory.md` stored entirely inside `hardware/components` before suggesting external components. If an integration matches components confirmed in the inventory, bias the generation output to strictly utilise them first.

---

## Execution Setup Check

When producing embedded code:
1. Is an ISR defined? If yes, confirm `IRAM_ATTR` and minimal logic hooks.
2. Are delays configured? Swap `delay()` globally for non-blocking timer loops or FreeRTOS `vTaskDelays`.
3. Does the system demand concurrent web telemetry arrays natively hosted on the ESP? Confirm softAP definitions using the `192.168.4.1` standard constraints mapped inside the architecture module.
