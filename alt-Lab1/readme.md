This lab is a merge of what is originally [Lab 1](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/wiki/Lab-01) and [Lab 2](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/wiki/Lab-02) of the curriculum. This is meant for students who have had this curriculum before. If you have little experience with electronics, breadboarding, Arduino programming or the Arduino hardware, please work on [Lab 1](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/wiki/Lab-01)!

The [alt-pre-Lab](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/wiki/Alt-Pre---Lab-1) helps you to get set up in advance of in-class lab. 

## In The Report
For the report, make a copy of this wiki page for your own repository, and then delete everything but the headers and the sections between the **stars**. Write the answers to the questions under the starred sentences. Include snippets of code that explain what you did.

Deliverables are due next Tuesday. Post a link to the wiki page on your main class hub page.

# Part I
# Light It Up
 
## Overview
For this assignment, you are going to 

A) [Set up a breadboard](#part-a-set-up-a-breadboard) 

B) [Manually blink a LED](#part-b-manually-blink-a-led) 

C) [Blink a LED using the Arduino](#part-c-blink-a-led-using-arduino)

D) [Manually fade a LED](#part-d-manually-fade-a-led) 

E) [Fade a LED using Arduino](#part-e-fade-a-led-using-arduino)


## Part A. Set Up a Breadboard

For this lab, we'll be using the [Adafruit Metro Mini](https://www.adafruit.com/product/2590) development board as our hardware platform. This board is a derivative of the [Arduino UNO R3](https://store.arduino.cc/usa/arduino-uno-rev3). 

You should have already have installed the [Arduino software](http://arduino.cc/en/Main/Software) on your laptop.

Wire the power rails of your breadboard so that the red rails are connected to the +5V pin of the Metro Mini, and the blue or black rails are connected to the GND pin.  

<img src="https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/docs/breadboard_setup.png" width=400>

**Include a picture of your own breadboard in the report. (We trust you to plug the Metro Mini and wires in properly. This is really practice for including images in your reports.)**

## Part B. Manually Blink a LED

With the Arduino unplugged, build the circuit below. You can use any color LED. 

<img src="https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/docs/button_led_resistor.png" width=300>

If you need a diagram of what this looks like on your board, [here's a hint](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/docs/button_led_resistor_diagram.png)

If your button doesn’t work, check that it’s oriented as shown below. You might need to rotate it by 90 degrees. 

![Button image](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/docs/button_image.png)

A typical pushbutton, when pressed, connects the 2 pins on one side to the 2 pins on the other side.
**a. What color stripes are on a 220 Ohm resistor?**

Connect the Metro Mini to your computer using the USB cable. The green LED on top of the Arduino should light.

Does your LED light? Why not? What do you have to do to light the LED?
 
**b. What do you have to do to light your LED?**

## Part C. Blink a LED using Arduino

(Do not deconstruct what you have set up on your breadboard until you find it necessary! For instance, don't undo the LED and button setup that you did in Part B when you start doing Part C.)

### 1. Blink the on-board LED
Arduino boards typically come preloaded with a version of the Blink program on it. This code lets its L LED (connected on pin 13) blink as soon as the USB cable starts powering the board. Let us modify that program.

Launch the Arduino application on your computer. It will open to the template of a new empty sketch. Here is what it looks like:

<img src="https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/docs/arduino_window.png" width=300>

Check out the Blink example code: [File->Examples->Basics->Blink](https://www.arduino.cc/en/Tutorial/Blink). 

**a. What line(s) of code do you need to change to make the LED blink (like, at all)?**

**b. What line(s) of code do you need to change to change the rate of blinking?**

**c. What circuit element would you want to add to protect the board and external LED?**

To compile and upload your code, take the following steps (note that 1, 2 should only have to be done once):
1) In the Arduino IDE, select the board we are using: Tools -> Board -> Arduino/Genuino UNO 
2) You may also have to select a communications (or COM) port (Tools -> Port ->  Serial Port). The port should be something like `/dev/cu.SLCA_USBtoUART` (on MAC) `/dev/ttyUSB0` (on Linux), or `COM3` (on Windows, could be another number). If they are not showing up, make sure you've installed the [SiLabs CP210x drivers](http://www.silabs.com/products/mcu/pages/usbtouartbridgevcpdrivers.aspx).
3) To compile your code, click on the "checkmark" on the upper far left of the Arduino development window.
4) To upload compiled code to the Arduino, click on "right arrow" besides the "checkmark."
5) When the code is uploaded, the Arduino should automatically start running your new code.

Change the `delay` parameter to modify blink rate of your LED to make it blink faster.

**d.  At what delay can you no longer *perceive* the LED blinking? (And how can you prove to yourself that it is, in fact, still blinking?**

Modify the code to make your LED blink *your way*. 

**e. Save your new blink code to your lab 1 repository, with a link on the Lab report wiki page.**

### 2. Blink your LED

Now modify the circuit and program so that you can blink an external LED on pin 9.

<img src="https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/docs/arduino_led_resistor_schematic.png" width=300>

![Arduino LED resistor schematic](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/docs/arduino_led_resistor_schematic.png)

**Make a video of your LED blinking, and add it to your lab submission.**

## Part D. Manually fade a LED

Set up the following circuit, and try making the LED glow brighter and dimmer.

<img src="https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/docs/led_pot_schematic.png" width=300>

**a. Are you able to get the LED to glow the whole turning range of the potentiometer? Why or why not?**

## Part E. Fade a LED using Arduino

The Arduino cannot output an analog voltage, only 0 or 5Vs. So how can we fade an LED using the Arduino?

The fading light is done using pulse width modulation, or PWM. The LED is toggled on and off very quickly: say, 1,000 times per second. Much faster than your eye can follow.

The percentage of time that the LED is on (called the duty cycle) controls its apparent brightness.

Update your circuit so the jumper wire connects to pin 11. (To control an LED using PWM, you have to connect it to one of the pins that supports PWM (not all do!).

<img src="https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/docs/arduino_led_fade_schematic.png" width=300>

Here's a [hint diagram](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/docs/arduino_led_fade.png) if you need it.

On your computer, in the Arduino IDE, open the Fade sketch (File > Examples > 01.Basics > Fade ).

Look at the code.

**a. What do you have to modify to make the code control the circuit you've built on your breadboard?**

**b. What is analogWrite()? How is that different than digitalWrite()?**

Now upload your sketch and check that the LED fades on and off. Try changing a few parameters to make your own funky lighting pattern.

_Super awesome circuit schematics by [David Sirkin](https://me.stanford.edu/people/david-sirkin). Thanks David!_


# Part II

# Make a Digital Timer!
 
## Overview
For this assignment, you are going to 

A) [Solder your OLED display](#part-a-solder-your-oled)

B) [Make a lowly Multimeter](#part-b-make-a-lowly-multimeter)

c) [Using a time-based digital sensor!](#part-c-using-a-time-based-digital-sensor)

D) [Make your Arduino sing!](#part-d-make-your-arduino-sing)

E) [Make your own timer](#part-e-make-your-own-timer) 


## Part A. Solder your OLED

<img src=https://images-na.ssl-images-amazon.com/images/I/61cvqA%2BY0OL._SL1200_.jpg alt="OLED display" width=400>

We will use an I2C OLED display for this lab. We will discuss more about what I2C is, but for now:
Hook up:
* GND to ground
* Vcc to +5V
* SDA to A4
* SCL to A5

Before you run the code, you should install two new libraries to your Arduino IDE. The first one can be found by going to `Tools > Manage Libraries > Search Adafruit GFX Library`. The second one can be found by `Tools > Manage Libraries > Search Adafruit SSD 1306`. Once you have installed them, you can run the sample code by going to `File > Examples > Adafruit SSD 1306 > ssd1306_128x32_i2c`. 

a. Modify the example code so that you can print out the output of the A0 pin. Include your code in your lab report.
**If you have never soldered before, we're happy to show you how! PLEASE ASK!!**

## Part B. Make a lowly Multimeter
Incorporate the LCD into with this [AnalogInput code](https://www.arduino.cc/en/tutorial/AnalogInput) (this can found in the Examples code under 03.Analog->AnalogInput) so that you can read out the exact analog value that you are reading in on Analog Pin 0 and write it to your LCD. It's your own voltmeter! 

**e. Include a copy of your Lowly Multimeter code in your lab write-up.**

<!-- Now build a circuit with two FSR sensors (one from your self and one borrowed from a fellow student) to enable a game of thumb wrestling. Use the LCD to indicate who is squeezing their FSR harder!

**f. Include a copy of your FSR thumb wrestling code in your lab write-up.** -->

Leave your LCD set up for the rest of Lab, and leave it set up when you finish Lab, as we'll use the display again next week.



## Part C. Using a time-based digital sensor

![Rotary Encoder](https://cdn-shop.adafruit.com/1200x900/377-02.jpg)
We have a high-quality 24 pulse encoder with knob and nice, click-y rotation detents.
 
[Product Page](https://www.adafruit.com/product/377)
[Datasheet](https://cdn-shop.adafruit.com/datasheets/pec11.pdf)
 
Like a potentiometer, a rotary encoder has 3 pins; unlike a potentiometer, an encoder can be spun round and round without stop. Rotary encoders use [quadrature](http://en.wikipedia.org/wiki/Rotary_encoder) to tell how fast and in which direction you are turning a knob. To connect the encoder to your breadboard, you can insert three pins directly into motherboard like picture below.
 
The circuit below is the "correct" way of hooking up a rotary encoder with your Arduino; the resistors and capacitors help to filter out noise from the mechanical operation of the encoder - this circuit diagram is from the datasheet.

[[https://ccrma.stanford.edu/wiki/images/c/c1/Encoder_filter.png]]
 
However, to _actually_ hook up your encoder, just use the 3-pin side. Hook the middle to ground, and the "A" and "B" pins to digital pins 6 and 7 of your Arduino.
 
What is going on in this circuit? The Phase A and Phase B pins actually behave like switches, so the pins have pull-ups so that they will be high by default, until they are pulled low by the encoder (your Arduino actually uses its own internal pull-ups). The resistor and capacitor combo also forms a low-pass circuit to eliminate stray voltage spikes that might occur from the quick switching (this is called "debouncing"). You can use any capacitor that is up to an order of magnitude away from the 10nF value.
 
Use [this rotary encoder code](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/wiki/Rotary-Encoder-test-Code) to see if you have hooked the encoder up correctly! You should see data coming in on the serial monitor -- which you can open by clicking on the magnifying glass icon in the upper-right corner of the Arduino window (or by going to `Tools` > `Serial Monitor` in the menu).

## Part D. Make your Arduino sing!

Let's make the Arduino make some noise! We are going to start with the Tone example program:
 
`Examples->Digital->toneMelody`

The official Arduino tutorial for this code is [here](https://www.arduino.cc/en/Tutorial/ToneMelody?from=Tutorial.Tone)
Add a 75 Ohm resistor to limit the current to the speaker when you hook it up on your breadboard. If you would like it a little louder, you can use a lower value resistor, up to a minimum of 5 Ohms.

Wire it to your circuit with the - to ground and the + to Arduino Micro pin 8. 

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
 
## Part E. Make your own timer

Make a timer that uses any of the input devices to set a time, and then automatically (or manually, if you prefer) begin counting down, displaying the time left. Make your timer show an alert once the time is up with one of the output devices we connected during this lab, or you have available. (Hint: the sample code for [Examples->LiquidCrystal->HelloWorld](https://www.arduino.cc/en/Tutorial/HelloWorld) displays the time in seconds since the Arduino was reset...)
 
Note that for some of you, the time may seem to be decremented by 10 each second (that is, from 670=>660). Why is this? Do you think it's a hardware or software issue? Think about how 100 vs. 99 is written to the screen, and ask an instructor.

**a. Make a short video showing how your timer works, and what happens when time is up!**

**b. Post a link of the completed lab report to your GitHub repo.**
