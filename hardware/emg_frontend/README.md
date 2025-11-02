# EMG Front-End (Starter Build)

**Goal:** Acquire surface EMG with an instrumentation amplifier, a 20–450 Hz band-pass, and digitize with an MCU ADC.

## Block Diagram (text)
[Image placeholder: A diagram showing `Body → Electrodes (2 + reference) → INA (G≈100) → High‑Pass (20 Hz) → Low‑Pass (450 Hz) → MCU ADC → Python`]

## Recommended Parts
- Instrumentation Amplifier: **AD8220** (or AD623 / INA128)
- Op‑amp for filters: TLV9002 / TLV2462 / LM358
- Electrodes: Ag/AgCl snap gel (3 pcs)
- Supply: Single 5 V (USB power bank) or 9 V battery (recommended for safety during prototyping)

## Suggested Values
- INA Gain: **G≈100** using RG ≈ 499 Ω (AD8220: G = 1 + 49.4k/RG)
- High‑Pass (20 Hz): choose C=0.1 µF → R≈80 kΩ (use 82 kΩ)
- Low‑Pass (450 Hz): choose C=1 nF → R≈360 kΩ

## Schematic (explained)
[Image placeholder: INA instrumentation amplifier with RG; AC‑coupled HPF; active LPF to 450 Hz; optional 60 Hz notch block.]

- **INA stage**: Gain 100, bias returns via large resistors to mid‑supply
- **HPF (20 Hz)**: Blocks DC offset and motion artifacts
- **LPF (450 Hz)**: Limits bandwidth and noise
- **Notch (60 Hz)**: Optional analog Twin‑T or do digital in Python

## BOM
See `hardware/common_blocks/BOM_emg_starter.csv`.

## Notes
- Use **battery power** during body-connected tests.
- Keep electrode leads short and twisted; avoid ground loops.
- Expect visible activation when you clench the target muscle.
