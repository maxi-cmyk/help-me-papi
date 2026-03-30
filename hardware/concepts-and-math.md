# Concepts & Math — Reference Sheet
> Grows as new concepts are applied in projects.

### Bitmask Grid (Conway / Asteroids)
- `uint32_t grid[ROWS]` — each row is a 32-bit word; each bit is one cell
- Read cell `(r, c)`: `(grid[r] >> c) & 1`
- Set cell `(r, c)`: `grid[r] |= (1UL << c)`
- Clear cell `(r, c)`: `grid[r] &= ~(1UL << c)`
- Toroidal left shift: `(r << 1) | (r >> (COLS-1))`
- Toroidal right shift: `(r >> 1) | (r << (COLS-1))`
- Count set bits: `__builtin_popcount(word)`
- **Never hardcode the shift amount** — `COLS-1` is the index of the MSB; wrong value silently teleports wrap-around cells to the wrong column (no crash, corrupted neighbour counts)
- **Never hardcode derived constants** — `256` from `32*8`, `31` from `32-1`; always compute from `COLS`/`ROWS` so a resize is a one-line change

### Shannon Binary Entropy
```
H = -(p · log₂(p) + (1-p) · log₂(1-p))
```
- `p` = fraction of cells alive (`pop / 256.0`)
- Returns 0.0 when uniform (all on or all off), peaks at 1.0 when p=0.5
- Use `log2f()` in C for float precision
- **Measures:** uncertainty in predicting the state of a randomly picked cell — how balanced the alive/dead distribution is
- **Blind spot:** spatial arrangement only — a static checkerboard (p=0.5) scores H=1.0 despite being completely ordered and static
- **Fix:** pair with activity rate — entropy catches ratio drift, activity rate catches spatial stagnation

### Dual-Metric Chaos Detection (Conway project)
| Metric | Formula | What it catches | Blind spot |
|---|---|---|---|
| Shannon entropy | `-(p·log₂p + (1-p)·log₂(1-p))` | alive/dead ratio collapsing toward 0 or 1 | static spatial patterns at p≈0.5 |
| Activity rate | `(born + died) / totalCells` | cells actually changing — spatial dynamics | overall density trends |

Together: entropy=1 + activity=0 → frozen ordered pattern (e.g. checkerboard). entropy→0 + activity→0 → uniform dead/alive. Both high → genuinely active simulation.

### Conway's Game of Life Rules
1. Alive + 2 or 3 neighbours → stays alive
2. Alive + <2 neighbours → dies (underpopulation)
3. Alive + >3 neighbours → dies (overpopulation)
4. Dead + exactly 3 neighbours → becomes alive (reproduction)

### ESP32 WiFi AP Mode
```cpp
WiFi.softAP(SSID, PASSWORD);   // broadcast network
WiFi.softAPIP();                 // returns 192.168.4.1
server.on("/data", handleData);  // register endpoint
server.begin();
// in loop:
server.handleClient();
```

### Flag Handshake Pattern (web→main)
```
web.cpp sets flag = true on HTTP POST
main.cpp polls flag in loop() → handles action → calls ack()
ack() resets flag = false
```
Keeps dependency one-directional: main.cpp knows nothing about HTTP.
