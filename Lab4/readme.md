Overview
What's in this lab?

A. Writing to the Serial Monitor

B. RGB LED

C. Resistance & Voltage Varying Sensors

D. I2C Sensors

E. Logging Values to the EEPROM and Reading Them Back

F. Create your own Data logger!


Part A. Writing to the Serial Monitor
pot schematic

The OLED display from the Lab 02 is a great and helpful tool for debug purposes; the serial monitor is another. Use the code from File->Examples->Communication->Graph as a template to print data from your potentiometer to the serial monitor. Don't disconnect the USB cable after uploading the code; instead, use the serial monitor button on the Arduino IDE (in the upper right corner, magnifying glass icon) to see the data coming from the Arduino.

a. Based on the readings from the serial monitor, what is the range of the analog values being read?

0 to 1023

b. How many bits of resolution does the analog to digital converter (ADC) on the Arduino have (hint: where might you look to find this sort of thing)? How many are you using with the range of values you're seeing?

10 as 2^10 is 1024. 


Part B. RGB LED
In your kit, you have a "common anode RGB LED." This means that the three LEDs in the RGB package share a common power source, and turn on when the R, G, or B legs have a low enough voltage to cause current to flow. The LONGEST leg is the "common anode" and should be connected to power (do you need a resistor?). The rest of the legs will be connected to pins based on the code you decide to use.

You should add the LEDs in the schematic below.

RGB LED schematic

Here is sample code that controls the color of an RGB LED using the Arduino.

Part C. Resistance & Voltage Varying Sensors
One of the useful aspects of the Arduino is the multitude of analog input pins. We'll explore this more now.

FSR
Now that you have a set up that lets you look at changes in the analog voltage from the potentiometer, let's swap in other analog sensors!

FSR

The FSR (force sensitive resistor) changes resistance — in this case when pressure is applied to the FSR. Here's the datasheet. We'll use a voltage divider with a 27kOhm resistor, using the analog input with the previous potentiometer code. (Feel free to use a 10kOhm resistor instead, or anything in this range.)

Voltage Divider

We need a voltage divider because the Arduino can't measure resistance directly, which is the thing that changes when you physically interact with the sensor. A voltage divider circuit converts a change in resistance to a change in voltage.

a. What voltage values do you see from your force sensor?

0 to 1000 

b. What kind of relationship does the voltage have as a function of the force applied? (e.g., linear?)
The plots look exponential since there is a ramp up period up pressure is applied. 

c. In Examples->Basic->Fading the RGB LED values range from 0-255. What do you have to do so that you get the full range of output voltages from the RGB LED when using your FSR to change the LED color?

Analog Read from FSR to Analog Write the RGB Values.

Flex Sensor, Photo cell, Softpot
Now experiment with the flex sensor (Optional), photo cell and softpot.

flex sensor

photocell

softpot

a. What resistance do you need to have in series to get a reasonable range of voltages from each sensor?

I used a 10kOhm resistor to setup a voltage divider to get consistent readings from the flex sensors. Photocell and softpot were not in my kit.

b. What kind of relationship does the resistance have as a function of stimulus? (e.g., linear?)

Control the colors of the LED using the above sensors ( including FSR )

Part D. I2C Sensors
Some more sophisticated sensors have ICs that measure physical phenomena and then output an digital signal indicating what the analog voltage reading is.

Accelerometer
The accelerometer is a 3-axis, accelerometer based on the LIS3DH. The LIS3DH is a 3.3V part, but the Adafruit board has an onboard voltage regulator so that the part can be powered on 5V power on the Vin pin.

Here's the Datasheet

Unlike the other parts we've used to date, this is a "smart sensor" which can communicate the sensor readings digitally (rather than through an analog voltage) using communication protocols I2C and SPI.

This example code is meant to read values from a 3-axis accelerometer out to a computer over the serial monitor. Test it out! Hint: make sure to read the I2C Wiring section carefully, because the picture uses a different kind of Arduino. Here's a Fritzing diagram of the correct wiring:

https://github.com/FAR-Lab/Interactive-Lab-Hub/tree/master/Lab4/LIS3DH_breadboard.JPG

Adapt the code to indicate what your readings are on the X, Y and Z axes of the accelerometer on your OLED panel.

Now set up the RGB LED so that each color is mapped to the X, Y and Z axes accelerations.

Get a feel for the data the accelerometer provides. Pick up the Arduino+accelerometer board and tilt it in various directions. Start by holding it so that the accelerometer board is parallel to the ground. Find in which direction the X reading increases and decreases; do the same for the Y reading.

a. Include your accelerometer read-out code in your write-up.
X:  304  	Y:  64  	Z:  15920		X: 0.16 	Y: 0.00 	Z: 9.56 m/s^2 

X:  240  	Y:  160  	Z:  16032		X: 0.34 	Y: 0.17 	Z: 9.45 m/s^2 

X:  1072  	Y:  -144  	Z:  16000		X: 0.56 	Y: -0.10 	Z: 9.59 m/s^2 

X:  1200  	Y:  1280  	Z:  16224		X: 0.80 	Y: 0.57 	Z: 9.51 m/s^2 

X:  -1040  	Y:  96  	Z:  15856		X: -0.35 	Y: 0.35 	Z: 9.51 m/s^2 

X:  1024  	Y:  -1872  	Z:  16032		X: 1.01 	Y: -0.64 	Z: 9.37 m/s^2 

X:  1360  	Y:  496  	Z:  17296		X: 0.81 	Y: 0.48 	Z: 10.54 m/s^2 

X:  1648  	Y:  3088  	Z:  16032		X: 1.02 	Y: 1.85 	Z: 9.67 m/s^2 

X:  1808  	Y:  1088  	Z:  17216		X: 0.95 	Y: 0.95 	Z: 9.55 m/s^2 

X:  2352  	Y:  -816  	Z:  16208		X: 1.54 	Y: -0.52 	Z: 9.80 m/s^2 

X:  3616  	Y:  -4288  	Z:  13728		X: 2.20 	Y: -2.57 	Z: 8.22 m/s^2 

X:  3904  	Y:  -3840  	Z:  14288		X: 3.91 	Y: -1.92 	Z: 8.68 m/s^2 

X:  4576  	Y:  1584  	Z:  15904		X: 2.74 	Y: 0.96 	Z: 9.38 m/s^2 

X:  6672  	Y:  -1536  	Z:  11968		X: 4.03 	Y: -0.98 	Z: 7.13 m/s^2 

X:  3168  	Y:  464  	Z:  16336		X: 1.64 	Y: 0.27 	Z: 9.78 m/s^2 

X:  -224  	Y:  -832  	Z:  16320		X: 0.16 	Y: -0.34 	Z: 9.82 m/s^2 

X:  176  	Y:  -80  	Z:  15968		X: 0.11 	Y: -0.09 	Z: 9.41 m/s^2 

X:  1376  	Y:  -1040  	Z:  15968		X: 0.75 	Y: -0.41 	Z: 9.57 m/s^2 


Part E. Logging values to the EEPROM and reading them back
1. Reading and writing values to the Arduino EEPROM
The sample code in File->Examples->EEPROM shows functions from the Arduino EEPROM Library to write and read values to Arduino's EEPROM. This modified version of the SwitchState code employs these functions in three different states. Try it out.

a. Does it matter what actions are assigned to which state? Why?

b. Why is the code here all in the setup() functions and not in the loop() functions?

Each character in the string is a byte. That is, it takes 8-bits to encode a character, so the number of characters in the string we are writing is the number of bytes we are occupying in EEPROM. The Atmega 328P at the heart of the Arduino has 1024 bytes of internal EEPROM Memory (which is separate from the 32KB of Program memory it has for the code it is running.)

c. How many byte-sized data samples can you store on the Atmega328?

d. How would you get analog data from the Arduino analog pins to be byte-sized? How about analog data from the I2C devices?

e. Alternately, how would we store the data if it were bigger than a byte? (hint: take a look at the EEPROMPut example)

Modify the code to take in analog values from your sensors and print them back out to the Arduino Serial Monitor.

2. Design your logger
You've been thinking at a high level about a data logger and what it is used for; now you need to adapt that to the specific implementation.

A lot of the art of data logging is being clever about how to use the sensor. Feel free to engage the teaching team for advice.

Your data logger will have two main modes: one where it logs data and another where it plays the data back. Think a little about what sensors you would like to log data from and how you would like to display your data. Create a state diagram sketch that indicates how you'd like to switch between one mode and the other, and also what you'd like the program to do in each state. This can help you decide what buttons or knobs might be useful for your design.

You might make changes to your design before this lab is complete.

a. Turn in a copy of your final state diagram.

Part G. Create your own data logger!
Now it's up to you to integrate the software and hardware necessary to interface with your data logger! Your logger should be able to record a stream of analog data (at a sample rate of your desire) and then play it back at some later point in time on your display of choice.

a. Record and upload a short demo video of your logger in action.
