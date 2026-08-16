---
name: embedded-cpp
description: Mastery skill triggered exclusively for embedded electronics, signal processing, hardware interactions, and firmware structuring in C++.
---

# Embedded Hardware Architecture 

This mastery skill encapsulates structural interactions when handling physical hardware configurations scaling across microcontrollers (e.g. Arduino / ESP32 interfaces). DO NOT deploy this documentation when managing pure web servers or general JS development.

**Rule One:** Ensure physical execution constraints are strictly honoured. Memory, floating pins, voltage bounds, and CPU blocking limits are primary considerations before any loop logic is structured.

**Rule Two:** Always explain a new physical component proposed to a user with an analogy mapped directly to logic they firmly possess (e.g., comparing an I2C multiplexer directly to a router switcher). 

---

## Navigating the Hardware Domains

For complex embedded systems, manually attach the following context files to your prompt to prevent hallucinatory or non-optimized code:

### 1. [Firmware Architecture](../architecture/skills/firmware-patterns.md)
**When to attach**: When structuring your `main.cpp` vs `web.cpp` logic partitions, preventing linker errors from double-includes, or implementing Flag Handshake protocols for multi-core ESP32 tasks.

### 2. [Performance and Optimization](../performance/skills/optimisation.md)
**When to attach**: For all display rendering, interrupt handling (`IRAM_ATTR`), or when timing is critical. Use this to ensure the AI swaps `delay()` for non-blocking timer loops.

### 3. [Math and Signal Processing](../math/skills/signal-processing.md)
**When to attach**: When implementing FFT calculations (e.g., `esp_dsp`), Hann windows, IMU filtering, or bitwise logic for high-speed LED arrays.

### 4. [Inventory and Components](../components/inventory.md)
**When to attach**: Always. This ensures the AI only recommends components, pins, and libraries that you actually have in your physical inventory.

---

## NFC / Physical-Digital Bridge (Portfolio Card Case Study)

When a project connects a physical object (NFC card, badge, tag) to a digital experience:

### Architecture
```
NFC Card (NTAG213/215/216)
    ↓ tap
Smartphone NFC reader → opens URL stored on the tag
    ↓
Web app (Vercel) → loads the user's portfolio / profile / digital business card
```

### NFC Tag Basics
- **NTAG213** (144 bytes), **NTAG215** (504 bytes), **NTAG216** (888 bytes). For URLs, 213 is usually enough (a short URL + query param).
- The tag stores a **URI record** (e.g., `https://yoursite.com/user/max`). No battery needed — the phone's RF field powers the tag.
- **NDEF message format**: Use a single URI record + a text record (optional). Keep the payload small — the tag has limited memory.

### Design Pattern: One Tag, Many Destinations
If you want one NFC card to serve different users or different content over time:
- The tag holds a **fixed URL** (your domain).
- The URL includes a **query param or hash** (`?user=max` or `#max`).
- The web app reads the param and renders the right profile. You can change the content server-side without reprogramming the card.
- This is how the NFC portfolio card works: one card per person, content managed in the web app.

### Implementation Tips
- **Program the tags once** with a fixed URL. Use an NFC app (NFC Tools on iOS/Android) or a USB NFC reader + Python (`nfcpy` library).
- **Test on both iOS and Android.** iOS supports background NFC reading (Core NFC); Android uses the NFC stack. Some older Android phones have weak NFC range — design the card placement accordingly.
- **The web site must work on mobile first** — the user is holding a phone, not a laptop.
- **Graceful fallback**: if the site is opened without NFC (e.g., someone shares the link), it should still work. The NFC is just the entry point.

### Coherence: Physical Object ↔ Digital Experience
The best NFC-linked experiences maintain a **consistent identity** between the physical object and the digital destination:
- If the card is matte black with gold foil, the website should echo that palette.
- If the site is terminal-styled (see `frontend/skills/layout-and-interaction.md`), the card's visual design should hint at that aesthetic.
- This coherence is what makes the interaction feel *intentional*, not gimmicky.

### Security Considerations
- Anyone with an NFC reader can read the tag's UID and URL. **Don't put secrets on the tag** — just a public URL.
- The tag is read-only in practice (you can lock NTAGs to prevent rewriting, but that's usually unnecessary for a business card).
- The web app handles its own auth if needed. The tag is just the key to the front door.

---

## Execution Setup Check

When producing embedded code:
1. Is an ISR defined? If yes, confirm `IRAM_ATTR` and minimal logic hooks.
2. Are delays configured? Swap `delay()` globally for non-blocking timer loops or FreeRTOS `vTaskDelays`.
3. Does the system demand concurrent web telemetry arrays natively hosted on the ESP? Confirm softAP definitions using the `192.168.4.1` standard constraints mapped inside the architecture module.
