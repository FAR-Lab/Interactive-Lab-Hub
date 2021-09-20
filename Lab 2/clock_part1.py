'''
Author: Wenlan Wei
Date: 2021-09-19 21:18:28
LastEditTime: 2021-09-20 16:52:46
LastEditors: Please set LastEditors
Description: Part1 Homework Lab2 A simple Customize Clock
FilePath: /Interactive-Lab-Hub/Lab 2/clock_part1.py
'''

import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
from adafruit_rgb_display.rgb import color565
import webcolors
# refer to image.py
import adafruit_rgb_display.ili9341 as ili9341
import adafruit_rgb_display.hx8357 as hx8357  # pylint: disable=unused-import
import adafruit_rgb_display.st7735 as st7735  # pylint: disable=unused-import
import adafruit_rgb_display.ssd1351 as ssd1351  # pylint: disable=unused-import
import adafruit_rgb_display.ssd1331 as ssd1331  # pylint: disable=unused-import


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
font = ImageFont.truetype(
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 70)
smallfont = ImageFont.truetype(
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 15)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True


buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

current_time = time.strftime("%H:%M")


# while True:
#     # Draw a black filled box to clear the image.
#     # draw.rectangle((0, 0, width, height), outline=0, fill=0)
#     # y = top
#     # draw.text((x, y), current_time, font=font, fill="#FFFFFF")
#     # disp.image(image, rotation)
#     # time.sleep(1)

# TODO: fill in here. You should be able to look in cli_clock.py and stats.py

n = 1
t = 0
interval = 1
SHOW = False

while True:

    # Create blank image for drawing.
    # Make sure to create image with mode 'RGB' for full color.

    if n >= 8:
        n = 1
        t = 0
        SHOW = False

    if buttonB.value and not buttonA.value:
        SHOW = True

    if buttonA.value and not buttonB.value:
        n = 1
        t = 0
        SHOW = False

    if SHOW == False:
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        REMIND = "Press Button A to start Timing"
        REMIND_2 = "Press Button B to reset"
        x = 0
        y = (top+bottom)/2
        draw.text((x, y), REMIND, font=smallfont, fill="#FFFFFF")
        draw.text((x, y+10), REMIND_2, font=smallfont, fill="#FFFFFF")
        disp.image(image, rotation)
        time.sleep(0.1)

    else:
        if disp.rotation % 180 == 90:
            height = disp.width  # we swap height/width to rotate it to landscape!
            width = disp.height

        else:
            width = disp.width  # we swap height/width to rotate it to landscape!
            height = disp.height

        image_cus = Image.new("RGB", (width, height))

        # Get drawing object to draw on image.
        draw = ImageDraw.Draw(image_cus)
        pictureName = 'images/'+"test"+str(n)+".jpg"
        image_cus = Image.open(pictureName)
        n = n+1

        image_2 = image_cus.transpose(Image.ROTATE_90)
        image_cus = image_2.resize((135, 240))
        disp.image(image_cus)
        time.sleep(interval)
        t += interval
        print("time pass", str(t), "second")
    # backlight = digitalio.DigitalInOut(board.D22)
    # backlight.switch_to_output()
    # backlight.value = True

    # # Scale the image to the smaller screen dimension
    # image_ratio = image.width / image.height
    # screen_ratio = width / height

    # if screen_ratio < image_ratio:
    #     scaled_width = image.width * height // image.height
    #     scaled_height = height
    # else:
    #     scaled_width = width
    #     scaled_height = image.height * width // image.width
    # image = image.resize((scaled_width, scaled_height), Image.BICUBIC)

    # # Crop and center the image
    # x = scaled_width // 2 - width // 2
    # y = scaled_height // 2 - height // 2
    # image = image.crop((x, y, x + width, y + height))
    # # Display image.
    # disp.image(image)
    # time.sleep(4)

    # Display image.
    #disp.image(image, rotation)
    # time.sleep(1)
