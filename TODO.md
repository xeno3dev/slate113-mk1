# Slate TODO

## ArmSoM-CM5 IO USB-C correction — before rerouting

Supersedes the earlier external-mux review and Raspberry Pi CM5 interpretation. Saved schematic netlists and ArmSoM reference schematics have now been checked. Circuit changes remain for Aylon to implement.

- [ ] Make In1.Cu continuous GND for the calculated F.Cu widths, or recalculate the actual plane arrangement. In2.Cu GND is L3, not calculator L2.
- [ ] Replace U7/U12/U15 topology with native ArmSoM four-pair USB3/DP and direct AUX wiring. Remove only their unused support circuits.
- [ ] Add missing module TX1 pins 152/154 and RX1 pins 158/160 paths; retain TX2 104/106 and RX2 146/148. Separate RX2P from RX1P.
- [ ] Follow ArmSoM carrier mapping and four 100 nF TX coupling capacitors; AUX pins 164/166 go to SBU1/SBU2.
- [ ] Move Type-C USB2 away from U18 downstream pins 25/26 to module OTG0 pins 105/103.
- [ ] Fix U1 VDD pins 3/4 direct to 3V3; C1/C2 decouple to GND. Route U1 INT pin 5 to module pin 58; fix USBC1_INT_L versus USBCC_INT_L label mismatch. Provide VCONN supply/decoupling for powered cables.
- [ ] Fix U14 DC power wiring: IN 5/6 direct to regulated 5V; OUT 1/2 direct to USB1_VBUS; C32/C33 shunt to GND, not in series.
- [ ] Provide current-limited, protected Type-C VBUS source control under native OTG/TCPM. Disconnect U14 EN from hub PWREN2J. Module pin 45 currently WIFI_CTRL; relocate that control if using native OTG0_PWREN_H.
- [ ] Fix U17 series power capacitors: IN 5/6 direct 3V3, OUT 1/2 direct WIFI_CAPS, C42/C43 decouple to GND.
- [ ] Upgrade IO interconnect/add dedicated high-speed flex for missing pairs, USB2, interrupt, VBUS enable and adequate grounds; calculate its actual flex geometry separately.
- [ ] Reroute native USB3/DP at 95 ohm; USB2 at 90; AUX/PCIe REFCLK/DSI/Ethernet MDI at 100; PCIe data at 85. New assignments are saved; existing copper was not changed.
- [ ] Configure FUSB302/TCPM, DP Alt Mode, native PHY orientation/mode switching and USB OTG role control in the board device tree.
- [ ] Run ERC, update PCB, refill zones, run DRC; check pair skew and complete connector/flex paths; test both cable orientations and USB/DP modes.

Detailed pin mapping and rerouting list: C:/Users/Aylon/Documents/Codex/2026-10-02/how/outputs/slate-armsom-usbc-change-list.md
Companion net-by-net list: C:/Users/Aylon/Documents/Codex/2026-10-02/how/outputs/slate-differential-rerouting.md

Status: netclass assignments corrected and verified. Schematic/PCB circuit edits and final ERC/DRC remain pending. Reference hardware checked: ArmSoM CM5 / CM5-IO V1.1; confirm purchased module revision before fabrication.
