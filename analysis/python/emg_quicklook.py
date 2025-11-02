#!/usr/bin/env python3
import csv
import numpy as np
import matplotlib.pyplot as plt

# Load CSV
ts = []
vals = []
with open('../data/sample_emg.csv') as f:
    r = csv.DictReader(f)
    for row in r:
        ts.append(float(row['timestamp_us']))
        vals.append(float(row['value_raw']))

ts = np.array(ts) * 1e-6  # to seconds
vals = np.array(vals)

# Detrend (midscale remove)
vals = vals - np.median(vals)

# Simple digital notch @ 60 Hz (biquad) - optional, not tuned here
fs = 1000.0
f0 = 60.0
w0 = 2*np.pi*f0/fs
bw = 3.0  # Hz
alpha = np.sin(w0)*np.sinh(np.log(2)/2*bw*w0/np.sin(w0)) if np.sin(w0)!=0 else 0.01

b0 = 1
b1 = -2*np.cos(w0)
b2 = 1
a0 = 1 + alpha
a1 = -2*np.cos(w0)
a2 = 1 - alpha

y = np.zeros_like(vals)
x1 = x2 = y1 = y2 = 0.0
for i, x0 in enumerate(vals):
    y0 = (b0/a0)*x0 + (b1/a0)*x1 + (b2/a0)*x2 - (a1/a0)*y1 - (a2/a0)*y2
    y[i] = y0
    x2, x1 = x1, x0
    y2, y1 = y1, y0

plt.figure()
plt.plot(ts, y)
plt.xlabel('Time (s)')
plt.ylabel('EMG (a.u.)')
plt.title('EMG Quicklook (Notch 60 Hz)')
plt.show()
