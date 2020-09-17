const int LED = 9;

int brightness = 0;
int increment = 1;

void setup()
{
  // Pins driven by analogWrite do not need to be declared as outputs
}

void loop()
{
  if(brightness < 255)
  {
    increment = -1; // Count down from 255
  }
  else if(brightness < 1)
  {
    increment = 1; // Count up after getting below 0
  }
  brightness = brightness + increment; // increment or decrement based on value of +1 or -1

  // Writing brightness value to the LED
  analogWrite(LED, brightness);
  delay(10); // 10 ms step
}
