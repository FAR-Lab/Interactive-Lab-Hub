import time
import subprocess
import digitalio
import board
import math
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

# Add buttons
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

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

# Reference for helper functions: Stackoverflow post on how to
# draw sun rays using PIL
# https://stackoverflow.com/questions/26747587/python-pil-to-draw-a-circle-segment-of-sunshine

def drawRays(begin=270, fin=630, thickness=5, gap=25):
    
    for start in range(begin, fin, thickness+gap):
        end = (start+thickness) * math.pi/180
        start = start*(math.pi/180)
        
        x1 = (width/2) + 70*math.cos(start)
        y1 = (height/2) + 70*math.sin(start)
        x2 = (width/2) + 70*math.cos(end)
        y2 = (height/2) + 70*math.sin(end)
        
        
        draw.polygon([(width/2, height/2), (x1,y1), (x2,y2)], fill = 'orange', outline='yellow')
            
def drawStars(begin=270, fin=630, thickness=10, gap=20):
    for start in range(begin, fin, thickness+gap):
        end = (start+thickness)*math.pi/180
        start = start * math.pi/180
        
        x1 = (width/2) + 60*math.cos(start)
        y1 = (height/2) + 60*math.sin(start)
        x2 = (width/2) + 60*math.cos(end)
        y2 = (height/2) + 60*math.sin(end)
        x3 = (width/2) + 60*math.cos(start) - 5
        y3 = (height/2) + 60*math.sin(start) - 5
        x4 = (width/2) + 60*math.cos(end) + 5
        y4 = (height/2) + 60*math.sin(end) + 5
        x5 = (width/2) + 60*math.cos(start) - 10
        y5 = (height/2) + 60*math.sin(start) - 10
        x6 = (width/2) + 60*math.cos(start)
        y6 = (height/2) + 60*math.sin(start) 
        draw.line([x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6], fill='yellow')

while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    #TODO: Lab 2 part D work should be filled in here. You should be able to look in cli_clock.py and stats.p
    # Daytime functionality
    if int(time.strftime("%H")) >= 6 and int(time.strftime("%H")) < 19:
            # Draw sky
            draw.rectangle((0, 0, width, height), outline=0, fill="skyBlue")
            # Draw sun rays equivalent to the integer value of the Hour (between 1-12)
            drawRays(fin=271+30*(int(time.strftime("%H"))%12))
            # Draw sun
            draw.ellipse([width/2-30, height/2 - 30, width/2 + 30, height/2 + 30], fill='#ffff33', outline='orange')
    # Nighttime functionality
    else:
            # draw nighttime sky
            draw.rectangle((0, 0, width, height), outline=0, fill=0)
            # draw moon
            draw.ellipse([width/2-30, height/2 - 30, width/2 + 30, height/2 + 30], fill='#ffff33')
            # draw black circle to create crescent 
            draw.ellipse([width/2-30, height/2 - 30, width/2 + 10 , height/2 + 30], fill=0)   
            # draw number of stars equivalent to the integer value of the hour
            drawStars(fin=271+30*(int(time.strftime("%H"))%12))
    
    # First button functionality
    if buttonB.value and not buttonA.value:
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        draw.text((0, 0), time.strftime("%m/%d/%Y %H:%M:%S"), font=font, fill="#FFFFFF")
    # Second button functionality
    if buttonA.value and not buttonB.value:
        if int(time.strftime("%H")) >= 6 and int(time.strftime("%H")) < 19:
            draw.rectangle((0, 0, width, height), outline=0, fill="skyBlue")
            draw.text((0, 0), "The sun is shining!", font=font, fill="#FFFFFF")
        else:
            draw.rectangle((0, 0, width, height), outline=0, fill=0)
            draw.text((0, 0), "What a wonderful night!", font=font, fill="#FFFFFF")
    # Display image.
    disp.image(image, rotation)
    time.sleep(1)
