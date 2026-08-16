# BOM source-resolution record — 2026-08-12

Verified and written to the schematic:

## 2026-08-13 — CM5 Pro landed cost

| Item | Qty | Item | Delivery | Sales tax | Landed total | Source |
|---|---:|---:|---:|---:|---:|---|
| ArmSoM CM5 Pro (8GB LPDDR5, 64GB eMMC, Wi-Fi 6 + BT 5.3) | 1 | US$229.00 | US$12.00 | US$62.98 | **US$303.98** | User checkout screenshot, 2026-08-13 |

This is an off-board purchase line in `outputs/slate113-mk1-bom.csv`; no schematic field was modified while KiCad is open.

## 2026-08-13 — JLC-priced outstanding parts

| Refs | MPN | LCSC | Unit price | Extended |
|---|---|---|---:|---:|
| C82, C233, C234 | CL05B104KB54PNC | C307331 | US$0.0093 | US$0.0279 |
| C85, C232 | 0402CG221J500NT | C39122 | US$0.0062 | US$0.0124 |
| C226 | CC0402JRNPO9BN180 | C106202 | US$0.0061 | US$0.0061 |
| C230 | CC0402JRNPO9BN120 | C106201 | US$0.0038 | US$0.0038 |
| C231 | 0402CG6R8C500NT | C1576 | US$0.0067 | US$0.0067 |
| R124 | 0603WAF1002T5E | C25804 | US$0.0084 | US$0.0084 |
| L1 | FEXL0530A-4R7M | C5378513 | US$0.6635 | US$0.6635 |
| Y2 (rename pending saved schematic as X1) | X322525MOB4SI | C9006 | US$0.0945 | US$0.0945 |

Subtotal: **US$0.8233**. Prices are JLC CLI live lookups on 2026-08-13. WG243 search result C9900172652 is zero stock, therefore excluded.

## 2026-08-13 — WG243 vendor cost

| Item | Amount | Note |
|---|---:|---|
| SkyLab WG243 combo module (U70) | US$7.98 | User vendor quote |
| Shipping | US$5.32 | DDP excluded |
| **Subtotal before DDP** | **US$13.30** | |

## 2026-08-13 — passives and radio reset/boot switches

| Refs | Resolution | Footprint | Source |
|---|---|---|---|
| R25, R31-R33, R36-R37, R76, R102, R130-R131 | 10kΩ 1%, UNI-ROYAL `0603WAF1002T5E` | `Resistor_SMD:R_0603_1608Metric` | LCSC `C25804` |
| R103 | 100kΩ 1%, UNI-ROYAL `0603WAF1003T5E` | `Resistor_SMD:R_0603_1608Metric` | LCSC `C25803` |
| R101 | 20kΩ 1%, Vishay `CRCW060320K0FKEA` | `Resistor_SMD:R_0603_1608Metric` | LCSC `C844923` |
| C34, C62, C158-C164, C212, C214, C218, C220-C225 | 100nF 50V, Samsung `CL10B104KB8NNNC` | `Capacitor_SMD:C_0603_1608Metric` | LCSC `C1591` |
| C61, C165, C216 | 10uF 16V X5R, CCTC `TCC0603X5R106M160CT` | `Capacitor_SMD:C_0603_1608Metric` | LCSC `C380317` |
| C227 | 18pF C0G, Yageo `CC0402JRNPO9BN180` | `Capacitor_SMD:C_0402_1005Metric` | LCSC `C106202` |
| SW3, SW4 | ESP reset/boot buttons, C&K `KMR231GLFS` | `slate113:KEY-SMD_KMR2XXGXXX` | LCSC `C99271` |
| C235 | 220uF 6.3V polymer, Chemi-Con `APXF6R3ARA221MF61G` | deliberately blank: exact 6.3mm-can land pattern still needs a verified footprint | DigiKey `565-3163-1-ND` |

`U16` is absent from the saved hierarchy. `U70` remains intentionally footprint-blank for AJ's project-local WG243 footprint. `Y2` remains blank because its two-pin symbol cannot be safely assigned the previously considered four-pad crystal footprint.

| References | MPN | Supplier P# | Verification |
|---|---|---|---|
| U38 | X4C60K1-20SR | DigiKey `1173-X4C60K1-20SRTR-ND` | DigiKey live product record |
| U39 | XEC24P3-30GR | DigiKey `1173-XEC24P3-30GRTR-ND` | DigiKey live product record |
| J6 | 395-016-520-202 | DigiKey `151-395-016-520-202-ND` | DigiKey live product record |
| L2, L4 | SPM6530T-1R0M120 | LCSC `C87572` | `jlc info C87572 --json` |
| L3 | SPM6530T-100M | LCSC `C112288` | `jlc info C112288 --json` |
| SW1, SW2 | KMR231GLFS | LCSC `C99271` | `jlc info C99271 --json` |

Already verified and retained: the SK9822-EC20 LED chain uses LCSC `C2909059`.

Deliberately left without a supplier P# pending a part-level decision rather than a guessed fit: U16 AMLGA7921, U70 SkyLab WG243, Y2 (two-pin symbol versus available four-pad crystal), the unannotated LED bulk capacitor C?, generic SW3/SW4, IO L1, and passives with no selected package/voltage class.

Validation: `python3 -B /tmp/regen_bom.py` completed and `kicad-cli sch export netlist slate113.kicad_sch -o /tmp/slate113-post-source.net` passed.
