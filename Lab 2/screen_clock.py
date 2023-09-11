import time
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

while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=400)

    #TODO: Lab 2 part D work should be filled in here. You should be able to look in cli_clock.py and stats.py 
    current_time = time.strftime("%m/%d/%Y %H:%M:%S")
    y = top
    draw.text((x, y), current_time, font=font, fill="#FFFFFF")

    # Display image.
    disp.image(image, rotation)
    time.sleep(1)

while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    
    #TODO: Lab 2 part D work should be filled in here. You should be able to look in cli_clock.py and stats.py 
    current_time = time.strftime("%m/%d/%Y %H:%M:%S")
    
    # Implement a recurring switch function for buttonA (4 cases)
    if buttonA.value and not buttonB.value:
        buttonA_current_case = (buttonA_current_case + 1) % 4
        # Implement your logic for buttonA press here based on buttonA_current_case
        # Update the text color based on the current case
        if buttonA_current_case == 0:
            image = Image.open("red.jpg")
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
            text_color = "#FF0000"  # Red
        elif buttonA_current_case == 1:
            text_color = "#FFFF00"  # Yellow
        elif buttonA_current_case == 2:
            text_color = "#0000FF"  # Blue
        elif buttonA_current_case == 3:
            text_color = "#FF00FF"  # Magenta
        # Add your custom functionality for each case here

    # Implement a recurring switch function for buttonB (2 cases)
    if buttonB.value and not buttonA.value:
        buttonB_current_case = (buttonB_current_case + 1) % 2
        
        # Implement your logic for buttonB press here based on buttonB_current_case
        # Update the text color bas
        if buttonB_current_case == 0:
            text_color = "#00FF00"  # Green
        elif buttonB_current_case == 1:
            # Add your custom functionality for this case
            pass

    # Display image.
    backlight.value = not (buttonA.value and buttonB.value)  # Turn off backlight when both buttons are pressed

    # Display the current_time with the calculated x, y coordinates
    y = top
    draw.text((x, y), current_time, font=font, fill=text_color)
    disp.image(image, rotation)
    time.sleep(1)
