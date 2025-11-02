# Bioelectronics Training (Template)

This repository is a **complete template** for a self‑guided path into **wearable biosensing & bioelectronics**.
It covers **EMG** first, with room to add **ECG** and **PPG** later. Use it to document projects, run firmware,
and analyze signals.

## Contents
- `hardware/` — Analog front-ends (schematics, BOM, notes)
- `firmware/` — Microcontroller code (STM32 template included; Nordic/Arduino easy to add)
- `analysis/` — Python tools to visualize, filter, and extract features
- `docs/` — Explanations, references, and images (use placeholders if you don't have images yet)

## Quick Start
1. **EMG first build**: `hardware/emg_frontend/README.md`
2. **Flash firmware**: `firmware/stm32_firmware_template/README.md`
3. **Stream or log CSV** from MCU ADC.
4. **Analyze/plot** using `analysis/python/emg_quicklook.py`

## Roadmap
- [x] EMG first build (INA + HPF + LPF)
- [ ] Add 60 Hz notch (analog) and digital notch in Python
- [ ] ECG front-end (RLD) and safety notes
- [ ] PPG optical board + motion artifact handling
- [ ] BLE streaming template (nRF52) and mobile app stub

## Safety
Only record **surface EMG** with battery‑powered devices. Do **not** connect your body to wall‑powered equipment
without proper isolation and supervision. This repo is for **learning**, not for clinical use.
