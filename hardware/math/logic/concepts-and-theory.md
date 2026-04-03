# Theoretical Logic & Hardware Math Concepts

This document explores the fundamental "why" behind the mathematics deployed on embedded hardware limits. It serves as a study guide rather than raw execution code.

## 1. Fast Fourier Transforms & Spectral Bleeds
The FFT (Fast Fourier Transform) takes raw time-domain signals (like microphone voltage over Time) and converts it to the frequency domain (Amplitude over Hz). 
- **The Problem with Raw FFTs:** If an audio wave doesn't perfectly complete a full wave cycle when you capture your sample array, the algorithm "clips" the edges together. This creates massive mathematical noise in the result known as *Spectral Leakage*, where frequencies bleed heavily into adjacent bins.
- **The Hann Window Solution:** By applying a "Hann Window" equation natively over your initial array *before* you run the FFT, you mathematically taper the edges of the sample to absolute zero. This forces an artificial perfect wave cycle, eradicating spectral bleed entirely.

## 2. Complementary Filters vs Kalman Filters
Sensors like the MPU6050 suffer from two distinct physics constraints:
- **Accelerometers:** Very accurate over *long* timeframes, but suffer from extreme high-frequency jitter in the short term.
- **Gyroscopes:** Incredibly stable and fast in the *short* time frame, but suffer from mathematical drift over the long term.

A **Kalman Filter** relies on continuous, heavy matrix math arrays to theoretically guess the exact sensor limits constantly—this completely locks up microcontrollers like the Arduino Nano due to memory processing bloat.
A **Complementary Filter** relies on one cheap single-line formula. It places a *low-pass filter* on the accelerometer (ignoring the jitter) and a *high-pass filter* on the gyroscope (ignoring the drift), combining them instantly at a roughly `0.96 \ 0.04` ratio for 95% perfect accuracy at 1% the CPU cost.

## 3. Cellular Automata & O(1) Operations
Handling massive 2D grids (like Conway's Game of Life on an LED Matrix) using nested arrays (e.g. `grid[x][y]`) is brutally intensive if you must iterate via nested `for loops` continually.
- **Bitmask Rows:** If you use a `uint8_t` (8-bit integer) to represent an entire row of LEDs, manipulating the visual state of the cell simply shifts bits left or right `(row >> 1)`.
- **Toroidal Wrapping via Logic Shifts:** A grid is "Toroidal" if moving off the right edge loops you instantly to the left edge (like Pac-Man). Checking this in logic requires multiple `if/else` boundaries checking if `x > width`. However, by using binary rotate shifts `(row << 1) | (row >> 31)`, you physically shift the bit sequence and wrap it to the opposite edge instantly in `O(1)` CPU speed.

## 4. PID Controller Saturation (Anti-Windup)
PID stands for Proportional, Integral, and Derivative control loops. The **`I` (Integral)** sums up historical error over time to force the motor/actuator to adjust to long-term drift.
- **The Saturation Danger:** If an actuator gets physically blocked (e.g. a motor is stuck), the Integral math keeps summing mathematically to infinity trying to force it to move. When the blockage is removed, the mathematical sum is so massive the actuator spins entirely out of control attempting to "wind-down". 
- **The Constraint:** Always mathematically clamp the Integral bounds tightly to prevent absolute wind-up. 

## 5. Shannon Binary Entropy
Borrowed directly from information systems theory: `-(p * log2(p) + q * log2(q))`
This logic is used to quantify exactly how chaotic or complex a system loop is. In hardware, if you run a cellular simulation infinitely, applying this formula to the population map instantly tells you if the visualization has died to equilibrium (static pixels), locked into a boring binary oscillator loop, or reached beautiful, chaotic complexity boundaries.
