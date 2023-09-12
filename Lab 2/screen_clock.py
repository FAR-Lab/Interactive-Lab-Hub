import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789

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

# add buttons for interactions
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

# index for which time slot selected for making changes
indexSelected = 0
# current time forward (by hours)
addTime = 0

from datetime import datetime, timedelta

while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill="grey")

    #TODO: Lab 2 part D work should be filled in here. You should be able to look in cli_clock.py and stats.py 
    from time import strftime, sleep
    x = 0
    y = 20
    #draw.text((x, y), strftime("%m/%d/%Y %H:%M:%S"), font=font, fill="#FFFFFF")

    now = datetime.now()
    now = now + timedelta(hours=addTime)

    draw.rectangle((0, 65, int(now.strftime("%M"))/60 * 240, 85), outline=0, fill="blue")
    draw.rectangle((0, 85, int(now.strftime("%S"))/60 * 240, 105), outline=0, fill="red")
    draw.rectangle((0, 105, int(datetime.now().strftime("%f"))/1000000 * 240, 125), outline=0, fill="white")

    #print(strftime("%m/%d/%Y %H:%M:%S"))

    fillColors = ['#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF']
    fillColors[indexSelected] = 'yellow'

    draw.text((10, 0), now.strftime("Year: %Y"), font=font, fill=fillColors[0])
    draw.text((10, 20), now.strftime("Month: %B"), font=font, fill=fillColors[1])
    draw.text((120, 0), now.strftime("Day: %A"), font=font, fill=fillColors[2])
    draw.text((10, 40), now.strftime("Hour: %I %p"), font=font, fill=fillColors[3])
    draw.text((10, 65), now.strftime("Minute: %M"), font=font, fill=fillColors[4])
    draw.text((10, 85), now.strftime("Seconds: %S"), font=font, fill="#FFFFFF")

    milliseconds = str(int(datetime.now().strftime("%f")) / 1000)
    draw.text((10, 105), datetime.now().strftime("Millisecond: " + milliseconds), font=font, fill="#000000")

    if not buttonB.value:
        if indexSelected == 4:
            indexSelected = 0
        else:
            indexSelected += 1

    if not buttonA.value:
        if (indexSelected == 0):
            addTime += 8736
        elif (indexSelected == 1):
            addTime += 720
        elif (indexSelected == 2):
            addTime += 24
        elif (indexSelected == 3):
            addTime += 1
        else:
            addTime += (1/60)

    # Display image.
    disp.image(image, rotation)
