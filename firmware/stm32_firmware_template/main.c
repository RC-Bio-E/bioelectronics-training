// Minimal STM32-like pseudocode for ADC @ ~1 kS/s and UART print.
// Adapt to your HAL (STM32Cube or libopencm3).

#include <stdint.h>
#include <stdio.h>

static volatile uint32_t micros = 0;

void SysTick_Handler(void) {
    // 1 kHz systick -> micros += 1000; (approximate)
    micros += 1000;
}

uint16_t adc_read(void) {
    // start conversion, wait EOC, return value
    // (placeholder - use your HAL)
    return 2048; // dummy midscale
}

void uart_write(const char* s) {
    // blocking UART transmit (placeholder)
}

int main(void) {
    // clock_init();
    // systick_init(1 kHz);
    // gpio_init();
    // uart_init(115200);
    // adc_init(single-ended, channel EMG_OUT);

    while (1) {
        uint16_t sample = adc_read();
        char line[64];
        // CSV: timestamp_us,value_raw
        snprintf(line, sizeof(line), "%lu,%u\r\n", (unsigned long)micros, sample);
        uart_write(line);
        // crude ~1 kS/s (adjust delay for your system)
        // delay 1 ms
    }
    return 0;
}
