# Controlled Angular Sweep — Measurement Protocol

**Status:** Planned protocol; **not yet completed as a validated measurement**. The existing polar plot is a software test.

## Objective

Measure the six-element Yagi's **relative directional received-power response** with a known, stable RF reference and fixed PlutoSDR receiver settings. Do not infer absolute antenna gain or measured beamwidth from the current uncontrolled captures.

## Apparatus

- Constructed six-element Yagi antenna (original design reference: **440 MHz**).
- ADALM-Pluto SDR with fixed manual receiver gain, known IQ sample rate, RF bandwidth and local oscillator.
- Known stable, appropriately authorized transmitter or signal generator, matched to the selected legal operating frequency and receiver bandwidth.
- Fixed transmitter antenna, measuring tape, angle reference/rotation fixture, cables and computer running `src/yagi_sdr_characterization.py`.

## Preparation

1. Record the test date, location/environment, transmitter configuration, frequency, antenna heights, separation, polarization, cable/adapter details, and measured Yagi orientation convention.
2. Confirm that the Yagi-connected PlutoSDR can receive a **distinct, identifiable signal**, separated from the SDR's LO/DC artifact and within the usable receiver passband.
3. Use a selected integration band that captures the intended signal without crossing the receiver DC spike or poorly behaved filter edges.
4. Keep transmitter power and position, receiver gain, sampling rate, antenna polarization and geometry fixed throughout the sweep.
5. Prefer an unobstructed, controlled test area; document nearby reflecting objects and limitations. A far-field setup is preferable where practical, but do not assert a far-field condition without evaluating it.

## Signal-on / signal-off reference

1. Capture multiple IQ buffers with the reference source **off**, with receiver settings unchanged, to estimate baseline band power.
2. Capture multiple IQ buffers with the reference source **on** and verify that power rises in the intended band.
3. Perform background subtraction in **linear power units**, then convert positive estimates to decibels. Negative or near-zero differences indicate inconclusive signal detection, not negative physical signal power.
4. The current code's median within-band PSD is only an exploratory background proxy. It **must not** be treated as an independent signal-off measurement.

## Angular measurements

1. Establish 0° and mark the antenna's forward-boresight direction clearly.
2. Rotate the **receiving** Yagi at 0°, 30°, 60°, ... 330°, preserving height and the rotation pivot; do not treat 360° as an additional independent measurement.
3. For each angle, acquire multiple settled IQ buffers, measure the same signal band, and record a mean/median plus variability; avoid touching cables while acquiring.
4. Repeat sweeps in both rotational directions if feasible to assess drift and reproducibility. A 30° step is coarse relative to the supplied design's predicted beamwidth, so refine angles around the main lobe and nulls before estimating beamwidth.
5. Export per-angle data and full settings to a CSV or equivalent. The current script does not yet export that CSV.

## Interpretation and reporting

- Normalize measured signal power to the maximum **only after** validating the source-on/off signal.
- Use an explicitly labeled relative-dB polar axis with a consistent radial range, rather than mapping the minimum small fluctuation to radius zero.
- Report peak orientation, observed front/back differences, beamwidth or uncertainty **only when the data support them**.
- Compare measured findings against the supplied design's predictions (8.917 dBd estimated gain, 47.4° predicted horizontal beamwidth) without presenting those predictions as experimentally obtained values.
- Include repeatability, room multipath, position uncertainty, polarization, drift, receiver saturation, leakage and noise-floor limitations.

## Related files

- [Antenna design](../hardware/antenna-design.md)
- [DSP software](../src/yagi_sdr_characterization.py)
- [Results status](../results/README.md)
