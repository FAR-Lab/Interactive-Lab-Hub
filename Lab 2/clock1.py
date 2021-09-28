import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
from time import strftime, sleep
from random import randint
import busio
from i2c_button import I2C_Button
#from __future__ import print_function
import qwiic_button 
import time
import sys
# initialize I2C
i2c = busio.I2C(board.SCL, board.SDA)

# scan the I2C bus for devices
while not i2c.try_lock():
        pass
devices = i2c.scan()
i2c.unlock()
print('I2C devices found:', [hex(n) for n in devices])
default_addr = 0x6f
if default_addr not in devices:
        print('warning: no device at the default button address', default_addr)

# initialize the button
button = I2C_Button(i2c)

def image_resize(image):
        image = image.convert('RGB')
        image_ratio = image.width / image.height
        screen_ratio = width / height
        if screen_ratio < image_ratio:
                scaled_width = image.width * height // image.height
                scaled_height = height
        else:
                scaled_width = width
                scaled_height = image.height * width // image.width
        image = image.resize((scaled_width, scaled_height), Image.BICUBIC)
        # Crop and center the image
        x = scaled_width // 2 - width // 2
        y = scaled_height // 2 - height // 2
        image = image.crop((x, y, x + width, y + height))
        return image

# demonstrate writing to registers
button.led_bright = randint(0, 255)
button.led_gran = randint(0, 1)
button.led_cycle_ms = randint(250, 2000)
button.led_off_ms = randint(100, 500)


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
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 16)
font1 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 22)
# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True
print('LED brightness', button.led_bright)
print('LED granularity', button.led_gran)
print('LED cycle ms', button.led_cycle_ms)
print('LED off ms', button.led_off_ms)

while True:
    # Draw a black filled box to clear the image.
    #draw.rectangle((0, 0, width, height), outline=0, fill=(255,0, 0))

    #TODO: Lab 2 part D work should be filled in here. You should be able to look in cli_clock.py and stats.py
    hours= int(strftime("%H"))
    minute= int(strftime("%M"))
    if  hours in range(0,2) :
        image2 = Image.open("batman_logo.jpg")
        Greet = "Batman is watching you"
    if  hours in range(2,4):
        image2 = Image.open("batman_logo.jpg")
        Greet = "Batman is watching you"
    if  hours in range(4,6):
        image2 = Image.open("batman_logo.jpg")
        Greet = "Batman is watching you"
    if  hours in range(6,8):
        image2 = Image.open("batman_logo.jpg")
        Greet = "Batman is watching you"
    if  hours in range(8,12):
        image2 = Image.open("batman_logo.jpg")
        Greet = "Batman is watching you"
    if  hours in range(12,14):
        image2 = Image.open("batman_logo.jpg")
        Greet = "Batman is watching you"
    if  hours in range(14,16):
 if  hours in range(14,16):
        image2 = Image.open("batman_logo.jpg")
        Greet = "Batman is watching you"
    if  hours in range(16,18):
        image2 = Image.open("batman_logo.jpg")
        Greet = "Batman is watching you"
    if  hours in range(18,20):
        image2 = Image.open("batman_logo.jpg")
        Greet = "Batman is watching you"
    if  hours in range(20,22):
        image2 = Image.open("batman_logo.jpg")
        Greet = "Batman is watching you"
    if  hours in range(22,24):
        image2 = Image.open ("superman.jpg")
        Greet = "Have a Super awesome day"

    try:
        button.clear() # status must be cleared manually
        time.sleep(1)
        print('status', button.status)
        if button.status.is_pressed == 1:
            image2 = Image.open ("superman.jpg")
        print('last click ms', button.last_click_ms)
        print('last press ms', button.last_press_ms)
    except KeyboardInterrupt:
        button.clear()
        button.led_bright = 0
        button.led_gran = 1
        button.led_cycle_ms = 0
        button.led_off_ms = 100
        break
    hours= int(strftime("%H"))
    minute= int(strftime("%M"))
    image2 = image_resize(image2)
    draw= ImageDraw.Draw(image2)
    if hours % 2 == 0:
Time=  str(minute)
    else :
        Time= str(minute + 60)
    y = top
    draw.text((x, y), Greet, font=font, fill="#FFFF00")
    y += font.getsize(Greet)[1]
    draw.text((x, y), "Minutes Elapsed: "+ Time, font=font1, fill="#FF0000")
    # Display image.
    disp.image(image2, rotation)

    time.sleep(1)
