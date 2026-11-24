# PlutoSDR DSP Analysis

The working source file is [`yagi_sdr_characterization.py`](yagi_sdr_characterization.py), developed incrementally in Spyder for the six-element Yagi characterization project.

## Implemented and locally tested

- PlutoSDR USB-Ethernet connection and fixed manual receiver gain.
- Complex IQ acquisition, FFT spectrum, and Welch power spectral density (PSD).
- Selection of a frequency band and integration of the **linear** PSD to estimate uncalibrated squared-IQ-sample power.
- Preliminary within-band median PSD/background calculations (exploratory, **not** a measured receiver-only noise reference).
- Operator-guided 0°–330° angular sweep at 30° steps with new IQ captures.
- Relative-dB normalization, a closed 360° polar software-test plot, and local PNG exports.

## Running the script

1. Install compatible Python packages listed in [`../requirements.txt`](../requirements.txt) in your chosen environment.
2. Connect and verify your ADALM-Pluto SDR; adjust the hardcoded URI (`ip:192.168.2.1` is the working USB-Ethernet example).
3. In Spyder, use the repository root as the working directory; the script creates `results/plots/` relative to the working directory.
4. Run the script or appropriate `# %%` cells in order. The angular loop prompts for each orientation; it is **interactive** and is not a headless batch program.
5. Check the plots and console diagnostics. The 425 MHz LO and 424.2–424.4 MHz integration band are **software-test settings**, not the 440 MHz Yagi's verified test frequency.

The script uses an installation-specific Windows C-runtime lookup workaround before importing `adi`. Its necessity depends on the local Python and pylibiio versions; it is not a general requirement for all systems.

## Limitations and next improvements

**No validated radiation pattern yet.** A controlled, stable RF reference transmitter, a true separate signal-off baseline, repeatable geometry, and documented receiver settings are required before interpreting angular variation as antenna directivity. See [controlled angular sweep procedure](../experiments/controlled-angular-sweep.md).

The current polar software-test plot shifts relative dB to nonnegative radii; this can exaggerate sub-dB variations. Initial plots and power figures have an arbitrary reference, **not dBm, dBi, or measured antenna gain**.

Planned: centralize configuration, record angle/power/settings as CSV, repeat captures with uncertainty estimates, move common DSP operations into reusable functions, and add robust acquisition/invalid-power checks. These features are not claimed to exist yet.
