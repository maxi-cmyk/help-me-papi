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

## Modern Debugging Workflow (beyond `Serial.println`)

Reach for these before resorting to guess-and-reflash cycles:

- **PlatformIO + `platformio.ini` debug config**: Use PlatformIO's native GDB/OpenOCD integration for ESP32/ARM targets instead of raw `esptool` flashing loops  breakpoints and live variable inspection beat sprinkling `Serial.println` everywhere.
- **ESP-IDF `idf.py monitor` with core-dump decoding**: On crash/panic, decode the backtrace with `idf.py coredump-info` rather than guessing from a raw hex dump  it maps straight back to source lines.
- **Logic analyzer for timing-critical bugs** (e.g. Saleae/sigrok clone): When `delay()`/ISR timing behaves inconsistently, a logic analyzer on the SPI/I2C lines settles the "is it code or is it hardware" question in minutes instead of hours of print-statement bisection.
- **RTT (Real-Time Transfer) over UART logging** where supported (SEGGER J-Link, some ESP32 debug probes): non-blocking, doesn't perturb timing-critical loops the way blocking `Serial.println` does.
- Keep the `#backlog` triage habit: attach this file plus the relevant `docs/decisions.md` entry before asking an AI agent to debug intermittent hardware failures  intermittent bugs are usually a wiring/power issue, not a logic bug, and the agent needs that context to avoid chasing code ghosts.
