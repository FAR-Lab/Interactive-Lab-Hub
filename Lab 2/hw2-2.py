from datetime import datetime
import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789

from board import SCL, SDA
import busio
import adafruit_ssd1306

from enum import Enum
import adafruit_apds9960.apds9960


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

#---------------------------------------------------------------
i2c = busio.I2C(SCL, SDA)
disp_small = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
# Clear display.
disp_small.fill(0)
disp_small.show()

width_small = disp_small.width
height_small = disp_small.height
image_small = Image.new("1", (width_small, height_small))

draw_small = ImageDraw.Draw(image_small)
#---------------------------------------------------------------


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

#---------------------------------------------------------------
bottom_small = height_small - padding
#---------------------------------------------------------------



# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font1 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
font2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True
buttonA = digitalio.DigitalInOut(board.D23)
buttonA.switch_to_input()

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)
sensor.enable_color = True


mar = 5
wid = 40
hei = 10

mood = [0] * 12
meet = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]

color2 = ["#FFFFFF", "#DBAF15", "#2784B5"]
friend = ["😈", "😂", "😇", "  "]

class color(Enum):
    RED=0
    GREEN=1
    BLUE=2

color = [color.RED, color.GREEN,  color.BLUE]

b23 = digitalio.DigitalInOut(board.D23)
b24 = digitalio.DigitalInOut(board.D24)
b23.switch_to_input()
b24.switch_to_input()

hour_flash = 3 # 0, 2: empty, 3: hour, 1: min

def detectUser(myColor):
    #Try to detect for 5 seconds
    draw.rectangle((0, 0, width, height), outline=0, fill=myColor)
    disp.image(image, rotation)
    for i in range(5):
        color_data = sensor.color_data
        max_value = max(color_data[:3])
        # print(str(color_data)+" "+str(max_value))
        if (max_value > 4500):
            # print(color[color_data.index(max_value)])
            return color[color_data.index(max_value)]
        elif (color_data.index(max_value) == 0) and max_value > 2900:
            # print(color[color_data.index(max_value)])
            return color[color_data.index(max_value)]
        time.sleep(1)
    return False

while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    now = datetime.now()
    hour = str(int(now.strftime("%H")) % 12).zfill(2)
    min = now.strftime("%M").zfill(2)

    line1 = ["09", "10", "11", "12", "01", "02"]
    line3 = ["03", "04", "05", "06", "07", "08"]

    for i in range(6):
        if line1[i] == hour:
            if hour_flash == 1:
                line1[i] = min
            elif hour_flash in [0,2]:
                line1[i] = "  "
        if line3[i] == hour:
            if hour_flash == 1:
                line3[i] = min
            elif hour_flash in [0,2]:
                line3[i] = "  "
    y = top
    for i in range(6):
        draw.text((mar + x + i*wid, y), line1[i], font=font1, fill=color2[mood[i]])
    y += font1.getsize(line1[0])[1]

    y += hei

    for i in range(6):
        draw.text((x + i*wid , y), friend[meet[i]], font=font2, fill="#00FFFF")
    y += font2.getsize(friend[meet[0]])[1]

    y += hei

    for i in range(6):
        draw.text((mar + x + i*wid, y), line3[i], font=font1, fill=color2[mood[6+i]])
    y += font1.getsize(line3[0])[1]

    y += hei

    for i in range(6):
        draw.text((x + i*wid , y), friend[meet[6+i]], font=font2, fill="#00FFFF")
    y += font2.getsize(friend[meet[0]])[1]

    # Display image.
    disp.image(image, rotation)
    time.sleep(0.5)

    hour_flash = (hour_flash + 1) %4

    h = (int(hour)+3)%12

    if not b23.value:
        print("b23 pressed")
        user = detectUser((0,0,255))

        if user:
            meet[h] = int(color.index(user))
            print(user)
            draw_small.rectangle((0, 0, width_small, height_small), outline=0, fill=0)
            draw_small.text((0, top), friend[meet[h]] + " is nearby... Run!", font=font1, fill=255)
            disp_small.image(image_small)
            disp_small.show()
        else:
            print("no friends detected")

    if not b24.value:
        print("b24 pressed")
        mood[h] = (mood[h]+1)%3
