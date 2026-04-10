# Sensor Fusion and Filtering

## Concept Definition
Sensor fusion involves taking inputs from multiple discrete sensors and combining them to mitigate physics constraints and generate a unified, highly accurate calculation of physical state.

## The Problem vs. The Solution
### The Problem: Divergent Physics Flaws
Standard IMUs (like the MPU6050) utilize two tools with completely opposite drawbacks:
- **Accelerometers:** Accurate over *long* timeframes, but suffer from extreme high-frequency noise and jitter in the short term.
- **Gyroscopes:** Incredibly stable and fast in the *short* time frame, but suffer from mathematical drift calculation over the long term.

### The Solution: Kalman vs. Complementary Filters
A **Kalman Filter** relies on continuous, heavy matrix math arrays to statistically predict and guess the exact sensor limits constantly. This completely locks up lightweight microcontrollers (like Arduino Nanos) due to memory and processing bloat.
A **Complementary Filter** relies on a cheap, single-line formula. It places a *low-pass filter* on the accelerometer (ignoring jitter) and a *high-pass filter* on the gyroscope (ignoring drift), bridging them near a 0.98/0.02 ratio.

## Example Code (Pseudo-code)

```c
float current_angle = 0.0f;
float dt = 0.01f; // Time delta (e.g., 100Hz loop)

// The Complementary Filter Execution
void update_state(float gyro_rate_dps, float accel_angle_deg) {
    // 1. High-pass the Gyro (Trust it for the immediate short term change)
    float gyro_estimate = current_angle + (gyro_rate_dps * dt);
    
    // 2. Low-pass the Accelerometer (Trust it to pull the system to true gravity over time)
    float accel_estimate = accel_angle_deg;
    
    // 3. Fuse: 98% Gyro calculation, 2% Accelerometer anchor
    current_angle = (0.98f * gyro_estimate) + (0.02f * accel_estimate);
}
```

## Complexity Analysis

**Time Complexity:** 
- **Complementary Filter:** $O(1)$. Floating point math happens instantly as a single algebraic operation per frame loop.
- **Kalman Filter (Contrast):** $O(N^3)$. Solving covariance matrices requires brutal linear algebra steps every cycle, devastating low-clock hardware.

**Space Complexity:** 
- **Complementary Filter:** $O(1)$. It simply overwrites a few floating point values in memory without array allocation.
