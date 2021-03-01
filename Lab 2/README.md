# The Clock of Pi

Does it feel like time is moving strangely during the pandemic?

For our first Pi project, we will pay homage to the [timekeeping devices of old](https://en.wikipedia.org/wiki/History_of_timekeeping_devices) by making simple clocks.

It is worth spending a little time thinking about how you mark time, and what would be useful in a clock of your own design.

## Acknowledgements and References

For this lab, I worked with Snigdha Singhania (ss4224). We worked in tandem on this project with group brainstorming as well as the actual building. 

A good deal of the images for our project were taken from external sources. These are credited below:
* Adafruit and Sparkfun API References were incredibly helpful for this lab
* [Sunrise Graphics](https://www.youtube.com/watch?v=JEEbmkDEQek)
* [Cheers Animation](https://www.youtube.com/watch?v=Gkb6bFdgSvM)
* [Soccer Animation](https://www.youtube.com/watch?v=TagGzVe1Xw0)
* [Goodnight Image](https://www.google.com/search?q=goodnight+cartoon&sxsrf=ALeKk00TRoLfzl6wrEQYCmJiSuwhtad6rA:1614306188304&tbm=isch&source=iu&ictx=1&fir=xyADWpXBPSBtmM%252CuYH3SdyNITyyeM%252C_&vet=1&usg=AI4_-kTyeizyNUFpTTtxMwJAu9keo2MQ6Q&sa=X&ved=2ahUKEwiKjKaXv4bvAhVJmuAKHclaDgUQ9QF6BAgTEAE&biw=1066&bih=1593#imgrc=xyADWpXBPSBtmM)
* [Go to Work Arrow](https://www.google.com/search?q=arrow+cartoon&sxsrf=ALeKk02MVPbAEMSeTQAq3d-l9WY6AJrikg:1614308797507&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiAlLvzyIbvAhXiUd8KHeLfBzoQ_AUoAXoECCgQAw&biw=1066&bih=1593#imgrc=ksTzXuZQQdDHGM)
* [Wine Time Image](https://www.google.com/search?q=wine+time&tbm=isch&ved=2ahUKEwjtl-LNlY7vAhWcC98KHasIB7kQ2-cCegQIABAA&oq=wine+time&gs_lcp=CgNpbWcQAzIECAAQQzICCAAyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADoFCAAQsQM6BAgjECc6CggAELEDEIMBEEM6BwgAELEDEEM6CAgAELEDEIMBUJqMAViPmAFgtZkBaABwAHgAgAFRiAHzBJIBATmYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=smE8YO32CJyX_AarkZzICw&bih=1593&biw=1600#imgrc=hLPWJJV5Y7elWM)

## Inventory List

The [parts list](partslist.md) lists all of the items I have received for this course and what things I am still missing.

## Overview

A) [Connect to the Pi](#part-a)  

B) [Try out cli_clock.py](#part-b) 

C) [Set up your RGB display](#part-c)

D) [Try out clock_display_demo](#part-d) 

E) [Modify the code to make the display your own](#part-e)

F) [Make a short video of your modified barebones PiClock](#part-f)

G) [Sketch and brainstorm further interactions and features you would like for your clock for Part 2](#part-g)

# Part 1: Testing and Planning
## Part A: Connect to the Raspberry Pi
Connecting to the pi and activating my working environment is achieved via the following commands:

```
sam@Sams-MacBook-Air ~ % ssh pi@100.64.4.253
pi@raspberrypi:~/Documents/Interactive-Lab-Hub$ cd Documents/Interactive-Lab-Hub
pi@raspberrypi:~/Documents/Interactive-Lab-Hub$ source circuitpython/bin/activate
(circuitpython) pi@raspberrypi:~/Documents/Interactive-Lab-Hub$ cd Lab\ 2
```

## Part B: Command Line Clock
The [command line clock](cli_clock.py) is run via the following command: 

```
(circuitpython) pi@raspberrypi:~/Documents/Interactive-Lab-Hub/Lab 2$ python cli_clock.py 
02/24/2021 11:20:49
```
and simply writes the current time on the command line (exited via CTRL+C) with update.

This functionality is shown below:

<p align="center"><img src="https://github.com/snlee159/Interactive-Lab-Hub/blob/Spring2021/Lab%202/cli_clock.gif" height="480"></p>

## Part C: Set up the RGB Display
The [Adafruit MiniPiTFT](https://www.adafruit.com/product/4393) is connected to the Raspberry Pi via the GPIO pins. <br>
<p align="center">
<img src="https://cdn-learn.adafruit.com/assets/assets/000/082/842/large1024/adafruit_products_4393_iso_ORIG_2019_10.jpg" height="480" />
</p>

### IO Options on the Raspberry Pi

The Raspberry Pi 4 has a variety of interfacing options. When you plug the pi in the red power LED turns on. Any time the SD card is accessed the green LED flashes. It has standard USB ports and HDMI ports. Less familiar it has a set of 20x2 pin headers that allow you to connect a various peripherals.

<p align="center">
<img src="https://maker.pro/storage/g9KLAxU/g9KLAxUiJb9e4Zp1xcxrMhbCDyc3QWPdSunYAoew.png" height="480" />
</p>

To learn more about any individual pin and what it is for go to [pinout.xyz](https://pinout.xyz/pinout/3v3_power) and click on the pin. 

### Installing the MiniPiTFT

Line up the screen and press it on the headers. The hole in the screen should match up with the hole on the raspberry pi.

<p align="center">
<img src="https://cdn-learn.adafruit.com/assets/assets/000/087/539/medium640/adafruit_products_4393_quarter_ORIG_2019_10.jpg?1579991932" height="200" />
<img src="https://cdn-learn.adafruit.com/assets/assets/000/082/861/original/adafruit_products_image.png" height="200">
</p>

### Testing the Screen

The display uses a communication protocol called [SPI](https://www.circuitbasics.com/basics-of-the-spi-communication-protocol/) to speak with the raspberry pi. The port on the bottom of the display connects to the SDA and SCL pins used for the I2C communication protocol. GPIO (General Purpose Input/Output) pins 23 and 24 are connected to the two buttons on the left. GPIO 22 controls the display backlight.

We can test it with the following command: 
```
(circuitpython) pi@raspberrypi:~/Documents/Interactive-Lab-Hub/Lab 2$ python screen_test.py
```

You can type the name of a color then press the top button to see the color you typed or the bottom button to see the color white. This functionality is shown below:

<p align="center"><img src="https://github.com/snlee159/Interactive-Lab-Hub/blob/Spring2021/Lab%202/screen_test.gif" width="600"></p>

### Displaying Info
By running the following command:
```
(circuitpython) pi@raspberrypi:~/Documents/Interactive-Lab-Hub/Lab 2$ python stats.py
```
we can see a list of the Raspberry Pi's statistics such as the CPU's temperature and the Pi's IP address:

<p align="center"><img src="https://github.com/snlee159/Interactive-Lab-Hub/blob/Spring2021/Lab%202/imgs/stats.png" width="480"></p>

### Displaying an image

Running `image.py` with the following command:
```
(circuitpython) pi@raspberrypi:~/Documents/Interactive-Lab-Hub/Lab 2$ python image.py
```
displays an image of the Cornell Tech logo:

<p align="center"><img src="https://github.com/singhaniasnigdha/Interactive-Lab-Hub/blob/Spring2021/Lab%202/imgs/cornell_tech_image.png" width="480"></p>

Similarly, `image_change.py` shows how we adjusted this code to switch between the Cornell Tech logo and one of the photos we intend to use for our clock's final functionality. Pressing button A shows the former while pressing button B shows the latter. 

<p align="center"><img src="https://github.com/singhaniasnigdha/Interactive-Lab-Hub/blob/Spring2021/Lab%202/imgs/image_change.gif" height="480" /></p>

## Part D: Set up the Display Clock Demo

`screen_clock.py` was copied into `display_clock.py` to show the basic clock functionality on the MiniPiTF. When run using the following command:
```
(circuitpython) pi@raspberrypi:~/Documents/Interactive-Lab-Hub/Lab 2$ python display_clock.py
```
we see the following output:

<p align="center"><img src="https://github.com/singhaniasnigdha/Interactive-Lab-Hub/blob/Spring2021/Lab%202/imgs/display_clock.png" height="480" /></p>

## Part E: Modify the barebones clock to make it your own

We decided to control time via the rotary encoder with the code found in `barebones_clock.py`. Every time the rotary encoder is turned clockwise one notch, the time on the clock moves forward 30 minutes. Similarly, when the rotary encoder is turned counter clockwise, the time displayed on the screen moves backwards 30 minutes. Time changing is shown not just with the printed time values but also with a series of images showing a cartoon sunrising and setting along with the appropriate times. 

Since we do not currently have Quiic cables, Snigdha and I improvised the necessary I2C connections by raising the MiniPiTFT screen off the GPIO pins slightly so we could shove some leads into the holes at the top and access the SDA/SCL I2C pins as well as the 3.3V power supply.

<p align="center"><img src="https://github.com/singhaniasnigdha/Interactive-Lab-Hub/blob/Spring2021/Lab%202/imgs/pi_rotary_encoder.png" height="480" /></p>

## Part F: Make a short video of your modified barebones PiClock

You can see the modified barebones clock with the time changing according to the rotary encoder's position and the accompanying animations below:

[![](https://res.cloudinary.com/marcomontalbano/image/upload/v1614566984/video_to_markdown/images/google-drive--1GTcadkFiFY9N9W-uxGgojbXpPkQuTO_T-c05b58ac6eb4c4700831b2b3070cd403.jpg)](https://drive.google.com/file/d/1GTcadkFiFY9N9W-uxGgojbXpPkQuTO_T "")

## Part G: Planning further interactions/features for the PiClock
We decided to model our final clock representation after life and the various activities that people perform on a day-to-day basis. While the user controls time with the rotary encoder, they have various activities that they are required to do at certain times. We decided to have our clock perform the following functions:

#### Control Time
  * __Interactive Tools__: Rotary Encoder, MiniPiTFT
  * __Costume__: The sun is shown "rising" and "setting" on the screen to make a more explicit representation of time.
  * __Activation Criteria__: User acts on the rotary encoder
  * __Description__: As in the barebones clock, the user will be able to move time in 30 minute increments via the rotary encoder. A clockwise turn moves time forward. A counter-clockwise turn moves time backwards.
#### Playing Soccer
  * __Interactive Tools__: Joystick, MiniPiTFT
  * __Costume__: A soccer ball cover for the joystick made out of paper.
  * __Activation Criteria__: User passes 10am on Sunday
  * __Description__: On Sundays at 10am, our user will play soccer. When this time is passed, the screen will alert the user it is time to play soccer and display a stick figure standing by ready to kick the ball. The joystick will be costumed to look like a soccer ball to make it clear to the user that they should use the joystick to perform the relevant action. Once the joystick is moved, the stick figure will kick the ball and the soccer activity will conclude.
#### Cooking
  * __Interactive Tools__: Accelerometer and cardboard frying pan, green Quiic button, MiniPiTFT
  * __Costume__: The green button is meant to signify food. This is likely the least clear interactive portion of our design. A cardboard frying pan costume for the accelerometer.
  * __Activation Criteria__: User presses the green button
  * __Description__: If the user "gets hungry," they can press the green button to begin dinner time. Once in this mode, the user is required to "cook" using the cardboard frying pan (with the attached accelerometer) to move on.
#### Sleeping
  * __Interactive Tools__: Proximity Sensor, MiniPiTFT
  * __Costume__: A cardboard "bed" costume is used here.
  * __Activation Criteria__: When the user pushes the cardboard "sheets" on to the bed.
  * __Description__: When the user wishes to sleep, they can push the cardboard "sheets" over the proximity sensor. This will trigger a "good night" message. When the sheets are lifted off the proximity sensor again, 7 hours have passed and the user can continue on with their day.
#### Drinking Wine
  * __Interactive Tools__: Red Quiic button, MiniPiTFT
  * __Costume__: The red button flashes to tell the user that they should interact with it.
  * __Activation Criteria__: At 5pm on Friday, "Wine Time" triggers
  * __Description__: It's 5 o'clock somewhere! And in the world of our interactive device, the user can enjoy 5 o'clock on Friday and "Wine Time" whenever they choose to pass that time! When this event is triggered, the screen tells the user it is wine time and the red button begins flashing to tell the user to interact with it. Once pressed, an animation of two champagne flutes is shown on the MiniPiTFT to indicate that the user has "enjoyed" wine time.

This is outlined in the following sketch:

<p align="center"><img src="https://github.com/singhaniasnigdha/Interactive-Lab-Hub/blob/Spring2021/Lab%202/imgs/future_interactions.png" height="480" /></p>

# Part 2: Video of the Final Interactions

The final product for our interactive device is shown in the demo below:

[![](https://res.cloudinary.com/marcomontalbano/image/upload/v1614566585/video_to_markdown/images/google-drive--1Zml_PnKv7Po2L-kpPTjNheOi9eHsNsjS-c05b58ac6eb4c4700831b2b3070cd403.jpg)](https://drive.google.com/file/d/1Zml_PnKv7Po2L-kpPTjNheOi9eHsNsjS "")
