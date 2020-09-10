This lab is a merge of what is originally Lab 4 and Lab 5 of the curriculum. This is meant for students who have had this curriculum before. If you have little experience with electronics, breadboarding, Arduino programming or the Arduino hardware, please work on Lab 4 and Lab 5 separately!

The alt-pre-Lab helps you to get set up in advance of in-class lab.

# Pre Lab 4
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

# Lab 4

# Make a Digital Timer!
 
## Overview
For this assignment, you are going to 
A) [revisit Blink with your Arduino,](#part-a-revisiting-blink) 
B) [explore cool input components,](#part-b-advanced-inputs) 
C) [write to a text LCD panel,](#part-c-writing-to-the-lcd) and 
D) [make your very own timer](#part-d-timer)
BONUS) [make your timer sing!](#part-e-tone).
 
## In The Report
Include your responses to the bold questions. Include snippets of code that explain what you did. Deliverables are due next Tuesday. Post your lab reports as 'wiki' pages on your GitHub, and post a link to that wiki on Slack under your channel and #Lab4.

## Part A. Revisiting Blink

For this lab, we'll be using the [Adafruit Metro Mini](https://www.adafruit.com/product/2590) development board as our hardware platform. This board is a derivative of the [Arduino UNO R3](https://store.arduino.cc/usa/arduino-uno-rev3). As a platform, Arduino comprises both hardware and software. We'll be using the [Arduino hardware](http://arduino.cc/en/Main/Hardware); for an [IDE](http://en.wikipedia.org/wiki/Integrated_development_environment), you have the option of using the [Arduino software](http://arduino.cc/en/Main/Software) on your laptop.
 
To use your laptop computer for programming the Metro Mini, you will need to download and install the software on your machine:
* [Arduino IDE](https://www.arduino.cc/en/Main/Software) 
* [SiLabs CP210x drivers](http://www.silabs.com/products/mcu/pages/usbtouartbridgevcpdrivers.aspx)
 
**1. Blinking LEDs with Arduino**

Connect the Metro Mini to your computer using the USB cable. Arduino boards typically come preloaded with a version of the Blink program on it. This code lets its LED (connected on pin 13) blink as soon as the USB cable starts powering the board. In this class, we have previously uploaded a different program to the Arduino. (Remember the [helloYouSketch from Lab1](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/wiki/Lab-%232#2-helloyou-test)). 

To get set up, we will use the Blink example code to see how to upload code to the Arduino from our computer. The Blink program itself can be found in the Arduino IDE's example code folder under [File->Examples->Basics->Blink](https://www.arduino.cc/en/Tutorial/Blink). Check it out!

**a. What line(s) of code do you need to change to make the LED blink (like, at all)?**

**b. What line(s) of code do you need to change to change the rate of blinking?**

**c. What circuit element would you want to add to protect the board and external LED?**
 
To compile and upload your code, take the following steps (note that 1, 2 should only have to be done once):
 
1) In the Arduino program, select the board we are using: Tools -> Board -> Arduino/Genuino UNO 
2) You may also have to select a communications (or COM) port (Tools -> Serial Port). The port should be something like `/dev/cu.SLCA_USBtoUART` (on MAC) `/dev/ttyUSB0` (on Linux), or `COM3` (on Windows, could be another number). If they are not showing up, make sure you've installed the [SiLabs CP210x drivers](http://www.silabs.com/products/mcu/pages/usbtouartbridgevcpdrivers.aspx).
3) To compile your code, click on the "checkmark" on the upper far left of the Arduino development window.
4) To upload compiled code to the Arduino, click on "right arrow" besides the "checkmark."
5) When the code is uploaded, the Arduino should automatically start running your new code.
 
Now modify the circuit and program so that you can blink an external LED on pin 9. Don't forget about question (c) above! (Also, don't forget to connect power and ground the power and ground rails of your breadboard, respectively!)
 
[[images/LED_schem.png]]

*Some tips and reminders:*
 
We don't have extra Arduinos, so be careful.

Remember that the USB connection to the Arduino supplies power.

Check that there are no shorts between power and ground before you plug in the USB cable (and apply power).

Unplug power before modifying circuits!
 
**2. Digitally toggle LEDs on and off using the Arduino**

With your LED still connected on digital pin 9, hook up a button circuit on digital pin 2 of the Arduino. One side of the pushbutton attaches to digital pin 2 and via a 10k resistor to Vcc. (Vcc is the supply voltage. In this case, it is 5V.). The other side of the pushbutton attaches to ground directly.
 
Use either the same circuit you used for the previous step or use the alternative design below. The alternate circuit causes the "on" state of the LED to occur when Arduino pin = LOW, not HIGH, as before.

 [[images/LEDandButton_schem.png]]

The Arduino pin configured as an input has a 'high input impedance.' This means that it can sense the voltage without affecting the circuit, like a probe.
 
Use the Button program ([File->Examples->Digital->Button](https://www.arduino.cc/en/Tutorial/Button)) to make your Arduino into a light switch.

**a. Which lines do you need to modify to correspond with your button and LED pins?**

**b. Modify the code or the circuit so that the LED lights only while the button is depressed. Include your code in your lab write-up.**
 
**3. Fading LEDs on and off using Arduino**
What about those "breathing" LEDs on (old) Macs? The fading from bright to dim and back is done using pulse-width modulation (PWM). In essence, the LED is toggled on and off very rapidly, say 1,000 times a second, faster than your eye can follow. The percentage of time the LED is on (the duty) controls the perceived brightness. To control an LED using PWM, you'll have to connect it to one of the pins that support PWM output —-- which are 4, 5, 6, 9, 10, 11, and 12 on the Arduino.
 
Use the Fading program `[File->Examples->Analog->Fading](https://www.arduino.cc/en/Tutorial/Fading)` to make your LED fade in and out.

**a) Which line(s) of code do you need to modify to correspond with your LED pin?**

**b) How would you change the rate of fading?**

**c) (Extra) Since the human eye doesn't see increases in brightness linearly and the diode brightness is also nonlinear with voltage, how could you change the code to make the light appear to fade linearly?**

## Part B. Advanced Inputs

First, it's important for you to understand that **_analog_** input ("analog pin 0") on your Arduino board shares pins with _**digital**_ input. Below is pinout for the Metro Mini. The pins with name A0-A12 are analog pins. 
 
[[images/MetroMini_pinout.png]]
 
So while a [digitalRead](http://www.arduino.cc/en/Reference/DigitalRead) or [digitalWrite](http://www.arduino.cc/en/Reference/DigitalWrite) command reads or sends only a logic-level high or low, an [analogRead](http://www.arduino.cc/en/Reference/AnalogRead) or [analogWrite](http://www.arduino.cc/en/Reference/AnalogWrite) command reads or sends a range of values.[Example: if you want to read analog pin 0—which corresponds to pin A0 on the right side of Arduino, you would call `analogRead(A0)`]. Note that the analogWrite function has nothing to do with analog pins; it uses the PWM pins.
 
### 1. Potentiometer
Set up the LED output and potentiometer input circuits from the following schematic on your breadboard. This setup is much like the LED fade, except now we're using analogRead to control the fade. Have a look at [File->Examples->Analog->AnalogInput](https://www.arduino.cc/en/Tutorial/AnalogInput) for the code.
 
[[images/LEDandPot_schem.png]]

[[images/PotPicture.JPG]]

The potentiometer is an instance of a voltage divider circuit, which we discussed in class. As you might recall:

[[images/potPicture.png]]
 
Change the code so that the LED fades and brightens with the analog value of the potentiometer, like a dimmer. (Save this code! We'll be using it again soon...)
 
**a. Post a copy of your new code in your lab write-up.**
 
### 2. Force Sensitive Sensor

The [FSR](http://en.wikipedia.org/wiki/Force-Sensing_Resistor) changes resistance — in this case when pressure is applied to the FSR. Here's the [datasheet](http://www.sparkfun.com/datasheets/Sensors/Pressure/fsrguide.pdf). We'll use a voltage divider with a 22kOhm(originally 27kOhm but they are not avalible right now) resistor, using the analog input with the previous potentiometer code.

[[images/forceResistor_schem.png]]
  
**a. What resistance values do you see from your force sensor?**

**b. What kind of relationship does the resistance have as a function of the force applied? (e.g., linear?)**

**c. Can you change the LED fading code values so that you get the full range of output voltages from the LED when using your FSR?**

## Part C. Writing to the LCD
Let's use your LCD screen to display some interesting information! There is a good deal of example code for playing with your LCD in the Arduino Examples:
 
` File->Examples->LiquidCrystal`
 
Let's start with the "Display" program, which just flashes "Hello World!" These LCDs are a custom part, but there's a lot of information at [this](https://www.adafruit.com/product/181) page, the [pinout and dimensions](https://cdn-shop.adafruit.com/product-files/181/p181.pdf) page and the [LCD controller](https://www.adafruit.com/datasheets/HD44780.pdf) page.
 
**a. What voltage level do you need to power your display?**
**b. What voltage level do you need to power the display backlight?**
 
Solder a 16 pin breakaway header to the LCD so you can connect it to your breadboard. 

**If you haven't soldered before, we're happy to show you how! PLEASE ASK.**
![](https://cdn-shop.adafruit.com/1200x900/181-03.jpg)

Wire up your LCD according to the schematic below. If you didn't have our diagram, you would use the data sheets for the LCD and follow the comments in the "Display" code to figure out how to wire it up. 

[[images/lcd_arduino_schematic.png]]
 
**Be very careful not to connect Pin 1 and Pin 2 on the LCD**, as this can **destroy** your Arduino. Check the connections for a short between power and ground before you plug in power or the USB cable.
 
See [Tutorial](http://www.arduino.cc/en/Tutorial/LiquidCrystal) for more information. See [LCD Library](http://arduino.cc/en/Reference/LiquidCrystal) for the various functions you can use.

Try compiling and running the code. If it doesn't work the first time, check your pinouts...
 
The 10K pot connected to Vo on the LCD adjusts the contrast, so try adjusting that if your LCD won't turn on. The contrast might be so low that you're not able to see it, so make sure you've checked both extremes.
 
LCD pin 15 and 16 (LED+, LED-) are designed for background lighting. If you feel the whole screen too dark, you may try to connect pin15(LED+) to +3V or +3.3V and pin16(LED-) to ground. **Don't connect pin15(LED+) to +5V as it may burn background light!**
 
Do try to set this up before peeking at this [diagram](images/lcd_arduino_diagram.png).
  
**b. What was one mistake you made when wiring up the display? How did you fix it?**

**c. What line of code do you need to change to make it flash your name instead of "Hello World"?**
 
Try a few of the other examples in the folder to get a feel for the capabilities of your LCD. There is a list of all the possible functions at the [Arduino LiquidCrystal Library](http://arduino.cc/en/Reference/LiquidCrystal?from=Tutorial.LCDLibrary).

Incorporate the LCD into your fading LED/potentiometer code so that you can read out the exact analog value that you are reading in on Analog Pin 0. It's your own lowly multimeter!

**d. Include a copy of your Lowly Multimeter code in your lab write-up.**


Now build a circuit with two FSR sensors (one from your self and one borrowed from a fellow student) to enable a game of thumb wrestling. Use the LCD to indicate who is squeezing their FSR harder!

**e. Include a copy of your FSR thumb wrestling code in your lab write-up.**

Leave your LCD set up for Part D of the Lab, and leave it set up when you finish Lab, as we'll use the display again next week.

## Part D. Timer

Make a timer that uses any of the input devices to set a time, and then automatically (or manually, if you prefer) begin counting down, displaying the time left. Make your timer show an alert once the time is up with one of the output devices we connected during this lab, or you have available. (Hint: the sample code for [Examples->LiquidCrystal->HelloWorld](https://www.arduino.cc/en/Tutorial/HelloWorld) displays the time in seconds since the Arduino was reset...)
 
Note that for some of you, the time may seem to be decremented by 10 each second (that is, from 670=>660). Why is this? Do you think it's a hardware or software issue? Think about how 100 vs. 99 is written to the screen, and ask an instructor.

**a. Make a short video showing how your timer works, and what happens when time is up!**

**b. Post a link to the completed lab report to the class Slack.**

## OPTIONAL:
## Part E. Tone

Let's make the Arduino make some noise! We are going to start with the Tone example program:
 
`Examples->Digital->toneMelody`

The official Arduino tutorial for this code is [here](https://www.arduino.cc/en/Tutorial/ToneMelody?from=Tutorial.Tone)
Add a 75 Ohm resistor to limit the current to the speaker when you hook it up on your breadboard. If you would like it a little louder, you can use a lower value resistor, up to a minimum of 5 Ohms.

Wire it to your circuit with the black to ground and the red to Arduino Micro pin 8. 

**a. How would you change the code to make the song play twice as fast?**
 
Now change the speed back, and replace the melody[] and noteDurations[] arrays with the following:
```c++

int melody[] = {
  NOTE_D3,NOTE_D3,NOTE_D3,NOTE_G3,NOTE_D4,NOTE_C4,NOTE_B3,NOTE_A3,NOTE_G4,NOTE_D4, \
  NOTE_C4,NOTE_B3,NOTE_A3,NOTE_G4,NOTE_D4,NOTE_C4,NOTE_B3,NOTE_C4,NOTE_A3,0};
 
int noteDurations[] = {
  10,10,10,2,2,10,10,10,2,4, \
  10,10,10,2,4,10,10,10,2,4};
 ```
You'll also have to increase the for() loop index max from 8 to 20:
 ```c++
  for (int thisNote = 0; thisNote < 20; thisNote++) {
 ```
**b. What song is playing?**
 



---
How to upload code using your [RaspberryPi over command line](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/wiki/Uploading-code-to-the-Arduino-via-Raspberry-Pi-SSH).

How to upload the [code with x11](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/wiki/Uploading-code-to-the-Arduino-via-Raspberry-Pi-XWindows).


# PreLab 5
For next week's lab, we'll be making useless boxes. For the lab, we'll have readymade files for you to customize and laser cut. However, we'd like you to take a moment to think about how to make a box with a hinged lid. 
1. Take a look at this [useless box example](https://makezine.com/projects/the-most-useless-machine/) and try to create one out of paper in less than 30 minutes. 
1. Where will the switch, Arduino, and servo go? 
1. Submit a picture of your paper prototype! Bonus points if you submit a timelapse of the process. 


[[images/paper-prototype.JPG]]


# Lab5

#  Data logging with Rpi and Arduino

For this lab, we will be experimenting with a variety of sensors, play it back on your LCD display or serial monitor, logging data back to the Raspberry Pi, and making it possible to remotely view the data in real-time.


## Part A.  Writing to the Serial Monitor
Hook up the simple potentiometer voltage divider circuit from lab 4.
 
[[images/Pot_schem.png]]
 
The LCD display from the last lab is a great and helpful tool for debug purposes; the serial monitor is another. Use the code from `File->Examples->Communication->Graph` as a template to print data from your potentiometer to the serial monitor. Don't disconnect the USB cable after uploading the code; instead, use the serial monitor button on the Arduino IDE (in the upper right corner, magnifying glass icon) to see the data coming from the Arduino. If the Arduino is connected to the RaspberryPi you can either use [xWindows](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/wiki/Uploading-code-to-the-Arduino-via-Raspberry-Pi-XWindows) to open the serial monitor or use [ArduinoMake](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/wiki/Uploading-code-to-the-Arduino-via-Raspberry-Pi-SSH) to Upload and monitor your Arduino.
 
**a. Based on the readings from the serial monitor, what is the range of the analog values being read?**
 
**b. How many bits of resolution does the analog to digital converter (ADC) on the Arduino have**(hint: where might you look to find this sort of thing)? How many are you using with the range of values you're seeing?
 
You can also read inputs from the serial monitor, or wait for the serial monitor to open before spewing data over the USB line! A nice tutorial on the basic serial transmit functions can be found at http://arduino.cc/en/Tutorial/AnalogReadSerial. You can see from the sample code included in the comments of the Graph program that you could use the serial communication functions to communicate data from your sensors to other programs, such as Processing, Flash, MaxMSP.
 
For this lab, you can use the serial monitor and/or the LCD whenever you are told to display something, depending on what you think is easier/prettier.
 
## Part B. Voltage Varying Sensors 
Some more sophisticated sensors have ICs that measure physical phenomena and then output an analog voltage level, varying voltage much as a voltage divider circuit would. We have one of these for each table.
 
### 1. IR Distance Sensor

[[images/IR_Sensor.png]]

 
Get an IR distance sensor and an IR distance sensor jumper cable. The circuit for the distance sensor is simple: just connect red to +5V, black to ground, and white to analog input 0.
 
[IR Sensor Datasheet](https://www.sparkfun.com/datasheets/Components/GP2Y0A21YK.pdf)
[More Info on Sharp Distance Sensors](https://acroname.com/blog-tags/sharp-infrared#e26)
 
Use your Lowly Multimeter program to look at the data the sensor returns. What happens when the field of view is clear? Move your hand or a piece of paper over the sensor and see how the readings vary with distance.
 
**a. Describe the voltage change over the sensing range of the sensor. A sketch of voltage vs. distance would work also. Does it match up with what you expect from the datasheet?**
 
### 2. Accelerometer
![ADXL335 part](https://cdn-shop.adafruit.com/1200x900/163-02.jpg)
 
The accelerometer is a 3-axis, accelerometer based on the ADXL335. The ADXL335 is a 3.3V part, but the Adafruit board has an onboard voltage regulator so that the part can be powered on 5V power on the Vin pin.
 
[Datasheet](http://www.analog.com/en/products/mems/accelerometers/adxl335.html)
[Product Page](https://www.adafruit.com/product/163)
 
You will need to solder the 5 pin header to the accelerometer board. 
 
[This example code](https://www.arduino.cc/en/Tutorial/ADXL3xx) is meant to read values from a 3-axis accelerometer out to a computer over the serial monitor. Test it out!
 
Adapt the code to indicate what your readings are on the X, Y and Z axes of the accelerometer on your 16x2 LCD panel.
 
Get a feel for the data the accelerometer provides. Pick up the Arduino+accelerometer board and tilt it in various directions. Start by holding it so that the accelerometer board is parallel to the ground. Find in which direction the X reading increases and decreases; do the same for the Y reading.
 
**a. Include your accelerometer read-out code in your write-up.**
 
## Part C. Count/Time-Based Sensors
One last type of sensor!
 
### 1. Rotary Encoder

![Rotary Encoder](https://cdn-shop.adafruit.com/1200x900/377-02.jpg)
We have a high-quality 24 pulse encoder with knob and nice, click-y rotation detents.
 
[Product Page](https://www.adafruit.com/product/377)
[Datasheet](https://cdn-shop.adafruit.com/datasheets/pec11.pdf)
 
Like a potentiometer, a rotary encoder has 3 pins; unlike a potentiometer, an encoder can be spun round and round without stop. Rotary encoders use [quadrature](http://en.wikipedia.org/wiki/Rotary_encoder) to tell how fast and in which direction you are turning a knob. To connect the encoder to your breadboard, you can insert three pins directly into motherboard like picture below.
 
The circuit below is the "correct" way of hooking up a rotary encoder with your Arduino; the resistors and capacitors help to filter out noise from the mechanical operation of the encoder - this circuit diagram is from the datasheet.

[[https://ccrma.stanford.edu/wiki/images/c/c1/Encoder_filter.png]]
 
However, to _actually_ hook up your encoder, just use the 3-pin side. Hook the middle to ground, and the "A" and "B" pins to digital pins 2 and 3 of your Arduino.
 
What is going on in this circuit? The Phase A and Phase B pins actually behave like switches, so the pins have pull-ups so that they will be high by default, until they are pulled low by the encoder (your Arduino actually uses its own internal pull-ups). The resistor and capacitor combo also forms a low-pass circuit to eliminate stray voltage spikes that might occur from the quick switching (this is called "debouncing"). You can use any capacitor that is up to an order of magnitude away from the 10nF value.
 
Use [this rotary encoder code](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/wiki/Rotary-Encoder-test-Code) to see if you have hooked the encoder up correctly!

## Part D. Logging values to the EEPROM and reading them back
 
### 1. Design your logger
You've been thinking at a high level about a data logger and what it is used for; now you need to adapt that to the specific implementation. 

In addition to the sensors you've tried out, your kit has a photocell, which is a light-varying resistor. We also have limited number (15) of the following sensors:
* Flex sensor
* Time of Flight sensor
* Long arm snap switch
* Rocker switch

as well as two sets of this sensor variety kit: [VKmaker T30 Sensor Module](https://www.amazon.com/VKmaker-Sensors-Modules-Starter-Arduino/dp/B01CS6UMKQ) the separate sensor documentation is [available for download](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/wiki/SensorDocumentation.zip).

A lot of the art of data logging is being clever about how to use the sensor. Feel free to engage the teaching team for advice.

Your data logger will have two main modes: one where it logs data and another where it plays the data back. Think a little about what sensors you would like to log data from and how you would like to display your data. Create a state diagram sketch that indicates how you'd like to switch between one mode and the other, and also what you'd like the program to do in each state. This can help you decide what buttons or knobs might be useful for your design.
 
You might make changes to your design before this lab is complete.
 
**a. Turn in a copy of your final state diagram.**

### 2. Reading and writing values to the Arduino EEPROM
The [Atmega 328P](https://www.microchip.com/wwwproducts/en/atmega328p) at the heart of the Arduino has 1024 bytes of internal [EEPROM](http://en.wikipedia.org/wiki/EEPROM) Memory (which is separate from the 32KB of [Program memory](https://en.wikipedia.org/wiki/Read-only_memory) it has for the code it is running.)

**a. How many byte-sized data samples can you store on the Atmega328?**
**b. How would you get your analog data from the ADC to be byte-sized?**

Use the code in the `File->Examples->EEPROM` as a template to write and read your own analog values to Arduino's EEPROM. (Ignore what they say about the EEPROM having only 512 bytes. You'll have to adjust your code to match the EEPROM size of the Arduino Micro. The [Atmega328 datasheet](https://www.microchip.com/wwwproducts/en/atmega328p) tells you how much EEPROM it has too).
 
[Arduino EEPROM Library](https://www.arduino.cc/en/Reference/EEPROM)

### 3. Reading and writing values to the Raspberry Pi
Alternatively, you can also store the data directly on the Raspberry Pi. This has certain advantages like disk space or the build in clock but also require the Pi to be constantly connected and on. The [simple-data-logger](https://github.com/FAR-Lab/simple-data-logger/tree/master) stores the data on the Raspberry Pi from the Arduino.

There are three folders inside the project.
* In the folder `sensorCode` is a simple Arduino program that periodically sends sensor values over the serial port.
* The `dataStorage` folder contains an node program `dataStorage.js`. It opens the serial port and writes any(!) incoming messages into the `dataBase.csv`.  Don't forget to run 'npm install' to get all required packages.
* `webServer` is a simple node web server `server.js` application, that streams the `dataBase.csv` file and additions to that file line by line to any connected web browser.Don't forget to run 'npm install' to get all required packages.

1. Set up your Arduino so that it sends its data over the serial port. You can use the provided `sensorCode.ino` or code from any of the earlier examples.

2. Start the `dataStorage.js` with `nohup` so it can keep logging data in the background, even if you log off. Like so:
```shell
nohup node dataStorage.js &
```
Before we go on lets verify that data is actually stored. Lets go one folder up with `cd ..` and look at the `tail` of the file with the `-F` flag so that it keeps refreshing any changes.
```shell
tail -F dataBase.csv
```
Every time the Arduino sends a new measurement it should appear here. It probably looks something like
```csv
date,value
1500000003500,868
1500000005501,867
1500000007499,866
```
The left side of the comma is a time measurement in [unix time](https://en.wikipedia.org/wiki/Unix_time) with milliseconds, the right side the sensor value at that time.

3. Start the web server by going into the web server folder `cd webServer` and run `node server.js`.
Now you can go to your browser and connect to the Raspberry Pi just like before with the Interaction Engine
`ixe[00].local:8000`.
 
4. The graph you'll see is rendered using [vega-light](https://vega.github.io/vega-lite/). For this assignment change the appearance so it fits your data. 

The design of the graph is defined at the top of the `client.js` file inside the `webServer/public/` folder. The available elements can be found by going through the [example](https://vega.github.io/vega-lite/examples/) looking at the [vega-light documentation](https://vega.github.io/vega-lite/docs/) and by playing with the [vega-light  online editor](https://vega.github.io/editor). 
The design define definition is all part of `vlSpec` object:

```javascript
var vlSpec ={
 "$schema": "https://vega.github.io/schema/vega-lite/v2.json",
 "data": { "name": "table","format": {
      "parse": {
        "date": "utc:'%Q'"
      }
    }
   },
 "width": 1000,
  "height":500,
  "mark": "line",
  "encoding": {
    "x": {
      "timeUnit":"utcyearmonthdatehoursminutessecondsmilliseconds",
      "field": "date",
      "type": "temporal"
    },
    "y": {
      "field": "value",
      "type": "quantitative"
    }
  }
};
```
### 4. Create your data logger!
Now it's up to you to integrate the software and hardware necessary to interface with your data logger! Your logger should be able to record a stream of analog data (at a sample rate of your desire) and then play it back at some later point in time. You are welcome to play back to either the 16x2 LCD or the Pi, as suits the application. 
 
**a. Use the lab camera or your own camera/cell phone to record and upload a short demo video of your logger in action.**
