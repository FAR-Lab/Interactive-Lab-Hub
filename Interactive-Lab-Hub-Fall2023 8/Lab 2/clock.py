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
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 36)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

# Button for interaction
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

# Sand radius
r = 8
# Number of rows and cols in the screen
rows = int(height / 2 / r)
cols = int(width / 2 / r)
# Position logs for the circle that is falling down
i = 0
j = 0
# Tracker for current row and col that is being filled
row = 0
col = 0


while True:
    # Draw the background
    draw.rectangle((0, 0, width, height), outline=0, fill="#0097ff")

    # Pressing any of the buttons resets the animation
    if not buttonA.value or not buttonB.value:
        i = 0
        j = 0
        row = 0
        col = 0
        draw.rectangle((0, 0, width, height), outline=0, fill="#0097ff")
    elif col != cols and row != rows:
        y = top
        p1 = (x + j) * 2 * r, (y + i + 1) * 2 * r + height % (2 * r)
        p2 = (x + j + 1) * 2 * r, (y + i + 2) * 2 * r + height % (2 * r)
        draw.ellipse([p1, p2], fill="#FFFFFF")
        if i != rows - row: # Circle is falling
            i = i + 1
        elif j != cols - 1: # Current row not filling up
            i = 0
            j = j + 1
            col = col + 1
        else:   # Current row is full
            col = 0
            row = row + 1
            i = 0
            j = 0
        
        # Draw circles that already fall down
        for m in range(rows):
            for n in range(cols):
                if m < row or (m == row and n < col):
                    p1 = (x + n) * 2 * r, (y + rows - m + 1) * 2 * r + height % (2 * r)
                    p2 = (x + n + 1) * 2 * r, (y + rows - m + 2) * 2 * r + height % (2 * r)
                    draw.ellipse([p1, p2], fill="#FFFFFF")
    else:
        draw.text((30, height / 2 - 0.5 * font.size), "Time's up!", font=font, fill="#1C4279")

    # Display image.
    disp.image(image, rotation)
    # time.sleep(0.01)
