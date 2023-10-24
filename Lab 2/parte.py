import time
import pytz
import datetime
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
buttonA = digitalio.DigitalInOut(board.D23)	
buttonB = digitalio.DigitalInOut(board.D24)	
buttonA.switch_to_input()	
buttonB.switch_to_input()

background_list = ["liberty.jpg", "paris.jpg", "au.jpg", "china.jpg"]

background_image = []
for image_name in background_list:
    bg_image = Image.open(image_name)	
    bg_image = bg_image.resize((width, height))
    background_image.append(bg_image)

def get_current_time_in_timezone(timezone_str):
    """Return the current time in the specified timezone."""
    local_timezone = pytz.timezone(timezone_str)
    local_time = datetime.datetime.now(local_timezone)
    return local_time

location_list = ['America/New_York', 
                 'Europe/Paris',
                 'Australia/Canberra',
                 'Asia/Shanghai'
                ]

index = 0
count = 0

def update_display(background_image, index, format_12_hour=True):
    """Updates the display with the given background and time format."""
    image.paste(background_image[index], (0, 0))
    if format_12_hour:
        current_time = get_current_time_in_timezone(location_list[index]).strftime("%m/%d/%Y %I:%M:%S %p")
    else:
        current_time = get_current_time_in_timezone(location_list[index]).strftime("%m/%d/%Y %H:%M:%S")
    text_offset = 10
    text_box = [(0, height // 2 - text_offset), (x + width, height // 2 + text_offset)]
    draw.rectangle(text_box, fill="#FFFFFF")
    draw.text((10, height // 2 - text_offset), current_time, font=font, fill="#000000")
    disp.image(image, rotation)

index = 0
format_12_hour = True

buttonA_pressed_last = False
buttonB_pressed_last = False

while True:
    if not buttonB.value and not buttonB_pressed_last:
        index = (index + 1) % len(background_list)
        buttonB_pressed_last = True
    elif buttonB.value:
        buttonB_pressed_last = False

    if not buttonA.value and not buttonA_pressed_last:
        format_12_hour = not format_12_hour
        buttonA_pressed_last = True
    elif buttonA.value:
        buttonA_pressed_last = False
    
    update_display(background_image, index, format_12_hour)
    time.sleep(0.1)