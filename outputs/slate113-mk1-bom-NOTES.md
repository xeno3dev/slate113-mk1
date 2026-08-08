# Slate113 MK1 BOM Notes

Generated from LCSC BOM quote export (`export_project_20260808_073413.xls`) and DigiKey cart export (`Slate113 BOM.csv`), both dated 2026-08-08.

## Discontinued / out-of-stock LCSC parts: 20

These 20 LCSC part numbers are flagged "Backordered" on the live LCSC BOM quote tool and confirmed "Out of Stock" on their individual LCSC product pages as of 2026-08-08. Every one of these needs a restocked/alternate source before ordering, or accept LCSC's backorder lead time.

| LCSC Part # | Mfr Part Number | Line Item |
|---|---|---|
| C15849 | CL10A105KB8NNNC | 1uF X5R 0603 ceramic cap |
| C17203964 | EM4095HMSO16B+ | RFID reader IC, SOIC-16 |
| C21190 | 0603WAF1001T5E | 1kΩ 0603 resistor |
| C22781 | 0603WAF1100T5E | 110Ω 0603 resistor |
| C22827 | 0603WAF1803T5E | 180kΩ 0603 resistor |
| C22859 | 0603WAF100JT5E | 10Ω 0603 resistor |
| C22869 | 0603WAF1273T5E | 127kΩ 0603 resistor |
| C23162 | 0603WAF4701T5E | 4.7kΩ 0603 resistor |
| C23186 | 0603WAF5101T5E | 5.1kΩ 0603 resistor |
| C25804 | 0603WAF1002T5E | 10kΩ 0603 resistor |
| C25811 | 0603WAF2003T5E | 200kΩ 0603 resistor |
| C25819 | 0603WAF4702T5E | 47kΩ 0603 resistor |
| C3303790 | PN7160A1HN/C100Y | NFC controller IC, HVQFN-40 |
| C36365 | SN74AHCT125PWR | Buffer/driver IC, TSSOP-14 |
| C37211559 | X4C60K1-20SR | RF directional coupler (U38) |
| C4184 | 0603WAF2002T5E | 20kΩ 0603 resistor |
| C470892 | PE4259-63 | RF switch, SC-70-6 |
| C49326357 | 0603X5R105K160NT | 1uF X5R 0603 ceramic cap |
| C49326370 | 0603X5R225K350NT | 2.2uF X5R 0603 ceramic cap |
| C49326377 | 0603X5R475K160NT | 4.7uF X5R 0603 ceramic cap |

Most of these are easy-to-substitute passives (UNI-ROYAL 0603 resistors, generic X5R caps) — any equivalent-spec part from another manufacturer works. The three ICs (`EM4095HMSO16B+`, `PN7160A1HN/C100Y`, `SN74AHCT125PWR`) and the RF parts (`X4C60K1-20SR`, `PE4259-63`) need real functional replacements, not just a passive swap.

## Pricing

- `Unit Price (USD)` and `Total Cost (USD)` columns added to `slate113-mk1-bom.csv`, sourced from the LCSC BOM quote (preferred) or DigiKey cart pricing (fallback) per line.
- 212 of 214 grouped BOM lines have a price. Missing: `U16` (AMLGA7921, no LCSC/DigiKey listing exists) and `LS1`/`LS2` (generic solder pads, not purchasable parts).
- Total matched cost: **$227.37** (sum of priced lines only, at requested BOM quantities — excludes U16/LS1/LS2 since they have no price).
