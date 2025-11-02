# EMG Front-End Build Plan (Phase 1)

**Goal:** Build a surface EMG amplifier chain using INA + HPF + LPF to acquire muscle signals and digitize them on MCU ADC.

### Tasks
- Order components (INA, op-amp, resistors/caps, electrodes)
- Build INA + HPF + LPF stages on breadboard
- Power from battery for safety
- Test with oscilloscope or ADC capture
- Stream samples to Python
- Plot + extract simple muscle activation envelope

### Expected Output
Working EMG trace from forearm muscle (flexing fist), visible bursts, stored as CSV.

### BOM Reference
See: `hardware/common_blocks/BOM_emg_starter.csv`

### Notes
This is the first major project milestone in this repository.
This will be updated as progress is made.
