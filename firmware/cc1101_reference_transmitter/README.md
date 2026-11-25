# Arduino UNO R4 WiFi + CC1101 reference transmitter

[Source code](cc1101_reference_transmitter.ino) · [Physical setup](../../hardware/README.md)

The Arduino uses **RadioLib** and SPI to initialize an eight-pin CC1101 and, only after explicit local enablement, request a direct RF carrier for brief authorized measurements.

| Parameter | Value |
|---|---|
| Commanded CC1101 frequency | **434.0 MHz** |
| Requested TX output power | **−10 dBm**, not independently verified |
| RadioLib module constructor | `new Module(10, 3, RADIOLIB_NC, 4)` |
| SPI CS / SCK / MOSI / MISO | D10 / D13 / D11 / D12 |
| GDO0 / GDO2 | D3 / D4 |
| Transmission mode | `radio.transmitDirect()` (unmodulated carrier) |
| Observed PlutoSDR carrier | ~**433.921 MHz**; the offset is not independently attributed to TX vs RX oscillator |


## CC1101 module pinout reference images

These are the **original pinout / wiring reference pictures uploaded with the Yagi characterization project**. They are stored in `hardware/photos/` and embedded here for convenience.

![CC1101 pinout reference image A](../../hardware/photos/image(20261125-200424).png)

*Pinout/wiring reference A — verify the labels against your specific CC1101 breakout board before connecting it.*

![CC1101 pinout reference image B](../../hardware/photos/image(20261125-200520).png)

*Pinout/wiring reference B — supporting pinout/wiring reference from the original upload.*

### Arduino UNO R4 WiFi ↔ CC1101 signal mapping

| CC1101 module signal | Arduino UNO R4 WiFi |
|---|---|
| CSN / CS | D10 |
| SCK | D13 |
| MOSI / SI | D11 |
| MISO / SO | D12 |
| GDO0 | D3 |
| GDO2 | D4 |
| VCC | Regulated 3.3 V **only if the module supports the available supply current** |
| GND | Common ground |

The table reflects the [uploaded RadioLib firmware](cc1101_reference_transmitter.ino). **Board pin position is not universal:** compare actual printed labels and documentation for your particular CC1101 module. The UNO R4 WiFi's 5-V logic outputs must not be connected directly to 3.3-V-only CC1101 logic inputs; use compatible logic-level translation.

**IMPORTANT:** The original experiment sketch had `ENABLE_RF_TX = true`. The published version defaults it to **false**. This makes the repository's public reference code nontransmitting until intentionally enabled. Unmodulated carrier alone does **not** satisfy amateur-radio station identification; any transmission must be lawful, identified and supervised.

**Voltage levels:** UNO R4 WiFi 5-V I/O is **not inherently compatible with CC1101 3.3-V digital pins**. Check the breakout module's pinout/regulator and provide safe logic-level translation before rebuilding the wiring.
