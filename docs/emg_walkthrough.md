# EMG Walkthrough

1. Place two active electrodes along the target muscle and one reference electrode.
2. Wire electrodes to INA inputs and reference to bias node.
3. Verify INA output baseline is mid-supply.
4. Inject test signal (finger taps / light muscle contractions) and check scope.
5. Confirm HPF/LPF cutoff frequencies by sweeping a test tone (optional).
6. Connect to MCU ADC and stream CSV.
7. Analyze in `analysis/python/emg_quicklook.py`.

[Image placeholder: Photo of breadboard with INA, RC filters, and MCU]
[Image placeholder: Oscilloscope screenshot showing EMG burst]
