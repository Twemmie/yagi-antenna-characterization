# Six-Element Yagi Antenna Characterization

An experimental RF and digital signal processing project studying a constructed six-element Yagi-Uda antenna with an **ADALM-Pluto SDR**, **Python**, and a **vector network analyzer (VNA)**.

## Project overview

The antenna was constructed from an existing **440 MHz design** (one reflector, one driven element, four directors) on an approximately **66 cm / 26 in boom**. The original antenna design was provided by another person; its design and predicted performance will be credited separately from the construction, measurement, and signal-processing work.

The project aims to characterize antenna impedance matching and the **relative directional response** using received IQ samples, frequency-domain analysis, and controlled measurements. **Design predictions are not experimental measurements.**

## Current progress

- [x] Constructed six-element Yagi using the provided element dimensions
- [x] Tuned antenna and photographed VNA measurements
- [x] Verified PlutoSDR connection and Python FFT spectrum visualization
- [x] Implemented and tested Welch PSD estimation and uncalibrated band-power calculations
- [x] Implemented and tested a 12-position angular-sweep workflow and preliminary polar plotting (software test only)
- [ ] Verify reception of a known reference signal through the Yagi and record separate signal-on/signal-off measurements
- [ ] Collect controlled angular measurements with a stable reference transmitter
- [ ] Produce and analyze a validated relative radiation pattern
- [ ] Publish final experimental results and limitations

## Repository contents

- [`theory/`](theory/) — six uploaded PDF chapters of handwritten RF/DSP theory notes
- [`hardware/`](hardware/) — supplied antenna design, attribution, uploaded construction images, and feed details
- [`src/yagi_sdr_characterization.py`](src/yagi_sdr_characterization.py) — working PlutoSDR IQ capture, FFT, Welch PSD, band-power estimation, guided angular sweep, and preliminary polar plotting
- [`experiments/`](experiments/) — controlled-test protocol, planned setup, and future verified measurements
- [`results/`](results/) — planned numeric measurement tables, verified result plots, and instrument evidence

## Equipment and environment

- Six-element, tape-measure Yagi antenna
- Coaxial BNC cable and BNC-to-SMA adapter connected to PlutoSDR receive input
- ADALM-Pluto SDR
- VNA used for impedance and matching assessment
- Windows laptop, Spyder IDE, Python, NumPy, Matplotlib, and SciPy

## Python analysis pipeline

The current single-file Python implementation uses PyADI-IIO, NumPy, SciPy, and Matplotlib to:

1. Configure the PlutoSDR receiver and acquire complex IQ samples.
2. Compute an FFT magnitude spectrum and Welch power spectral density.
3. Integrate a selected frequency band to estimate uncalibrated received sample power, including a preliminary median-based background estimate.
4. Prompt the operator at 30° increments, capture a fresh IQ buffer at each of 12 unique orientations (0°–330°), and store a band-power estimate.
5. Normalize these measurements and generate a **software-test** polar visualization, reusing the 0° point at 360° to close the curve.

The script saves FFT, PSD, and angular-sweep PNGs to `results/plots/` when run locally; these locally generated files are not necessarily committed to GitHub. These plot exports are not proof of physical antenna directivity. The angular-sweep workflow has been exercised, but a controlled, stable RF reference has **not** yet been used to validate its radiation pattern. The current polar plot shifts the relative-dB values to nonnegative radii for visualization, which can make small variations appear dramatic.

The current script is designed for incremental experimentation in Spyder. See [`src/README.md`](src/README.md) for run instructions and [`experiments/controlled-angular-sweep.md`](experiments/controlled-angular-sweep.md) for the future controlled-test protocol. Receiver settings and the test band are hardcoded; measurement values are not yet exported to CSV, and the analysis steps have not yet been refactored into reusable functions. These are planned reproducibility and maintainability improvements, not completed features.

## Experimental approach

1. Document the existing antenna construction and VNA tuning evidence.
2. Verify reception with the antenna connected and establish a stable reference signal.
3. Estimate relative received power using a controlled SDR configuration.
4. Rotate the antenna through known angular increments and save observations.
5. Plot the relative directional pattern and discuss beamwidth, front-to-back ratio, and limitations **only to the extent supported by measurements**.

The receiver's initial **425 MHz** configuration and **424.2–424.4 MHz** integration band were software demonstrations, not the antenna's **440 MHz design frequency**. Final measurement frequencies will be recorded from the actual test setup.

## Measurement limitations

Uncalibrated PlutoSDR sample magnitudes do not establish absolute power in dBm or absolute antenna gain. The within-band median PSD is only a preliminary background proxy, not an independently measured noise floor; positive background-subtracted power alone does not confirm an external transmission. Original VNA photographs can support qualitative observations, but values not reliably readable from the display will not be presented as precise measurements.

## Attribution

The antenna geometry originated from a design supplied by another person. The final hardware documentation will identify the original designer and distinguish that contribution from this project's construction, tuning, DSP implementation, and experimental characterization.
