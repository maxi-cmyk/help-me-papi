# Embedded Firmware Patterns

When writing native code for embedded microcontrollers (like ESP32/Arduino), these multi-file and systemic architectures prevent spaghetti state machines.

## Multi-File Application Structure
When mixing hardware logic and a web server dashboard, **never dump it all into a single `.cpp` file**. Use this generic structure:

- `main.cpp`  Device setup, main execution loop (`loop()`), task dispatcher.
- `web.cpp`  Server callback logic, endpoints, wifi AP setup.
- `web.h`  Definition parameters to allow the `main.cpp` and `web.cpp` to understand each other.

### The Flag Handshake Pattern
`web.cpp` should **never** call directly into functions owned by `main.cpp` (like `resetSimulation()` or `flashLEDs()`)  this causes race conditions on shared memory.
Instead:
1. Web server route sets a boolean flag (`restartRequested = true`).
2. `main.cpp` constantly checks for `restartRequested` in its main loop.
3. Once actioned, `main.cpp` resets the flag back (`restartRequested = false`).

### Shared Struct Rule 
If both `main.cpp` and `web.cpp` need access to the same configuration struct (e.g. `GameSettings settings`), **define the `struct` in the `.h` file**. Never define it in a `.cpp`. 

### `#pragma once`
Always place `#pragma once` at the very top of `.h` files to prevent double-include linker explosions when scaling files.

---

## ESP32 SoftAP Architecture
When building fully detached, self-contained devices without internet:
- **`WiFi.softAP("MyDevice")`**: Spawns a localized Wi-Fi network.
- **Fixed IP**: The gateway address is inherently hardcoded by the SDK to `192.168.4.1`. You never have to configure this.
- **Data Transfer**: Always use JSON polling on a single endpoint (e.g., `server.on("/data", HTTP_GET, ...)`). The ESP32 should *only* serve raw telemetry JSON. It should never render heavy HTML chunks directly  dump the UI rendering out to Chart.js and raw JavaScript in `index.html`.
