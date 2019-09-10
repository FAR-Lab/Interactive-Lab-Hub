# IDD-Fa19-Lab1: Blink!

**A lab report by Eduardo Castillo**
## Part A. Set Up a Breadboard
![](http://nurburgcosmetics.com/WhatsApp%20Image%202019-09-09%20at%2011.06.48%20PM.jpeg)
\n
## Part B. Manually Blink a LED
\n
**a. What color stripes are on a 100 Ohm resistor?**
\n
 The stripes are brown, black, brown and gold.
 
**b. What do you have to do to light your LED?**
To light the LED, the push button has to be pushed.
## Part C. Blink a LED using Arduino
### 1. Blink the on-board LED
**a. What line(s) of code do you need to change to make the LED blink (like, at all)?**
The code does not need to be modified to get the LED to blink, provided the circuit is connected properly.
**b. What line(s) of code do you need to change to change the rate of blinking?**
Lines 34 and 36: delay(1000). Specifically, one needs to change the argument of the delay function from 1000 to a different integer value.
**c. What circuit element would you want to add to protect the board and external LED?**
 We could add a fuse (maybe an inductor?) to the output pin going into the LED.
**d. At what delay can you no longer *perceive* the LED blinking? How can you prove to yourself that it is, in fact, still blinking?**
A period of 10 miliseconds (I used "a" as a global variable = 10) definitely does the trick. I proved it to myself that it was still blinking by creating two more iterations of blinking. One iteration had a period of 1*a =1* 10 = 10(miliseconds), a second iteration had a period of 10*10 = 100(miliseconds) and a third one had a period of 100*10 = = 1000(miliseconds). Since I could see iterations 2 and 3, iteration 1 must be occurring in the loop function even if it is not visible to the naked eye because of sampling rate limitations. I also created a integer variable "count" and added 1 every time the loop was completed. Then I printed its output on the serial monitor. That is kind of an indirect way to verify the loop was executing but worth considering too as a sanity check. 
**e. Modify the code to make your LED blink your way. Save your new blink code to your lab 1 repository, with a link on the README.md.**
https://github.com/joAQUINCE/IDD_lab_1/blob/master/sketch_castillo.ino
### 2. Blink your LED
**Make a video of your LED blinking, and add it to your lab submission.**
https://youtu.be/PYxz3WwDUgQ
## Part D. Manually fade an LED
**a. Are you able to get the LED to glow the whole turning range of the potentiometer? Why or why not?**
Yes, it glows at different intensities over the full range. My though is that even though the resistance gets really high –to the point where the resistors should be¬ drawing all the voltage–, the forward voltage across the LED would need to reach at least ~1.8 volts for current to continue to flow, even as resistance is increased. So, forward voltage would build up if the LED is not drawing enough voltage to maintain current flowing, which would cause it to light up and draw the voltage it needs to maintain current flowing.
Based on my readings using analog input A3, 1.8 is the minimum voltage that can be attained with the potentiometer, point after which increasing the resistance no longer impacts the voltage drop across the LED.
https://www.youtube.com/watch?v=FFjn94S0WWs
## Part E. Fade an LED using Arduino
**a. What do you have to modify to make the code control the circuit you've built on your breadboard?**
The output pin for PWM needs to be changed  to Pin 11 in the Arduino IDE. 
https://www.youtube.com/watch?v=vzFAC1Ba35M
**b. What is analogWrite()? How is that different than digitalWrite()?**
analogWrite uses Pulse Width Modulation to regulate perceived intensity of LED light using a 0-255 (8 bit) resolution between zero and full pulse width.
digitalWrite just takes two values: 0(Digital Low) or 5 volts(Digital High).
## Part F. FRANKENLIGHT!!!

### 1. Take apart your electronic device, and draw a schematic of what is inside. 

**a. Is there computation in your device? Where is it? What do you think is happening inside the "computer?"**
Yes, there is a Bluetooth audio receiver on the circuit. Digital signals from the connected device are being received and converted into analog audio signals at appropriate frequencies and amplitudes for the speaker. There is also a 5W digital power amplifier (XPT8871)
**b. Are there sensors on your device? How do they work? How is the sensed information conveyed to other portions of the device?**
Yes, the Bluetooth audio receiver senses signals in the Bluetooth frequency range (2.45 GHz). When a successful connection is established, the speaker output (i.e.: music) is delivered based on the signals received from the connected device.  There are also push buttons that translate user inputs into changes in state of speaker (i.e.: increase/decrease volume) and changes in state of the connected device (i.e.: play/pause music).
**c. How is the device powered? Is there any transformation or regulation of the power? How is that done? What voltages are used throughout the system?**
The device is battery powered via a rechargeable 5VDC battery. There are external push buttons that regulate the output power of the speaker between 0 and 5W (peak).
**d. Is information stored in your device? Where? How?**
Yes, the name of the device is stored somewhere in the device’s ROM. Also, some default sounds to provide user feedback as well as a counter for idle self shut off are programmed into memory. Fundamentally, I should be some binary encoding in memory that is decoded into the appropriate outputs or changes in state.


### 2. Using your schematic, figure out where a good point would be to hijack your device and implant an LED.

**Describe what you did here.**

I took appart the Bluetooth speaker and found that the actual coil impedance was 4 Ohms, with a maximum power of 5 Watts (peak) . Based on that, I calculted a max current of about 1.12 amps, equivalent to about 4.5 volts (peak). 

At that point, I was pretty confident that connecting the LED in parallel would be safe in terms of loads to the XPT8871 power amplifier and the LED

### 3. Build your light!

**Make a video showing off your Frankenlight.**

https://www.youtube.com/watch?v=fZuKcc2cGpU

**Include any schematics or photos in your lab write-up.**

![](http://nurburgcosmetics.com/Schematic.jpg)

