---
title: "Slate113 MK1"
author: "Aylon Johnson"
description: "Slate113 Mk1 is a Beefy Phone-Like Cyberdeck, powered by the [ArmSOM CM5](https://www.armsom.org/product-page/cm5?variantId=052f14c0-9009-4c4c-8e45-79380a8dca78), and meant to be a more capable and feature-rich alternative to the Flipper One."
created_at: "2026-07-09"
---

# July 8: The Beginnings...

![image](https://cdn.hackclub.com/019f409b-5131-7b3c-8cb0-b96994d38a39/1783495345806657641.png)
![image](https://cdn.hackclub.com/019f409b-9866-7853-9312-fc8e59a8d696/1783495361167186329.png)

**Why Slate**
I decided to build Slate because I've always wanted something like the Flipper Zero, but was never able to get one. So, despite how hard and expensive it is to get SoMs/SBCs due to the RAM shortage, I've decided to make my OWN Layer One AND Layer Zero Pentesting Device. It will have Linux, a coprocessor, M.2 Expansion, Ethernet Ports, the entire list of things the Flipper One will have, plus some extras, like a Snap On Addon-System.

**Devlog One (Quick One)**
As the starting point of this project, I decided to work on the Power System, and am almost done with it. I just need to fix a few wiring issues, and fix countless issues related to the Battery Boost IC, as I need to fix a few issues with the capacitors used, polarity, and overall for the power tree, start connecting it to the other boards and sections.

**Timelapses**
Video: Timelapse #1: [link](https://cdn.hackclub.com/019f40ac-bddb-7a27-b3a3-3d11d2861776/timelapse_recording_2026-07-07_22-59-48.mp4)
Video: Timelapse #2: [link](https://cdn.hackclub.com/019f41eb-ce91-7891-b4af-4a7b57797483/timelapse_recording_2026-07-08_00-46-15.mp4)
Video: Timelapse #3: [link](https://cdn.hackclub.com/019f40ad-fbb8-72db-bb06-92e5782ad97f/timelapse_recording_2026-07-08_01-09-29.mp4)

Lapse Broke On Me :(

**Total time spent: 1 hour**

# July 9: ERC and Improper Symbols

**What was done**
For this session, all I did was go through DRC issues, and fix mistakes made while wiring, as well as add PWR_FLGs.

**Main Issue**
When I was fixing the ERC Errors I cam upon this one prominent issue related to the FETs. They we giving me an error on the gate pins saying the following:

![image](https://cdn.hackclub.com/019f4465-d221-73cf-8422-d9f1e703218c/1783558942681760721.png)

At first my dumb ahh thought it was an issue related to the pin(s) not being connected. I was wrong. Every time I deleted and replaced the FETs or removed the Global Net Label, the ERC Error would switch to the OPPOSITE FET. I tried several fixes before ***eventually*** realizing it was most likely an issue with the symbol; boy was I ***RIGHT!*** When I tell you all they did was just place the component outline and pins, that's all they did. The PINS weren't even configured.

**Fix**
I ended up changing this:

![image](https://cdn.hackclub.com/019f446b-5a33-76ae-b196-ab402e22deef/Screenshot%20from%202026-07-08%2015-58-54.png) 

To this:

![image](https://cdn.hackclub.com/019f446b-c5e6-71ed-ae9d-7bb0f72032bf/Screenshot%20from%202026-07-08%2015-59-04.png)

Which fixed the entire situation.

**What's Next**
I will be starting work on the Carrier Board tomorrow, which shouldn't be that hard, and literally just some GPIO pins and ports.

**Total time spent: 1 hour**

# July 10: Wiring and Boost Converters

**Work Done**
Today was a bit more productive, I was able to start working on wiring the CM5 Carrier Board/Main Board, right after adding a 5V Boost Converter I forgot. I added the two 100P Connectors and started wiring it to the Power Tree, as well as wiring up several other ports up, like:

- USB A
- Micro SD
- M.2 B-Key Slot

With the B-Key being partially wired (PCIE wired, USB not). I almost used M-Key for this just for convenience and how much more it was supposedly used, but ended up with B-Key for LTE, Satellite, and more capabilities.

**Timelapse**
Video: Timelapse #4: [link](https://cdn.hackclub.com/019f49a3-20a2-7500-93b7-c8d6d9a0f06e/timelapse.mp4)

**Total time spent: 1 hour**

# July 12: USB and More USB

**Work Done**
I added a USB Hub to the schematic and wired it up, as well as wire up a nano sim slot, and finish up wiring the M.2.

Video: Timelapse #5: [link](https://cdn.hackclub.com/019f5476-4859-70de-bd7f-614d8edeece7/timelapse.mp4)

**Total time spent: 1 hour**

# July 13: CM5 gets Data

**What was done**
I finished wiring the CM5 Connector to the current placed components, fixed some issues missed in the power tree, and added the ethernet port and wired it up.

Video: Timelapse #6: [link](https://cdn.hackclub.com/019f590a-e018-79a5-91ce-3e56cb04b021/timelapse.mp4)

**Total time spent: 1 hour**

# July 14: Communication Initialized

**What was done**
I started work today on the board to board FPC connectors, as well as organize the schematics.

Video: Timelapse #7: [link](https://cdn.hackclub.com/019f62ca-fd6f-7296-8bf4-bf5947586010/timelapse.mp4)

**Total time spent: 1 hour**

# July 15: More Connecting and Wiring

**What Work Was Done**
Today, I started working on migrating from the USB 2.0 Hub I had to a USB 3.1 Hub. I ended up having to do this due to the MT7921AUN requiring USB 3.0 SS (SuperSpeed), so I had to sadly move from my simple hub to this goliath of a hub:

![image](https://cdn.hackclub.com/019f679f-fc3d-7f08-877d-10bf4b68c01c/Screenshot%20from%202026-07-15%2015-24-54.png)

I also ended up realizing that I had to move my Data + DP port from the power board to my IO board due to: 1.) It doesn't belong there, and 2.) I need the SS ports for the new Hub

I also created a simple schematic for my custom Tri-Direction FPCB Setup, as some signals between the dedicated m.2 board, io, AND carrier boards need to communicate between each other:

![image](https://cdn.hackclub.com/019f67a3-8570-7845-852b-ff8a8a11ec73/image.png)

**Timelapse**

Video: Timelapse #8: [link](https://cdn.hackclub.com/019f67a4-22e2-71b1-9c33-ab5ef81e8cb7/timelapse_recording_2026-07-15_13-16-36.mp4)

**Total time spent: 1 hour**

# July 16: Mux'n

**What Work Was Done**
Today I finished wiring up the new USB Hub, and added a USB Mux for the Data USB-C Port.

**Problems Encountered**
While wiring up the Mux, halfway through I realized that DP Alt Mode wouldn't work at all, because if I finished up with just the current mux I was working with atm, and didn't do anything else... DP Alt wouldn't work altogether. The reason why this happens is due to the two modes that the port can be in, and the locations the SS lines need to go to:

1.) USB: Regular Data Operations: 3.1 USB Hub
2.) DP Alt Mode: ***CM5***

Because of this, in short, I need to add a 2:1 SS mux between the first mux, and the CM5/3.1 Hub.

**Pictures**

![image](https://cdn.hackclub.com/019f6d1c-2257-76f2-9e33-1357a2a94296/image.png)
![image](https://cdn.hackclub.com/019f6d1c-3e5a-759d-b868-c1c82330666f/1784241992959118164.png)

**Timelapse**
None today sadly as Lapse decided to pause at 10 Minutes in, while not visually showing it, and I never realized.

**Total time spent: 1 hour**

# July 17: Mux or Not To Mux

**What Work Was Done**
I got the mux situation in line, and went with the PI3USB302-AZBEX 1:2 mux, placed it between HD3SS3220 and the VL817/CM5 DP lanes, addded an SBU Router, and was going to do WiFi and BLE Combo today, but ended up in a FCC rabbit hole 🫩

**Pictures**
![image](https://cdn.hackclub.com/019f723c-6342-7af8-99a5-aeecfccc84f8/image.png)

**Timelapse**
Video: Timelapse #9: [link](https://cdn.hackclub.com/019f723d-169a-7a61-b152-59fe4e85bf2a/timelapse_recording_2026-07-17_12-33-36.mp4)

**Total time spent: 1 hour**

# July 18: Nearing Completion (Somewhat)

**What work was done**
Today I made the symbol for the WIFi + BLE Combo Card, as well as wire up up, update all the connectors to use accurate pin counts, switch to slimmer B2B Connectors as the prev one I had would take up too much space, as well as ditch the 3 Way Flex Cable.

**Pictures**
![image](https://cdn.hackclub.com/019f776f-325b-7990-9b93-73dc77159d4b/image.png)
![image](https://cdn.hackclub.com/019f776f-57bb-75f1-983c-7fa8ed81cba3/image.png)
![image](https://cdn.hackclub.com/019f776f-8927-76f0-a667-4818ac510d3f/image.png)
![image](https://cdn.hackclub.com/019f776f-db39-7af9-ae34-cf94e49c1073/image.png)

**Timelapse**
Video: Timelapse #10: [link](https://cdn.hackclub.com/019f7b7f-10b1-7c74-b3f1-37939690a9ec/timelapse_since_2026-07-17_20-00.mp4)

**Total time spent: 1 hour**

# July 19: ERC Time!

**What work was done**
I wired up the DP Lines to the CM5 and fixed a plethora of DRC errors, with most of them being bloody "Output -> Output" or "Power Input isn't connected to Power Output" errors.

**Timelapse**
Video: Timelapse #11: [link](https://cdn.hackclub.com/019f7c8e-346b-7d6c-ada4-9ddd66274d07/timelapse_since_2026-07-19_new.mp4)

**Total time spent: 1 hour**

# July 20: Radio Started. Over.

**What work was done**

I started work on the Radio Board today, and specifically wired up the RP2350B completely (except for USB DP/DM), and started wiring up the CC1101.

**Timelapse**
Video: Timelapse #12: [link](https://cdn.hackclub.com/019f81b2-d924-7ef3-83f0-51ea41dd4f03/timelapse_recording_2026-07-20_16-08-46.mp4)

**Total time spent: 1 hour**

# July 21: GPS and Sub-GHz will see the light of day

**What Work was Done**
Today, I finished wiring up the CC1101, and made a big decision on how Sub-GHz will work today

**Problems Encountered**
The way I was going to wire up the Radio Module (containing GPS and Sub-GHz) involved there being ***two*** SMA Ports, on top of the one I decided to allocate to GPS. As a cost, and space saving decision, I decided to go with the following plan, instead of using two antennas:

Instead of having two antennas on the system for both Sub-GHz bands intended to be implemented into Slate113 (433MHz + 868/915MHz), it will have one Balun tuned to 868/915MHz, and one SMA Port. The CC1101 will be controlled via software to switch between focusing on 433MHz OR 868/915MHz. Although the 433MHz capabilities will be degraded, it still will work somewhat, and unless I come up with another way to make it work flawlessly for both, this is the sad reality.

On top of that, I forgot to add this into yesterday's devlog, but I realized that I needed to have a USB-C/USB Port for BadUSB to work properly. I was considering to make the data port on IO act as the BadUSB Port when that was running, but I'm considering adding a third USB-C port now.

**Pictures**
![image](https://cdn.hackclub.com/019f86e1-2355-77ef-a111-c25d39ec1a25/image.png)
![image](https://cdn.hackclub.com/019f86e1-d43a-7860-82c8-00c158fa312e/image.png)
![image](https://cdn.hackclub.com/019f86e2-11ce-7424-8078-b33a165b5a4f/image.png)

**Total time spent: 1 hour**

# July 22: Sub-GHz Problems

**What Work was Done**
I worked more on Sub-Ghz today and found a workaround to make ALL three/four bands to work, with (in theory) good preformance. I also started wiring up NFC.

**Problems**
**Balun'ing**
Yesterday, I had decided to just use a Balun meant for 868/915MHz, I discovered with enough switches, 2 Baluns for 868/915MHz and 433MHz, and a makeshift Balun tuned to 315Hz made from Inductors and Capacitors, I could capture ALL three major bands used from one SMA, with the only catch being you had to switch antennas depending on which of the 3 bands u wanted to capture.

**Flash**
I also ended up solving the BadUSB Problem from yesterday by simply adding a new USB-C Port, and after that, a new problem arose; how would I flash the RP2350? At first, I was intending to just wire up the Reset, Boot, etc. pins to the CM5 to easily be able to flash the MCU during OTA Updates. With the USB Pins on the MCU being wired up for BadUSB, it would make it a bit harder to flash it. I ended up going for a software OTA System, which uses UART/I2C to send a signal to the RP2350B that "It needs to be updated!" It then finishes up all processes, receives the update via UART, and put's it on one of it's "A/B Partitions" on it's flash, verifies the update, and reboots to the new part, and uses the old one in case of an emergency or it corrupt during transit.

**Pictures**
![image](https://cdn.hackclub.com/019f8c0a-d0fb-7867-965f-a1ee46c92048/1784760941879171594.png)

**Timelapse**
Video: Timelapse #13: [link](https://cdn.hackclub.com/019f8c0e-bc87-7bae-816e-367ee146a7c2/timelapse_merged.mp4)

**Total time spent: 1 hour**

# July 23: NFC and RFID Time

**What Work Was Done**
Today, I switched to a new NFC IC, Wired up the RFID IC, and found a problem that will delay me finishing the schematic.

**Problems**
I'm gonna keep this short, the NFC + RFID IC/Coils can't be wired in full (yet) due to the RFID Coil requiring the Q (quality factor) for a calculation, and the same thing for NFC, but for La and Ra (inductance and series resistance). This means I can't finish the radio board until I get those two coils.

**Timelapse**
Video: Timelapse #14: [link](https://cdn.hackclub.com/019f9116-7740-7642-b358-225b89b049a3/timelapse_recording_2026-07-23_12-18-15.mp4)

**Total time spent: 1 hour**

# July 25: CAD Time!

**What Work Was Done**
Yesterday and today, I worked on mocking up the enclosure to see what may or may not be too big, what I can still add, and what has to change.

**Problems Encountered**
**BIG BACK**
When I started modeling this in Fusion, after making a very basic model of the battery, I realized that the battery was a bit... thicker than expected. Although I wanted to make this as slim as possible, I decided to keep the battery I had decided to use for this (10,000 mAh) and just take the ~10 mm thickness increase.

**Pictures**
![image](https://cdn.hackclub.com/019f9b03-bb43-779b-9389-6a140d6e0a19/1785012132021885032.png)
![image](https://cdn.hackclub.com/019f9b08-355d-7dab-98c4-ac90f44e1708/image.png)

**Timelapses**
Video: Timelapse #15: [link](https://cdn.hackclub.com/019f9b2c-40a8-76b4-84ee-6805ac5900e7/timelapse_since_2026-07-23_12-16_1of2.mp4)
Video: Timelapse #16: [link](https://cdn.hackclub.com/019f9b2c-f594-7f81-9407-04e0e323902b/timelapse_since_2026-07-23_12-16_2of2.mp4)

**Total time spent: 1 hour**

# July 26: Location Acquired

**What Work Was Done**
Today I went back to Schematic Work and continued working on the Radio Schematic, specifically the GPS Part, which was the last part needed, closing it out (right after I finish the natenna placeholder stuff)

**Timelapse**
Video: Timelapse #17: [link](https://cdn.hackclub.com/019fa056-0363-7aa1-a1e0-004a0743cc0e/timelapse_since_2026-07-26_15-35.mp4)

**Total time spent: 1 hour**

# July 27: Closed Out

**What Work Was Done**
I finished up the Radio Board, added 2 Load Switches, and fixed an issue related to the wrong B2B connector being used on the flex and boards, in addition to adding the Flash for the RP2350B

**Timelapse**
Video: Timelapse #18: [link](https://cdn.hackclub.com/019fa59e-9dc5-71a0-9739-8a9648e0e136/timelapse_since_2026-07-26_19-32.mp4)

**Total time spent: 1 hour**

# July 28: RF Sense

**What Work Was Done**
Today, I started work on the Antenna Module (Top Sub Board that just converts SMA to U.FL for internal component use) and started work on "RF Sense".

**RF Sense**

RF Sense is what I'll use to automatically switch between the internal patch antenna and an external SMA Antenna, on both the WiFi and BT diversity paths.

A directional coupler sits inline on each SMA feed line, continuously sampling a tiny fraction of whatever's traveling backward; from antenna towards the radio chip. That sample feeds into an AD8317 log detector, which converts it into a DC voltage, and then an LM339 comparator thresholds that voltage into a clean digital signal the CM5 can read. Depending on what the CM5 reads, it does the following:

- Low reflection (external SMA antenna present, properly matched) > detect signal flips > 2:1 switch routes the diversity antenna path to the SMA jack, improving TX + RX when an external antenna is attached.

- High reflection (SMA line open, nothing attached) > detect signal flips back > switch reverts to the internal patch antenna.

The primary antenna on each radio stays hardwired to its onboard patch regardless; however RF Sense only governs the second (diversity/ANT1) antenna path. (PS: There are two antenna patches EACH for WiFi and Bluetooth)

**Timelapse**
Video: Timelapse #19: [link](https://cdn.hackclub.com/019fab20-5164-750b-8316-fad0dd421261/timelapse_since_2026-07-27_18-04.mp4)

**Total time spent: 1 hour**

# July 30: IO Closed Again, Back To M.2

**What Work Was Done**
Today I finished up RF Sense, closing out the IO Board for the x2 time, and started work on the Audio System, as well as figured out a problem with the LTE Module I have decided to base LTE Support on this for.

**Problems**

**GPIO Mix-Match**
After finishing up working on the RF Sense system, I started work on the... Audio System! As part of the work on this, I also decided to also hook up PCM, or the ability to make Voice Calls. At first, I had just wired up everything as it was supposed to be wired, then realized, the GPIO, Config, AND I2C would possibly interfere with any other bloody M.2 B-Key Cards someone would plug into this, hence why I took LONGER wiring up THREE SPDT switches JUST to prevent short circuiting M.2 Cards.

**Timelapse**
Video: Timelapse #20: [link](https://cdn.hackclub.com/019fb112-6182-7cb7-8822-5b7983d38521/timelapse_since_2026-07-29_17-21.mp4)

**Total time spent: 1 hour**

# July 31: Audio

**What Work Was Done**
Today I continued wiring up the Audio Subsystem and am almost done, and now just need to wire up everything to the CM5, and update the M.2 Connector (as part of the components are on the M.2 Sub Board)

**Problems Encountered**
**Speakers**
When looking for what speakers to use in this, I ended looking and searching through LCSC/Mouser/DigiKey, trying to find a Phone-Style Speaker (with the Port Location being on the Side) for 2 hours, as they barely exist, and I needed a specific kind. I ended up making Claude use Firecrawl and search and find one, and it did.

**Timelapse**
Video: Timelapse #21: [link](https://cdn.hackclub.com/019fb652-4ced-7b32-b7ab-b60cb094626a/timelapse_since_2026-07-30_12-23.mp4)

**Total time spent: 1 hour**

# August 1: Audio and SIM Expansion

**What Work Was Done**
Today I added an LDO for the Audio Subsystem, wire everything up to the GPIO, wired up a new SD/Sim Card Slot, and finished up the changes required on M.2/Audio, and can now move on to working on Slate Connect.

**Timelapse**
Video: Timelapse #22: [link](https://cdn.hackclub.com/019fbd5b-2171-7fe3-b74c-630b3bf08881/timelapse_since_2026-07-31_10-15.mp4)

**Total time spent: 1 hour**

# August 3: SlateConnect Down (almost)

**What Work Was Done**
Today, I work on and finished SlateConnect (except for the I2C Part)

**Timelapse**
Video: Timelapse #23: [link](https://cdn.hackclub.com/019fc673-d7b9-7834-b83f-3cbeed27a587/timelapse_since_2026-08-03_00-07.mp4)

**Total time spent: 1 hour**

# August 4: Plenty Down, One More To Go

**What Work Was Done**
Today, I FINALLY got down to the last thing i needed to finish for Slate, the LED Status Bar. I finished the last item from SlateConnect today (I2C GPIO Expander Addition), and wired up the display. Tomorrow I will be finishing up the Status LED Bar and running DRC, then assigning footprints and preparing for me to start work on the PCB.

**Timelapse**
Video: Timelapse #24: [link](https://cdn.hackclub.com/019fce43-aa56-75e4-95f3-793cb3441164/timelapse_since_2026-08-03_11-39.mp4)

**Total time spent: 1 hour**

# August 5: Tiring Work.

**What Work Was Done**
Today I fixed all DRC errors, and I have started making the BOM, assigning Footprints, and Making Footprints... i still have to go through ~200+ components out of over 500, assign LCSC/Digikey P#s, fillout missing fields, and whatnot, then i can start working the PCB.

**Timelapse**
Video: Timelapse #25: [link](https://cdn.hackclub.com/019fd2f5-bc21-7f17-a006-c62d8f45f734/timelapse_since_2026-08-04_11-20.mp4)

**Total time spent: 1 hour**

# August 7: Assigning More Footprints and Stuff

**What Work Was Done**
Today, I continued assigning Footprints and MPNs, and am almost done with the BOM and Footprint work.

Video: Timelapse #26: [link](https://cdn.hackclub.com/019fda3c-0100-7503-89d9-d974f94ecedc/timelapse_since_2026-08-05_22-56.mp4)

**Total time spent: 1 hour**

# August 8: BOM Completed

**What Work Was Done**
Today I finished the BOM, and started adding missing Footprints/Making Them. I also have to find and replace 20 Discontinued Parts, on top of the 10 I already replaced.

**Timelapse**
Video: Timelapse #27: [link](https://cdn.hackclub.com/019fdf11-b633-7b83-892d-72dd336d0c3e/timelapse_since_2026-08-07_20-17.mp4)

**Total time spent: 1 hour**

# August 8: Footprints...

**What Work Was Done**
Today, I continued importing missing footprints, and started making some.

**Problems Encountered**
While making the SIM Footprint, I ended up realizing one of the crucial dimensions weren't there, after almost finishing it. I ended up switching to a different SIM Slot, and guess what, the appropriate footprint was already in my LIBRARY. Great waste of time...

(Note: I ended up switching from the 3in2 SIM/SD Card Module I was using to 2 separate modules.) 

**Timelapse**
Video: Timelapse #28: [link](https://cdn.hackclub.com/019fe3cc-494c-7ab4-9b61-a2e2fd1ab261/timelapse_since_2026-08-08_13-12.mp4)

**Total time spent: 1 hour**

# August 10: Component Swap.

**What Work Was Done**
Today, I finished working on Footprints and started replacing components for their replacements (Due to: A.) Being Out Of Stock, B.) Wiped Off DigiKey/LCSC, or C.) Discontinued). For example:

- GPS Module
- RP2350B
- USB Hub
- + more

**Timelapse**
Video: Timelapse #29: [link](https://cdn.hackclub.com/019fe91c-bc2f-7a9e-b2f0-698b4a4da34a/timelapse_since_2026-08-09_01-41.mp4)

**Total time spent: 1 hour**

# August 11: USB Hub Done (Again)

**What Work Was Done**
I wired up the the USB Hub, a flash chip for it, and removed a few stale nets.

**Timelapse**
Video: Timelapse #30: [link](https://cdn.hackclub.com/019feead-11e6-720d-a34e-1eb31486fd3e/timelapse_since_2026-08-10_11-05.mp4)

**Total time spent: 1 hour**

# August 12: Done, at LAST

**What Work Was Done Today**
Today, I FINISHED working on the schematic, and now I just need to audit all the schematics. 

**ERC Misclick**
While updating some symbols, I accidentally clicked Update All Symbols, causing a LOT of ERC errors due to unconnected pins, and more. Took me ~5 mins to fix it all.

**Timelapse**
Video: Timelapse #31: [link](https://cdn.hackclub.com/019ff3d1-6480-7674-9577-e9751466338a/timelapse_since_2026-08-11_12-51.mp4)

**Total time spent: 1 hour**

# August 13: PCB At Last!

**What Work Was Done**
Today, I finished the Schematic Work at LAST and now I can start working on routing the PCB once i assign a few more components their MPNs, and Footprints...

**Pictures (of three biggest sheets)**
![sheet](https://cdn.hackclub.com/019ff8e8-9c05-7bf1-947e-6aca0eb36370/1786587409141181569.png)
![sheet](https://cdn.hackclub.com/019ff8e8-9f89-7af6-80a9-55b0e8debb18/1786587411081069463.png)
![sheet](https://cdn.hackclub.com/019ff8e8-a309-73bc-a7b7-deff47bb0c83/1786587412921297256.png)

**Total time spent: 1 hour**

# August 14: Routing Started

**What Work Was Done**
Today, I finished up a few final changes and got to work on the PCB! I set up the board layers and set it to 6, with the first two being GND and Power.

**Timelapse**
Video: Timelapse #32: [link](https://cdn.hackclub.com/019ffdcc-a64c-7745-a71a-6c325ed7daf9/timelapse_since_2026-08-13_11-37.mp4)

**Total time spent: 1 hour**

# August 15: Complexity

**What Work Was Done**
Today I finished wiring up the Power Mezzanine and now I have started working on the IO Mezzanine. It got so complicated I had to start using Micro Vias AND make the board 8 layers, from the initial 6 + it's so jampacked around the connectors it's become an eyesore.

**Timelapse**
Video: Timelapse #33: [link](https://cdn.hackclub.com/01a00317-9c77-7cf0-bb05-6c8f7491d08c/timelapse_since_2026-08-14_11-57_part-1.mp4)
Video: Timelapse #34: [link](https://cdn.hackclub.com/01a00323-48b4-78c5-9ef7-78036b50775a/timelapse_since_2026-08-14_11-57_part-2.mp4)

**Total time spent: 1 hour**

# August 16: More Complexity

**What Work Was Done**
Today, I couldn't do much do to personal reasons, but I finished up the IO Port, and started work on the SlateConnect mezzanine.

**Pictures**
![image](https://cdn.hackclub.com/01a00be9-9998-777f-9db6-b6a58d2d4165/image.png)

**Timelapse**
Video: Timelapse #35: [link](https://cdn.hackclub.com/01a00bea-0cb7-7fa3-b0d8-e211283a013f/timelapse_since_2026-08-15_10-50.mp4)

**Total time spent: 1 hour**

# August 18: Move To M.2

**What Work Was Done**
Today I continued working on the Carrier Board, and started working on the M.2 Board, as I js wanted a break from the Carrier.

**Timelapse**
Video: Timelapse #36: [link](https://cdn.hackclub.com/01a01232-8a23-7de1-af61-dcff5c022341/timelapse_since_2026-08-17_13-33.mp4)

**Total time spent: 1 hour**

# August 19: M.2 Done

**What Work Was Done**
Today I finished up the M.2 Board, and setup the Pours

![image](https://cdn.hackclub.com/01a017ca-1060-7cd6-8889-99d02fe66591/shot-20260818-213314.png)

Tomorrow, I'll just move onto the next easiest board.

**Timelapse**
Video: Timelapse #37: [link](https://cdn.hackclub.com/01a017cb-4110-76a9-9379-77de3b7122c0/timelapse_since_2026-08-18_11-51.mp4)

**Total time spent: 1 hour**

# August 20: Power AND Antenna Bracket Done

**What Work Was Done**
Today was very productive. I completed the Antenna Bracket AND Power Board :D

![image](https://cdn.hackclub.com/01a01d60-d745-7eef-ac14-3d245a0d77b3/shot-20260819-235417.png)
![image](https://cdn.hackclub.com/01a01d61-9500-7cbe-874f-8e5b6fa5065c/shot-20260819-141447.png)

**Timelapse**
Video: Timelapse #38: [link](https://cdn.hackclub.com/01a01d62-6cd5-7f28-9aad-15430278cdf1/timelapse_since_2026-08-19_10-50.mp4)

**Total time spent: 1 hour**

# August 20: SlateConnect Done, 4 More to Go

**What Work Was Done**
Today I completed the SC Board (Board Edge Connector System that's just a replacement for GPIO) and this is how it looks:
![image](https://cdn.hackclub.com/01a0205d-adb9-7121-80ff-5a68b26245c3/shot-20260820-134853.png)
![image](https://cdn.hackclub.com/01a0205d-cde2-7a80-87c8-790d8ee87d53/shot-20260820-134817.png)

**Timelapse**
Video: Timelapse #39: [link](https://cdn.hackclub.com/01a02064-cfc6-7106-a8a1-fdad60f2e3cb/timelapse_since_2026-08-20_11-53.mp4)

**Total time spent: 1 hour**
