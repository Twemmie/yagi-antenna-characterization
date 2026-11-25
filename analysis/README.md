# Five-sweep statistical analysis

[Full consolidated report](Yagi_Consolidated_Statistical_Analysis.md) · [Raw measurements](../results/data/yagi_five_sweeps_raw.csv)

Run from repository root:

```bash
python -m pip install -r requirements.txt
python analysis/analyze_yagi.py
```

This reads the **59 committed physical angle–power values**, preserving Sweep 1's missing 330° observation. For each sweep, subtract the 0° dB reading before computing the across-run **mean, median, and sample standard deviation** at each angle. The code writes the four summary CSVs under `results/data/` and regenerates `results/plots/yagi_five_sweeps_overlay.png` and `yagi_mean_sd_by_angle.png`.

The sample SD describes **between-sweep variation**, not instrument calibration or a confidence interval. The 0° SD is zero by definition. The 270° SD is approximately **7.31 dB**; no validated null, beamwidth, free-space pattern, absolute gain, or reliable front-to-back ratio is claimed.
