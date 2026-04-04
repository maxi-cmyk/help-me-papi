# Hardware Debugging Macros

Pass these prompts alongside your query when the hardware completely fails or acts erratically.

## System Panics & Reboots

```text
The ESP32 is throwing Watchdog Resets (random reboots) natively.
Check the main `loop()`. Are there blocking calls over 5s? Implement `vTaskDelay`, ensure I2C scanners confirm memory addresses before writes, and check that IRAM_ATTR is strictly placed on all our newly declared ISRs. Check tasks to see if our 8KB default stack overflowed via huge local array variables!
```

## Mysterious State Failures

```text
The inputs are completely erratic and sensors are failing sporadically. 
1. Check the code for unconnected inputs. Are we strictly applying `INPUT_PULLUP` or pulling pins HIGH/LOW manually? Floating pins ruin state logic.
2. Ensure you have commanded a Common GND block. Check the logic to verify all components definitely share GND with the ESP32 array itself.
3. Check the HTTP polling route. The browser charts feel stutteryadjust `genDelay` to sync deeply with the frontend poll interval (150ms).
```

## Compilation / Multi-file Linker Chaos

```text
The compiler is throwing massive errors when linking files.
I suspect `web.cpp` and `main.cpp` are incorrectly sharing structures. Verify `#pragma once` is inside headers, verify I didn't define a struct within `.cpp` directly, and confirm we strictly invoke `webHandle()` or `server.handleClient()` on every primary loop tick so the browser is never ghosted.
```
