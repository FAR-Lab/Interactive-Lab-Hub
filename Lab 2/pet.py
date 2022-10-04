import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
import cv2
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

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
if disp.rotation % 180 == 90:
    height = disp.width  # we swap height/width to rotate it to landscape!
    width = disp.height
else:
    width = disp.width  # we swap height/width to rotate it to landscape!
    height = disp.height
image = Image.new("RGB", (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image)

#image = Image.open("red.jpg")
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True


# Scale the image to the smaller screen dimension
def rs(image):
    
    image.thumbnail([240, 135])
    x = 0
    y = 0
    draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
    
    #disp.image(image, 90)
    return image 
    #image = rs(image)

buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()


import os
pics = []
for filename in os.listdir("./poke"):
    f = os.path.join("./poke", filename)
    pics.append(Image.open(f))


i = 0
from time import strftime, sleep
import random
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
response = ['Yummy', 'I love snacks', 'Thank you', "That was delicious"]

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

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True



while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    
    h = strftime('%H')
    p = strftime('%p')

    if p != 'PM':
        i = 0
    else:
        if int(h) < 6 or int(h) == 12:
            i = 1
        else:
            i = 2
        
    pic = rs(pics[i])
    disp.image(pic, 90)


    if buttonB.value and not buttonA.value:  # just button A pressed
        import os
        os.system('aplay Slam.wav')

    if buttonA.value and not buttonB.value:
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        t = random.choice(response)
        y = top
        draw.text((x, y), t, font=font, fill="#FFFFFF")
        y += font.getsize(t)[1]
        disp.image(image, rotation)
        time.sleep(2)
        disp.fill(color565(0, 0, 0))
    
