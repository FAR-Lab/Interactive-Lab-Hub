import time
import subprocess
import digitalio
import board
import random
from PIL import Image, ImageDraw, ImageFont
from adafruit_lsm6ds.lsm6ds3 import LSM6DS3
import adafruit_rgb_display.st7789 as st7789
import numpy as np


# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
sensor = LSM6DS3(i2c)

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
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 15)
fontLarge = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)

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
i = rows - 1
j = 0
# Tracker for current row and col that is being filled
row = 0
col = 0
# Whether a snow particle has fallen to ground
fallen = False
# Highest row a snow particle is in; if is at the top game is over
highestRow = 0
# The state of the game - logs time once game is over
gameOver = False
y = top

# 2d array that stores if there is a snow particle in specific index
snow = np.zeros((rows, cols))

# Draw a snow particle based on position index m and n
def drawSnow(m, n):
    p1 = (x + n) * 2 * r, (y + rows - m + 1) * 2 * r + height % (2 * r)
    p2 = (x + n + 1) * 2 * r, (y + rows - m + 2) * 2 * r + height % (2 * r)
    draw.ellipse([p1, p2], fill="#FFFFFF")

# Draw all snow particles according to values stored in snow (a 2d array)
def drawAllSnow():
    for m in range(rows):
            for n in range(cols):
                if snow[m][n]:
                    drawSnow(m, n)

# Updates column based on player's input of accelerometer
def updateJ(i, j):
    if sensor.acceleration[0] < -3:     # accelerometer turns left
        if not snow[i][max(j - 1, 0)]:
            j = max(j - 1, 0)
    elif sensor.acceleration[0] > 3:    # accelerometer turns right
        if not snow[i][min(j + 1, cols - 1)]:
            j = min(j + 1, cols - 1)
    return j

startTime = time.time() # Logs start time of the game

while True:
    # Draw the background
    draw.rectangle((0, 0, width, height), outline=0, fill="#0097ff")

    # Pressing any of the buttons resets the animation
    if not buttonA.value or not buttonB.value:
        i = rows - 1
        j = 0
        snow = np.zeros((rows, cols))
        draw.rectangle((0, 0, width, height), outline=0, fill="#0097ff")
        fallen = False
        highestRow = 0
        startTime = time.time()
        gameOver = False
    elif highestRow != rows - 1:
        if fallen:
            i = rows - 1    # Initialize a new snow at the top
            fallen = False
            j = random.randint(0, cols - 1)
            snow[i][j] = True
        elif i != 0 and not snow[i - 1][j]:    # Current snow can fall down
            snow[i][j] = False
            j = updateJ(i - 1, j)
            snow[i - 1][j] = True
            i = i - 1
        else:
            fallen = True
            highestRow = max(highestRow, i)
        
        drawAllSnow()
    else:
        if not gameOver:
            timePassed = time.time() - startTime
            gameOver = True
        draw.text((7, height / 2 - 2 * font.size), "Game Over", font=fontLarge, fill="#FFFFFF")
        draw.text((7, height / 2), "You've survived %.1f seconds!" % timePassed, font=font, fill="#1C4279")
        draw.text((7, height / 2 + font.size), "Press any button to restart", font=font, fill="#1C4279")
    

    # y = top
    # draw.text((x, y), "Acceleration (m/s^2): ", font=font, fill="#FFFFFF")
    # y += 20
    # draw.text((x, y), "X:%.2f, Y: %.2f, Z: %.2f" % (sensor.acceleration), font=font, fill="#FFFFFF")
    # y += 20
    # draw.text((x, y), "Gyro (radians/s): ", font=font, fill="#FFFFFF")
    # y += 20
    # draw.text((x, y), "X:%.2f, Y: %.2f, Z: %.2f" % (sensor.gyro), font=font, fill="#FFFFFF")
    # Display image.
    disp.image(image, rotation)
    time.sleep(0.1)

    

