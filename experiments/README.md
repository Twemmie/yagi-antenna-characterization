# Physical experiments — completed and proposed

**Date:** November 25, 2026. **Status:** Five indoor physical sweeps and transmitter reference tests completed; no calibrated free-space pattern established.

## Experiment inventory

| Dataset | Coverage and interpretation |
|---|---|
| CC1101 transmitter verification | On/off spectral peaks and power contrast around the observed 433.921 MHz carrier |
| Stationary receiver checks | Five-capture and sequential fixed-position tests, including some with the antenna pointing upward on a chair; these are NOT angular patterns |
| Physical sweep 1 | 0°, 30°, … 300° (**11 measured angles; missing 330°**) |
| Physical sweeps 2–5 | 0°, 30°, … 330° (**12 angles per run**) |
| Additional half-sweeps | Two physical 0°–150° studies, preserved separately and **not averaged** with the five full sweeps |

**Total analyzed full-sweep data:** 59 actual angle-power observations, no invented values for Sweep 1 at 330°.

See [measurement procedure](controlled-angular-sweep.md), [raw CSV](../results/data/yagi_five_sweeps_raw.csv), and [consolidated analysis](../analysis/Yagi_Consolidated_Statistical_Analysis.md).

**Interpretation:** Initial 0°–150° readings are nearly constant within each sweep; rearward directions exhibit inconsistent minima and substantial run-to-run scatter. A handheld indoor environment, reflection, transmitter/receiver drift, and changing coax geometry are plausible influences. The data do not justify a validated beamwidth, gain, or free-space front-to-back ratio.
