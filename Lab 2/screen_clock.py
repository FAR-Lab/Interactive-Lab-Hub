import time
import subprocess
import digitalio
import board
import glob
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
from time import strftime, sleep

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
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image_fill = Image.new("RGB", (height, width))
rotation = 90

# Get drawing object to draw on image.
#draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
#draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
#disp.image(image, rotation)
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

# Draw a black filled box to clear the image.
#draw.rectangle((0, 0, width, height), outline=0, fill=0)

# Image size 
normal_size = 135, 240

# Image resize 
images = []
images = glob.glob("./vine/*.png")
print(images)
images = sorted(images)
print(images)
for image_file in images:
    #DEBUG
    #print(image_file)
    with open(image_file, 'rb') as image_file_open:
        img = Image.open(image_file_open)
        imgResize = img.resize((240, 135), Image.ANTIALIAS)
        imgResize.save(image_file, 'PNG')

#TODO: Lab 2 part D work should be filled in here. You should be able to look in cli_clock.py and stats.p 
while True:
    for image_file in images:
        print(image_file)
        with open(image_file, 'rb') as image_file_open:
            img = Image.open(image_file_open)
            disp.image(img, rotation)
        #if rotation >= 270:
            #rotation = 0
        #else: 
            #rotation = rotation + 90
        time.sleep(0.5)
        #disp.image(image_fill)
    break
# Display image.\
#disp.image(image, rotation)
#time.sleep(1)
