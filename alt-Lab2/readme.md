This is an experimental lab where you will make your own Arduino. It has never been tried before! Please help to build out the activity.

## Pre-Lab
Make sure you do the [pre-lab](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/wiki/Alt-Pre---Lab-2) in advance of this activity, and start your writeup by documenting these plans.


## In The Report
For the report, make a copy of this wiki page for your own repository, and then delete everything but the headers and the sections between the **stars**. Write the answers to the questions under the starred sentences. Include snippets of code that explain what you did.

Deliverables are due next Tuesday. Post a link to the wiki page on your main class hub page.
 
## Overview
For this assignment, you are going to 

A) [Design your Arduino+](#part-a-design-your-arduino) 

B) [Order parts for your Arduino+](#part-b-order-parts-for-your-arduino) 

C) [Prototype your Arduino+](#part-c-prototype-your-arduino)

D) [Layout your Arduino+](#part-d-layout-your-arduino) 

E) [Send your board off to be made](#part-e-send-your-board-off-to-be-made)


## Part A. Design your Arduino+

Think of a small (emphasis on small) improvement that can be made to the basic design of an Arduino. For example, you could make an Arduino with a real time clock. Or you could make an Arduino that was laid out in a different shaped board. Please keep your design to be an Arduino *plus one thing*. 

The questions below should help scaffold important considerations when you are making your design. The plan is for this week's lab to be about designing, laying out and sending out the board; if you need to order parts to prototype and test your design before sending out the board, please outline the expected plan.

Use [PCBShopper](https://pcbshopper.com) to look at the trade offs between different quick turn PCB fab shops in time, cost, number of boards, design constraints, etc. Depending on your design needs and risk tolerance, different companies might suit your needs better. 

Please document the design of your Arduino+:

**a) What is the + improvement of your Arduino+**

**b) What Arduino form-factor/design are you basing your design off of?**

**c) What features/parts need to be incorporated for your Arduino+? Include your research!**

**d) What is the timeline for the overall development of your Arduino?**

**e) Which fabrication company are you using, what do you plan to order, and what is the design rationale for the selection?**

## Part B. Order parts for your Arduino+

Develop a bill of materials for your Arduino +.

This is a spreadsheet/table to help you keep tabs on what parts you need to order to populate your board. [Here is an example of a BOM](http://solderpad.com/solderpad/arduino-uno/) for an Arduino Uno, from Solderpad.com. 

The best way to generate the BOM is probably to make an excel file or CSV, and then [use this tables generator website](https://www.tablesgenerator.com/markdown_tables) to convert the input to markdown:

**Bill of Materials**
Use the table below (pre-populated with parts from the Adafruit Metro Mini), or just include a link to a spreadsheet or pdf.

| Part   | Value                 | Device                    |   | Package                | Description                      | Notes                                                                          | Example part                                                                                                                                                                                                                                                                                                                                |
|--------|-----------------------|---------------------------|---|------------------------|----------------------------------|--------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| U2     | ATMEGA328P            | ATMEGA328P                | * | MLF32-TH               | ATMEGA 328P                      | BRAINZ                                                                         | https://www.digikey.com/product-detail/en/ATMEGA328P-MU/ATMEGA328P-MU-ND/1914588/?itemSeq=338642865                                                                                                                                                                                                                                         |
| Y2     | CSTCE16M0V53-R0 16MHZ | RESONATORMU               | * | RESONATOR              |                                  | Set ATMEGA clock speed                                                         | https://www.digikey.com/product-detail/en/CSTNE16M0V530000R0/490-17948-1-ND/8747756/?itemSeq=338642875                                                                                                                                                                                                                                      |
| U3     | CP2104                | CP2104                    | * | QFN24_4MM_SMSC         | CP2104 - USB to UART Bridge      | USB communication with ATMEGA                                                  | https://www.digikey.com/product-detail/en/CP2104-F03-GMR/336-4146-1-ND/7650425/?itemSeq=338642880                                                                                                                                                                                                                                           |
| U1     | MIC5225-5.0           | VREG_SOT23-5              | + | SOT23-5                | SOT23-5 Fixed Voltage Regulators | 5V Voltage Regulator                                                           | https://www.digikey.com/product-detail/en/LP2985IM5-5.0%2fNOPB/LP2985IM5-5.0%2fNOPBCT-ND/334983/?itemSeq=338642872                                                                                                                                                                                                                          |
| U4     | MIC5225-3.3           | VREG_SOT23-5              | + | SOT23-5                | SOT23-5 Fixed Voltage Regulators | 3V Voltage Regulator                                                           | https://www.digikey.com/product-detail/en/LP2985IM5X-3.3%2fNOPB/LP2985IM5X-3.3%2fNOPBCT-ND/3527394/?itemSeq=338642873                                                                                                                                                                                                                       |
| D3     | MBR120                | DIODE-SCHOTTKYSOD-123     | + | SOD-123                | Diode                            | ESD protection for USB port                                                    | https://www.digikey.com/product-detail/en/BAT60AE6327HTSA1/BAT60AE6327HTSA1CT-ND/1557845/?itemSeq=338642881                                                                                                                                                                                                                                 |
| AD     |                 20609 | HEADER-1X6ROUND           | @ | 1X06_ROUND             | PIN HEADER                       | Footprint for pin headers                                                      | https://www.digikey.com/product-detail/en/harwin-inc/D01-9923246/952-2521-ND/3918909?utm_adgroup=Rectangular%20Connectors%20-%20Headers%2C%20Specialty%20Pin&utm_source=google&utm_medium=cpc&utm_campaign=Shopping_Product_Connectors%2C%20Interconnects&utm_term=&utm_content=Rectangular%20Connectors%20-%20Headers%2C%20Specialty%20Pin |
| AD1    |                 20609 | HEADER-1X6ROUND           | @ | 1X06_ROUND             | PIN HEADER                       | Footprint for pin headers                                                      | https://www.digikey.com/product-detail/en/harwin-inc/D01-9923246/952-2521-ND/3918909?utm_adgroup=Rectangular%20Connectors%20-%20Headers%2C%20Specialty%20Pin&utm_source=google&utm_medium=cpc&utm_campaign=Shopping_Product_Connectors%2C%20Interconnects&utm_term=&utm_content=Rectangular%20Connectors%20-%20Headers%2C%20Specialty%20Pin |
| IOL    |                 20610 | HEADER-1X8ROUND           | @ | 1X08_ROUND             | PIN HEADER                       | Footprint for pin headers                                                      | https://www.digikey.com/product-detail/en/harwin-inc/D01-9923246/952-2521-ND/3918909?utm_adgroup=Rectangular%20Connectors%20-%20Headers%2C%20Specialty%20Pin&utm_source=google&utm_medium=cpc&utm_campaign=Shopping_Product_Connectors%2C%20Interconnects&utm_term=&utm_content=Rectangular%20Connectors%20-%20Headers%2C%20Specialty%20Pin |
| POWER1 |                 20610 | HEADER-1X870MIL           | @ | 1X08_ROUND_70          | PIN HEADER                       | Footprint for pin headers                                                      | https://www.digikey.com/product-detail/en/harwin-inc/D01-9923246/952-2521-ND/3918909?utm_adgroup=Rectangular%20Connectors%20-%20Headers%2C%20Specialty%20Pin&utm_source=google&utm_medium=cpc&utm_campaign=Shopping_Product_Connectors%2C%20Interconnects&utm_term=&utm_content=Rectangular%20Connectors%20-%20Headers%2C%20Specialty%20Pin |
| X1     |                 20329 | USB_MICRO_20329_V2        | @ | 4UCONN_20329_V2        | USB Connectors                   | USB connector                                                                  | https://www.digikey.com/product-detail/en/amphenol-icc-fci/10103594-0001LF/609-4050-1-ND/2350357                                                                                                                                                                                                                                            |
| RESET  | KMR2                  | SWITCH_TACT_SMT4.6X2.8    | @ | BTN_KMR2_4.6X2.8       | SMT Tact Switches                | Reset Button                                                                   | https://www.digikey.com/product-detail/en/c-k/KMR211GLFS/401-1426-1-ND/550461                                                                                                                                                                                                                                                               |
| D4     | YELLOW                | LED0805_NOOUTLINE         | ! | CHIPLED_0805_NOOUTLINE | LED                              | Indicator LED                                                                  | https://www.digikey.com/product-detail/en/150080YS75000/732-4987-1-ND/4489925/?itemSeq=338642883                                                                                                                                                                                                                                            |
| D5     | YELLOW                | LED0805_NOOUTLINE         | ! | CHIPLED_0805_NOOUTLINE | LED                              | Indicator LED                                                                  | https://www.digikey.com/product-detail/en/150080YS75000/732-4987-1-ND/4489925/?itemSeq=338642883                                                                                                                                                                                                                                            |
| L      | RED                   | LED0805_NOOUTLINE         | ! | CHIPLED_0805_NOOUTLINE | LED                              | Indicator LED                                                                  | https://www.digikey.com/product-detail/en/LH+R974-LP-1/475-1415-1-ND/1802604/?itemSeq=338642877                                                                                                                                                                                                                                             |
| ON     | GREEN                 | LED0805_NOOUTLINE         | ! | CHIPLED_0805_NOOUTLINE | LED                              | Indicator LED                                                                  | https://www.digikey.com/product-detail/en/LG+R971-KN-1/475-1410-1-ND/1802598/?itemSeq=338642882                                                                                                                                                                                                                                             |
| C1     | 10uF                  | CAP_CERAMIC0805-NOOUTLINE | = | 0805-NO                | Ceramic Capacitors               | Decoupling Capacitor: smoothes longer changes in voltage                       | https://www.digikey.com/product-detail/en/GRM21BC81D106KE51L/490-10500-1-ND/5026426/?itemSeq=338642887                                                                                                                                                                                                                                      |
| C2     | 10uF                  | CAP_CERAMIC0805-NOOUTLINE | = | 0805-NO                | Ceramic Capacitors               | Decoupling Capacitor: smoothes longer changes in voltage                       | https://www.digikey.com/product-detail/en/GRM21BC81D106KE51L/490-10500-1-ND/5026426/?itemSeq=338642887                                                                                                                                                                                                                                      |
| C3     | 10uF                  | CAP_CERAMIC0805-NOOUTLINE | = | 0805-NO                | Ceramic Capacitors               | Decoupling Capacitor: smoothes longer variation in voltage                     | https://www.digikey.com/product-detail/en/GRM21BC81D106KE51L/490-10500-1-ND/5026426/?itemSeq=338642887                                                                                                                                                                                                                                      |
| C4     | 0.1uF                 | CAP_CERAMIC0805-NOOUTLINE | = | 0805-NO                | Ceramic Capacitors               | Decoupling Capacitor: smoothes high frequency changes in voltage               | https://www.digikey.com/product-detail/en/C0805C104M3RACTU/399-8000-6-ND/3472531/?itemSeq=338642888                                                                                                                                                                                                                                         |
| C5     | 0.1uF                 | CAP_CERAMIC_0805MP        | = | _0805MP                | Ceramic Capacitors               | When the DTR changes from high to low the reset pin on the ATMega will go high | https://www.digikey.com/product-detail/en/C0805C104M3RACTU/399-8000-6-ND/3472531/?itemSeq=338642888                                                                                                                                                                                                                                         |
| C6     | 0.1uF                 | CAP_CERAMIC0805-NOOUTLINE | = | 0805-NO                | Ceramic Capacitors               | Decoupling Capacitor: smoothes high frequency changes in voltage               | https://www.digikey.com/product-detail/en/C0805C104M3RACTU/399-8000-6-ND/3472531/?itemSeq=338642888                                                                                                                                                                                                                                         |
| C8     | 0.1uF                 | CAP_CERAMIC0805-NOOUTLINE | = | 0805-NO                | Ceramic Capacitors               | Decoupling Capacitor: smoothes high frequency changes in voltage               | https://www.digikey.com/product-detail/en/C0805C104M3RACTU/399-8000-6-ND/3472531/?itemSeq=338642888                                                                                                                                                                                                                                         |
| C10    | 0.1uF                 | CAP_CERAMIC0805-NOOUTLINE | = | 0805-NO                | Ceramic Capacitors               | Decoupling Capacitor: smoothes high frequency changes in voltage               | https://www.digikey.com/product-detail/en/C0805C104M3RACTU/399-8000-6-ND/3472531/?itemSeq=338642888                                                                                                                                                                                                                                         |
| C12    | 10uF                  | CAP_CERAMIC0805-NOOUTLINE | = | 0805-NO                | Ceramic Capacitors               | Decoupling Capacitor: smoothes longer changes in voltage                       | https://www.digikey.com/product-detail/en/GRM21BC81D106KE51L/490-10500-1-ND/5026426/?itemSeq=338642887                                                                                                                                                                                                                                      |
| R2     | 1K                    | RESISTOR_4PACK            | ~ | RESPACK_4X0603         | Resistor Packs (4 resistors)     | 4x resistor array to current limit the LEDs                                    | https://www.digikey.com/product-detail/en/742C083102JP/742C083102JPCT-ND/1124573/?itemSeq=338642869                                                                                                                                                                                                                                         |
| R8     | 10K                   | RESISTOR0805_NOOUTLINE    | ~ | 0805-NO                | Resistors                        | Pullup resistor on reset pin: when you hit reset pulls pin high                | https://www.digikey.com/product-detail/en/RC0805FR-0710KL/311-10.0KCRCT-ND/730482/?itemSeq=338642870                                                                                                                                                                                                                                        |
| R11    | 1K                    | RESISTOR0805_NOOUTLINE    | ~ | 0805-NO                | Resistors                        | Allows you to use the RX pin on the board over CP2104 chip                     | https://www.digikey.com/product-detail/en/RC0805JR-071KL/311-1.0KARCT-ND/731165/?itemSeq=338642876                                                                                                                                                                                                                                          |
|        |                       |                           |   |                        |                                  |                                                                                |                                                                                                                                                                                                                                                                                                                                             |
| *      | Major components      |                           |   |                        |                                  |                                                                                |                                                                                                                                                                                                                                                                                                                                             |
| +      | Power managment       |                           |   |                        |                                  |                                                                                |                                                                                                                                                                                                                                                                                                                                             |
| @      | Inputs and connectors |                           |   |                        |                                  |                                                                                |                                                                                                                                                                                                                                                                                                                                             |
| !      | Indicators            |                           |   |                        |                                  |                                                                                |                                                                                                                                                                                                                                                                                                                                             |
| =      | Capacitors            |                           |   |                        |                                  |                                                                                |                                                                                                                                                                                                                                                                                                                                             |


## Part C. Prototype your Arduino+

As much as is possible, prototype the design of your Arduino +. This step may require time. For example, if you have to order breadboard able parts that you don't have on hand, you might have to order those and wait for them to arrive. On the other hand, for other aspects of your design, like layout, you might be able to use sketches to figure out how everything will fit together, or if it will be large enough or small enough for the application you have in mind. 

Sometimes you're just testing out design constraints. For example, if you are making an Arduino + speaker to be a musical dog collar for your pet, you can see how heavy a collar your dog will tolerate by making a dummy board and case.

**Describe key design questions (how big are the parts? what pins need to be connected?) and how you used/will use prototyping to answer them.**

## Part D. Layout your Arduino+

Use EAGLE, KiCAD, Fritzing or the ECAD program of your choice to layout your Arduino +. The source files for the existing Arduino designs is available from Arduino.cc. For example, [here is the page](https://store.arduino.cc/usa/arduino-uno-rev3) with the open source designs for the Arduino UNO R3. 

**Document what you files, with enough specificity that anyone else could have the same thing made.**

## Part E. Send your board off to be made

When you have laid out your board, send it off to be fabricated. You might need to order components, tools or other apparatus (like programmers or FTDI interfaces) to complete the design at this time too.

**Document what you sent, and to where, with enough specificity that anyone else could have the same thing made.**

**In the report, please tell us any pain points you faced in this lab, and how we could make this process easier for future students.**

## Example Project

[In this](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/tree/2020Fall/alt-Lab2) repo you will find the original files from Adafruit for the [Metro Mini](https://github.com/adafruit/Adafruit-METRO-328-PCB) you all have in your kit and a file I have edited.  You can compare the changes to the schematic and the board file to see which changes were made.


I've decided I want to be able to control my Metro Mini with a standard television remote control and have that be a part of the board itself. This requires adding an [IR Receiver](https://www.adafruit.com/product/157). For the first version I will use the same through hole product linked. In a future version I may want to use a surface mount component such as [TSOP752](https://www.vishay.com/docs/82494/tsop752.pdf).
### Getting from the original Metro Mini to the Final Design

1. How are components wired?  
Looking at the [Data sheet](https://cdn-shop.adafruit.com/datasheets/tsop382.pdf) I can see I need to connect pins `1 = OUT, 2 = GND, 3 = VS`  
With an Arduino that might look something like ![Arduino wiring](https://cdn-learn.adafruit.com/assets/assets/000/000/555/original/light_arduinopna4602.gif?1447976120)
2. Open the metro mini schematic file in Eagle. The component we will need to add to our schematic is a 3 pin connector. You can find that in the [Sparkfun Connectors Library](https://www.autodesk.com/products/eagle/blog/library-basics-install-use-sparkfun-adafruit-libraries-autodesk-eagle/). The add part button ![Add part](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/assets/Screen%20Shot%202020-09-08%20at%202.15.36%20PM.png?raw=true) will let you put your part on the schematic. In our case the CONN_03 part in the Sparkfun Connectors library.
3. Using the net tool we draw a trace from pin 2 to PD2 on our ATMEGA 328P. We add a ground connector by copying and pasting. We draw an unconnected net and name it VCCIO.  
![connections](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/assets/Screen%20Shot%202020-09-08%20at%202.19.29%20PM.png?raw=true)
4. Hit the BRD button ![brd button](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/assets/Screen%20Shot%202020-09-08%20at%202.24.11%20PM.png?raw=true) in the top left to see your board file. We need to make routes for all the unconnected airwires. See the final design do see which parts and traces were moved.
  - the board was made longer by moving the outline in layer 20
  - The ground planes on the top and bottom were also moved the meet the extended length
  - Traces were shifted to the right and the reset button was moved
  - Routes were added for the new component and a few via's to easily route wires.  
You can see the final design and compare the differences. 
5. Before getting anything manufactured hit the ULP button, generate BOM. Find a link to every component you will need for your board. [Digikey](https://www.digikey.com/) is a good resource for this.

## Get your schematic, board, BOM and who you think you might order reviewed from BEFORE ordering anything.


