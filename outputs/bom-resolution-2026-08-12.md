# BOM source-resolution record — 2026-08-12

Verified and written to the schematic:

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
