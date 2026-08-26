![Slate113 Mk1](./Assets/Logo/logo_slate.png)

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC_BY--NC--SA_4.0-blue.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

# Slate113 Mk1

## Overview

Slate113 Mk1 is a Beefy Phone-Like Cyberdeck, powered by the [ArmSOM CM5](https://www.armsom.org/product-page/cm5?variantId=052f14c0-9009-4c4c-8e45-79380a8dca78), and meant to be a more capable and feature-rich alternative to the Flipper One.

## Inspired By
[Pi Flux by Carbon Computers](https://carboncomputers.us/products/pi-flux) and the [Flipper One by Flipper Devices](https://blog.flipper.net/flipper-one-we-need-your-help/)

## Features
- DP Alt Mode
- ESP32 Co-Processor
- NFC via PN7160
- RFID via EM3095
- Sub-GHz via CC1101
- BadUSB
- Wi-Fi 6/6E and BLE 5.2
- 6 SMAs (Interchangable between GPS, WIFI, Sub-GHz, BLE, and LTE)
- SlateConnect (Custom Board-Edge Connector System)
- GNSS w/ IMU
- Cellular Modem (via M.2 B-Key Slot)
- Stereo Bottom Firing Speakers (w/ Amps)
- MEMS Microphone
- Side Mounted Customizable Adressable RGB LED Strip

## Sheets¹

### Main Board

![Main_Board](./Assets/Sheet%20Pictures/Main_Board.png)

Sheet BOM [here](./Manufacturing%20Files/BOMs/Per%20Sheet/slate113-mk1_main_board.csv)

---

### IO

![IO](./Assets/Sheet%20Pictures/IO.png)

Sheet BOM [here](./Manufacturing%20Files/BOMs/Per%20Sheet/slate113-mk1_io.csv)

---

### Power

![Power Sheet](./Assets/Sheet%20Pictures/Power.png)
![Power 3D Render](./Assets/PCB%20Pictures/Power.png)

Sheet BOM [here](./Manufacturing%20Files/BOMs/Per%20Sheet/slate113-mk1_power.csv)

---

### M.2

![M.2 Sheet](./Assets/Sheet%20Pictures/M.2.png)
![M.2 3D Render](./Assets/PCB%20Pictures/M.2.png)

Sheet BOM [here](./Manufacturing%20Files/BOMs/Per%20Sheet/slate113-mk1_m.2.csv)

---

### Radio

![Radio](./Assets/Sheet%20Pictures/Radio.png)

Sheet BOM [here](./Manufacturing%20Files/BOMs/Per%20Sheet/slate113-mk1_radio.csv)

---

### Antenna Bracket

![AntennaBracket](./Assets/Sheet%20Pictures/AntennaBracket.png)
![AntennaBracket 3D Render](./Assets/PCB%20Pictures/AntennaBracket.png)

Sheet BOM [here](./Manufacturing%20Files/BOMs/Per%20Sheet/slate113-mk1_antennabracket.csv)

---

### SlateConnect

![SlateConnect Sheet](./Assets/Sheet%20Pictures/SlateConnect.png)
![SlateConnect 3D Render](./Assets/PCB%20Pictures/SlateConnect.png)

Sheet BOM [here](./Manufacturing%20Files/BOMs/Per%20Sheet/slate113-mk1_slateconnect.csv)

---

### LED Bar

![LEDBar](./Assets/Sheet%20Pictures/LEDBar.png)

Sheet BOM [here](./Manufacturing%20Files/BOMs/Per%20Sheet/slate113-mk1_ledbar.csv)

---

### PCB(s)²

![PCB](./Assets/PCB%20Pictures/Main.png)

Total BOM [here](./Manufacturing%20Files/BOMs/slate113-mk1.csv)

---

### Total Price Breakdown
---
| Item | Price | Link |
| --- | --- | --- |
| Main Board | USD$14.31 | [BOM](./Manufacturing%20Files/BOMs/Per%20Sheet/slate113-mk1_main_board.csv) |
| IO Board + Flex | USD$85.59 | [BOM](./Manufacturing%20Files/BOMs/Per%20Sheet/slate113-mk1_io.csv) |
| Power Board + Flex | USD$15.81 | [BOM](./Manufacturing%20Files/BOMs/Per%20Sheet/slate113-mk1_power.csv) |
| M.2 Board + Flex | USD$7.23 | [BOM](./Manufacturing%20Files/BOMs/Per%20Sheet/slate113-mk1_m.2.csv) |
| Radio Board + Flex | USD$77.90 | [BOM](./Manufacturing%20Files/BOMs/Per%20Sheet/slate113-mk1_radio.csv) |
| Antenna Bracket | USD$15.17 | [BOM](./Manufacturing%20Files/BOMs/Per%20Sheet/slate113-mk1_antennabracket.csv) |
| SlateConnect + Flex | USD$16.31 | [BOM](./Manufacturing%20Files/BOMs/Per%20Sheet/slate113-mk1_slateconnect.csv) |
| LED Bar Flex | USD$7.39 | [BOM](./Manufacturing%20Files/BOMs/Per%20Sheet/slate113-mk1_ledbar.csv) |
| Display | USD$55.49³ | [Alibaba Link](https://www.alibaba.com/product-detail/Industrial-5-5inch-Touch-Screen-720_1601790231031.html?spm=a2756.order-detail-ta-ta-b.0.0.fb3ef19cmzzMxB) |
| PCBs | ~USD$531⁴ | [JLCPCB](https://jlcpcb.com/) |

**Estimated Total**: US$971.53–1,286.53

---

## Fineprint

¹Certain Sheets aren't included here, such as the Slate113 Sheet, as it's the root sheet, and has nothing, and the flex sheets (excluding the LED Bar Flex), as they are just two of the same connectors.

---

²Not Done at the time of writing this.

---

³Includes SHipping and DDP

---

⁴Estimate, as all PCBs haven't been made yet.

---

⁵All parts haven't been finalized, including items like enclosure, batteries, and others; subject to change
