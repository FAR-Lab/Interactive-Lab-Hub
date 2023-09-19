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

# button settings
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

# daylight
daylight = ["#d1e5ff", "#d1e5ff", "#d9e9f8", "#e1ecf1",
            "#e9f0e9", "#e9f0e9", "#f0f4e2", "#f0f4e2", 
            "#f7f7db", "#f7f7db", "#fdfbd3", "#fdfbd3"
            "#fdfbd3", "#fdfbd3", "#fdfbd3", "#f7f7db", 
            "#f7f7db", "#f7f7db", "#f0f4e2", "#e9f0e9",  
            "#e9f0e9", "#d9e9f8", "#d9e9f8", "#d1e5ff"
            ]

# Image Preprocessing
def pre_process(path):
    image = Image.open("images/" + path)
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
    return image




while True:
    # Draw a black filled box to clear the image.
    # draw.rectangle((0, 0, width, height), outline=0, fill=0)

    #TODO: Lab 2 part D work should be filled in here. You should be able to look in cli_clock.py and stats.py 
    DAY_TIME = time.strftime("%m/%d/%Y %H:%M:%S")
    hour_text = time.strftime('%H')
    hour = int(time.strftime('%H'))
    # Vanilla digital clock in text.
    
    # draw.text((x, y), DAY_TIME, font=font, fill="#000000")
    
    # IMAGE LAYER
    

    if hour == 7:
        image = pre_process("clock.jpeg")
        draw = ImageDraw.Draw(image)
        disp.image(image, rotation)   
    elif hour == 8:
        image = pre_process("brush.png")
        draw = ImageDraw.Draw(image)
        disp.image(image, rotation)
        # draw.rectangle((8, 7, 50, 120), fill=daylight[hour])
        
    elif hour == 11:
        image = pre_process("lunch.jpeg")
        draw = ImageDraw.Draw(image)
        disp.image(image, rotation)
    elif hour == 14:
        image = pre_process("meeting.jpeg")
        draw = ImageDraw.Draw(image)
        disp.image(image, rotation)
    elif hour == 17:
        image = pre_process("finite.jpeg")
        draw = ImageDraw.Draw(image) 
        disp.image(image, rotation)   
    elif hour == 22:
        image = pre_process("bed.png")
        draw = ImageDraw.Draw(image)
        disp.image(image, rotation)
    else:
        image = pre_process("cup2.png")
        draw = ImageDraw.Draw(image)
        disp.image(image, rotation)
        
    if buttonA.value and not buttonB.value:
        while True:
            # print(1)
            text_y = top
            # draw.text((x, text_y), DAY_TIME, font=font, fill="#000000")
            draw.rectangle((8, 7, 50, 120), fill=daylight[hour])
            disp.image(image, rotation)
            time.sleep(1)
            if buttonB.value and not buttonA.value:
                break
  
    disp.image(image, rotation)
    time.sleep(1)
