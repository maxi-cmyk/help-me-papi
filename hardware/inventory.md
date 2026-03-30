# User Profile & Inventory

## User Profile

### Platforms (confirmed used)
- **ESP32** — primary microcontroller
- **Arduino Uno R3** — secondary, used for simpler/standalone projects

### Components (confirmed used)
| Component | Protocol | Notes |
|---|---|---|
| MAX7219 4-in-1 LED matrix (32×8) | SPI | Main display; always use frame buffer approach |
| INMP441 microphone | I2S | 24-bit left-justified; L/R pin must never float |
| MPU-6050 IMU | I2C | Always calibrate offsets before use |
| PIR sensor | Digital GPIO | Motion detection |
| Joystick module | Analog + Digital | X/Y axes + button |
| RGB LED module | PWM / Digital | Colour mixing |
| Discrete LEDs | Digital / PWM | |
| Tilt switch (ball type) | Digital GPIO | INPUT_PULLUP + debounce always needed |
| LCD display | I2C / parallel | Text display |
| Push buttons | Digital GPIO | Always debounce |
| Decoupling capacitors | Power | 100nF ceramic + 10µF electrolytic per IC |
| Potentiometer | Analog GPIO | Used for runtime-tunable parameters (e.g. seed density); always `analogRead()` into a mapped range |

### Software / Libraries (confirmed used)
| Library / Service | Used For |
|---|---|
| Blynk | WiFi cloud dashboard |
| LightBlue | BLE data monitoring |
| Adafruit MPU6050 | IMU reads |
| ArduinoFFT | Spectral analysis (or manual FFT) |
| ESP32 Arduino core | Base framework |
| scikit-learn (Python) | Gesture classification |
| pyserial (Python) | Serial data streaming from ESP32 to laptop |
| ESP32 WiFi + WebServer (built-in) | WiFi AP mode + HTTP endpoints for live dashboards |
| Chart.js (browser, CDN) | Live-updating web charts polled from ESP32 JSON endpoints |
| LedControl | MAX7219 matrix driver (Arduino/ESP32) |

### Interests & Strengths
- Math-heavy logic: FFT, PID, Kalman, ML classification
- Real-time signal processing
- Interactive hardware with polished UX
- Bitmask manipulation, raw SPI, no-library approaches when performance demands it

---

## Completed Projects
> Claude update instruction: ask user to confirm completion before adding a row.

| Project | Key Components | Key Techniques |
|---|---|---|
| Room security system | ESP32-CAM, PIR, Blynk | WiFi cloud streaming, motion trigger |
| Asteroids arcade game | ESP32, joystick, MAX7219 | Bitmask rendering, sound, persistent scores, difficulty scaling |
| Music LED visualiser | Arduino Uno, LEDs, RGB module | Manual FFT (no libs), tempo following, frequency band splitting |
| LCD interactive display | ESP32, LCD, LED matrix, buttons | UI state machine |
| Push-up counter | ESP32, BLE | LightBlue phone sync |
| Conway's Game of Life + Web Dashboard | ESP32, MAX7219, potentiometer | Bitmask grid, toroidal wrap, bit-shift neighbour sum, Shannon entropy, WiFi AP mode, Chart.js live polling, multi-file PlatformIO, flag handshake pattern |
