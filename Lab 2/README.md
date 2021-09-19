# Interactive Prototyping: The Clock of Pi

Does it feel like time is moving strangely during this semester?

For our first Pi project, we will pay homage to the [timekeeping devices of old](https://en.wikipedia.org/wiki/History_of_timekeeping_devices) by making simple clocks.

It is worth spending a little time thinking about how you mark time, and what would be useful in a clock of your own design.

**Please indicate anyone you collaborated with on this Lab here.**
Be generous in acknowledging their contributions! And also recognizing any other influences (e.g. from YouTube, Github, Twitter) that informed your design. 

## Prep

[Lab prep](prep.md) is extra long this week! Make sure you read it over in time to prepare for lab on Thursday.

### Get your kit
If you are remote but in the US, let the teaching team know you need the parts mailed.

If you are in New York, you can come to the campus and pick up your parts. If you have not picked up your parts by Thursday lab you should come to Tata 351.

### Set up your Lab 2

1. [Pull changes from the Interactive Lab Hub](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2021Fall/readings/Submitting%20Labs.md#to-pull-lab-updates) so that you have your own copy of Lab 2 on your own lab hub. (This may have to be done again at the start of lab on Thursday.)
  
  If you are organizing your Lab Hub through folder in local machine, go to terminal, cd into your Interactive-Lab-Hub folder and run:

  ```
  Interactive-Lab-Hub $ git remote add upstream https://github.com/FAR-Lab/Interactive-Lab-Hub.git
  Interactive-Lab-Hub $ git pull upstream Fall2021
  Interactive-Lab-Hub $ git add .
  Interactive-Lab-Hub $ git commit -m'merge'
  Interactive-Lab-Hub $ git push
  ```
  Your local and remote should now be up to date with the most recent files.

2. Go to the [lab prep page](prep.md) to inventory your parts and set up your Pi before the lab session on Thursday.


## Overview
For this assignment, you are going to 

A) [Connect to your Pi](#part-a)  

B) [Try out cli_clock.py](#part-b) 

C) [Set up your RGB display](#part-c)

D) [Try out clock_display_demo](#part-d) 

E) [Modify the code to make the display your own](#part-e)

F) [Make a short video of your modified barebones PiClock](#part-f)

G) [Sketch and brainstorm further interactions and features you would like for your clock for Part 2.](#part-g)

## The Report
This readme.md page in your own repository should be edited to include the work you have done. You can delete everything but the headers and the sections between the \*\*\***stars**\*\*\*. Write the answers to the questions under the starred sentences. Include any material that explains what you did in this lab hub folder, and link it in the readme.

Labs are due on Mondays. Make sure this page is linked to on your main class hub page.

## Part A. 
### Connect to your Pi
I connected the pi and set up a python environment using the following commands: 

```
(base) kristychen@Kristys-MBP ~ % ssh pi@192.168.1.76
...
pi@ixe00:~ $ virtualenv circuitpython
pi@ixe00:~ $ source circuitpython/bin/activate
(circuitpython) pi@ixe00:~ $ 
```

## Part B. 
### Try out the Command Line Clock
I cloned my own lab-hub to the pi and changed the directory to Lab 2 via the following commands:

```
(circuitpython) pi@ixe00:~ $ git clone https://github.com/kchen1009/Interactive-Lab-Hub.git
(circuitpython) pi@ixe00:~ $ cd Interactive-Lab-Hub/Lab\ 2/
```

I then installed the packages and ran ```cli_clock.py```:
```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ pip install -r requirements.txt
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ python cli_clock.py 
09/19/2021 15:32:15
```

## Part C. 
### Set up your RGB Display
We have asked you to equip the [Adafruit MiniPiTFT](https://www.adafruit.com/product/4393) on your Pi in the Lab 2 prep already. Here, we will introduce you to the MiniPiTFT and Python scripts on the Pi with more details.

<img src="https://cdn-learn.adafruit.com/assets/assets/000/082/842/large1024/adafruit_products_4393_iso_ORIG_2019_10.jpg" height="200" />

The Raspberry Pi 4 has a variety of interfacing options. When you plug the pi in the red power LED turns on. Any time the SD card is accessed the green LED flashes. It has standard USB ports and HDMI ports. Less familiar it has a set of 20x2 pin headers that allow you to connect a various peripherals.

<img src="https://maker.pro/storage/g9KLAxU/g9KLAxUiJb9e4Zp1xcxrMhbCDyc3QWPdSunYAoew.png" height="400" />

To learn more about any individual pin and what it is for go to [pinout.xyz](https://pinout.xyz/pinout/3v3_power) and click on the pin. Some terms may be unfamiliar but we will go over the relevant ones as they come up.

### Hardware (you have done this in the prep)

From your kit take out the display and the [Raspberry Pi 4](https://cdn-shop.adafruit.com/1200x900/4296-13.jpg)

Line up the screen and press it on the headers. The hole in the screen should match up with the hole on the raspberry pi.

<p float="left">
<img src="https://cdn-learn.adafruit.com/assets/assets/000/087/539/medium640/adafruit_products_4393_quarter_ORIG_2019_10.jpg?1579991932" height="200" />
<img src="https://cdn-learn.adafruit.com/assets/assets/000/082/861/original/adafruit_products_image.png" height="200">
</p>

### Testing your Screen

By running the following command and inputting 'yellow', I was able to see a yellow background on the display. <br />
Video: https://drive.google.com/file/d/1USkp8Tc9PRqcqepnwEbqRUxKPRlJ5pll/view?usp=sharing
```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ python screen_test.py
```

#### Displaying Info with Texts
![P1:Testing2](https://github.com/kchen1009/Interactive-Lab-Hub/blob/Fall2021/Lab%202/images/Testing2.JPG)

#### Displaying an image
![P2:Testing3](https://github.com/kchen1009/Interactive-Lab-Hub/blob/Fall2021/Lab%202/images/Testing3.JPG)



## Part D. 
### Set up the Display Clock Demo
Work on `screen_clock.py`, try to show the time by filling in the while loop (at the bottom of the script where we noted "TODO" for you). You can use the code in `cli_clock.py` and `stats.py` to figure this out.

### How to Edit Scripts on Pi
By adding the following python scripts in the #TODO section of ```screen_clock.py```, I was able to edit scripts on the pi and make the display to show the current date/time.
```
now = time.strftime("%m/%d/%Y %H:%M:%S")
y = top
draw.text((x, y), now, font=font, fill="#FFFFFF")           
```
![P3:Setup](https://github.com/kchen1009/Interactive-Lab-Hub/blob/Fall2021/Lab%202/images/Setup.JPG)

## Part E.
### Modify the barebones clock to make it your own

**We strongly discourage and will reject the results of literal digital or analog clock display.** <br />
The code can be found in ```screen_clock.py``` where I designed an interaction to tell people how much water they need to drink at the current time. If it's 5 in the afternoon, the clock would show users that the curren time is 1416 milliliters of water (2L / 24 hours a day * 17). The number is rounded to the nearest ineger.
\*\*\***A copy of your code should be in your Lab 2 Github repo.**\*\*\*<br />
```
import datetime
import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
from adafruit_rgb_display.rgb import color565

# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font1 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True
buttonA = digitalio.DigitalInOut(board.D23)
buttonA.switch_to_input()
buttonB = digitalio.DigitalInOut(board.D24)
buttonB.switch_to_input()
while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    #TODO: Lab 2 part D work should be filled in here. You should be able to look in cli_clock.py and stats.py 
    y = top
    draw.text((x, y), "You need to drink 2L water daily", font=font1, fill="#FFFFFF")
    time = datetime.datetime.now()
    hour = time.hour
    now = int(2000/24*hour)
    if not buttonA.value:
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        y = top
        draw.text((x, y), "Current time: " + str(now) + " milliliters", font=font1, fill="#FFFFFF")
    disp.image(image, rotation)
```

## Part F. 
## Make a short video of your modified barebones PiClock

\*\*\***Take a video of your PiClock.**\*\*\* <br />
Video: https://drive.google.com/file/d/1L8v0-awETzKBZa9sKYQwTQRkRqNWqmSq/view?usp=sharing

## Part G. 
## Sketch and brainstorm further interactions and features you would like for your clock for Part 2.


# Prep for Part 2

1. Pick up remaining parts for kit.

2. Look at and give feedback on the Part G. for at least 2 other people in the class (and get 2 people to comment on your Part G!)

# Lab 2 Part 2

Pull Interactive Lab Hub updates to your repo.

Modify the code from last week's lab to make a new visual interface for your new clock. You may [extend the Pi](Extending%20the%20Pi.md) by adding sensors or buttons, but this is not required.

As always, make sure you document contributions and ideas from others explicitly in your writeup.

You are permitted (but not required) to work in groups and share a turn in; you are expected to make equal contribution on any group work you do, and N people's group project should look like N times the work of a single person's lab. What each person did should be explicitly documented. Make sure the page for the group turn in is linked to your Interactive Lab Hub page. 


