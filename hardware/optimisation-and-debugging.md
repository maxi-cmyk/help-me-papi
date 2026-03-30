# Optimisation & Debugging

## ⚡ Optimisation Reminders
> Scan this at the start of every hardware response. Flag every applicable technique to the user.

| # | Technique | When to Apply |
|---|---|---|
| 1 | **Hardware SPI over software/bit-bang** | Any SPI device (MAX7219, TFT, etc.) |
| 2 | **Full frame buffer → single SPI push** | Any LED matrix or display animation |
| 3 | **Double buffering** | Animations that show visible flicker |
| 4 | **Direct GPIO register writes** (`GPIO.out_w1ts/w1tc`) | Time-critical signal toggling on ESP32 |
| 5 | **Hardware timer ISR for fixed-rate sampling** | FFT, audio, ADC — never use `delay()` |
| 6 | **Interrupt-driven inputs with flag pattern** | Buttons, tilt switch, IMU data-ready, encoders |
| 7 | **`IRAM_ATTR` on all ISR functions** | Every interrupt handler on ESP32 |
| 8 | **`char[]` + `sprintf` instead of Arduino `String`** | Any string work in embedded C++ |
| 9 | **Hann window before FFT** | All FFT / spectral analysis |
| 10 | **`esp_dsp` hardware-accelerated FFT** | FFT on ESP32 (faster than ArduinoFFT) |
| 11 | **Complementary filter for angle** (α≈0.96) | IMU tilt/angle estimation — fast and sufficient |
| 12 | **Anti-windup clamp on PID integral** | Any PID control loop |
| 13 | **Decoupling capacitors on every IC** | 100nF ceramic (HF noise) + 10µF electrolytic (bulk) |
| 14 | **`INPUT_PULLUP` + 10–20ms software debounce** | All mechanical switches and tilt sensors |
| 15 | **MPU-6050 offset calibration before data collection** | Any IMU project |
| 16 | **Bitmask row representation (`uint32_t grid[8]`)** | Any 2D LED grid — neighbour sums via bit shifts, O(1) cell access |
| 17 | **`rotL/rotR` for toroidal wrap** (`(r<<1)\|(r>>31)`) | Any cellular automaton or wrapping grid |
| 18 | **`__builtin_popcount()` for fast bit counting** | Population counts, entropy calc on bitmask grids |
| 19 | **Shannon binary entropy** (`-(p·log₂p + q·log₂q)`) | Chaos/complexity metric for grid-based simulations |
| 20 | **ESP32 WiFi Access Point mode** (`WiFi.softAP()`) | Self-contained device; no router/credentials; fixed IP 192.168.4.1 |
| 21 | **Multi-file PlatformIO structure** (`main.cpp`, `web.cpp`, `web.h`) | Any project mixing hardware logic + web server; keeps concerns separated |
| 22 | **Flag handshake pattern** (`restartRequested()` / `restartAck()`) | Browser→ESP32 commands; prevents web.cpp calling into main.cpp directly |
| 23 | **Browser polling `/data` endpoint (JSON, 150ms)** | Live dashboards; ESP32 serves raw data, browser does all rendering (Chart.js) |
| 24 | **`analogRead()` for noise-seeded `randomSeed()`** | Any simulation needing different seed each boot |
| 25 | **Potentiometer → initial density mapping** | Tunable simulation parameters without reflashing |

---

## 🐞 Debugging Checklist

1. **Measure power rails under load** — voltage sag causes mysterious failures before any code issue
2. **No floating inputs** — every unconnected input pin must be pulled HIGH or LOW
3. **Common GND** — all components share GND with the ESP32
4. **Run I2C scanner** before writing code to confirm device addresses
5. **`Serial.begin(115200)` minimum** — slower speeds cause noticeable debug lag
6. **Watchdog resets** — random ESP32 reboots = blocking `loop()` >5s; use `vTaskDelay`
7. **Stack overflow** — ESP32 default task stack 8KB; increase for large local arrays in tasks

### Multi-file / Web Server Debugging
8. **`#pragma once` in every `.h` file** — prevents double-include linker errors
9. **Shared structs go in the header** (`web.h`) — never define a struct in `.cpp` that both files need
10. **`webHandle()` every loop** — forgetting `server.handleClient()` means the browser never gets a response
11. **`192.168.4.1` is always the AP gateway** — hardcoded in ESP32 SDK, never needs configuration
12. **HTTP polling lag** — if browser charts feel stuttery, check `genDelay` vs poll interval; they should be close
