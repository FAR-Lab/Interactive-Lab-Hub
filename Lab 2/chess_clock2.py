import time
from datetime import datetime
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
from time import strftime, sleep

# import qwiic_button library
import qwiic_button

# Configuration for proximity sensor
import busio
import adafruit_apds9960.apds9960
from adafruit_apds9960.apds9960 import APDS9960
i2c = board.I2C()
apds = APDS9960(i2c)
apds.enable_proximity = True

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
font = ImageFont.truetype("/usr/share/fonts/truetype/roboto/RobotoMono.ttf", 32)
small_font = ImageFont.truetype("/usr/share/fonts/truetype/roboto/RobotoMono.ttf", 20)

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

# Ask time input


time_limit = int(input('Input time in seconds: '))

# Add initial time variables
now = time.time()
time_a = time_limit
time_b = time_limit
future_a = now + time_a
future_b = now + time_b
future_a_updated = time_a
future_b_updated = time_b

# Add Qwiic button
my_button = qwiic_button.QwiicButton()
brightness = 100

while True:
    # Draw starting position
    
    if state == True:
        draw.rectangle((0, 0, 120, height), outline=0, fill="#875AFF")
        draw.rectangle((120, 0, width, height), outline=0, fill="#191919")
        draw.text((45,50), str(round(future_a - time.time())), font=font, fill="#FFFFFF")
        draw.text((155,50), str(future_b_updated), font=font, fill="#FFFFFF")
        if round(future_a - time.time()) < 0:
            draw.rectangle((0, 0, width, height), outline=0, fill="#D2011B")
            msg = "Game Over!"
            msg_2 = "Player B wins"
            w, h = draw.textsize(msg)
            w2, h2 = draw.textsize(msg_2)
            draw.text(((width-w)/2 - 25, 45), msg, font=small_font, fill="#FFFFFF")
            draw.text(((width-w2)/2 - 25, 40 + font.getsize(msg)[1]), msg_2, font=small_font, fill="#FFFFFF")
    else:
        draw.rectangle((0, 0, 120, height), outline=0, fill="#191919")
        draw.rectangle((120, 0, width, height), outline=0, fill="#875AFF")
        draw.text((45,50), str(future_a_updated), font=font, fill="#FFFFFF")
        draw.text((155,50), str(round(future_b - time.time())), font=font, fill="#FFFFFF")
        if round(future_b - time.time()) < 0:
            draw.rectangle((0, 0, width, height), outline=0, fill="#D2011B")
            msg = "Game Over!"
            msg_2 = "Player A wins"
            w, h = draw.textsize(msg)
            w2, h2 = draw.textsize(msg_2)
            draw.text(((width-w)/2 - 25, 45), msg, font=small_font, fill="#FFFFFF")
            draw.text(((width-w2)/2 - 25, 40 + font.getsize(msg)[1]), msg_2, font=small_font, fill="#FFFFFF")

    # Create button triggers to adjust state
    if apds.proximity > 0 and state == True:  # just button A pressed
        my_button.LED_on(brightness)
        state = False
        future_a_updated = round(future_a - time.time())
        future_b = future_b_updated + time.time()
        time.sleep(0.5)
    if apds.proximity > 0 and state == False:  # just button B pressed
        my_button.LED_on(brightness)
        state = True
        future_b_updated = round(future_b - time.time())  # create snapshot of time remaining
        future_a = future_a_updated + time.time()  # update new future time
        time.sleep(0.5)
    else:
        my_button.LED_off()
    
    if my_button.is_button_pressed() == True:
        my_button.LED_on(brightness)
        now2 = time.time()
        time_a = time_limit
        time_b = time_limit
        future_a = now2 + time_a
        future_b = now2 + time_b
        future_a_updated = time_a
        future_b_updated = time_b   

    # y = top
    # draw.text((x, y), str(state), font=font, fill="#875AFF")

    # Display image.
    disp.image(image, rotation)
    time.sleep(0.1)
