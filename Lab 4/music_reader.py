from datetime import datetime
import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import busio
import adafruit_rgb_display.st7789 as st7789
import adafruit_mpr121

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
font2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True
buttonA = digitalio.DigitalInOut(board.D23)
buttonA.switch_to_input()

i2c = busio.I2C(board.SCL, board.SDA)
mpr121 = adafruit_mpr121.MPR121(i2c)


input = ""
string = ""
stage = False
submit = True

while True:
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    if mpr121[0].value:
        string = "A"
        stage = True
    if mpr121[1].value:
        string = "A#"
        stage = True
    if mpr121[2].value:
        string = "B"
        stage = True
    if mpr121[3].value:
        string = "C"
        stage = True
    if mpr121[4].value:
        string = "C#"
        stage = True
    if mpr121[5].value:
        string = "D"
        stage = True
    if mpr121[6].value:
        string = "D#"
        stage = True
    if mpr121[7].value:
        string = "E"
        stage = True
    if mpr121[8].value:
        string = "F"
        stage = True
    if mpr121[9].value:
        string = "F#"
        stage = True
    if mpr121[10].value:
        string = "G"
        stage = True
    if mpr121[11].value:
        string = "G#"
        stage = True

    for i in range(11):
        if mpr121[i].value:
            input += string


    if stage == True:
        line1 = input
    else:
        line1 = "Play music"
        line2 = input

    y = top
    draw.text((x, y), line1, font=font, fill="#FFFFFF")
    y += font.getsize(line1)[1]
    draw.text((x, y), line2, font=font, fill="#FFFFFF")
    y += font.getsize(line2)[1]
    #draw.text((x, y), line3, font=font, fill="#FFFFFF")
    #y += font.getsize(line3)[1]
    #draw.text((x, y), line4, font=font, fill="#FFFFFF")
    #y += font.getsize(line4)[1]

    # Display image.
    disp.image(image, rotation)
    # time.sleep(1)
    if submit:
        submit = False
        time.sleep(1)
    else:
        time.sleep(0.25)
