import time
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
import sys
import random

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
# image = Image.new("RGB", (width, height))
rotation = 90
image = Image.new("RGB", (width, height))
rotation = 90
draw = ImageDraw.Draw(image)

padding = -2
top = padding
bottom = height - padding

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype("font/TahitiSansD.otf", 35)
time_font = ImageFont.truetype("font/LemonDays.ttf", 50)
br_font = ImageFont.truetype("font/LemonDays.ttf", 40)


# these setup the code for our buttons and the backlight and tell the pi to treat the GPIO pins as digitalIO vs analogIO
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

x = 0
y = top
keyinput = "0840" # default time
displaytxt = ""
font_color = "#FFFFFF"  
mode = 0
breakfast_option = {30:['breakfast'], 20:['omelette', 'sandwich'],10:['yogurt','toast', 'toasts', 'cereal', 'coffee'], 5:['bananas', 'milk', 'cheese', 'nuts']} 

def checktime(timestr: str) -> bool:
    hourinput = int(timestr[0:2])
    mininput = int(timestr[2:4])
    if not hourinput < 24 or not mininput < 60:
        return False
    else:
        return True

def breakfastchoice(remain_min):
    choice = []
    time_left = remain_min
    while time_left >= 5 and len(choice) < 3:
        if time_left < 10:
            br_item = random.choice(breakfast_option[5])
            if br_item not in choice:
                choice.append(br_item)
                time_left -= 5
        elif time_left < 20:
            time_spent = random.choice([10,5])
            br_item = random.choice(breakfast_option[time_spent])
            if br_item not in choice:
                choice.append(br_item)
                time_left -= time_spent
        elif time_left < 30:
            time_spent = random.choice([20,10,5])
            br_item = random.choice(breakfast_option[time_spent])
            if br_item not in choice:
                choice.append(br_item)
                time_left -= time_spent
        else:
            time_spent = random.choice([30,20,10,5])
            br_item = random.choice(breakfast_option[time_spent])
            if br_item not in choice:
                choice.append(br_item)
                time_left -= time_spent
    return choice

while True:
    now_time = time.strftime("%H:%M")
    record_hour = int(keyinput[0:2])
    record_min = int(keyinput[2:4])
    now_hour = int(now_time[0:2])
    now_min = int(now_time[3:5])
    remain_min = (((record_hour - now_hour) * 60 + record_min) - now_min)
    if mode == 0: # recommend breakfast option
        if now_hour > record_hour:
            text = "See You Nextday"
            draw.text((x+32, y+50), text, font=font, fill=font_color)
        else:
            btr = "BTR {:2d} min".format(remain_min)
            no_of_items = len(result)
            if no_of_items != 0:
                i = 0
                space = int((240 - (65 * no_of_items)) / (no_of_items + 1))
                while i < no_of_items:
                    icon = Image.open('icon/{filename}.png'.format(filename=result[i]))
                    icon = icon.resize((65, 65), Image.BICUBIC).convert("RGBA")
                    image.paste(icon, (space+((65+space)*i), 55))
                    i += 1
            else:
                draw.text((x+30, 55), 'Just Go!', font=br_font, fill=font_color)
            draw.text((x+65, y+5), btr, font=font, fill=font_color)
    elif mode == 1: # main menu
        draw.rectangle((0, 0, width, height), outline=0, fill=000)
        draw.text((x+30, y+10), "Breakfast Clock", font=font, fill="#D9DCD6")        
        draw.text((x+65, y+50), now_time, font=time_font, fill="#F3BA20")
        draw.rectangle((0, 0, width, height), outline=0, fill=000)
        
            # draw.text((x, y+50), result, font=br_font, fill=font_color)
        # draw.text((x+65, y+50), displaytxt, font=time_font, fill=font_color)
    else: # set when2breakfast
        draw.rectangle((0, 0, width, height), outline=0, fill=000)
        charButton = chr(button)
        keyinput = keyinput[-4:]
        if button != 0:
            if charButton == '#':
                if checktime(keyinput):
                    displaytxt = "{:02d}:{:02d}".format(int(keyinput[0:2]), int(keyinput[2:4]))
                else:
                    keyinput = '0000'
                    displaytxt = 'invalid'
            elif charButton == '*':
                keyinput = keyinput[:-1]
            else: 
                keyinput += charButton
        else:
            displaytxt = "{:02d}:{:02d}".format(int(keyinput[0:2]), int(keyinput[2:4]))
        draw.text((x+60, y+10), "When to Go", font=font, fill=font_color)
        draw.text((x+65, y+50), displaytxt, font=time_font, fill=font_color)
        # Flush the stdout buffer to give immediate user feedback
        sys.stdout.flush()
    if buttonB.value and not buttonA.value:  # just button A pressed -> What to Eat
        if mode == 1: # -> Switch options
            result = breakfastchoice(remain_min)
        else:
            mode = 1
            result = breakfastchoice(remain_min)
    if buttonA.value and not buttonB.value:  # just button B pressed -> Set Time
        mode = 2
    if not buttonA.value and not buttonB.value:  # both pressed -> Home Page
        mode = 0
    # Display image.
    disp.image(image, rotation)
    # time.sleep(.25)
