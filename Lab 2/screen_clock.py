import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
from datetime import datetime
import pytz
from PIL import Image, ImageDraw, ImageFont


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

# Image Formatting
def image_formatting(imagef, width, height):
    imagef = imagef.convert('RGB')
    imagef = imagef.resize((240, 135), Image.BICUBIC)

    return imagef

# Buttons
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

height = disp.width 
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    #TODO: fill in here. You should be able to look in cli_clock.py and stats.py
    x = 4
    y = 10

    if buttonB.value and not buttonA.value:  # just button A pressed
        image3 = Image.open("/home/pi/Interactive-Lab-Hub/Lab 2/beijing.jpg")
        image3 = image_formatting(image3, width, height)
    
        draw = ImageDraw.Draw(image3)

        tz_NY = pytz.timezone('PRC') 
        datetime_NY = datetime.now(tz_NY)
        draw.text((4, 0), "Beijing:", fill="#000000")
        draw.text((x, y), datetime_NY.strftime("%H:%M:%S%p"), font=font, fill="#000000")

    elif buttonA.value and not buttonB.value:  # just button B pressed
        image3 = Image.open("/home/pi/Interactive-Lab-Hub/Lab 2/telaviv.jpg")
        image3 = image_formatting(image3, width, height)
    
        draw = ImageDraw.Draw(image3)

        tz_NY = pytz.timezone('Asia/Tel_Aviv') 
        datetime_NY = datetime.now(tz_NY)
        draw.text((4, 0), "Tel Aviv:", fill="#000000")
        draw.text((x, y), datetime_NY.strftime("%H:%M:%S%p"), font=font, fill="#000000")

    else:
        image3 = Image.open("/home/pi/Interactive-Lab-Hub/Lab 2/nyc.jpg")
        image3 = image_formatting(image3, width, height)
    
        draw = ImageDraw.Draw(image3)

        tz_NY = pytz.timezone('America/New_York') 
        datetime_NY = datetime.now(tz_NY)
        draw.text((4, 0), "New York:", fill="#000000")
        draw.text((x, y), datetime_NY.strftime("%H:%M:%S%p"), font=font, fill="#000000")

    # Display image.
    disp.image(image3, rotation)
    time.sleep(1)
