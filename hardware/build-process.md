# Six-Element Yagi — Physical Build Process

This document records the appearance and construction features of the completed tape-measure Yagi-Uda antenna built for the RF/DSP characterization project. It follows the existing **440 MHz, six-element** design documented in [antenna-design.md](antenna-design.md). It is a photographic construction record, **not** a claim that the antenna geometry was independently designed for this project.

## 1. Construction overview

The photographs show:

- A **white PVC boom** and **six yellow tape-measure elements**.
- Black mounting fixtures at each element, with visible fasteners. The fixtures look 3D printed, but their manufacturing method is not confirmed by the photos.
- A split driven-element region with visible metallic conductors and soldered joints.
- A black coaxial feed cable routed along the boom, coiled near the reflector-side end.
- A coaxial connector at the free cable end.

The supplied design specifies **one reflector, one driven element, and four directors**. Exact element positions and lengths are listed in the [original design](antenna-design.md), rather than estimated from the photographs.

## 2. Mounting the elements

The photos show the six sections of tape measure spanning the PVC boom, held by individual black fixtures. The nonmetallic boom helps physically support the elements without acting as the conductive antenna boom assumed in some Yagi designs.

Both faces of the assembled antenna are photographed, revealing the fasteners, fixtures, spacing, feed region, and wire routing.

**Front/feed-facing view:** [`images/yagi-front-view.jpg`](images/yagi-front-view.jpg) — source photograph: `IMG_9417.JPG`.

**Reverse view:** [`images/yagi-reverse-view.jpg`](images/yagi-reverse-view.jpg) — source photograph: `IMG_9416.JPG`.

**Additional assembled view:** [`images/yagi-assembled-upright.jpg`](images/yagi-assembled-upright.jpg) — source photograph: `IMG_8717.JPG`.

**Additional floor view:** [`images/yagi-assembled-floor.jpg`](images/yagi-assembled-floor.jpg) — source photograph: `IMG_8736.JPG`.

> Image links above refer to the intended image paths. The image files need to be uploaded separately before these links will open in GitHub.

## 3. Driven-element feed area

A close-up of the driven-element mounting area shows yellow conductive tape-measure sections, solder joints, exposed copper conductors, and the incoming black coaxial cable.

**Feed close-up:** [`images/driven-element-feed.jpg`](images/driven-element-feed.jpg) — source photograph: `IMG_8779.JPG`.

The presence of a looped conductor is visible, but the photograph alone does **not** establish the exact electrical connection topology or prove a particular matching-network design. A verified electrical feed schematic should be added separately if available.

## 4. Coax routing and connector

The assembled-antenna photographs show a loop of black coaxial cable secured near the reflector-side portion of the boom, continuing to a coaxial connector. Keeping the feed cable in a documented arrangement matters because routing and nearby conductors can influence an RF measurement.

The exact coaxial cable type, electrical length, and connector specifications have not yet been verified.

## 5. Initial PlutoSDR setup

A separate photograph documents a blue ADALM-Pluto SDR attached through an RF adapter/cable and USB to a laptop running the receiver setup.

**PlutoSDR setup image:** [`images/plutosdr-connection.jpg`](images/plutosdr-connection.jpg) — source photograph: `IMG_9017.JPG`.

The general measurement chain is:

```text
Yagi driven-element feed
    -> coax cable
    -> BNC-to-SMA adapter
    -> ADALM-Pluto SDR RX input
    -> USB
    -> Windows laptop / Spyder / Python
```

The initial working software spectrum analyzer used a **425 MHz center frequency** for receiver testing; that is separate from the antenna's **440 MHz design frequency**.

## 6. What remains to document

- Confirm the exact feed wiring and any matching arrangement from construction details or a schematic.
- Verify coax type and assembly dimensions where required.
- Upload these construction photographs to `hardware/images/`.
- Record VNA results and controlled directional measurements in `experiments/` and `results/` rather than treating construction photographs as RF performance measurements.

## Design attribution

The original design sheet was supplied by **Travis through the UCF Amateur Radio Club**. See [antenna-design.md](antenna-design.md) for the design specifications, documented software warnings, and attribution caveat.
