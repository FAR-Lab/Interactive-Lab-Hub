Alt Lab 1. Arduino Deep Dive

Part I

Light It Up

Overview

For this assignment, you are going to

A) Set up a breadboard

B) Manually blink a LED

C) Blink a LED using the Arduino

D) Manually fade a LED

E) Fade a LED using Arduino

Part A. Set Up a Breadboard



Part B. Manually Blink a LED



A typical pushbutton, when pressed, connects the 2 pins on one side to the 2 pins on the other side. 

a. What color stripes are on a 220 Ohm resistor?
Red-Red-Black for 2, 2, 0.

b. What do you have to do to light your LED?
* Connect the anode towards our 5V supply and the lead the cathode to the 220-ohm resistor and ground.

Part C. Blink a LED using Arduino

1. Blink the on-board LED

a. What line(s) of code do you need to change to make the LED blink (like, at all)?
* Changed the loop to set Pin 13 to HIGH.

b. What line(s) of code do you need to change the rate of blinking?
* The delay lines

c. What circuit element would you want to add to protect the board and external LED?
* Keep the 220-ohm resistor in series with the cathode of the LED and ground.
To compile and upload your code, take the following steps (note that 1, 2 should only have to be done once):

In the Arduino IDE, select the board we are using: Tools -> Board -> Arduino/Genuino UNO
You may also have to select a communications (or COM) port (Tools -> Port -> Serial Port). The port should be something like /dev/cu.SLCA_USBtoUART (on MAC) /dev/ttyUSB0 (on Linux), or COM3 (on Windows, could be another number). If they are not showing up, make sure you've installed the SiLabs CP210x drivers.
To compile your code, click on the "checkmark" on the upper far left of the Arduino development window.
To upload compiled code to the Arduino, click on "right arrow" besides the "checkmark."
When the code is uploaded, the Arduino should automatically start running your new code.
Change the delay parameter to modify blink rate of your LED to make it blink faster.

d. At what delay can you no longer perceive the LED blinking? (And how can you prove to yourself that it is, in fact, still blinking?
* Between 10 and 15 ms the blinking becomes imperceivable.

Modify the code to make your LED blink your way.

e. Save your new blink code to your lab 1 repository, with a link on the Lab report wiki page.

2. Blink your LED

Now modify the circuit and program so that you can blink an external LED on pin 9.


Arduino LED resistor schematic

Make a video of your LED blinking, and add it to your lab submission.

Part D. Manually fade a LED

Set up the following circuit, and try making the LED glow brighter and dimmer.


a. Are you able to get the LED to glow the whole turning range of the potentiometer? Why or why not?
Yes, but the LED shuts off about 1/3 of the way through the potentiometer's range likely due to the high resistance. 

Part E. Fade a LED using Arduino

The Arduino cannot output an analog voltage, only 0 or 5Vs. So how can we fade an LED using the Arduino?

The fading light is done using pulse width modulation, or PWM. The LED is toggled on and off very quickly: say, 1,000 times per second. Much faster than your eye can follow.

The percentage of time that the LED is on (called the duty cycle) controls its apparent brightness.

Update your circuit so the jumper wire connects to pin 11. (To control an LED using PWM, you have to connect it to one of the pins that supports PWM (not all do!).


Here's a hint diagram if you need it.

On your computer, in the Arduino IDE, open the Fade sketch (File > Examples > 01.Basics > Fade ).

Look at the code.

a. What do you have to modify to make the code control the circuit you've built on your breadboard?

b. What is analogWrite()? How is that different than digitalWrite()?
* analogWrite() makes use of Pulse Width Modulations. 

Part II

Make a Digital Timer!

Overview

For this assignment, you are going to

A) Solder your OLED display

B) Make a lowly Multimeter

c) Using a time-based digital sensor!

D) Make your Arduino sing!

E) Make your own timer

Part A. Solder your OLED

OLED display
We will use an I2C OLED display for this lab. We will discuss more about what I2C is, but for now: Hook up:

GND to ground
Vcc to +5V
SDA to A4
SCL to A5
Before you run the code, you should install two new libraries to your Arduino IDE. The first one can be found by going to Tools > Manage Libraries > Search Adafruit GFX Library. The second one can be found by Tools > Manage Libraries > Search Adafruit SSD 1306. Once you have installed them, you can run the sample code by going to File > Examples > Adafruit SSD 1306 > ssd1306_128x32_i2c.

a. Modify the example code so that you can print out the output of the A0 pin. Include your code in your lab report. If you have never soldered before, we're happy to show you how! PLEASE ASK!!

Part B. Make a lowly Multimeter

Incorporate the LCD into with this AnalogInput code (this can found in the Examples code under 03.Analog->AnalogInput) so that you can read out the exact analog value that you are reading in on Analog Pin 0 and write it to your LCD. It's your own voltmeter!

e. Include a copy of your Lowly Multimeter code in your lab write-up.

Leave your LCD set up for the rest of Lab, and leave it set up when you finish Lab, as we'll use the display again next week.

Part C. Using a time-based digital sensor

Rotary Encoder We have a high-quality 24 pulse encoder with knob and nice, click-y rotation detents.

Product Page Datasheet

Like a potentiometer, a rotary encoder has 3 pins; unlike a potentiometer, an encoder can be spun round and round without stop. Rotary encoders use quadrature to tell how fast and in which direction you are turning a knob. To connect the encoder to your breadboard, you can insert three pins directly into motherboard like picture below.

The circuit below is the "correct" way of hooking up a rotary encoder with your Arduino; the resistors and capacitors help to filter out noise from the mechanical operation of the encoder - this circuit diagram is from the datasheet.



However, to actually hook up your encoder, just use the 3-pin side. Hook the middle to ground, and the "A" and "B" pins to digital pins 6 and 7 of your Arduino.

What is going on in this circuit? The Phase A and Phase B pins actually behave like switches, so the pins have pull-ups so that they will be high by default, until they are pulled low by the encoder (your Arduino actually uses its own internal pull-ups). The resistor and capacitor combo also forms a low-pass circuit to eliminate stray voltage spikes that might occur from the quick switching (this is called "debouncing"). You can use any capacitor that is up to an order of magnitude away from the 10nF value.

Use this rotary encoder code to see if you have hooked the encoder up correctly! You should see data coming in on the serial monitor -- which you can open by clicking on the magnifying glass icon in the upper-right corner of the Arduino window (or by going to Tools > Serial Monitor in the menu).

Part D. Make your Arduino sing!

Let's make the Arduino make some noise! We are going to start with the Tone example program:

Examples->Digital->toneMelody

The official Arduino tutorial for this code is here Add a 75 Ohm resistor to limit the current to the speaker when you hook it up on your breadboard. If you would like it a little louder, you can use a lower value resistor, up to a minimum of 5 Ohms.

Wire it to your circuit with the - to ground and the + to Arduino Micro pin 8.

a. How would you change the code to make the song play twice as fast?

Now change the speed back, and replace the melody[] and noteDurations[] arrays with the following:

int melody[] = {
  NOTE_D3,NOTE_D3,NOTE_D3,NOTE_G3,NOTE_D4,NOTE_C4,NOTE_B3,NOTE_A3,NOTE_G4,NOTE_D4, \
  NOTE_C4,NOTE_B3,NOTE_A3,NOTE_G4,NOTE_D4,NOTE_C4,NOTE_B3,NOTE_C4,NOTE_A3,0};
 
int noteDurations[] = {
  10,10,10,2,2,10,10,10,2,4, \
  10,10,10,2,4,10,10,10,2,4};
You'll also have to increase the for() loop index max from 8 to 20:

 for (int thisNote = 0; thisNote < 20; thisNote++) {
b. What song is playing?

Part E. Make your own timer

Make a timer that uses any of the input devices to set a time, and then automatically (or manually, if you prefer) begin counting down, displaying the time left. Make your timer show an alert once the time is up with one of the output devices we connected during this lab, or you have available. (Hint: the sample code for Examples->LiquidCrystal->HelloWorld displays the time in seconds since the Arduino was reset...)

Note that for some of you, the time may seem to be decremented by 10 each second (that is, from 670=>660). Why is this? Do you think it's a hardware or software issue? Think about how 100 vs. 99 is written to the screen, and ask an instructor.

a. Make a short video showing how your timer works, and what happens when time is up!

b. Post a link of the completed lab report to your GitHub repo.
