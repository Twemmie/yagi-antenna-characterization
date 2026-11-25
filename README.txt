YAGI ANTENNA CHARACTERIZATION — COMBINED DOWNLOAD

This package contains source code, Arduino CC1101 firmware, five-sweep statistical results,
selected experimental images, measurement setup photos and six theory PDFs.

src/yagi_sdr_characterization_original.py is exactly the newly uploaded script.
src/yagi_sdr_characterization_corrected.py is a minimal convenience edit:
 - correct count of angles measured
 - calculate stationary sample standard deviation after five captures
 - save numbered plot and CSV while the polar plot figure exists
Check sweep_number before running. The code was syntax-checked but not hardware-tested.

Important scientific cautions:
 - Plotted values are uncalibrated, not dBm, dBi, or free-space antenna gain.
 - Polar radial-offset plotting can exaggerate small differences.
 - Data were acquired indoors with manual antenna positioning and possible multipath.
 - Arduino sketch has automatic RF transmit enabled; use only legally authorized and properly
   identified transmissions, and verify 3.3V compatibility/level shifting for CC1101.
 - Images represent different experiments and are not necessarily a one-to-one mapping to every sweep.
 - The project source code is provided for reproducibility; no GitHub updates were performed.
