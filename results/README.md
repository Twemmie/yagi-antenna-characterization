# Measured results

This directory holds the **five physical indoor Yagi sweep datasets**, their CSV statistics and original experimental screenshots. Values are uncalibrated logarithmic received **sample power**, **not dBm/dBi**.

## Consolidated figures

![Five physical sweeps referenced to their own 0° reading](plots/yagi_five_sweeps_overlay.png)

![Angle-by-angle mean and between-sweep standard deviation](plots/yagi_mean_sd_by_angle.png)

## Machine-readable results

- [Raw values for all five sweeps](data/yagi_five_sweeps_raw.csv) — **59 measured orientation records**; Sweep 1 lacks 330°.
- [Each sweep referenced to its 0° value](data/yagi_five_sweeps_relative_to_0deg.csv).
- [Per-angle mean, median, count, SD and range](data/yagi_angle_statistics.csv).
- [Per-sweep summary](data/yagi_sweep_summary.csv).
- [Consolidated interpretation and limitations](../analysis/Yagi_Consolidated_Statistical_Analysis.md).

## Original figure inventory

| Figure set | Files |
|---|---|
| Sweep 1 polar chart | [image(20261125-211135).png](plots/image(20261125-211135).png) |
| Sweep 2 polar chart | [image(20261125-212558).png](plots/image(20261125-212558).png) |
| Reference transmitter FFT/PSD | [image(20261125-214907).png](plots/image(20261125-214907).png), [image(20261125-214909).png](plots/image(20261125-214909).png) |
| Sweep 4 polar, FFT, PSD | [215417](plots/image(20261125-215417).png), [215426](plots/image(20261125-215426).png), [215430](plots/image(20261125-215430).png) |
| Sweep 5 polar, FFT, PSD | [215802](plots/image(20261125-215802).png), [215805](plots/image(20261125-215805).png), [215837](plots/image(20261125-215837).png) |
| First-versus-second comparison | [yagi_first_vs_second_sweep.png](plots/yagi_first_vs_second_sweep.png) |

Not every run has an individually archived PSD/FFT or polar screenshot. The polar radius transformation can greatly amplify small relative-dB differences visually; use the numerical CSV and comparison charts for inference.
