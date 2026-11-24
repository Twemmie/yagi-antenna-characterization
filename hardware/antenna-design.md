# Six-Element Yagi-Uda Antenna — Original Design

## Overview

This project characterizes a **six-element Yagi-Uda antenna** constructed using an existing **440 MHz antenna design** supplied through the UCF Amateur Radio Club. The dimensions listed below are taken from the original design sheet and were used to build the antenna.

The antenna geometry was **not independently designed as part of this characterization project**. The project's separate contributions include physical construction, VNA-assisted tuning, PlutoSDR-based signal processing, and experimental characterization.

> **Design attribution:** The design sheet was supplied by **Travis (UCF Amateur Radio Club)**. The original designer/authorship of the design calculations should be verified before assigning design credit more specifically.

## Design Specifications

| Parameter | Value |
|---|---|
| Design frequency | **440 MHz** |
| Antenna type | Yagi-Uda |
| Number of elements | **6** |
| Reflector | 1 |
| Driven element | 1 |
| Directors | 4 |
| Electrical boom length | **26 in (66.04 cm)** |
| Boom type | Nonmetallic, with insulated elements |
| Boom correction | None applied in the design software |
| Estimated design gain | **8.917 dBd** (approximately **11.07 dBi**) |
| Predicted horizontal beamwidth | **47.4°** |
| Predicted vertical beamwidth | **51.9°** |
| Element-length dimensional tolerance shown | **0.08 in (3/32 in)** |

**Note:** Gain and beamwidth are **estimates from the original design software**, not measured results for the constructed antenna.

## Element Dimensions

Positions below are **cumulative distances along the boom from the reflector** (as labeled in the design sheet). All values are in inches.

| Element | Cumulative spacing from reflector | Element length |
|---|---:|---:|
| Reflector (Refl.) | 0 | 12-25/32 |
| Driven element (D.E.) | 5-3/8 | 12-7/32 |
| Director 1 (D1) | 7-3/8 | 10-13/16 |
| Director 2 (D2) | 12-7/32 | 10-19/32 |
| Director 3 (D3) | 17-31/32 | 10-13/32 |
| Director 4 (D4) | 24-11/16 | 10-7/32 |

These are the supplied design dimensions used for the constructed antenna. They should not be confused with new dimensions derived from VNA measurements.

## Design Software Parameters and Warnings

The supplied design sheet also lists:

- **1.000 in** driven-element diameter input.
- **1.000 in** parasitic-element diameter input.
- Suggested two-Yagi stacking separation of **28.8 in horizontally** and **26.4 in vertically**.

The design program displayed two warnings:

1. **Boom length warning:** The specified 26-inch boom was flagged as too small under the software's criterion that boom length exceed 2.2 wavelengths.
2. **Driven-element diameter warning:** The entered 1.000-inch driven-element diameter exceeded the software's indicated acceptable range of 0.027–0.536 inches.

The actual antenna was built using **flat tape-measure elements**, so the software's cylindrical-diameter input does not directly describe the flat element geometry. These warnings are recorded as displayed in the original design sheet; they have not been independently resolved through electromagnetic simulation.

For these reasons, the predicted gain and beamwidth must be treated as **design reference values**, not established antenna performance.

## Original Design Image

The original design screenshot documents the element positions, lengths, estimated performance, and software warnings.

**Uploaded design reference:** [Original 440 MHz Yagi design screenshot](images/original-yagi-design.jpg). This is supplied reference material, not an independently produced antenna design.

## Design Versus Measurements

The following must remain distinct in this project:

- **Design frequency:** 440 MHz, as specified in the original design sheet.
- **Initial PlutoSDR software center frequency:** 425 MHz, used during early receiver/FFT testing and as an instructional example.
- **Experimental frequency, matching, and radiation-pattern results:** To be reported from verified VNA and PlutoSDR measurements.

A good VNA impedance match does not alone establish absolute antenna gain, radiation efficiency, or beamwidth. Those require separate characterization methods.

See the repository's `experiments/` and `results/` directories for procedures and recorded measurements as they become available.
