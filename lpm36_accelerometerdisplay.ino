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

#include <Adafruit_LIS3DH.h>
#include <Adafruit_Sensor.h>

// I2C
Adafruit_LIS3DH lis = Adafruit_LIS3DH();


#define SCREEN_WIDTH 128 // OLED display width, in pixels
#define SCREEN_HEIGHT 32 // OLED display height, in pixels

// Declaration for an SSD1306 display connected to I2C (SDA, SCL pins)
#define OLED_RESET     4 // Reset pin # (or -1 if sharing Arduino reset pin)
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);


void setup() {

  lis.begin(0x18);
  display.begin(SSD1306_SWITCHCAPVCC, 0x3C);
  
  lis.setRange(LIS3DH_RANGE_4_G);   // 2, 4, 8 or 16 G!
  
}

void loop() {
  display.clearDisplay();
  display.setCursor(0,0);
  display.setTextColor(WHITE);

  
//  lis.read();      // get X Y and Z data at once
//    long babyx = (lis.x)/100;
//    display.print(babyx); 
  // Then print out the raw data
 // display.print("X:  "); display.print(lis.x); 
//  display.print("  \tY:  "); display.print(lis.y); 
//  display.print("  \tZ:  "); display.print(lis.z); 
//
//  /* Or....get a new sensor event, normalized */ 
  sensors_event_t event; 
  lis.getEvent(&event);

  long babyx = event.acceleration.x;
  long babyy = event.acceleration.y;
  long babyz = event.acceleration.z;

//  display.print(babyx);
//  display.print(babyy);
//  display.print(babyz);   
  
  /* Display the results (acceleration is measured in m/s^2) */
  display.print("\t\tX: "); display.print(babyx);
  display.print(" \tY: "); display.print(babyy); 
  display.print(" \tZ: "); display.print(babyz); 
  display.println(" m/s^2 ");

  display.display();
  //delay(200); 
}
