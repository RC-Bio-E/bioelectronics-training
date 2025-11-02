# Serial Protocol

CSV line per sample:
```
timestamp_us,value_raw
```
- `timestamp_us`: monotonically increasing (from systick or timer)
- `value_raw`: ADC raw code (e.g., 0..4095 for 12-bit)
