import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789

from suntime import Sun
from datetime import datetime, timedelta
import pytz
import matplotlib as mpl
import numpy as np

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
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 40)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

def colorFader(c1,c2,mix=0): #fade (linear interpolate) from color c1 (at mix=0) to c2 (mix=1)
    c1=np.array(mpl.colors.to_rgb(c1))
    c2=np.array(mpl.colors.to_rgb(c2))
    return mpl.colors.to_hex((1-mix)*c1 + mix*c2)

#color selection
sunset = '#9c0041'
daytime = '#ff8400'
nighttime = '#2d006b'

#setup buttons
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

cycle = 0
toggle = False

while True:
    # Draw a black filled box to clear the image.
    # draw.rectangle((0, 0, width, height), outline=0, fill="#000000")

    #TODO: Lab 2 part D work should be filled in here. You should be able to look in cli_clock.py and stats.py 
    if not buttonA.value:
        toggle = True 
    if not buttonB.value:
        toggle = False
        cycle = 0

    lat = 40.7619
    lng = -73.9501
    
    sun = Sun(lat, lng)

    y = top
    x=0

    today = datetime.utcnow().replace(tzinfo=pytz.utc)
    today_local = datetime.now()
    if toggle:
        today = today + timedelta(hours = cycle)
        today_local = today_local + timedelta(hours = cycle)
        cycle += 1
    time_str = today_local.strftime("%H:%M:%S")

    today_sr = sun.get_sunrise_time(today)
    today_ss = sun.get_sunset_time(today)

    bg_color = "#000000"

    #pre sunrise
    if today < today_sr:
        yesterday = today - timedelta(days=1)
        yesterday_ss = sun.get_sunset_time(yesterday)
        total_delta = today_sr - yesterday_ss
        curr_delta = today - yesterday_ss
        ratio = float(curr_delta.seconds)/float(total_delta.seconds)
        if ratio <= 0.5:
            ratio = ratio * 2.0
            bg_color = colorFader(sunset, nighttime, ratio)
        else:
            ratio = ratio * 2.0
            ratio = ratio - 1.0
            bg_color = colorFader(nighttime, sunset, ratio)

    #daytime
    elif today < today_ss:
        total_delta = today_ss - today_sr
        curr_delta = today - today_sr
        ratio = float(curr_delta.seconds)/float(total_delta.seconds)
        if ratio <= 0.5:
            ratio = ratio * 2.0
            bg_color = colorFader(sunset, daytime, ratio)
        else:
            ratio = ratio * 2.0
            ratio = ratio - 1.0
            bg_color = colorFader(daytime, sunset, ratio)
    #post sunset
    else:
        tomorrow = today + timedelta(days=1)
        tomorrow_sr = sun.get_sunrise_time(tomorrow)
        total_delta = tomorrow_sr - today_ss
        curr_delta = today - today_ss
        ratio = float(curr_delta.seconds)/float(total_delta.seconds)
        if ratio <= 0.5:
            ratio = ratio * 2.0
            bg_color = colorFader(sunset, nighttime, ratio)
        else:
            ratio = ratio * 2.0
            ratio = ratio - 1.0
            bg_color = colorFader(nighttime, sunset, ratio)

    #Draw background based on with color sun position
    draw.rectangle((0, 0, width, height), outline=0, fill=bg_color)

    #sunrise_str = 'Sunrise: ' + today_sr.strftime("%m/%d/%Y %H:%M:%S")
    #draw.text((x, y), sunrise_str, font=font, fill="#FFFFFF")

    #sunset_str = 'Sunset: ' + today_ss.strftime("%m/%d/%Y %H:%M:%S")
    #draw.text((x, y), sunset_str, font=font, fill="#FFFFFF")
    y += 45
    x += 30

    draw.text((x, y), time_str, font=font, fill="#FFFFFF")


    # Display image.
    disp.image(image, rotation)
    time.sleep(1)
