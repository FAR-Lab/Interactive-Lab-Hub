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
Use the table below, or just include a link to a spreadsheet or pdf.
| Part name | Part ID | Part description | # of units | link to data sheet | link to source | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Atmega 328P    |   U1 |   Microcontroller  |  1   |  [datasheet](http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-7810-Automotive-Microcontrollers-ATmega328P_Datasheet.pdf)   |   [Amazon](https://www.amazon.com/dp/B004G51AMW)  |  Bootloader   |
|     |    |     |     |     |     |     |
|     |    |     |     |     |     |     |




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


