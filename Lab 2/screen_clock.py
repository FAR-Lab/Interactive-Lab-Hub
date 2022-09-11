import time
import subprocess
import digitalio
import board
from datetime import datetime as dt
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
from time import strftime, sleep

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

h = 0

while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    time2 = (strftime("%m/%d/%Y %H:%M:%S"))
    y = top

    h = dt.now().hour
    
    # Simulation of 24h
    #h = h % 24 + 1
    
    # Draw hourglass top
    draw.line((120 , 64.5, 208, 22.5 ), fill="#FFFFFF", width=1)
    draw.line((120 , 70.5, 208, 108.5 ), fill="#FFFFFF", width=1)
    draw.line((208, 22.5, 224, 22.5 ), fill="#FFFFFF", width=1)
    draw.line((208, 108.5, 224, 108.5 ), fill="#FFFFFF", width=1)
    draw.line((224, 108.5, 224, 22.5 ), fill="#FFFFFF", width=1)

    # Draw hourglas bottom
    draw.line((32 , 22.5, 120, 64.5 ), fill="#FFFFFF", width=1)
    draw.line((32 , 108.5, 120, 70.5 ), fill="#FFFFFF", width=1)
    draw.line((32 , 22.5, 16, 22.5 ), fill="#FFFFFF", width=1)
    draw.line((32, 108.5, 16, 108.5), fill="#FFFFFF", width=1)
    draw.line((16, 22.5, 16, 108.5), fill="#FFFFFF", width=1)

    # 24h
    if h == 24:
        draw.polygon([(224, 22.5), (224, 108.5), (208, 108.5), (120, 70.5), (120, 64.5), (208, 22.5)], fill="#FFFFFF")

    # 1h
    elif h == 1:
        draw.polygon([(216, 22.5), (216, 108.5), (208, 108.5), (120, 70.5), (120, 64.5), (208, 22.5)], fill="#FFFFFF")
        draw.polygon([(24, 22.5), (24, 108.5), (16, 108.5), (16, 22.5)], fill="#FFFFFF")

    # 2 h
    elif h == 2:
        draw.polygon([(208, 108.5), (120, 70.5), (120, 64.5), (208, 22.5)], fill="#FFFFFF")
        draw.polygon([(32, 22.5), (32, 108.5), (16, 108.5), (16, 22.5)], fill="#FFFFFF")

    # 3 h to 23 h
    else:
        #h = h - 3 
        draw.polygon([(204-(h-3)*4, 24.5+(h-3)*2), (204-(h-3)*4, 106.5-(h-3)*2), (120, 70.5), (120, 64.5)], fill="#FFFFFF")
        draw.polygon([(16, 22.5), (32, 22.5), (36+(h-3)*4, 24.5+(h-3)*2), (36+(h-3)*4, 106.5-(h-3)*2), (32, 108.5), (16, 108.5)], fill="#FFFFFF")

    y += font.getsize(time2)[1]
    #TODO: Lab 2 part D work should be filled in here. You should be able to look in cli_clock.py and stats.py

    # Display image.
    disp.image(image, rotation)
    time.sleep(1)