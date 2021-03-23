import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
from time import strftime, sleep


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

buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)


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
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 22)
# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    #TODO: fill in here. You should be able to look in cli_clock.py and stats.py


    image = Image.open("time.jpg")
    backlight = digitalio.DigitalInOut(board.D22)
    backlight.switch_to_output()
    backlight.value = True


    # Scale the image to the smaller screen dimension
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

    # Display image.

    curTime = strftime("%H:%M:%S")
    draw = ImageDraw.Draw(image)
    if buttonA.value and buttonB.value:  # just button A pressed
        # display.fill(screenColor) # set the screen to the users color
        # backlight.value = False  # turn off backlight
        curTime = strftime("%H:%M:%S")

        curHour = int(strftime("%H"))
        # print(type(curHour))
        draw = ImageDraw.Draw(image)
        unitWidth = disp.width/4
        unitHeight = disp.height/6
        # print(unitWidth, unitHeight)
        draw.rectangle( (0,0, width, height), fill =(0,0,0), outline =(0,0,0))
        for i in range(curHour):
            shape = [(i%6)*unitHeight,(i//6)*unitWidth,(i%6)*unitHeight+unitHeight,(i//6)*unitWidth+unitWidth]
            if i<8 or i>20:
                draw.rectangle( shape, fill =(0,120,180), outline =(0,0,0))
            else:
                draw.rectangle( shape, fill =(i*10,i*10,0), outline =(0,0,0))
        draw.text((0, top), "Press Button\n To See Clock \n Upper button: Date \n Upper button: Time", font=font, fill="#FFFFFF")
    elif buttonB.value:
        curDate = strftime("%m/10/%Y")
        draw.text((0, top), curDate, font=font, fill="#0000FF")
        print("B button")

    else:
        # image = Image.new("RGB", (width, height))
        # backlight.value = True  # turn off backlight
        draw.text((0, top), curTime, font=font, fill="#0000FF")
        print("A button")



    disp.image(image, rotation)

    time.sleep(1)
