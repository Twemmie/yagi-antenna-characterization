# RF/DSP Theory Notes

Six handwritten theory chapters supporting the six-element Yagi antenna characterization project. These are **learning notes**, not measured experimental results. The original handwritten material is preserved in PDF format.

| Chapter | Document | Topics |
|---|---|---|
| 1 | `01-sampling-and-nyquist.pdf` | Sampling, Nyquist–Shannon, complex IQ, PlutoSDR sampling rate and RF bandwidth |
| 2 | `02-frequency-downconversion.pdf` | Local oscillator, mixing, heterodyning, IQ baseband conversion |
| 3 | `03-fourier-analysis.pdf` | DFT/FFT, frequency bins, resolution, spectral leakage, windowing, FFT magnitudes |
| 4 | `04-power-spectral-density.pdf` | RMS and signal power, periodograms, Welch PSD, PSD integration, PlutoSDR examples |
| 5 | `05-receiver-characteristics.pdf` | Gain, AGC, noise floor, SNR, dynamic range, receiver artifacts, uncertainty |
| 6 | `06-yagi-antenna-theory.pdf` | Yagi-Uda structure, radiation patterns, gain, impedance, resonance, S11, VSWR, bandwidth |

**PDF upload status:** The six original PDFs are being prepared for upload. The names above are the target filenames; PDFs are not yet attached in this repository.

## Notes and limitations

- Values near **425 MHz** in the introductory SDR examples illustrate the initial software setup. The provided physical antenna design is for **440 MHz**.
- Chapter 3 uses a direct DFT complexity statement that should read **O(N²)**, rather than **O(N³)**. The original handwriting has been retained instead of silently modified.
- Code snippets in these learning notes are illustrative. Working experimental code belongs in `../src/` and will be verified in Spyder.
- Chapter 4's PSD methods will be tested with actual IQ samples before interpreting received-power differences.
- Absolute antenna gain cannot be inferred from uncalibrated PlutoSDR relative power measurements.
