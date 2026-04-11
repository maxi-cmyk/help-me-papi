# Hardware Optimisation Rules

Microcontrollers have extremely constrained processing limits. Adhere to these exact rules to prevent stuttering, thermal throttling, and missed signals.

## Communication Protocols
- **Hardware over Software SPI:** Always connect devices (MAX7219, TFTs) to default hardware SCK/MOSI pins. Bit-banging software SPI burns CPU cycles heavily.

## Input / Output Rendering
- **The Frame Buffer:** Never write to an LED matrix directly pixel-by-pixel if performance drops. Calculate an entire `buffer` in RAM, then push via single SPI transaction.
- **Double Buffering:** For animations showing tearing or flicker, write into a hidden array (`bufferB`), then swap pointer addresses instantly with `bufferA`.
- **Interrupt Flag Toggling:** Never hook long logic sequences onto physical button pushes or tilt switches. The ISR should simply set a boolean `buttonPressed = true` and return immediately. Let `loop()` handle the heavy logic.
- **Debounce:** All mechanical inputs bounce. Use hardware `INPUT_PULLUP` alongside a 10-20ms software debounce lock.

## ESP32 Specific Boosts
- **IRAM_ATTR**: Place the `IRAM_ATTR` tag on every interrupt handler function. It forces the function into RAM rather than Flash memory, preventing fatal cache-miss panics.
- **vTaskDelay vs delay**: If writing FreeRTOS tasks, never use standard `delay()`. It blocks the CPU. Use `vTaskDelay` to correctly yield the core thread.
- **Avoid Arduino String**: The `String` object heavily fragments heap memory. In time-critical endpoints or matrix grids, use `char[]` arrays alongside `sprintf` to format data.
