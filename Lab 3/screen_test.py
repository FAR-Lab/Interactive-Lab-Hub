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
emoticon_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 28)
text_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 23)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

# Test related
sleep_emoticon = "(-_-) zzzZZZ"
wakeup_emoticon = "╭( ๐ _๐)╮"
result_emoticon = "٩( ᐛ )و"

welcome_text = "Welcome to PiTest!"
welcome_text_2 = "Please answer the questions."

question_text = "Which animals do you think you are?"
question_text_2 = "If it doesn't exist, which" 
question_text_3 = "other animal do you think you are?"

result_text = "You are an INFP!"

buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

def draw_text(mode):
    if mode==1:
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        y = top
        draw.text((x, y), wakeup_emoticon, font=emoticon_font, fill="#FF7D99")
        y += (emoticon_font.getsize(wakeup_emoticon)[1])*2
        draw.text((x, y), welcome_text, font=text_font, fill="#FFFFFF")
        y += (text_font.getsize(welcome_text)[1])
        draw.text((x, y), welcome_text_2, font=text_font, fill="#FFFFFF")
        disp.image(image, rotation)
        time.sleep(3)
        mode=2
        
    elif mode==2:
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        y = top
        draw.text((x, y), question_text, font=text_font, fill="#FFFFFF")
        time.sleep(3)
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        y = top
        draw.text((x, y), question_text_2, font=text_font, fill="#FFFFFF")
        y += (text_font.getsize(question_text_2)[1])
        draw.text((x, y), question_text_2, font=text_font, fill="#FFFFFF")
        disp.image(image, rotation)
        time.sleep(3)
        mode=3
        
    elif mode==3:
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        y = top
        draw.text((x, y), result_emoticon, font=emoticon_font, fill="#FF7D99")
        y += (emoticon_font.getsize(result_emoticon)[1])*2
        draw.text((x, y), result_text, font=text_font, fill="#FFFFFF")
        disp.image(image, rotation)
        time.sleep(5)
        mode = 0
    else:
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        y = top
        draw.text((x, y), sleep_emoticon, font=emoticon_font, fill="#FF7D99")
        disp.image(image, rotation)
        time.sleep(1)
