# PI Requirements
import board
import busio
import adafruit_mpr121
import RPi.GPIO as GPIO
from adafruit_servokit import ServoKit

# Preliminary Setup
kit = ServoKit(channels=8)
i2c = busio.I2C(board.SCL, board.SDA) # Required 
mpr121 = adafruit_mpr121.MPR121(i2c) # CircuitPython driver for the MPR121 capacitive touch breakout board.

#############################################

# new import 
import adafruit_rgb_display.st7789 as st7789
import digitalio
from PIL import Image, ImageDraw, ImageFont

# remove warnings 
import warnings 
warnings.filterwarnings("ignore", category=DeprecationWarning)

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
height = disp.height  # we swap height/width to rotate it to landscape!
width = disp.width
print(height)
print(width)
print(disp.height)
print(disp.width)

image_fill = Image.new("RGB", (height, width))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image_fill)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image_fill, rotation)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0
y = 0

font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)

backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

#############################################

# Custom For Game Import
import time
import random 
from threading import Thread
import os

# Game
random_value_list = []
value_selected = []
t = 10

# Thread countdown
def countdown():
    global t
    global y
    while True:
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            y += 200
            print(timer, end="\r")
            time.sleep(1)
            t -= 1

# Set random variable to click
def RandomValueSet(value):
    if(value in random_value_list):
        print("Got " + str(value))
        random_value_list.remove(value)
    if(len(random_value_list) == 0):
        return True

# Random value gather
def RandomValueGather():
    random_value_list.clear()

    for i in range(0, 3):
        random_value_list.append(random.randint(1, 8))

    return RandomValueGather

timer_thread = Thread(target=countdown, args=[])
timer_thread.start()
RandomValueGather()

# Main Loop
while True:

    # Thread for countdown
    while(timer_thread.is_alive()):
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        if(t == 0):
            RandomValueGather()
            t = 10
            os.system('cls||clear')
            print("You have " + str(t) + " seconds to select the 3 numbers!" + "\n")
            print("Numbers: " + str(random_value_list) + "\n")

        for i in range(12):
            if(mpr121[i].value):
                if(RandomValueSet(i) and t != 0):
                    draw.rectangle((0, 0, width, height), outline=0, fill=0)
                    y = top+36
                    draw.text((x, y), str("you won!"), font=font, fill="#FFFFFF")
                    disp.image(image_fill,rotation) 
                    print("You got them!" + "\n")
                    break

        y = top
        draw.text((x, y), str(random_value_list), font=font, fill="#FFFFFF")
        y = top + 72
        draw.text((x, y), "00:0" + str(t), font=font, fill="#FFFFFF")
        disp.image(image_fill,rotation)

    time.sleep(1)
    print("\n Go again \n")

# Properly exit
GPIO.cleanup()

