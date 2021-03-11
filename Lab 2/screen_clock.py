import time
import datetime
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
from datetime import date
from adafruit_rgb_display.rgb import color565
import adafruit_rgb_display.st7789 as st7789
import webcolors
import re



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
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=0)

#TODO: fill in here. You should be able to look in cli_clock.py and stats.py

"""
    Days = str(Clock.days)
    Hours = str(Clock.hours)
    Minutes = str(Clock.minutes)
    Seconds = str(Clock.seconds)
"""



# Main loop:
while True:
    Clock = datetime.datetime(2021,4,8,hour=13, minute=10, second=0, microsecond=0) - datetime.datetime.now()
    Days = str(Clock.days)
    Clock = str(Clock)
    Hour = Clock [7:10]
    Min = Clock [11:13]
    Sec = Clock [14:16]
    ClockA = datetime.datetime(2021,4,1,hour=19, minute=9, second=0, microsecond=0) - datetime.datetime.now()
    DaysA = str(ClockA.days)
    ClockA = str(ClockA)
    HourA = ClockA [7:10]
    MinA = ClockA [11:13]
    SecA = ClockA [14:16]

    if buttonA.value and buttonB.value:
        backlight.value = True  # turn on backlight
        draw.rectangle((0, 0, width, height), outline=0, fill="#000000")
        y = top
        draw.text((x, y), "Select Mets Countdown", font=font, fill="#FFFFFF")
        y += font.getsize(Clock)[1]
        draw.text((x, y), "Top: Home Opener", font=font, fill="#0000FF")
        y += font.getsize(Clock)[1]
        draw.text((x, y), "Bottom: Away Opener", font=font, fill="#FF6600")

        # Display image.
        disp.image(image, rotation)
    else:
        backlight.value = True  # turn on backlight

    if buttonB.value and not buttonA.value:  # just button A pressed
        draw.rectangle((0, 0, width, height), outline=0, fill="#000000")
        y = top
        draw.text((x, y), Days + " Days " + Hour + " Hr " + Min + " M " + Sec + " S ", font=font, fill="#FFFFFF")
        y += font.getsize(Clock)[1]
        draw.text((x, y), "Countdown to:", font=font, fill="#0000FF")
        y += font.getsize(Clock)[1]
        draw.text((x, y), "The Mets Home Opener!", font=font, fill="#FF6600")

        # Display image.
        disp.image(image, rotation)

    if buttonA.value and not buttonB.value:  # just button B pressed
        draw.rectangle((0, 0, width, height), outline=0, fill="#000000")
        y = top
        draw.text((x, y), DaysA + " Days " + HourA + " Hr " + MinA + " M " + SecA + " S ", font=font, fill="#FFFFFF")
        y += font.getsize(ClockA)[1]
        draw.text((x, y), "Countdown to:", font=font, fill="#0000FF")
        y += font.getsize(ClockA)[1]
        draw.text((x, y), "The Mets Away Opener!", font=font, fill="#FF6600")

        # Display image.
        disp.image(image, rotation)

    if not buttonA.value and not buttonB.value:  # none pressed
        disp.fill(color565(0, 0, 0))  # green
"""
# Main loop:
while True:
    if buttonA.value and buttonB.value:
        backlight.value = False  # turn off backlight
    else:
        backlight.value = True  # turn on backlight
    if buttonB.value and not buttonA.value:  # just button A pressed
        display.fill(screenColor) # set the screen to the users color
    if buttonA.value and not buttonB.value:  # just button B pressed
        display.fill(color565(255, 255, 255))  # set the screen to white
    if not buttonA.value and not buttonB.value:  # none pressed
        display.fill(color565(0, 255, 0))  # green
"""
