# Platform Config

- **MCU**: STM32F103C8T6 (Blue Pill), but any Cortex-M is fine
- **ADC**: single-ended, referenced to mid-supply (e.g., 1.65 V if 3.3 V system)
- **Pin**: PA0 (ADC1_IN0) suggested
- **UART**: USART1 at 115200 (PA9 TX, PA10 RX)
- **Sample rate**: 1000 Hz target
