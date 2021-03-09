from time import strftime, sleep
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
import os


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

    # Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=0)

a = strftime("%H:%M")
c = ""
cmd = "curl -s wttr.in/?format=2"
cmd2 = "curl -s wttr.in/?format=%t"
cmd3 = "curl -s wttr.in/?format=%w"
TEMP = str(subprocess.check_output(cmd2, shell=True).decode("utf-8"))
WIND = str(subprocess.check_output(cmd3, shell=True).decode("utf-8"))
TEMP2 = str(int(''.join(filter(str.isdigit, TEMP))))
WIND2 = str(int(''.join(filter(str.isdigit, WIND))))
print(TEMP2)
print(WIND2)
WTTR = subprocess.check_output(cmd, shell=True).decode("utf-8")
y = top
tem = str(WTTR[6:8])
wind = str(WTTR[13])
exercise = ""
img = ""
while True:
    if buttonA.value and not buttonB.value:
        if str(1000)<= a < str(1300):
            if str(20) <=TEMP2 <= str(70):
                if str(0) <= WIND2 <= str(10):
                    c = "Outdoor: running\n "
                if str(10) <= WIND2 <= str(15):
                    c = "Indoor:squats\n"
            if str(70) <= TEMP2:
                c = "Indoor: yoga\n"
            draw.text((x, y), a, font=font, fill="#FFFFFF")
            y += font.getsize(a)[1]
            draw.text((x, y), WTTR, font=font, fill="#FFFFFF")
            y += font.getsize(WTTR)[1]
            draw.text((x, y), c, font=font, fill="#FFFFFF")
            y += font.getsize(c)[1]
            disp.image(image, rotation)
            sleep(1)
        if str(1300)<= a <= str(1600):
            if str(20) <=TEMP2 <= str(70):
                if str(0) <= WIND2 <= str(10):
                    c = "Outdoor: running\n "
                if str(10) <= WIND2 <= str(15):
                    c = "Indoor:squats\n"
            if str(70) <= TEMP2:
                c = "Indoor: yoga\n"
            draw.text((x, y),a, font=font, fill="#FFFF00")
            y += font.getsize(a)[1]
            draw.text((x, y), WTTR, font=font, fill="#FFFF00")
            y += font.getsize(WTTR)[1]
            draw.text((x, y), c, font=font, fill="#FFFF00")
            y += font.getsize(c)[1]
            disp.image(image, rotation)
            sleep(1)
        if str(1800)<= a <= str(2200):
            if str(20) <= TEMP2 <= str(70):
                if str(0) <= WIND2 <= str(10):
                    print(TEMP2, WIND2)
                    c = "Indoor: HIIT\n"
                if str(10) <= WIND2 <= str(15):
                    c = "Indoor: squats\n"
            if str(70) <= TEMP2:
                c = "Indoor: yoga\n"
            draw.text((x, y), a, font=font, fill="#0000FF")
            y += font.getsize(a)[1]
            draw.text((x, y), WTTR, font=font, fill="#0000FF")
            y += font.getsize(WTTR)[1]
            draw.text((x, y), c, font=font, fill="#0000FF")
            y += font.getsize(c)[1]
            disp.image(image, rotation)
            sleep(1)
    
    if buttonB.value and not buttonA.value: 
        if disp.rotation % 180 == 90:
            height = disp.width  # we swap height/width to rotate it to landscape!
            width = disp.height
        else:
            width = disp.width  # we swap height/width to rotate it to landscape!
            height = disp.height
        image = Image.new("RGB", (width, height))      
        draw = ImageDraw.Draw(image)
        draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
        disp.image(image)
        
        image = Image.open("sports.jpg").convert('RGB')
        backlight = digitalio.DigitalInOut(board.D22)
        backlight.switch_to_output()
        backlight.value = True
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
        disp.image(image)


