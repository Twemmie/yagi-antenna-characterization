# Python receiver and DSP pipeline

**Recommended runnable script:** [`yagi_sdr_characterization.py`](yagi_sdr_characterization.py).

It includes PlutoSDR connection, IQ diagnostics, 16,384-bin FFT, Welch PSD, 433.87–433.97 MHz power integration, interactive 30° physical sweeps, plots, reference-carrier detection, and five-capture stability measurements.

## Reproducibility

From the **repository root** with PlutoSDR attached at `ip:192.168.2.1`:

```bash
python -m pip install -r requirements.txt
python src/yagi_sdr_characterization.py
```

Or run `# %%` cells in Spyder. The script **prompts for each angle** and should not be run unattended. Change the `sweep_number` in the plotting section before any new experiment; it saves a numbered `results/plots/yagi_sweep_N.png` and `results/yagi_sweep_N.csv`, along with FFT and PSD snapshots.

**Files preserved:** [historical original script](archive/yagi_sdr_characterization_uploaded_2026-11-25.py) and [previous repository source](archive/yagi_sdr_characterization_legacy.py). The working script incorporates only minimal count/statistics/export fixes; it has not been revalidated on physical SDR hardware following cleanup.

### Cautions

- IQ/FFT/PSD and band-power levels are **uncalibrated sample-based quantities**, not absolute power.
- The in-band PSD median is only a crude background proxy, **not** an independent transmitter-OFF baseline.
- A pair of nonidentical IQ captures does not prove that no stale data are queued.
- The original polar chart shifts the minimum relative level to zero radius and can exaggerate small differences. For scientific interpretation use the [five-sweep overlay](../results/plots/yagi_five_sweeps_overlay.png).
- The Windows C-runtime library lookup workaround is installation-specific.
- Offline analysis runs independently with `python analysis/analyze_yagi.py`.
