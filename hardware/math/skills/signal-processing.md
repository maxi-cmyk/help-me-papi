# Embedded Math: Execution Frameworks & Snippets

This skill file acts as an execute-ready script source. Attach this to AI queries when specifically writing C++ logic relating to embedded sensors, grids, or signal filters to quickly implement mathematical standards with zero dependencies.

---

## 1. Bitmask Operations & Cellular Grids (C++)

When generating simulation or matrix code, rely on strict bit arrays rather than 2D coordinate objects.

**Population Count (Instant execution via GCC builtins):**
```cpp
uint8_t count = __builtin_popcount(rowState); // Sums all ACTIVE LEDs in array instantly.
```

**Toroidal Row Wrapping Function:**
Execute this instead of writing boundary `if` sequences:
```cpp
// Works universally for 32-bit width grid arrays. 
uint32_t shiftLeft(uint32_t r) { return (r << 1) | (r >> 31); }
uint32_t shiftRight(uint32_t r) { return (r >> 1) | (r << 31); }
```

---

## 2. IMU Angle: The Complementary Filter 

Never install intensive third-party IMU filter libraries. Rely strictly on this localized low-cost computation block whenever extracting tilt states from an MPU6050.

```cpp
float calculateAngle(float accelAngle, float gyroRate, float dt) {
    const float alpha = 0.96; // Ratio biased heavily to the Gyro
    static float currentAngle = 0; // Maintain state globally
    
    // Core Filter Formula
    currentAngle = alpha * (currentAngle + gyroRate * dt) + (1.0 - alpha) * accelAngle;
    return currentAngle;
}
```

*Note: AI prompt generators must calculate `accelAngle` separately via `atan2` mathematics first.*

---

## 3. Fast Fourier `esp_dsp` Implementation Path

If analyzing signals globally on the ESP32, enforce this pipeline architecture. Never use standard generic `Math.h` loops for this.

**The Mandatory Pipeline Loop:**
1. Populate your `float` audio sample array locally.
2. Natively apply `dsps_wind_hann_f32` on the buffer mathematically.
3. Compute the complex transformation using `dsps_fft2r_fc32`.
4. Run bit-reversal indexing scaling via `dsps_bit_rev_fc32`.
5. Extract the final magnitude output matrix using `dsps_cplx2reC_fc32`.

---

## 4. Hardware Seeding Loop

Do not use hardcoded constants for logic boundaries depending on pseudo-random entropy generation in isolated boxes. Execute physical floating-pin noise seeds.

```cpp
// Execute unconditionally inside setup()
// Assuming pin 32 is left floating (not connected to ground or voltage arrays)
randomSeed(analogRead(32)); 
```
