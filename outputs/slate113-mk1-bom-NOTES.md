# Slate113 MK1 BOM sourcing notes

Verified against the live schematic BOM on 2026-08-09. This is sourcing preparation only; no order was placed.

## Resolved passives

The old out-of-stock supplier codes were replaced in the schematic fields and regenerated BOM with same-value, same-package parts. Voltage/power ratings are equal or higher.

| Value | Old LCSC | Replacement source | Replacement MPN |
|---|---:|---:|---|
| 1 uF, 50 V, X5R, 0603 | C15849 | C92848 | UMK107BJ105KA-T |
| 1 kOhm, 1%, 0603 | C21190 | C118155 | ERJ3EKF1001V |
| 110 Ohm, 1%, 0603 | C22781 | C217696 | ARG03FTC1100 |
| 180 kOhm, 1%, 0603 | C22827 | C123419 | RC0603FR-07180KL |
| 10 Ohm, 1%, 0603 | C22859 | C109318 | RC0603FR-0710RL |
| 127 kOhm, 1%, 0603 | C22869 | DigiKey 311-127KHRCT-ND | RC0603FR-07127KL |
| 4.7 kOhm, 1%, 0603 | C23162 | C163914 | WR06X4701FTL |
| 10 kOhm, 1%, 0603 | C25804 | C840630 | CR0603-FX-1002ELF |
| 200 kOhm, 1%, 0603 | C25811 | C118142 | ERJ3EKF2003V |
| 20 kOhm, 1%, 0603 | C4184 | C844923 | CRCW060320K0FKEA |
| 1 uF, 16 V minimum, X5R, 0603 | C49326357 | C5673 | CL10A105KA8NNNC (25 V) |
| 2.2 uF, 35 V minimum, X5R, 0603 | C49326370 | C7432769 | HGC0603R5225K500NTHJ (50 V) |
| 4.7 uF, 16 V, X5R, 0603 | C49326377 | C77045 | GRM188R61C475KE11D |

`C23186` (5.1 kOhm) and `C25819` (47 kOhm) were not changed: their live LCSC listings are stocked again.

## RFPC-SMA27-F correction

`RFPC-SMA27-F` is the manufacturer part number for J1, J8, J11, J22, J23, and J25. Their BOM fields now declare:

- MPN: `RFPC-SMA27-F`
- manufacturer: `GradConn` / GCT
- DigiKey supplier order number: `2073-RFPC-SMA27-F-ND`
- LCSC part: blank; no exact LCSC listing was verified

`C496552` belongs to J3, J7, J10, J12, J24, and J26: the I-PEX `BWIPX-1-001E` U.FL connectors. It is not the SMA connector code.

A supplier order number is the distributor's SKU for ordering an MPN. Example: `RFPC-SMA27-F` is the MPN; `2073-RFPC-SMA27-F-ND` is DigiKey's orderable SKU.

## U37, U38, and U39

- U37: `CPL0605AT13R2455A`, Pulse, DigiKey `553-CPL0605AT13R2455ATR-ND`. Footprint intentionally left for AJ to create. Placed U37 still uses old eight-pin `2450CF15A0100001E` symbol, while Pulse part has four terminals. Symbol/pin mapping must be corrected first.
- U38: locked to active replacement `X4C60K1-20S`, RFMW listing `711055`; exact DigiKey SKU not verified. Footprint still required.
- U39: `XEC24P3-30GR`, TTM/Anaren. Primary source restored to DigiKey cut-tape SKU `1173-XEC24P3-30GRCT-ND`; DigiKey currently lists it active and stocked. Mouser field cleared.

U39 source fields exist on placed symbol, but KiCad CLI currently omits U39 from exported BOM because its newly created `slate113:XEC24P3-30G` library symbol has not been embedded into `io.kicad_sch` by a schematic-editor save. This is BOM/export state, not sourcing availability.

## Remaining sourcing blockers

Passive shortage set resolved. Remaining parts and purpose:

| References | Part | Purpose in Slate113 | Source state / blocker |
|---|---|---|---|
| U23 | `EM4095HMSO16B+` | 125/134 kHz RFID analog front end: drives `RFID_ANT1/2`, exposes demod/mod/ready/shutdown signals | Resolved through DigiKey `2651-EM4095HMSO16B+CT-ND`; active and stocked |
| U29 | `PN7160A1HN/C100Y` | 13.56 MHz NFC controller: I2C host, NFC TX/RX and antenna matching network | Resolved through DigiKey `568-PN7160A1HN/C100YCT-ND`; active and stocked |
| U68 | `SN74AHCT125PWR` | 3.3 V to 5 V buffer for LED bar `DATA` and `CLK`, controlled by `LED_BUF_OE_N` | Exact part active; DigiKey/LCSC out, but Arrow has small-quantity stock. Blocker only if BOM must use LCSC/DigiKey exclusively |
| U24-U27 | `4259-63` / PE4259 | Four SPDT RF switches selecting differential RF/GPS band paths through `BAND_SEL_1/2` | Resolved through DigiKey `1046-1011-1-ND`; active and stocked |
| U30, U36 | `4259-63` / PE4259 | Wi-Fi and BLE antenna-path switching between module path, SMA/test path, and sensing branch | Same resolved DigiKey source |
| U16 | `AMLGA7921` | Wi-Fi/Bluetooth radio module connected to USB, Wi-Fi/BT antennas, wake/control signals | FCC ID `2AB877921` verified; contact ALFA/ICOnnect for samples, current datasheet, MOQ and lead time. |
| U37 | `CPL0605AT13R2455A` | Samples BLE RF power into `BLE_CPL` while main RF path goes between switch and SMA antenna | Footprint left for AJ; blocker is old incompatible eight-pin symbol/pin mapping |
| U39 | `XEC24P3-30GR` | 2.4 GHz 30 dB directional coupler candidate for Wi-Fi RF sensing | Sourcing resolved at DigiKey; blocker is schematic-library embedding/BOM export cleanup |
| U38 | `X4C60K1-20S` | 4.4-6.5 GHz 20 dB directional coupler for Wi-Fi RF sensing | RFMW listing `711055`, reported stock; no verified DigiKey SKU for exact `20S` MPN. Footprint still required from TTM drawing. |

## Validation

- BOM note state updated for U38 replacement; regenerate exports after footprint/library work.
- KiCad ERC: 0 errors, 0 warnings.
- PCB layout is not started, so footprint/layout readiness remains a separate gate.
