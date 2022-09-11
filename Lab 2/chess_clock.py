import time
import subprocess
import digitalio
import board
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
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 32)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

# Add button inputs
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

state = True
time_a = 60
time_b = 60

if buttonB.value and not buttonA.value:  # just button A pressed
    state = False
if buttonA.value and not buttonB.value:  # just button B pressed
    state = True

while True:
    # Draw starting position
    
    if state == True:
        draw.rectangle((0, 0, 120, height), outline=0, fill="#ED4242")
        draw.rectangle((120, 0, width, height), outline=0, fill="#191919")
        draw.text((50,50), str(time_a), font=font, fill="#FFFFFF")
        draw.text((150,50), str(time_b), font=font, fill="#FFFFFF")
        time_a = time_a - 1
    else:
        draw.rectangle((0, 0, 120, height), outline=0, fill="#191919")
        draw.rectangle((120, 0, width, height), outline=0, fill="#ED4242")
        draw.text((50,50), str(time_a), font=font, fill="#FFFFFF")
        draw.text((150,50), str(time_b), font=font, fill="#FFFFFF")
        time_b = time_b - 1

    # Create button triggers to adjust state

        
    # y = top
    # draw.text((x, y), str(state), font=font, fill="#875AFF")

    # Display image.
    disp.image(image, rotation)
    time.sleep(1)
