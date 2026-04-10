# Frequency Analysis and Signal Processing

## Concept Definition
Fast Fourier Transforms (FFT) take raw time-domain signals (like microphone voltage over time) and convert them into the frequency domain (Amplitude over Hz). 

## The Problem vs. The Solution
### The Problem: Spectral Leakage
If an audio wave doesn't perfectly complete a full wave cycle when you capture your sample array, the algorithm "clips" the edges together. This creates massive mathematical noise in the result known as *Spectral Leakage*, where frequencies bleed heavily into adjacent bins.

### The Solution: Windowing Functions
By applying a "Hann Window" equation natively over your initial array *before* you run the FFT, you mathematically taper the edges of the sample to absolute zero. This forces an artificial perfect wave cycle, generally eradicating spectral bleed entirely.

## Example Code (Pseudo-code)

```c
// Example: Applying a Hann Window to a signal buffer in-place
#define PI 3.14159265358979323846

void apply_hann_window(float* buffer, int length) {
    for (int i = 0; i < length; i++) {
        // Hann window formula: 0.5 * (1 - cos(2 * PI * i / (length - 1)))
        float multiplier = 0.5f * (1.0f - cos(2.0f * PI * i / (length - 1)));
        buffer[i] = buffer[i] * multiplier;
    }
}

// System execution flow
void process_audio_signal(float* raw_signal, int length) {
    // 1. Taper the edges to prevent bleed
    apply_hann_window(raw_signal, length);
    
    // 2. Safely run frequency analysis without leakage
    // run_fft(raw_signal, length);
}
```

## Complexity Analysis

**Time Complexity:** 
- **Hann Window:** $O(N)$ where $N$ is the length of the sample buffer.
- **FFT Algorithm:** $O(N \log N)$. Radix-2 FFT recursively splits the time-domain signal, making it significantly faster than the naive $O(N^2)$ Discrete Fourier Transform.

**Space Complexity:** 
- **In-place Operations:** $O(1)$ auxiliary space. Direct buffer manipulation prevents memory bloat, which is critical for embedded hardware with heavily constrained SRAM.
