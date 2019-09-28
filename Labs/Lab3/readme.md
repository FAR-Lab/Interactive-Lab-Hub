# Data Logger (and using cool sensors!)

*A lab report by John Q. Student.*

## In The Report

Include your responses to the bold questions on your own fork of [this lab report template](https://github.com/FAR-Lab/IDD-Fa18-Lab2). Include snippets of code that explain what you did. Deliverables are due next Tuesday. Post your lab reports as README.md pages on your GitHub, and post a link to that on your main class hub page.

For this lab, we will be experimenting with a variety of sensors, sending the data to the Arduino serial monitor, writing data to the EEPROM of the Arduino, and then playing the data back.

## Part A.  Writing to the Serial Monitor
 
**a. Based on the readings from the serial monitor, what is the range of the analog values being read?**
 The range of analogous values being read should be between 0 VDC and 4.985 VDC, based on the Serial Monitor readings of 0-1020. Ideally, (i.e.: if zero or infinite resistance were achievable) the Serial Monitors readings would range from 0 to 1023 (1024 different values, corresponding to a binary resolution of 10 bits).
**b. How many bits of resolution does the analog to digital converter (ADC) on the Arduino have?**
The analog to digital converter (ADC) on the Arduino has resolution of 10 bits.
## Part B. RGB LED

**How might you use this with only the parts in your kit? Show us your solution.**
https://www.youtube.com/watch?v=PgsvFvJrpX8
/*
Adafruit Arduino - Lesson 3. RGB LED
*/
 
int redPin = 11;
int greenPin = 10;
int bluePin = 9;
 
//uncomment this line if using a Common Anode LED
#define COMMON_ANODE
 
void setup()
{
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);  
}
 
void loop()
{
  setColor(255, 0, 0);  // red
  delay(1000);
  setColor(0, 255, 0);  // green
  delay(1000);
  setColor(0, 0, 255);  // blue
  delay(1000);
  setColor(255, 255, 0);  // yellow
  delay(1000);  
  setColor(80, 0, 80);  // purple
  delay(1000);
  setColor(0, 255, 255);  // aqua
  delay(1000);
}
 
void setColor(int red, int green, int blue)
{
  #ifdef COMMON_ANODE
    red = 255 - red;
    green = 255 - green;
    blue = 255 - blue;
  #endif
  analogWrite(redPin, red);
  analogWrite(greenPin, green);
  analogWrite(bluePin, blue);  
}

## Part C. Voltage Varying Sensors 
 
### 1. FSR, Flex Sensor, Photo cell, Softpot
**a. What voltage values do you see from your force sensor?**
The voltage values range from 5 VDC (at zero force) to about 0.15 VDC (applying full force with my fingers).
**b. What kind of relationship does the voltage have as a function of the force applied? (e.g., linear?)**
I believe the relationship is of the form R = k/F, where R is resistance, k is an arbitrary constant (linked to the design of the FSR) and F is the force applied. Hence, voltage would drop asymptotically from 5 VDC (no force) to approach 0 VDC (asymptotically) as the force applied increases.   
**c. Can you change the LED fading code values so that you get the full range of output voltages from the LED when using your FSR?**
Yes, the modified code is below along with a video to the working circuit.
/*
Adafruit Arduino - Lesson 3. RGB LED
*/
 
int redPin = 11;
int greenPin = 10;
int bluePin = 9;
int FSR_range = 1023-31;
float FSR_READ_PIN = A0;
int k = 1023;
int red;
int green;
int blue;
//uncomment this line if using a Common Anode LED
#define COMMON_ANODE
 
void setup()
{
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);  
}
 
void loop()
{
  k = FSR_range/analogRead(FSR_READ_PIN);
    #ifdef COMMON_ANODE
      red = 255 * k;
      green = 255 * k;
      blue = 255 * k;
    #endif
  analogWrite(redPin, red);
  analogWrite(greenPin, green);
  analogWrite(bluePin, blue);  

 


  }

https://www.youtube.com/watch?v=33CFScawCwQ


**d. What resistance do you need to have in series to get a reasonable range of voltages from each sensor?**
flex sensor: about 250kohm or higher (to get enough resolution because the sensor only goes down to about 25kohm when straight)
photo cell: about 30kohm or higher(to get enough resolution because the sensor only goes down to about 5kohm when exposed to light)
softpot: a 1 kohm would do the trick here (to limit current through Arduino) because this sensor goes from about 0 ohms to about 10 kohm depending on where it is pressed.

**e. What kind of relationship does the resistance have as a function of stimulus? (e.g., linear?)**
flex sensor: resistance it seems to increase hyperbolically with angle of bend 
photo cell: seems to be somewhat linear with respect to intensity of radiation in the visible spectrum
softpot: very linear with respect to what location of the softpot is pressed.

### 2. Accelerometer
 
// Basic demo for accelerometer readings from Adafruit LIS3DH

#include <Wire.h>
#include <SPI.h>
#include <LiquidCrystal.h>

#include <Adafruit_LIS3DH.h>
#include <Adafruit_Sensor.h>

// Used for software SPI
#define LIS3DH_CLK A5
#define LIS3DH_MISO A4
#define LIS3DH_MOSI 11
// Used for hardware & software SPI
#define LIS3DH_CS 10

// software SPI
//Adafruit_LIS3DH lis = Adafruit_LIS3DH(LIS3DH_CS, LIS3DH_MOSI, LIS3DH_MISO, LIS3DH_CLK);

// hardware SPI
//Adafruit_LIS3DH lis = Adafruit_LIS3DH(LIS3DH_CS);

// I2C
Adafruit_LIS3DH lis = Adafruit_LIS3DH();

// initialize the library by associating any needed LCD interface pin
// with the arduino pin number it is connected to
const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);
unsigned long previousMillis = 0;
int wait = 500; 
void setup(void) {
#ifndef ESP8266
  while (!Serial);     // will pause Zero, Leonardo, etc until serial console opens
#endif

  Serial.begin(9600);
  Serial.println("LIS3DH test!");
  
  if (! lis.begin(0x18)) {   // change this to 0x19 for alternative i2c address
    Serial.println("Couldnt start");
    while (1);
  }
  Serial.println("LIS3DH found!");
  
  lis.setRange(LIS3DH_RANGE_4_G);   // 2, 4, 8 or 16 G!
  
  Serial.print("Range = "); Serial.print(2 << lis.getRange());  
  Serial.println("G");

  lcd.begin(16, 2);
  // Print a message to the LCD.
  //lcd.print("hello, world!");
}

void loop() {
    unsigned long currentMillis = millis();
  lis.read();      // get X Y and Z data at once
//  // Then print out the raw data
//  Serial.print("X:  "); Serial.print(lis.x); 
//  Serial.print("  \tY:  "); Serial.print(lis.y); 
//  Serial.print("  \tZ:  "); Serial.print(lis.z); 

  /* Or....get a new sensor event, normalized */ 
  sensors_event_t event; 
  lis.getEvent(&event);
  
//  /* Display the results (acceleration is measured in m/s^2) */
//  Serial.print("\t\tX: "); Serial.print(event.acceleration.x);
//  Serial.print(" \tY: "); Serial.print(event.acceleration.y); 
//  Serial.print(" \tZ: "); Serial.print(event.acceleration.z); 
//  Serial.println(" m/s^2 ");
//
//  Serial.println();
// 
//  delay(200);
  
  // Turn off the display:
 // lcd.noDisplay();
previousMillis = millis();
lcd.clear();
lcd.print(" X Acceleration");
lcd.setCursor(0, 1);
lcd.print("is: "); 
lcd.print(event.acceleration.x);
lcd.print("m/sec^2. ");

while ( millis() - previousMillis <wait){

lcd.noDisplay();
}
while ( millis() - previousMillis <2*wait){
lcd.display();
}

previousMillis = millis();
lcd.clear();
lcd.print(" Y Acceleration");
lcd.setCursor(0, 1);
lcd.print("is: "); 
lcd.print(event.acceleration.y);
lcd.print("m/sec^2. ");

while ( millis() - previousMillis <wait){

lcd.noDisplay();
}
while ( millis() - previousMillis <2*wait){
lcd.display();
}

previousMillis = millis();
lcd.clear();
lcd.print(" Z Acceleration");
lcd.setCursor(0, 1);
lcd.print("is: "); 
lcd.print(event.acceleration.z);
lcd.print("m/sec^2. ");

while ( millis() - previousMillis <wait){

lcd.noDisplay();
}
while ( millis() - previousMillis <2*wait){
lcd.display();
}


}


## Optional. Graphic Display

/**************************************************************************
 This is an example for our Monochrome OLEDs based on SSD1306 drivers

 Pick one up today in the adafruit shop!
 ------> http://www.adafruit.com/category/63_98

 This example is for a 128x32 pixel display using I2C to communicate
 3 pins are required to interface (two I2C and one reset).

 Adafruit invests time and resources providing this open
 source code, please support Adafruit and open-source
 hardware by purchasing products from Adafruit!

 Written by Limor Fried/Ladyada for Adafruit Industries,
 with contributions from the open source community.
 BSD license, check license.txt for more information
 All text above, and the splash screen below must be
 included in any redistribution.
 **************************************************************************/

#include <SPI.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128 // OLED display width, in pixels
#define SCREEN_HEIGHT 32 // OLED display height, in pixels

// Declaration for an SSD1306 display connected to I2C (SDA, SCL pins)
#define OLED_RESET     4 // Reset pin # (or -1 if sharing Arduino reset pin)
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

#define NUMFLAKES     10 // Number of snowflakes in the animation example

#define LOGO_HEIGHT   16
#define LOGO_WIDTH    16
static const unsigned char PROGMEM logo_bmp[] =
{ B00000000, B11000000,
  B00000001, B11000000,
  B00000001, B11000000,
  B00000011, B11100000,
  B11110011, B11100000,
  B11111110, B11111000,
  B01111110, B11111111,
  B00110011, B10011111,
  B00011111, B11111100,
  B00001101, B01110000,
  B00011011, B10100000,
  B00111111, B11100000,
  B00111111, B11110000,
  B01111100, B11110000,
  B01110000, B01110000,
  B00000000, B00110000 };

int val;
void setup() {
  Serial.begin(9600);

  // SSD1306_SWITCHCAPVCC = generate display voltage from 3.3V internally
  if(!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) { // Address 0x3C for 128x32
    Serial.println(F("SSD1306 allocation failed"));
    for(;;); // Don't proceed, loop forever
  }

  // Show initial display buffer contents on the screen --
  // the library initializes this with an Adafruit splash screen.
  display.display();
  delay(2000); // Pause for 2 seconds

  // Clear the buffer
  display.clearDisplay();

  // Draw a single pixel in white
  display.drawPixel(10, 10, WHITE);

  // Show the display buffer on the screen. You MUST call display() after
  // drawing commands to make them visible on screen!
  display.display();
  delay(2000);
  // display.display() is NOT necessary after every single drawing command,
  // unless that's what you want...rather, you can batch up a bunch of
  // drawing operations and then update the screen all at once by calling
  // display.display(). These examples demonstrate both approaches...

 

  testscrolltext();    // Draw scrolling text


  // Invert and restore display, pausing in-between
  display.invertDisplay(true);
  delay(1000);
  display.invertDisplay(false);
  delay(1000);

 // testanimate(logo_bmp, LOGO_WIDTH, LOGO_HEIGHT); // Animate bitmaps
}

void loop() {
  testscrolltext();
}

void testscrolltext(void) {
  val = analogRead(A0);
  display.clearDisplay();

  display.setTextSize(2); // Draw 2X-scale text
  display.setTextColor(WHITE);
  display.setCursor(10, 0);
  display.println(val);

  display.display();      // Show initial text
  delay(100);
}

## Part D. Logging values to the EEPROM and reading them back
 
### 1. Reading and writing values to the Arduino EEPROM

**a. Does it matter what actions are assigned to which state? Why?**
Yes, because a user would want to make sure that specific actions are performed within a certain range or position of the potentiometer.
**b. Why is the code here all in the setup() functions and not in the loop() functions?**
Because the  "SwitchState2" script calls the different state functions once, runs through the control flow once and then breaks (to check the new potentiometer value). If we had the state functions contained loops, then, once one state was read, the state function would enter the loop and never return the control flow back to the main function so that the potentiometer value could be updated and the appropriate new state entered.
**c. How many byte-sized data samples can you store on the Atmega328?** 
1024 data samples can be stored on the Atmega328.
Each character in the string is a byte. That is, it takes 8-bits to encode a character, so the number of characters in the string we are writing is the number of bytes we are occupying in EEPROM. The Atmega 328P at the heart of the Arduino has 1024 bytes of internal EEPROM Memory (which is separate from the 32KB of Program memory it has for the code it is running.)
**d. How would you get analog data from the Arduino analog pins to be byte-sized? How about analog data from the I2C devices?** Bytes are composed of a given number of bits, which are pulses sent at a certain frequency, and encode a 0 or 1 logical value (for low and high). Therefore, by sending signals that follow that frequency and encode logical values of interest, we could enable communication between an analog pin and external equipment –such as encoding an address for an I2C device.
**e. Alternately, how would we store the data if it were bigger than a byte? (hint: take a look at the [EEPROMPut](https://www.arduino.cc/en/Reference/EEPROMPut) example)** The EEPROM Library includes the put() method, which allows the user to specify an specific address they would want to write to. This way, data larger than one byte can be stored at different locations of the Atmega 328P EEPROM.
**Upload your modified code that takes in analog values from your sensors and prints them back out to the Arduino Serial Monitor.**
#include <EEPROM.h>
const int EEPROMSIZE=1024;
const int storePin = 2;
const int sensorPin = A0;    // select the input pin for the potentiometer

volatile int pushButtom = 0;

int ledPin = LED_BUILTIN;  

void setup() {
  // initialize serial communication:
  Serial.begin(9600);
    
  pinMode(ledPin, OUTPUT);
  pinMode(storePin,INPUT); 
  pinMode(sensorPin,INPUT);
  attachInterrupt(digitalPinToInterrupt(2), ISR1, FALLING);
}

void loop() {
  if (EEPROM.read(0) == 1){
    Serial.println(EEPROM.read(0));
    
  digitalWrite(ledPin,HIGH);}
  else {
    digitalWrite(ledPin,LOW);
  }
}

void ISR1(){
  Serial.println("ISR is running");
  EEPROM.write(0,0);
  pushButtom = digitalRead(storePin);
Serial.println(digitalRead(sensorPin));
if (digitalRead(sensorPin) == 0){
  EEPROM.write(0,1);
  }  
  }


### 2. Design your logger
 

![](http://nurburgcosmetics.com/IDD_Finite_State_Diagram.png)

### 3. Create your data logger!
 
**a. Record and upload a short demo video of your logger in action.**
