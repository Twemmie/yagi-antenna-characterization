# Indoor Yagi angular-sweep protocol and record

**Experiment performed:** November 25, 2026. **Status:** Preliminary, manual indoor measurements.

## Apparatus and settings

- Six-element tape-measure Yagi built from a supplied **440 MHz** antenna design.
- Fixed Arduino UNO R4 WiFi + CC1101 reference transmitter; **434.0 MHz programmed**, ~**433.921 MHz observed** on PlutoSDR.
- PlutoSDR at **434.2 MHz LO**, ~**3 MSPS**, **2 MHz** receiver bandwidth, manual **20 dB RX gain**.
- **16,384** complex IQ samples per acquisition; **2,048** samples per Welch segment; PSD integrated over **433.87–433.97 MHz**.
- A floor-marked reference circle with **0° defined toward the CC1101**; manually held Yagi centered above the circle and rotated in 30° steps.
- Indoor environment includes furniture, floor/walls, and a Christmas tree; the operator, coax, height and positioning were not perfectly controlled.

## Method used

1. Verify receiver connection, FFT peak in the intended CC1101 region, and repeatability of IQ/PSD processing.
2. Compare signal ON/OFF with unchanged settings and record fixed-orientation controls.
3. At each angle, physically rotate the receiving antenna, press Enter in the Python measurement loop and capture a fresh 16,384-sample IQ buffer.
4. Compute two-sided Welch PSD, integrate linear sample PSD in the target band and apply `10 log10` to obtain **uncalibrated logarithmic received sample power**.
5. Collect the available angle series: one 11-position sweep, four 12-position sweeps, plus two supplementary half-sweeps.
6. Normalize each sweep to its own **0°** reading and compute the cross-sweep mean, median and sample standard deviation.

## Results and limitations

- **59 measurements** across five full sweeps. Sweep 1's missing 330° remains missing.
- Within-run 0°–150° spans range **0.015–0.068 dB**.
- The 270° between-sweep sample SD is **7.31 dB**, and the minimum moves between 180°, 210°, 240° and 270° across sweeps.
- Data support *indoor relative received-power variations*, **not** independently calibrated gain, free-space beamwidth, stable nulls, S11, or front-to-back performance.
- Different FFT/PSD screenshots belong to separate acquisitions; do not treat a single initial FFT as a complete spectral record for every angular point.
- The within-band median PSD is **not** an independent TX-off noise floor; normalized dB means are descriptive, not an antenna calibration.
- Original polar plot shifts the radial minimum to zero and may exaggerate the visualization.

## Improved future controlled experiment

Mount the Yagi on a fixed-height nonmetallic turntable; fix polarization, cable route and the operator's position. Run a physically interleaved **0° → 180° → 0° → 270° → 0°** sequence, collect multiple settled buffers per orientation, independently verify transmitter-on/off power, log timestamps, and repeat at a more open location if practical. Measure feed-point S11/VSWR at the reference frequency with a VNA.

**Legal/electrical precautions:** 434 MHz test transmissions must be appropriately authorized and identified. Continuous unmodulated carrier alone does not identify a station. Verify 5-V UNO R4 vs 3.3-V CC1101 logic compatibility.
