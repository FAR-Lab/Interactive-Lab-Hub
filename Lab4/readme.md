# PreLab4

For the upcoming labs, we will be building paper displays inspired by [Isaac Blankensmith](http://www.isaacblankensmith.com/) and [Smooth Technology's](https://smooth.technology) [Paper Signals](https://experiments.withgoogle.com/paper-signals) project (Lab 4) or building a paper jack in a box (Lab 5). W

1. CATCHING UP ON UNDERSTANDING: If you are confused on the following topics, you can read [Scherz and Monk](http://www.engineeringbookspdf.com/practical-electronics-inventors-fourth-edition-paul-scherz-simon-monk/)'s excellent textbook which can give you more background.

Basics CH 2
*  Electric Current Ch 2.2

 *  Voltage Ch 2.3, 2.13

 *  Resistance, Ohm's Law Ch 2.5, 2.12

* Ground Ch 2.10

*  Circuits Ch 2.11, 2.16

Electric components Ch 3

*  Batteries 3.2

*  Switches 3.3

*  Resistors 3.5

Sensors Ch 6

*  Proximity and Touch Ch 6.3

*  Movement, Force, Pressure Ch 6.4

*  Light, Magnetism, Sound Ch 6.6

Digital Electronics Ch 12

* Analog Digital Interfacing Ch 12.9

* Displays Ch 12.10

* Memory Devices Ch 12.11

Microcontrollers Ch 13

*  Arduino Ch 13.4

*  Other examples Ch 13.2

2. PAPER MECHANICS: [Paper prototyping](https://www.uxpin.com/studio/blog/paper-prototyping-the-practical-beginners-guide/) is used by UX designers to quickly develop interface ideas and run them by people before any programming occurs. [Cardboard prototypes](https://www.youtube.com/watch?v=k_9Q-KDSb9o) help interactive product designers to work through additional issues, like how big something should be, how it could be carried, where it would sit. [Surprisingly complicated forms](https://www.pinterest.com/pin/50032245843343100/) can be built with paper, cardstock or cardboard. The most advanced and challenging prototypes to prototype with paper are [cardboard mechanisms](https://www.pinterest.com/helgangchin/paper-mechanisms/) which move and change. 

<img src="https://dysonthedesigner.weebly.com/uploads/2/6/3/9/26392736/427342_orig.jpg"  width="200" > Dyson Vacuum cardboard prototypes

3. BRING CARDBOARD FOR LAB 5

# Data Logger (and using cool sensors!)

For this lab, we will be experimenting with a variety of sensors, sending the data to the Arduino serial monitor, writing data to the EEPROM of the Arduino, and then playing the data back.

## Overview

What's in this lab?

A. [Writing to the Serial Monitor](#part-a--writing-to-the-serial-monitor)

B. [RGB LED](#part-b-rgb-led)

C. [Resistance & Voltage Varying Sensors](#part-c-resistance--voltage-varying-sensors)

D. [I2C Sensors](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/wiki/Lab-03#part-d-i2c-sensors)

E. [Logging Values to the EEPROM and Reading Them Back](#part-f-logging-values-to-the-eeprom-and-reading-them-back)

F. [Create your own Data logger!](#part-g-create-your-own-data-logger)

## In The Report
For the report, make a copy of this wiki page for your own repository, and then delete everything but the headers and the sections between the **stars**. Write the answers to the questions under the starred sentences. Include snippets of code that explain what you did.

Deliverables are due next Tuesday. Post a link to the wiki page on your main class hub page.

## Part A.  Writing to the Serial Monitor
 
[[images/Pot_schem.png]]
 
The OLED display from the Lab 02 is a great and helpful tool for debug purposes; the serial monitor is another. Use the code from `File->Examples->Communication->Graph` as a template to print data from your potentiometer to the serial monitor. Don't disconnect the USB cable after uploading the code; instead, use the serial monitor button on the Arduino IDE (in the upper right corner, magnifying glass icon) to see the data coming from the Arduino. 
 
**a. Based on the readings from the serial monitor, what is the range of the analog values being read?**
 
**b. How many bits of resolution does the analog to digital converter (ADC) on the Arduino have** (hint: where might you look to find this sort of thing)? How many are you using with the range of values you're seeing?
 
You can also read inputs from the serial monitor, or wait for the serial monitor to open before spewing data over the USB line! A nice tutorial on the basic serial transmit functions can be found at http://arduino.cc/en/Tutorial/AnalogReadSerial. 

NEW!!! Also you can plot the data with the Arduino Serial Plotter! This can be found under `Tools->Serial Plotter`. Try it out.
 
For this lab, you can use the serial monitor, plotter and/or the LCD whenever you are told to display something, depending on what you think is easier/prettier.

## Part B. RGB LED

In your kit, you have a "common anode RGB LED." This means that the three LEDs in the RGB package share a common power source, and turn on when the R, G, or B legs have a low enough voltage to cause current to flow. The LONGEST leg is the "common anode" and should be connected to power (do you need a resistor?). The rest of the legs will be connected to pins based on the code you decide to use. 

**You should add the LEDs in the schematic below.**

![RGB LED schematic](images/rgbled.png)

<!--Modify the Fade code from Lab 1 so that you have the R, G and B leads of the LED on pins 9, 10 and 11, respectively. You will want to change the code so that you can fade each of the colors separately.-->
[Here is sample code](https://learn.adafruit.com/adafruit-arduino-lesson-3-rgb-leds/arduino-sketch) that controls the color of an RGB LED using the Arduino.  

<!--**How might you use this with only the parts in your kit? Show us your solution.**-->

## Part C. Resistance & Voltage Varying Sensors 
One of the useful aspects of the Arduino is the multitude of analog input pins. We'll explore this more now.
 
### FSR
Now that you have a set up that lets you look at changes in the analog voltage from the potentiometer, let's swap in other analog sensors!

<img src=https://cdn-shop.adafruit.com/1200x900/166-00.jpg alt="FSR" width=400>

The FSR (force sensitive resistor) changes resistance — in this case when pressure is applied to the FSR. [Here's the datasheet](https://cdn-shop.adafruit.com/datasheets/FSR400Series_PD.pdf). We'll use a voltage divider with a 27kOhm resistor, using the analog input with the previous potentiometer code. (Feel free to use a 10kOhm resistor instead, or anything in this range.)

[[images/fsr_voltage_divider.png]]

We need a voltage divider because the Arduino can't measure resistance directly, which is the thing that changes when you physically interact with the sensor. A voltage divider circuit converts a change in resistance to a change in voltage.

**a. What voltage values do you see from your force sensor?**

**b. What kind of relationship does the voltage have as a function of the force applied? (e.g., linear?)**

**c. In `Examples->Basic->Fading` the RGB LED values range from 0-255. What do you have to do so that you get the full range of output voltages from the RGB LED when using your FSR to change the LED color?**

## Flex Sensor, Photo cell, Softpot
Now experiment with the [flex sensor (Optional)](https://www.adafruit.com/product/1070), [photo cell](https://www.adafruit.com/product/161) and [softpot](https://www.adafruit.com/product/178).

<img src=https://cdn-shop.adafruit.com/1200x900/1070-01.jpg alt="flex sensor" width=250>
<img src=https://cdn-shop.adafruit.com/1200x900/161-00.jpg alt="photocell" width=250>
<img src=https://cdn-shop.adafruit.com/1200x900/178-00.jpg alt="softpot" width=250>

**a. What resistance do you need to have in series to get a reasonable range of voltages from each sensor?**

**b. What kind of relationship does the resistance have as a function of stimulus? (e.g., linear?)**


## Part D. I2C Sensors 

Some more sophisticated sensors have ICs that measure physical phenomena and then output an digital signal indicating what the analog voltage reading is. 
### Accelerometer
 
The accelerometer is a 3-axis, accelerometer based on the LIS3DH. The LIS3DH is a 3.3V part, but the Adafruit board has an onboard voltage regulator so that the part can be powered on 5V power on the Vin pin.
 
Here's the [Datasheet](https://cdn-shop.adafruit.com/datasheets/LIS3DH.pdf) [
 
Unlike the other parts we've used to date, this is a "smart sensor" which can communicate the sensor readings digitally (rather than through an analog voltage) using communication protocols I2C and SPI. 
 
[This example code](https://learn.adafruit.com/adafruit-lis3dh-triple-axis-accelerometer-breakout/arduino) is meant to read values from a 3-axis accelerometer out to a computer over the serial monitor. Test it out! Hint: make sure to read the I2C Wiring section carefully, because the picture uses a different kind of Arduino. Here's a Fritzing diagram of the correct wiring:

[[images/LIS3DH_breadboard.png]]
 
Adapt the code to indicate what your readings are on the X, Y and Z axes of the accelerometer on your 16x2 LCD panel.

Now set up the RGB LED so that each color is mapped to the X, Y and Z axes accelerations.
 
Get a feel for the data the accelerometer provides. Pick up the Arduino+accelerometer board and tilt it in various directions. Start by holding it so that the accelerometer board is parallel to the ground. Find in which direction the X reading increases and decreases; do the same for the Y reading.
 
**a. Include your accelerometer read-out code in your write-up.**


## Part E. Logging values to the EEPROM and reading them back
 
### 1. Reading and writing values to the Arduino EEPROM
The sample code in `File->Examples->EEPROM` shows functions from the [Arduino EEPROM Library](https://www.arduino.cc/en/Reference/EEPROM) to write and read values to Arduino's EEPROM. This [modified version of the SwitchState code](code/SwitchState2.zip) employs these functions in three different states. Try it out.

**a. Does it matter what actions are assigned to which state? Why?**

**b. Why is the code here all in the setup() functions and not in the loop() functions?**

Each character in the string is a byte. That is, it takes 8-bits to encode a character, so the number of characters in the string we are writing is the number of bytes we are occupying in EEPROM. The [Atmega 328P](https://www.microchip.com/wwwproducts/en/atmega328p) at the heart of the Arduino has 1024 bytes of internal [EEPROM](http://en.wikipedia.org/wiki/EEPROM) Memory (which is separate from the 32KB of [Program memory](https://en.wikipedia.org/wiki/Read-only_memory) it has for the code it is running.)

**c. How many byte-sized data samples can you store on the Atmega328?**

**d. How would you get analog data from the Arduino analog pins to be byte-sized? How about analog data from the I2C devices?**

**e. Alternately, how would we store the data if it were bigger than a byte? (hint: take a look at the [EEPROMPut](https://www.arduino.cc/en/Reference/EEPROMPut) example)**

Modify the code to take in analog values from your sensors and print them back out to the Arduino Serial Monitor.

### 2. Design your logger
You've been thinking at a high level about a data logger and what it is used for; now you need to adapt that to the specific implementation. 


A lot of the art of data logging is being clever about how to use the sensor. Feel free to engage the teaching team for advice.

Your data logger will have two main modes: one where it logs data and another where it plays the data back. Think a little about what sensors you would like to log data from and how you would like to display your data. Create a state diagram sketch that indicates how you'd like to switch between one mode and the other, and also what you'd like the program to do in each state. This can help you decide what buttons or knobs might be useful for your design.
 
You might make changes to your design before this lab is complete.
 
**a. Turn in a copy of your final state diagram.**

## Part G. Create your own data logger!
Now it's up to you to integrate the software and hardware necessary to interface with your data logger! Your logger should be able to record a stream of analog data (at a sample rate of your desire) and then play it back at some later point in time on your display of choice.
 
**a. Record and upload a short demo video of your logger in action.**
