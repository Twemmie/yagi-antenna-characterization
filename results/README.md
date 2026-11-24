# Results

This folder is for reproducible numerical measurements, plots, and instrument evidence, with clear separation between software tests, original design predictions, and controlled measurements.

## Current status

The Python script has successfully created these files **locally** under `results/plots/`:

- `received_spectrum.png` — initial 425 MHz SDR FFT spectrum.
- `power_spectral_density.png` — Welch PSD from an IQ capture.
- `angular_sweep_software_test.png` — preliminary polar plot from the interactive test workflow.

Local successful saves do **not** necessarily mean the images were uploaded to GitHub. The polar plot is explicitly labeled a **software test**: variation with angle is not a validated antenna radiation pattern without a controlled RF source and setup.

## For future controlled measurements

Record test date, RF center and signal frequency, receiver bandwidth/sample rate/gain, antenna geometry and polarization, angle, received band power, a separate signal-off noise reference, and repeated observations. Export numerical observations (ideally CSV) so plots can be regenerated from the underlying data.

The original design's predicted gain and beamwidth are documented in [antenna-design.md](../hardware/antenna-design.md); those figures are **not** experimental results.
