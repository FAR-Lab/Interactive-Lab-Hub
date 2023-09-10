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
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 22)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

# Configuring button A (top) and button B (bottom)
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

morning_image = Image.open("morning.jpg")
morning_image = morning_image.resize((width,height))
afternoon_image = Image.open("afternoon.jpg")
afternoon_image = afternoon_image.resize((width,height))
evening_image = Image.open("evening.jpg")
evening_image = evening_image.resize((width,height))
# Idea: everytime you press the button A, you switch from date to time 


# # Create a blank background image
# background_image = Image.new("RGB", (width, height))
while True:
    # Create a copy of the background image
    display_image = morning_image.copy()
    display_image_evening = evening_image.copy()
    # Draw a black filled box to clear the image.
    # draw.rectangle((0, 0, width, height), outline=0, fill=400) #the fill 400 = red

    #TODO: Lab 2 part D work should be filled in here. You should be able to look in cli_clock.py and stats.py 
    # Get the current time in the format "mm/dd/yyyy hh:mm:ss"
    date = time.strftime("%m/%d/%Y")
    current_time = time.strftime("%H:%M:%S")
    if not buttonA.value: # button A is pressed
        x, y = 30, 50  # Adjust the coordinates as needed.
        draw_on_image = ImageDraw.Draw(display_image_evening)
        draw_on_image.text((x, y), date, font=font, fill="#FFFFFF")
        # Display the modified images with the time on the screen
        disp.image(display_image_evening, rotation)

    else: # The default screen   
        # Draw the current time text on the copy of the background image
        x, y = 50, 50  # Adjust the coordinates as needed.
        draw_on_image = ImageDraw.Draw(display_image)
        draw_on_image.text((x, y), current_time, font=font, fill="#FFFFFF")
        # Display the modified image with the time on the screen
        disp.image(display_image, rotation)

    time.sleep(0.2)
