from time import strftime, sleep
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
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 13)

# Turn on the backlight

backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

drunk = 0

while True:
    y = top
    if buttonA.value and buttonB.value:
        draw.rectangle((0, 0, width, height), outline=0, fill="#000000")
        backlight.value = True
        y = top
        if strftime("%H:%M") == "00:00":
            drunk = 0

        tim = int(strftime("%H"))
        tim2 = int(strftime("%M"))
        tim3 = ((tim*60)+tim2)/1440
        ww = width * tim3
        rui_time = strftime("%m/%d/%Y %H:%M:%S")
        y = top
        draw.rectangle((0, 0, ww, height), outline=0, fill="#3944BC")
        draw.text((x+5, y), rui_time, font=font, fill="#FFFFFF")
        
        var = int(strftime("%H")) *125
        text = str(var) + " mL / 3L of water recommended."
        draw.text((x+5, y), rui_time, font=font, fill="#FFFFFF")
        draw.text((x+5, y+20), text, font=font, fill="#FFFFFF")


        y = top
        text = "This clock measures time based on"
        text2 = "mL of water consumed. Starting at"
        text3 = "midnight, 125mL of water is added"
        text4 = "every hour."

        draw.text((x+5, y+60), text, font=font, fill="#FFFFFF")
        draw.text((x+5, y+80), text2, font=font, fill="#FFFFFF")
        draw.text((x+5, y+100), text3, font=font, fill="#FFFFFF")
        draw.text((x+5, y+120), text4, font=font, fill="#FFFFFF")
    if buttonA.value and not buttonB.value:
        drunk += 125
    if buttonB.value and not buttonA.value:
        backlight.value = True
        draw.rectangle((0, 0, width, height), outline=0, fill="#016064")
        text = str(drunk) + " mL of water consumed"
        draw.text((x+25, y+55), text, font=font, fill = "#FFFFFF")

    # Display image.
    disp.image(image, rotation)
    time.sleep(1)
