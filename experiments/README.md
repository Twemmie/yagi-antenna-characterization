# Experiments

This folder documents repeatable physical measurements and distinguishes actual observations from software-only testing.

- [Controlled angular sweep — protocol](controlled-angular-sweep.md): setup, fixed receiver settings, sample acquisition, noise reference, and data reporting checklist.
- Physical Yagi build and VNA tuning context: [hardware documentation](../hardware/).
- Current software-test analyzer: [`src/yagi_sdr_characterization.py`](../src/yagi_sdr_characterization.py).

## Current status

The Python FFT/PSD, band-power estimator, and interactive 12-position angular loop have run successfully. Initial polar plots are **software workflow demonstrations**, not validated Yagi patterns. VNA-assisted tuning and instrument photographs have been documented, but a complete set of calibrated, repeatable directional test data is still pending.

Do not report predicted gain/beamwidth from the supplied design as measured values, or infer RF transmitter power from uncalibrated IQ values.
