# Yagi antenna characterization — consolidated statistical analysis

**Date:** 25 November 2026  
**Status:** Preliminary, indoor, uncalibrated received-power measurements. Not a calibrated free-space antenna pattern.

## 1. Purpose and system

Evaluate repeatability of received RF power as a six-element tape-measure Yagi is manually rotated through 30-degree increments, with a fixed Arduino UNO R4 WiFi + CC1101 transmitter and an ADALM-Pluto SDR receiver.

**Known acquisition settings:** CC1101 commanded 434.0 MHz; received peak around 433.921 MHz (uncalibrated frequency estimates); PlutoSDR center 434.2 MHz; sampling rate approximately 3 MSPS; receiver bandwidth 2 MHz; gain 20 dB manual; IQ buffer 16,384; Welch PSD with 2,048-sample segments; integrated band 433.87–433.97 MHz. Signal integration uses linear PSD with a frequency-bin-width multiplier, then 10 log10(power); values are arbitrary sample-power dB, **not dBm**. Initial antenna design was near 440 MHz.

**Geometry:** 0° defined as Yagi forward direction pointing at the CC1101; rotation center marked on the floor; handheld/manual positioning, indoor furniture and a Christmas tree may affect propagation. Tx reference power, true antenna orientation/height, cable routing, and local reflections are not independently calibrated.

## 2. Dataset inventory

- Five reported physical sweeps: Sweep 1 has 11 measurements (0° to 300°; 330° omitted); Sweeps 2–5 have 12 measurements (0° to 330°). **59 angle–power pairs total**.
- Additional 0°–150° half-sweeps and fixed-orientation checks collected separately; **not included** in the five-sweep mean or between-sweep standard deviation.
- Reference transmitter ON/OFF, spectral and IQ captures, FFT/PSD images and antenna construction photographs exist separately. Some stationary tests were performed with the Yagi pointing upward on a chair, not in the same floor-referenced geometry.

## 3. Processing and methodology

Let measured logarithmic integrated band power be P(i, θ) for sweep i. Define the per-sweep **0-degree-referenced** level as R(i, θ) = P(i, θ) − P(i, 0) in dB. This removes each run's constant power offset, but does **not** correct changing multipath or receiver/transmitter instability within a sweep. Normalization is to **0°**, not each sweep's maximum.

For each angle: n = number of available runs, sample mean of R, sample standard deviation of R (ddof=1), and median of R. Missing 330° in Sweep 1 remains missing, not estimated. Standard deviation here describes **between-run dispersion**, not instrument accuracy or a formal confidence interval. Arithmetic means of dB values are means of logarithmic ratios; they do not equal the logarithm of the arithmetic mean of linear received powers.

See `yagi_five_sweeps_raw.csv`, `yagi_five_sweeps_relative_to_0deg.csv`, `yagi_sweep_summary.csv`, and `yagi_angle_statistics.csv`.

## 4. Full-sweep summary

| Sweep | Valid angles | 0° level (arbitrary dB) | Maximum angle | Minimum angle | Max-to-min span (dB) | P(0°) − P(180°) (dB) | 0°–150° span (dB) |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | 11 | 18.35 | 300° | 210° | 12.77 | +1.82 | 0.067 |
| 2 | 12 | 17.90 | 180° | 270° | 12.06 | −0.71 | 0.028 |
| 3 | 12 | 17.42 | 330° | 180° | 4.78 | +2.91 | 0.015 |
| 4 | 12 | 20.82 | 30° | 270° | 14.36 | +13.18 | 0.023 |
| 5 | 12 | 12.19 | 330° | 240° | 5.44 | +0.87 | 0.068 |

The mean of the five within-sweep max–min spans is **9.88 dB**, but this is descriptive only; it is **not** measured antenna gain, a stable beamwidth, or an estimate of directivity.

The 0° absolute sample-power level spans **8.63 dB** across runs, reinforcing the need for per-run normalization and controlled geometry. Large between-run changes remain after normalization in the rearward angles.

## 5. Angle-by-angle repeatability

| Angle | n | Mean relative to 0° (dB) | Between-sweep SD (dB) | Median relative to 0° (dB) |
|---|---:|---:|---:|---:|
| 0° | 5 | 0.00 | 0.00 | 0.00 |
| 30° | 5 | +0.00 | 0.01 | +0.01 |
| 60° | 5 | +0.02 | 0.03 | +0.02 |
| 90° | 5 | +0.01 | 0.04 | +0.00 |
| 120° | 5 | −0.00 | 0.04 | −0.01 |
| 150° | 5 | −0.01 | 0.04 | −0.00 |
| 180° | 5 | −3.61 | 5.51 | −1.82 |
| 210° | 5 | −5.21 | 5.08 | −3.79 |
| 240° | 5 | −5.73 | 4.61 | −5.33 |
| 270° | 5 | −4.94 | 7.31 | +0.08 |
| 300° | 5 | −1.66 | 4.36 | +0.25 |
| 330° | 4 | −1.80 | 4.95 | −1.17 |

The 0° zero standard deviation is **by construction**, not evidence that the instrument has zero noise. The five-run first-half (0°–150°) **within-run spans** range from 0.015 to 0.068 dB (mean 0.040 dB). The near-flat first half is remarkably consistent, but this could be caused by experimental geometry, common-mode coupling/cable pickup, delayed buffers, or other systematic effects as well as true antenna behavior. It should not be assumed to establish a 150° beamwidth or radiation lobe.

The most inconsistent direction is 270° (between-sweep SD **7.31 dB**). Specifically, power relative to each sweep's 0° reading at 270° was **+0.08, −11.35, +0.81, −14.35, +0.14 dB**. This is not a repeatable 270° null.

The apparent forward–rear difference P(0°) − P(180°) varied **from −0.71 to +13.18 dB**; mean **+3.61 dB** and sample SD **5.51 dB**. These are *indoor received-power contrasts* and **not** a validated free-space front-to-back ratio.

## 6. Plots

- `yagi_five_sweeps_overlay.png`: five sweeps aligned to their own 0° levels, plotted against measured physical angle.
- `yagi_mean_sd_by_angle.png`: mean relative level with ±1 sample standard deviation across sweeps; 330° uses four observations.

**Plotting caution:** The original polar visualization subtracted each run's minimum from its relative dB data to make radii nonnegative; it can make tiny variations appear dramatic. Use the angle-versus-relative-power overlay for numerical interpretation, and clearly document any radial transform in a polar figure.

## 7. Interpretation and limitations

**Supported observations**

1. The RF reference carrier is detected near 433.921 MHz when commanded to 434.0 MHz; this is an observed receiver frequency and not an independent calibration of CC1101 transmit frequency.
2. A substantial run-to-run stable segment appears between 0° and 150° in the sequential captures; the angle-labeled measurements from physical sweeps do not prove this is a physical antenna pattern without stronger controls.
3. Variations are substantially larger at 180°–330°, with minima changing location between sweeps.
4. Indoor reflections and slight adjustments to the hand-held antenna, its height, position, polarization and cable routing are plausible influences. No causal attribution to the Christmas tree is proven.
5. Several post-sweep five-capture tests show significant drift even when the antenna was reportedly held in a fixed position, and some were taken with different orientations. The RF setup does not yet support a calibrated free-space gain or front-to-back claim.

**Important controls to improve confidence**

- Repeat an interleaved physical **0° → 180° → 0° → 270° → 0°** experiment with several captures averaged per position and a consistent rotation axis.
- Use a nonmetallic mount at fixed height and keep nearby bodies and coax placement consistent. If possible use a more open site and greater separation.
- Compare raw peak power at the known carrier with integrated band power; test whether received signal changes when the Yagi feed is intentionally disconnected (with appropriate receiver protection), and check for unintended pickup through coax/chassis. Keep fixed gain.
- Log run ID, timestamps, antenna orientation, environment, cable routing, transmitter state and brief valid RF transmission windows. Preserve raw IQ from representative captures if storage permits.
- Consider a dedicated transmitter ON/OFF control captured without moving the antenna. Do not mistake a within-band PSD median for a transmitter-OFF reference.

## 8. Project assessment

**Overall portfolio strength: 8.8/10 (subjective, relative to a first-year EE portfolio).** Strengths: physical antenna fabrication, RF instrumentation integration, embedded firmware, Python SDR acquisition, FFT/Welch PSD analysis, quantitative multi-run experiments and frank documentation of uncertainty. Limits: no independently calibrated antenna gain, no validated free-space directional pattern, no robust setup alignment or measured feed-point matching at this test frequency, and a transmitter sketch that should default RF off and require properly authorized/identified operation. The Arduino UNO R4 WiFi is 5-V logic whereas the CC1101 uses 3.3-V logic; verify level shifting and electrical safety rather than relying on successful operation alone.

**Defensible resume statement:** *Built a six-element Yagi antenna test system using ADALM-Pluto SDR and an Arduino/CC1101 RF reference transmitter; implemented FFT/Welch PSD-based received-power extraction and collected five indoor angular sweeps (59 orientation measurements) to evaluate directional response and between-run repeatability.*

**Next milestone:** improve repeatability/fixture and measure antenna matching (e.g., VNA S11/VSWR at the frequency of interest), then document the validated results.
