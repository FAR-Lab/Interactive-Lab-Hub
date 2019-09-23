# Digital Timer
 
Include your responses to the bold questions below. Include snippets of code that explain what you did. Deliverables are due next Tuesday. Post your lab reports as README.md pages on your GitHub, and post a link to that on your main class hub page.

## Part A. Solder your LCD panel

![](http://nurburgcosmetics.com/lcd.jpg)

## Part B. Writing to the LCD
 
**a. What voltage level do you need to power your display?**
The voltage level needed to power the display is 5 VDC.

**b. What voltage level do you need to power the display backlight?**
The voltage level needed to power the display backlight is 3.3 VDC.
   
**c. What was one mistake you made when wiring up the display? How did you fix it?**
I didn't have the two halves of the breadboard connected on the ground side, which was required for it to work. I fixed this with the orange jumper between columns 30 and 31, pictured above.

**d. What line of code do you need to change to make it flash your name instead of "Hello World"?**
Line 50 would need to be changed from:
 lcd.print("hello, world!") 
to 
lcd.print("Eduardo Castillo");
 
**e. Include a copy of your Lowly Multimeter code in your lab write-up.**

// include the library code:

#include <LiquidCrystal.h>


// initialize the library by associating any needed LCD interface pin
// with the arduino pin number it is connected to

const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;

LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

int sensorPin = A0;    // select the input pin for the potentiometer

int ledPin = 13;      // select the pin for the LED

int sensorValue = 0;  // variable to store the value coming from the sensor

void setup() {

  // declare the ledPin as an OUTPUT:
  
  pinMode(ledPin, OUTPUT);

  // set up the LCD's number of columns and rows:
  
  lcd.begin(16, 2);
  
}

void loop() {

  // read the value from the sensor:
  
  sensorValue = analogRead(sensorPin);
  
  // turn the ledPin on
  
  digitalWrite(ledPin, HIGH);
  
  lcd.print("  ***The input is: ");
  
  lcd.print(sensorValue);
  
  lcd.print("***  ");

  // stop the program for <sensorValue> milliseconds:
  
  delay(sensorValue);
  
  // turn the ledPin off:
  
  digitalWrite(ledPin, LOW);
  
  // stop the program for for <sensorValue> milliseconds:
  
  delay(pow(sensorValue,.5));
  
}


## Part C. Using a time-based digital sensor

https://youtu.be/HOCfDjpOSZQ


## Part D. Make your Arduino sing!

**a. How would you change the code to make the song play twice as fast?**

Change the following:
int noteDuration = 1000 / noteDurations[thisNote] 
to
int noteDuration = 250 / noteDurations[thisNote];

 
**b. What song is playing?**

I think it is La Cucaracha.


## Part E. Make your own timer

**a. Make a short video showing how your timer works, and what happens when time is up!**

https://youtu.be/rXndz9NLDVQ
As you can see, when you 10 second countdown is up, the screen prints "Time is up!". I could have added more cool functionality (such as playing a sound with the speaker to mimic an alarm clock) but given my mom's health issues last week, I am trying to complete the labs as quickly and efficiently as possible while meeting the deliverable requirements. Nonetheless, the implemented solution can do a lot more just hardware added to breadboard and corresponding code.


**b. Post a link to the completed lab report your class hub GitHub repo.**
