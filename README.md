# Six-Element Yagi Antenna Characterization

An experimental RF and digital signal processing project studying a constructed six-element Yagi-Uda antenna with an **ADALM-Pluto SDR**, **Python**, and a **vector network analyzer (VNA)**.

## Project overview

The antenna was constructed from an existing **440 MHz design** (one reflector, one driven element, four directors) on an approximately **66 cm / 26 in boom**. The original antenna design was provided by another person; its design and predicted performance will be credited separately from the construction, measurement, and signal-processing work.

The project aims to characterize antenna impedance matching and the **relative directional response** using received IQ samples, frequency-domain analysis, and controlled measurements. **Design predictions are not experimental measurements.**

## Current progress

- [x] Constructed six-element Yagi using the provided element dimensions
- [x] Tuned antenna and photographed VNA measurements
- [x] Verified PlutoSDR connection and initial Python FFT spectrum visualization
- [ ] Verify Yagi-connected signal reception and implement/test PSD-based power measurement
- [ ] Collect controlled angular measurements with a stable reference signal
- [ ] Reconstruct and analyze a relative radiation pattern
- [ ] Publish final experimental results and limitations

## Repository contents

- [`theory/`](theory/) — six completed blocks of RF/DSP theory notes (to be transferred from handwritten notes)
- [`hardware/`](hardware/) — original antenna design, attribution, construction images, and feed details
- [`src/`](src/) — PlutoSDR and analysis Python code, developed and tested incrementally
- [`experiments/`](experiments/) — repeatable setups, procedures, verified measurements, and interpretations
- [`results/`](results/) — measurement tables, screenshots, and plots

## Equipment and environment

- Six-element, tape-measure Yagi antenna
- Coaxial BNC cable and BNC-to-SMA adapter connected to PlutoSDR receive input
- ADALM-Pluto SDR
- VNA used for impedance and matching assessment
- Windows laptop, Spyder IDE, Python, NumPy, Matplotlib, and SciPy

## Experimental approach

1. Document the existing antenna construction and VNA tuning evidence.
2. Verify reception with the antenna connected and establish a stable reference signal.
3. Estimate relative received power using a controlled SDR configuration.
4. Rotate the antenna through known angular increments and save observations.
5. Plot the relative directional pattern and discuss beamwidth, front-to-back ratio, and limitations **only to the extent supported by measurements**.

The receiver's initial **425 MHz** configuration was a software demonstration, not the antenna's **440 MHz design frequency**. Final measurement frequencies will be recorded from the actual test setup.

## Measurement limitations

Uncalibrated PlutoSDR sample magnitudes do not establish absolute power in dBm or absolute antenna gain. Original VNA photographs can support qualitative observations, but values not reliably readable from the display will not be presented as precise measurements.

## Attribution

The antenna geometry originated from a design supplied by another person. The final hardware documentation will identify the original designer and distinguish that contribution from this project's construction, tuning, DSP implementation, and experimental characterization.
