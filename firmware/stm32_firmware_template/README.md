# STM32 Firmware Template (ADC → UART)

This template samples one ADC channel (EMG front-end output) at ~1 kS/s
and streams comma-separated values over UART at 115200 baud.

## Files
- `main.c` — barebones polling demo
- `platform_config.md` — clock and pin notes
- `serial_protocol.md` — CSV lines: `timestamp_us,value_raw`

## Build
You can port this to mbed/STM32CubeMX easily. Pseudocode is included for portability.

> Tip: On a Blue Pill use PA0 (ADC1_IN0) and USART1 (PA9/PA10).
