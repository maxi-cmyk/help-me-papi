# Information Theory and Entropy

## Concept Definition
Borrowed directly from information systems theory, Shannon Entropy measures predictability. The core formula involves quantifying the proportion of different states across a dataset: $H = -(p \times \log_2(p) + q \times \log_2(q))$.

## The Problem vs. The Solution
### The Problem: Quantifying Visual Chaos
In hardware simulation algorithms (like Conway's Game of Life matrices running on infinite loops), visual states can easily lock dynamically into boring static oscillators or die completely to pure black pixels. Having the CPU visually "look" at the grid to determine if the simulation is still beautifully chaotic and complex is mathematically very difficult. 

### The Solution: Shannon Binary Entropy
By applying the Shannon Binary Entropy formula to the global population map output, the system instantly generates an exact floating point number quantifying the "chaos" of the system.
- Score of `0.0`: The matrix is completely dead or completely maxed (pure white).
- Score of `1.0`: Perfect, unpredictable visual chaos (50% on, 50% off).
This allows the hardware to automatically reboot the simulation simulation natively without human intervention if the chaos drops too low.

## Example Code (Pseudo-code)

```c
#include <math.h>

float calculate_shannon_entropy(int active_pixels, int total_pixels) {
    // 1. Math bounds check
    if (active_pixels == 0 || active_pixels == total_pixels) {
        return 0.0f; // Perfect predictability
    }
    
    // 2. Quantify population probabilities
    float p = (float)active_pixels / total_pixels; 
    float q = 1.0f - p;
    
    // 3. Information Theory Execution
    float entropy = -(p * log2f(p) + q * log2f(q));
    
    return entropy; // Will return bounded 0.0 -> 1.0
}
```

## Complexity Analysis

**Time Complexity:**
- **Entropy Calculation:** $O(1)$. Given a raw pixel count, computing the complexity requires only a few rapid mathematical constants across the FPU (Floating Point Unit).
- **Pixel Counting:** $O(N)$. Tallying the actual `active_pixels` before the calculation requires passing over the total grid constraints.

**Space Complexity:**
- **Execution Overhead:** $O(1)$. No arrays or grid buffers are generated, the quantification rests entirely on single-variable float allocation.
