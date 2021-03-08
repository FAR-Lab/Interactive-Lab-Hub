import time
from time import strftime, sleep
from datetime import datetime, timedelta
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

# Clock related
LINE = "================"
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

# DIET is used to record the time of my daily 8-hour dieting period ending time
# buttonA is used to display the ending time
# buttonB (pressed together with buttonA) is used to save the ending time
DIET=None
PAGE=0

while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    #TODO: fill in here. You should be able to look in cli_clock.py and stats.py
    if PAGE==0:
        TIME = "TIME: "+ strftime("%m/%d/%Y %H:%M:%S")
        y = top
        draw.text((x, y), TIME, font=font, fill="#FFFFFF")
    elif PAGE==1:
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        # Add Night & Late Night Notifier
        hour = int(time.strftime("%H"))
        if (hour >= 23):
            NIGHT="It's late night!!!"
        elif (hour >= 21):
            NIGHT="It's night time!"
        else:
            NIGHT="Not night time."
            y += (font.getsize(TIME)[1])*(1.5)
            draw.text((x, y), LINE, font=font, fill="#FFFFFF")    
            y += font.getsize(LINE)[1]
            draw.text((x, y), NIGHT, font=font, fill="#FFFFFF")  
            y += font.getsize(NIGHT)[1]
            draw.text((x, y), LINE, font=font, fill="#FFFFFF")
    else:
        if DIET:
            draw.rectangle((0, 0, width, height), outline=0, fill=0)
            y += font.getsize(LINE)[1]
            draw.text((x, y), DIET, font=font, fill="#FFFFFF")
            
        # Update DIET
        if buttonA.value and not buttonB.value:
            eight_hours_from_now = datetime.now() + timedelta(hours=8)
            DIET="DIET ENDING AT: " + format(eight_hours_from_now, '%H:%M:%S')

    if buttonB.value and not buttonA.value:
        if PAGE==2:
            PAGE=0
        else:
            PAGE+=1
            
    # Display image.
    disp.image(image, rotation)
    time.sleep(1)
