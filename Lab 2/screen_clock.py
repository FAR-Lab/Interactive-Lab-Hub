import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont, ImageSequence
import adafruit_rgb_display.st7789 as st7789
from time import strftime, sleep
from datetime import datetime

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
fontA = ImageFont.truetype("fonts/DejaVuSans.ttf", 30)
fontB = ImageFont.truetype("fonts/SuperMario256.ttf", 30)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

# Images
day_image = Image.open("images/day_background.jpg")
day_image = day_image.resize((width,height))
night_image = Image.open("images/night_background.jpg")
night_image = night_image.resize((width, height))
bg_arr = [day_image, night_image]

# Gifs
dog_gif = Image.open("gifs/new_dog.gif")
dog_gif_iter = ImageSequence.Iterator(dog_gif)
bone_img = Image.open("images/dog_bone.png").convert("RGBA").resize((40, 30))
yum_img = Image.open("images/yum.png").convert("RGBA").resize((80, 50))

# Inital frames
dog_frame = dog_gif_iter
# bone_frame = bones_gif_iter

# Status
bone_triggered = False
bone_x = 180
time_stamp = None
bg_index = 0

pre_sec = cur_sec = 0

while True:
    #TODO: Lab 2 part D work should be filled in here. You should be able to look in cli_clock.py and stats.py 
    cur_time = strftime("%H:%M:%S") 
    cur_sec = int(cur_time.split(':')[-1].split('.')[0])
    
    if not buttonA.value:
        bg_index += 1
        bg_index %= len(bg_arr)
    if not buttonB.value:
        bone_triggered = True
    if bone_x <= 40:
        bone_triggered = False
        bone_x = 180
        time_stamp = strftime("%H:%M:%S")
    if bone_triggered:
        bone_x -= 3
     
     
    display_image = bg_arr[bg_index].copy()
    
    # Dog frame:
    try:
        dog_frame = next(dog_gif_iter)
        dog_frame = dog_frame.convert("RGBA").resize((120, 80))
    except StopIteration:
        dog_gif_iter = ImageSequence.Iterator(dog_gif)
        dog_frame = next(dog_gif_iter)
        dog_frame = dog_frame.convert("RGBA").resize((120, 80)) 
    
    display_image.paste(bone_img, (bone_x, 92), bone_img)
    display_image.paste(dog_frame, (0, 60), dog_frame)
    
    draw_on_image = ImageDraw.Draw(display_image)
    
    if time_stamp:
        display_image.paste(yum_img, (85, 50), yum_img)
        draw_on_image.text((55, 10), cur_time, font=fontB, fill="#f41f1f")
        t1 = datetime.strptime(cur_time, "%H:%M:%S")
        t2 = datetime.strptime(time_stamp, "%H:%M:%S")
        if (t1 - t2).total_seconds() >= 4:
            time_stamp = None
    
    # Display image.
    disp.image(display_image, rotation)
    pre_sec = cur_sec
    
    time.sleep(0.05)