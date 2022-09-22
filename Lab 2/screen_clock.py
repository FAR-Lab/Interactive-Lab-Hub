import time
from time import strftime
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
from adafruit_rgb_display.rgb import color565

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
disp2 = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=100,
    y_offset=190,
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

# these setup the code for our buttons and the backlight and tell the pi to treat the GPIO pins as digitalIO vs analogIO
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

while True:
    # Draw a black filled box to clear the image.
    # draw.rectangle((0, 0, width, height), outline=0, fill=0)

    #TODO: Lab 2 part D work should be filled in here. You should be able to look in cli_clock.py and stats.py 

    # Draw a black filled box to clear the image.
    # draw.rectangle((0, 0, width, height), outline=0, fill=0)


    Clo1 = strftime("%m/%d/%Y")
    #Clo2 = strftime("%H:%M:%S")
    ftime = ("10:00")

    
    if buttonA.value and buttonB.value:
        y = top
        draw.text((x, y), Clo1, end="", flush=True, font=font, fill="#FFFFFF")
        y += font.getsize(ftime)[1]
        draw.text((x, y), ftime, font=font, fill="#FFFFFF")  # turn off backlight
        disp.image(image, rotation)
        # y += font.getsize(new_fullmoon)[1]
        fullmoon = Image.open("Crescent_moon.jpg")
        new_fullmoon = fullmoon.resize((90,90))
        rotated_moon = new_fullmoon.rotate(-90)
        disp2.image(rotated_moon)
   

        y = top
        my_image1 = Image.open("ocean2.jpeg")
        new_image1 = my_image1.resize((120,120))
        # Rotate Image By 180 Degree
        rotated_image1 = new_image1.rotate(90)
        
        disp.image(rotated_image1)
        
    else:
        backlight.value = True  # turn on backlight
    if buttonB.value and not buttonA.value:  # just button A pressed
        my_image2 = Image.open("blue_fish.jpg")
        new_image2 = my_image2.resize((135,240))
        rotated_image2 = new_image2.rotate(90)
        disp.image(rotated_image2)



    if buttonA.value and not buttonB.value:  # just button B pressed
        disp.fill(color565(191, 19, 195))  # set the screen to white
    if not buttonA.value and not buttonB.value:  # none pressed
        disp.fill(color565(0, 255, 0))  # green

    # Display image.
    # disp.image(image, rotation)
    time.sleep(0.1)

    