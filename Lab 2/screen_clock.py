import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
from adafruit_rgb_display.rgb import color565
import webcolors

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
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 15)
font_big = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)
font_massive = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 70)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

stop_watch = 0

from time import strftime, sleep
while True:
    # Draw a black filled box to clear the image.
    if buttonA.value and buttonB.value:
        backlight.value = True
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        stop_watch = 0

        date = strftime("%m/%d/%Y")
        time_nf = strftime("%H:%M:%S")
        y = top
        draw.text((x, y), "Eiffel Tower is 984ft tall", font=font, fill=color565(123,222,32))
        y += font.getsize(date)[1]
        draw.text((x, y), "41 days in 1 Tower", font=font, fill=color565(123,222,32))
        y += font.getsize(date)[1]
        draw.text((x, y), "Almost 9 Towers in 1 year", font=font, fill=color565(123,222,32))
        if float(strftime("%m")) == 1:
                dateint = float(strftime("%d"))
        if float(strftime("%m")) == 2:
                dateint = 31+float(strftime("%d"))
        if int(strftime("%m")) == 3:
                dateint = 59+float(strftime("%d"))
        if int(strftime("%m")) == 4:
                dateint = 90+float(strftime("%d"))
        if int(strftime("%m")) == 5:
                dateint = 120+float(strftime("%d"))
        if int(strftime("%m")) ==6:
                dateint = 151+float(strftime("%d"))
        if int(strftime("%m")) == 7:
          dateint = 181+float(strftime("%d"))
        if int(strftime("%m")) == 8:
                dateint = 212+float(strftime("%d"))
        if int(strftime("%m")) == 9:
                dateint = 243+float(strftime("%d"))
        if int(strftime("%m")) == 10:
                dateint = 273+float(strftime("%d"))
        if int(strftime("%m")) == 11:
                dateint = 304+float(strftime("%d"))
        if int(strftime("%m")) == 12:
                dateint = 334+float(strftime("%d"))

        if float(strftime("%H")) != 0 or 23:
                hourint = int(strftime("%H"))
                hourint = "Flatiron Floor "+str(hourint)
        if float(strftime("%H")) == 0:
                hourint = str("You are outside aka Midnight")
        if float(strftime("%H")) == 23:
                hourint = str("You are jetpacking down aka 11pm")       
        
        dateint = dateint/41
        dateint = round(dateint, 3)
        dateint = str(dateint)
        y += font.getsize(date)[1]
        draw.text((x, y), dateint+" Eiffel Towers", font=font, fill=color565(255, 0, 0))
        y += font.getsize(date)[1]
        draw.text((x, y), "Flatiron Building has 22 Floors", font=font, fill=color565(123,222,32))
        y += font.getsize(date)[1]
        draw.text((x, y), hourint , font=font, fill=color565(255,0,0))
        y += font.getsize(date)[1]
        draw.text((width/2-((font.getsize(hourint)[0])/2), y+1), date, font=font_big, fill=color565(0,255,0))
        y += font.getsize(date)[1]
        draw.text((width/2-((font.getsize(date)[0])/2), y+8), time_nf, font=font_big, fill=color565(0,255,0))

    if buttonB.value and not buttonA.value:  # just button A pressed
        backlight.value = True
        draw.rectangle((0, 0, width, height), outline=0, fill=0)

        stop_watch += 1
        stop_watch_text = str(stop_watch)
        y = top
        draw.text((width/2-((font.getsize("Timer")[0])/2)-12, y+1), "Timer", font=font_big, fill="#ADD8E6")
        y += font.getsize("Timer")[1]
        draw.text((width/2-((font.getsize(stop_watch_text)[0])/2)-15, y+30), stop_watch_text, font=font_massive, fill="#FFC0CB")
    # Display image.
    disp.image(image, rotation)
    time.sleep(1)
