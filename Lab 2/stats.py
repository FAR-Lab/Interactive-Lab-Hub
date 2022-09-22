import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
from adafruit_rgb_display.rgb import color565
import adafruit_rgb_display.st7789 as st7789

from time import strftime, sleep

def resize(image):
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

# these setup the code for our buttons and the backlight and tell the pi to treat the GPIO pins as digitalIO vs analogIO
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

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
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

# these setup the code for our buttons and the backlight and tell the pi to treat the GPIO pins as digitalIO vs analogIO
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    # Shell scripts for system monitoring from here:
    # https://unix.stackexchange.com/questions/119126/command-to-display-memory-usage-USD-usage-and-WTTR-load
    # cmd = "hostname -I | cut -d' ' -f1"
    # IP = "IP: " + subprocess.check_output(cmd, shell=True).decode("utf-8")
    # cmd = "curl -s wttr.in/?format=2"
    # WTTR = subprocess.check_output(cmd, shell=True).decode("utf-8")
    # cmd = 'curl -s ils.rate.sx/1USD | cut -c1-6'
    # USD = "$1USD = ₪" + subprocess.check_output(cmd, shell=True).decode("utf-8") + "ILS"
    # cmd = "cat /sys/class/thermal/thermal_zone0/temp |  awk '{printf \"CPU Temp: %.1f C\", $(NF-0) / 1000}'" 
    # Temp = subprocess.check_output(cmd, shell=True).decode("utf-8")

    # Write four lines of text.
    # y = top
    # draw.text((x, y), IP, font=font, fill="#FFFFFF")
    # y += font.getsize(IP)[1]
    # draw.text((x, y), WTTR, font=font, fill="#FFFF00")
    # y += font.getsize(WTTR)[1]
    # draw.text((x, y), USD, font=font, fill="#0000FF")
    # y += font.getsize(USD)[1]
    # draw.text((x, y), Temp, font=font, fill="#FF00FF")

    # Display image.
    # disp.image(image, rotation)
    # print (strftime("%m/%d/%Y %H:%M:%S"), end="", flush=True)
    # print("\r", end="", flush=True)
    # sleep(1)
    Clo1 = strftime("%m/%d/%Y")
    Clo2 = strftime("%H:%M:%S")
    

    
    if buttonA.value and buttonB.value:
        y = top
        draw.text((x, y), Clo1, end="", flush=True, font=font, fill="#FFFFFF")
        y += font.getsize(Clo2)[1]
        draw.text((x, y), Clo2, font=font, fill="#FFFFFF")  # turn off backlight
   
   
    else:
        backlight.value = True  # turn on backlight
    if buttonB.value and not buttonA.value:  # just button A pressed
        my_image = Image.open("red.jpg")
        new_image = my_image.resize((135,240))

     

        disp.image(new_image) # set the screen to the users color



    if buttonA.value and not buttonB.value:  # just button B pressed
        disp.fill(color565(255, 255, 255))  # set the screen to white
    if not buttonA.value and not buttonB.value:  # none pressed
        disp.fill(color565(0, 255, 0))  # green



    # Display image.
    disp.image(image, rotation)
    time.sleep(0.1)
