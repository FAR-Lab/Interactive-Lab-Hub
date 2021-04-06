import time
import board
import busio
import adafruit_rgb_display.st7789 as st7789
from PIL import Image, ImageDraw, ImageFont
import random
import sys

import adafruit_mpr121

# The display uses a communication protocol called SPI.
# SPI will not be covered in depth in this course.
# you can read more https://www.circuitbasics.com/basics-of-the-spi-communication-protocol/
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None
BAUDRATE = 64000000  # the rate  the screen talks to the pi
# Create the ST7789 display:
display = st7789.ST7789(
    board.SPI(),
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)


# these setup the code for our buttons and the backlight and tell the pi to treat the GPIO pins as digitalIO vs analogIO
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))

font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 32)
font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)

draw.text((0.5, 10), "<<< START", font=font_small, fill="#FFFFFF")
draw.text((0.5, 105), "<<< QUIT", font=font_small, fill="#FFFFFF")
disp.image(image, rotation)

while True:
    if buttonB.value and not buttonA.value:
        break
    if buttonA.value and not buttonB.value:
        sys.exit()

countdown = 3
while countdown > 0:
    draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
    draw.text((0.5, 0.5), "Ready? Go!", font=font, fill="#FFFFFF")
    draw.text((0.5, 40), str(countdown), font=font, fill="#FFFFFF")
    disp.image(image, rotation)
    countdown -= 1
    time.sleep(1)


i2c = busio.I2C(board.SCL, board.SDA)

mpr121 = adafruit_mpr121.MPR121(i2c)

player1_range = range(0, 4)
player2_range = range(8, 12)

color_match = {
    3: ("#FFFFFF", "WHITE"),
    2: ("#1E90FF", "BLUE"),
    1: ("#228B22", "GREEN"),
    0: ("#DC143C", "RED"),
    8: ("#FFFFFF", "WHITE"),
    9: ("#1E90FF", "BLUE"),
    10: ("#228B22", "GREEN"),
    11: ("#DC143C", "RED")
}

player1_error = player2_error = 0
max_error = 3
while player1_error < max_error and player2_error < max_error:
    draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
    curr_key = random.randint(0, 3)
    draw.rectangle((40, 40, 80, 80), outline=0, fill=color_match[curr_key][0])
    draw.text((90, 40), color_match[curr_key][1], font=font, fill="#FFFFFF")

    draw.text((0.5, 90), "P1 ERROR", font=font_small, fill="#FFFFFF")
    draw.text((0.5, 110), str(player1_error), font=font_small, fill="#FFFFFF")
    draw.text((120, 90), "P2 ERROR", font=font_small, fill="#FFFFFF")
    draw.text((220, 110), str(player2_error), font=font_small, fill="#FFFFFF")

    disp.image(image, rotation)

    curr_time = time.time()

    player1_firstkey = player2_firstkey = None

    while time.time() - curr_time < 0.5:
        for i in range(12):
            if mpr121[i].value:
                if i < 4 and player1_firstkey is None:
                    player1_firstkey = i
                if i > 7 and player2_firstkey is None:
                    player2_firstkey = i

    if player1_firstkey is None or player1_firstkey != curr_key:
        player1_error += 1
    if player2_firstkey is None or player2_firstkey != 11-curr_key:
        player2_error += 1

draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
if player1_error < player2_error:
    draw.text((60, 50), "P1 WINS!", font=font_small, fill="#FFFFFF")
elif player2_error < player1_error:
    draw.text((60, 50), "P2 WINS!", font=font_small, fill="#FFFFFF")
else:
    draw.text((60, 50), "IT'S A TIE!", font=font_small, fill="#FFFFFF")

draw.text((0.5, 10), "<<< RESET", font=font_small, fill="#FFFFFF")
draw.text((0.5, 105), "<<< QUIT", font=font_small, fill="#FFFFFF")
disp.image(image, rotation)

while True:
    if buttonB.value and not buttonA.value:
        break
    if buttonA.value and not buttonB.value:
        sys.exit()
