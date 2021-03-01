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

while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    #TODO: fill in here. You should be able to look in cli_clock.py and stats.py 

    # Display image.
    ahaantime = strftime("%m/%d/%Y %H:%M:%S")
    y = top
    # print("\r", end="", flush=True)
    if int(strftime("%H")) == 0:
        text  = "The sun is at an angle"
        var = int(strftime("%H")) * 15 + 270
        text2 = "of " + str(var) + " degrees"
        draw.text((x, y), ahaantime, font=font, fill="#FFFFFF")
        draw.text((x, y+20), text, font=font, fill="#FFFFFF")
        draw.text((x, y+40), text2, font=font, fill="#FFFFFF")
    elif int(strftime("%H")) == 1:
        text  = "The sun is at an angle"
        var = int(strftime("%H")) * 15 + 270
        text2 = "of " + str(var) + " degrees"
        draw.text((x, y), ahaantime, font=font, fill="#FFFFFF")
        draw.text((x, y+20), text, font=font, fill="#FFFFFF")
        draw.text((x, y+40), text2, font=font, fill="#FFFFFF")
    elif int(strftime("%H")) == 2:
        text  = "The sun is at an angle"
        var = int(strftime("%H")) * 15 + 270
        text2 = "of " + str(var) + " degrees"
        draw.text((x, y), ahaantime, font=font, fill="#FFFFFF")
        draw.text((x, y+20), text, font=font, fill="#FFFFFF")
        draw.text((x, y+40), text2, font=font, fill="#FFFFFF")
    elif int(strftime("%H")) == 3:
        text  = "The sun is at an angle"
        var = int(strftime("%H")) * 15 + 270
        text2 = "of " + str(var) + " degrees"
        draw.text((x, y), ahaantime, font=font, fill="#FFFFFF")
        draw.text((x, y+20), text, font=font, fill="#FFFFFF")
        draw.text((x, y+40), text2, font=font, fill="#FFFFFF")
    elif int(strftime("%H")) == 4:
        text  = "The sun is at an angle"
        var = int(strftime("%H")) * 15 + 270
        text2 = "of " + str(var) + " degrees"
        draw.text((x, y), ahaantime, font=font, fill="#FFFFFF")
        draw.text((x, y+20), text, font=font, fill="#FFFFFF")
        draw.text((x, y+40), text2, font=font, fill="#FFFFFF")
    elif int(strftime("%H")) == 5:
        text  = "The sun is at an angle"
        var = int(strftime("%H")) * 15 + 270
        text2 = "of " + str(var) + " degrees"
        draw.text((x, y), ahaantime, font=font, fill="#FFFFFF")
        draw.text((x, y+20), text, font=font, fill="#FFFFFF")
        draw.text((x, y+40), text2, font=font, fill="#FFFFFF")
    elif int(strftime("%H")) == 6:
        text = "The sun is at an angle"
        var = 15 * int(strftime("%H")) - 90
        text2 = "of " + str(var) + " degrees"
        draw.text((x, y), ahaantime, font=font, fill="#FFFFFF")
        draw.text((x, y + 20), text, font=font, fill="#FFFFFF")
        draw.text((x, y + 40), text2, font=font, fill="#FFFFFF")
    elif int(strftime("%H")) == 7:
        text = "The sun is at an angle"
        var = 15 * int(strftime("%H")) - 90
        text2 = "of " + str(var) + " degrees"
        draw.text((x, y), ahaantime, font=font, fill="#FFFFFF")
        draw.text((x, y + 20), text, font=font, fill="#FFFFFF")
        draw.text((x, y + 40), text2, font=font, fill="#FFFFFF")
    elif int(strftime("%H")) == 8:
        text = "The sun is at an angle"
        var = 15 * int(strftime("%H")) - 90
        text2 = "of " + str(var) + " degrees"
        draw.text((x, y), ahaantime, font=font, fill="#FFFFFF")
        draw.text((x, y + 20), text, font=font, fill="#FFFFFF")
        draw.text((x, y + 40), text2, font=font, fill="#FFFFFF")
    elif int(strftime("%H")) == 9:
        text = "The sun is at an angle"
        var = 15 * int(strftime("%H")) - 90
        text2 = "of " + str(var) + " degrees"
        draw.text((x, y), ahaantime, font=font, fill="#FFFFFF")
        draw.text((x, y + 20), text, font=font, fill="#FFFFFF")
        draw.text((x, y + 40), text2, font=font, fill="#FFFFFF")
    elif int(strftime("%H")) == 10:
        text = "The sun is at an angle"
        var = 15 * int(strftime("%H")) - 90
        text2 = "of " + str(var) + " degrees"
        draw.text((x, y), ahaantime, font=font, fill="#FFFFFF")
        draw.text((x, y + 20), text, font=font, fill="#FFFFFF")
        draw.text((x, y + 40), text2, font=font, fill="#FFFFFF")
    elif int(strftime("%H")) == 11:
        text = "The sun is at an angle"
        var = 15 * int(strftime("%H")) - 90
        text2 = "of " + str(var) + " degrees"
        draw.text((x, y), ahaantime, font=font, fill="#FFFFFF")
        draw.text((x, y + 20), text, font=font, fill="#FFFFFF")
        draw.text((x, y + 40), text2, font=font, fill="#FFFFFF")
    elif int(strftime("%H")) == 12:
        text = "The sun is at an angle"
        var = 15 * int(strftime("%H")) - 90
        text2 = "of " + str(var) + " degrees"
        draw.text((x, y), ahaantime, font=font, fill="#FFFFFF")
        draw.text((x, y + 20), text, font=font, fill="#FFFFFF")
        draw.text((x, y + 40), text2, font=font, fill="#FFFFFF")
    elif int(strftime("%H")) == 13:
        text = "The sun is at an angle"
        var = 15 * int(strftime("%H")) - 90
        text2 = "of " + str(var) + " degrees"
        draw.text((x, y), ahaantime, font=font, fill="#FFFFFF")
        draw.text((x, y + 20), text, font=font, fill="#FFFFFF")
        draw.text((x, y + 40), text2, font=font, fill="#FFFFFF")
    elif int(strftime("%H")) == 14:
        text = "The sun is at an angle"
        var = 15 * int(strftime("%H")) - 90
        text2 = "of " + str(var) + " degrees"
        draw.text((x, y), ahaantime, font=font, fill="#FFFFFF")
        draw.text((x, y + 20), text, font=font, fill="#FFFFFF")
        draw.text((x, y + 40), text2, font=font, fill="#FFFFFF")

    elif int(strftime("%H")) == 15:
        text = "The sun is at an angle"
        var = 15 * int(strftime("%H")) - 90
        text2 = "of " + str(var) + " degrees"
        draw.text((x, y), ahaantime, font=font, fill="#FFFFFF")
        draw.text((x, y + 20), text, font=font, fill="#FFFFFF")
        draw.text((x, y + 40), text2, font=font, fill="#FFFFFF")
    elif int(strftime("%H")) == 16:
        text = "The sun is at an angle"
        var = 15 * int(strftime("%H")) - 90
        text2 = "of " + str(var) + " degrees"
        draw.text((x, y), ahaantime, font=font, fill="#FFFFFF")
        draw.text((x, y + 20), text, font=font, fill="#FFFFFF")
        draw.text((x, y + 40), text2, font=font, fill="#FFFFFF")
    elif int(strftime("%H")) == 17:
        text = "The sun is at an angle"
        var = 15 * int(strftime("%H")) - 90
        text2 = "of " + str(var) + " degrees"
        draw.text((x, y), ahaantime, font=font, fill="#FFFFFF")
        draw.text((x, y + 20), text, font=font, fill="#FFFFFF")
        draw.text((x, y + 40), text2, font=font, fill="#FFFFFF")
    elif int(strftime("%H")) == 18:
        text = "The sun is at an angle"
        var = 15 * int(strftime("%H")) - 90
        text2 = "of " + str(var) + " degrees"
        draw.text((x, y), ahaantime, font=font, fill="#FFFFFF")
        draw.text((x, y + 20), text, font=font, fill="#FFFFFF")
        draw.text((x, y + 40), text2, font=font, fill="#FFFFFF")
    elif int(strftime("%H")) == 19:
        text = "The sun is at an angle"
        var = 15 * int(strftime("%H")) - 90
        text2 = "of " + str(var) + " degrees"
        draw.text((x, y), ahaantime, font=font, fill="#FFFFFF")
        draw.text((x, y + 20), text, font=font, fill="#FFFFFF")
        draw.text((x, y + 40), text2, font=font, fill="#FFFFFF")
    elif int(strftime("%H")) == 20:
        text = "The sun is at an angle"
        var = 15 * int(strftime("%H")) - 90
        text2 = "of " + str(var) + " degrees"
        draw.text((x, y), ahaantime, font=font, fill="#FFFFFF")
        draw.text((x, y + 20), text, font=font, fill="#FFFFFF")
        draw.text((x, y + 40), text2, font=font, fill="#FFFFFF")
    elif int(strftime("%H")) == 21:
        text = "The sun is at an angle"
        var = 15 * int(strftime("%H")) - 90
        text2 = "of " + str(var) + " degrees"
        draw.text((x, y), ahaantime, font=font, fill="#FFFFFF")
        draw.text((x, y + 20), text, font=font, fill="#FFFFFF")
        draw.text((x, y + 40), text2, font=font, fill="#FFFFFF")
    elif int(strftime("%H")) == 22:
        text = "The sun is at an angle"
        var = 15 * int(strftime("%H")) - 90
        text2 = "of " + str(var) + " degrees"
        draw.text((x, y), ahaantime, font=font, fill="#FFFFFF")
        draw.text((x, y + 20), text, font=font, fill="#FFFFFF")
        draw.text((x, y + 40), text2, font=font, fill="#FFFFFF")
    elif int(strftime("%H")) == 23:
        text = "The sun is at an angle"
        var = 15 * int(strftime("%H")) - 90
        text2 = "of " + str(var) + " degrees"
        draw.text((x, y), ahaantime, font=font, fill="#FFFFFF")
        draw.text((x, y + 20), text, font=font, fill="#FFFFFF")
        draw.text((x, y + 40), text2, font=font, fill="#FFFFFF")

    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 12)
    y = top
    text = "This clock measures time based"
    text2 = "on the angle of the sun"
    text3 = "relative to the sunrise (6am) being 0"
    draw.text((x, y+60), text, font=font, fill="#FFFFFF")
    draw.text((x, y+80), text2, font=font, fill="#FFFFFF")
    draw.text((x, y+100), text3, font=font, fill="#FFFFFF")
    # Display image.
    disp.image(image, rotation)
    time.sleep(1)

