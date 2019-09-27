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

#include <EEPROM.h>

struct MyObject {
  float field1;
  byte field2;
  char name[10];
};


void setup() {

  lis.begin(0x18);
  display.begin(SSD1306_SWITCHCAPVCC, 0x3C);
  
  lis.setRange(LIS3DH_RANGE_4_G);   // 2, 4, 8 or 16 G!
  
}

void loop() {
  // put your main code here, to run repeatedly:
  display.clearDisplay();
  display.setCursor(0,0);
  display.setTextColor(WHITE);

  sensors_event_t event; 
  lis.getEvent(&event);

  long babyx = event.acceleration.x;
  long babyy = event.acceleration.y;
  long babyz = event.acceleration.z;   
  
  /* Display the results (acceleration is measured in m/s^2) */
  display.print("\t\tX: "); display.print(babyx);
  display.print(" \tY: "); display.print(babyy); 
  display.print(" \tZ: "); display.print(babyz); 
  display.println(" m/s^2 ");

  display.display();
  //delay(200); 

// EEPROM starts here

  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }

  float f = 123.456f;  //Variable to store in EEPROM.
  int eeAddress = 0;   //Location we want the data to be put.


  //One simple call, with the address first and the object second.
  EEPROM.put(eeAddress, f);

  Serial.println("Written float data type!");

  /** Put is designed for use with custom structures also. **/

  //Data to store.
  MyObject customVar = {
    babyx,
    babyy,
    babyz
  }; "Working!";

  eeAddress += sizeof(float); //Move address to the next byte after float 'f'.

  EEPROM.put(eeAddress, customVar);
  Serial.print("Written custom data type! \n\nView the example sketch eeprom_get to see how you can retrieve the values!");
  Serial.print(babyx); 
  Serial.print(babyy); 
  Serial.print(babyz);
}
