# Components

> Good to know how they work, for info on how to build with them, ask max.

## Anticipated Components
> Components the user has NOT yet used but will likely encounter based on their project trajectory.
> Claude update instruction: when user confirms acquisition or use, move to `inventory.md`'s Confirmed Used table and remove from here.
> When suggesting any of these for the first time, always explain: what it is, how it works, and give an analogy to a component already in the Confirmed Used table.

| Component | Analogy To | Why Likely Needed |
|---|---|---|
| **Motor driver (L298N / DRV8833)** | Like the discrete LEDs  you switch it with GPIO  but it handles the high current a motor needs so the ESP32 isn't fried | Balancing robot, rover, any actuated build |
| **DC gear motor / stepper motor** | Like the joystick in reverse  mechanical movement, but output rather than input | Any physically moving project |
| **OLED display (SSD1306 12864)** | Like the MAX7219 matrix but pixel-precise and I2C-driven; higher-resolution grayscale version of the matrix | Oscilloscope UI, cleaner data readouts |
| **TFT colour display (ILI9341)** | Like the OLED but full colour and SPI-driven  same protocol as MAX7219 | Rich visualisations, game displays |
| **HC-SR04 ultrasonic sensor** | Like the PIR but instead of "motion yes/no" it gives exact distance in cm via a timed pulse | Theremin synth, obstacle avoidance |
| **IR distance sensor (Sharp GP2Y)** | Like HC-SR04 but analog output, no timing  like reading a joystick axis | Faster distance sensing, Theremin |
| **GPS module (NEO-6M)** | Like the PIR (passive input) but streams UART coordinate strings instead of a trigger pin | Navigation, dead-reckoning |
| **LiPo battery + TP4056 charger** | Like USB power but flat, embeddable, rechargeable  TP4056 is just a charge controller IC | Portable / wireless builds |
| **ESP-NOW (ESP32 built-in)** | Like Blynk WiFi but peer-to-peer between two ESP32s with no internet needed | Wireless sensor mesh, multi-device builds |
| **Rotary encoder** | Like the joystick's rotation axis but gives precise stepped counts  no drift, no analog noise | Menu navigation, precise input |
| **DMA-driven SPI / I2S** | Like the hardware timer ISR but with zero CPU involvement  hardware moves data itself | High-throughput audio or display streaming |
