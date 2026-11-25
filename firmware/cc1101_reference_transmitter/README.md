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

**IMPORTANT:** The original experiment sketch had `ENABLE_RF_TX = true`. The published version defaults it to **false**. This makes the repository's public reference code nontransmitting until intentionally enabled. Unmodulated carrier alone does **not** satisfy amateur-radio station identification; any transmission must be lawful, identified and supervised.

**Voltage levels:** UNO R4 WiFi 5-V I/O is **not inherently compatible with CC1101 3.3-V digital pins**. Check the breakout module's pinout/regulator and provide safe logic-level translation before rebuilding the wiring.
