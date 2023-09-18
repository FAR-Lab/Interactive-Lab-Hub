import time
from time import strftime, sleep
from datetime import datetime
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
from random import randint

import requests
import json
import time
import board
import busio
import adafruit_mpr121
i2c = busio.I2C(board.SCL, board.SDA)
mpr121 = adafruit_mpr121.MPR121(i2c)


def trigger_IFTTT(hug_counts):
    # Your IFTTT URL with event name, key and json parameters (values)
    #r = requests.post('https://maker.ifttt.com/trigger/llama_hug/with/key/c3f5EtBBtgkPJLH3POgEkk', params={"value1":"none","value2":"none","value3":"none"})
    # Replace 'YOUR_WEBHOOK_URL' with your IFTTT webhook URL
    WEBHOOK_URL = 'https://maker.ifttt.com/trigger/llama_hug/json/with/key/c3f5EtBBtgkPJLH3POgEkk'

    # Define the event name and data you want to send
    data = {'hug_counter': hug_counts}
    print(data)

    # Send the HTTP POST request
    response = requests.post(WEBHOOK_URL, json=data)

    # Check the response
    if response.status_code == 200:
        print('HTTP POST request successful!')
    else:
        print('HTTP POST request failed. Status code:', response.status_code)


def hugging_animation(hug_counts):
    for _ in range(8):
        # Draw a black filled box to clear the image.
        # draw.rectangle((0, 0, width, height), outline=0, fill=0)
        llama_image = Image.open(f'llama.png')
        image.paste(llama_image, (0, 0))
        
        # Draw several diamonds with random colors and positions
        for _ in range(10):
            # Generate random coordinates for the diamond
            x = randint(0, width - 20)
            y = randint(0, height - 20)
            
            # Generate a random color
            color = (randint(0, 255), randint(0, 255), randint(0, 255))
            
            # Draw a diamond shape
            draw.polygon([
                (x+10, y),
                (x, y+10),
                (x+10, y+20),
                (x+20, y+10)
            ], fill=color, outline="white")
            
            # Text
            #draw.text((5, 40), "Lots of Love!", font=Sans_bold, fill=(255, 255, 255))
            #draw.text((5, 75), f'Hugs Received: {hug_counts}', font=Sans, fill=(255, 255, 255))

        # Display image
        disp.image(image, rotation)
        sleep(0.1)

def standby_animation(elapsed_time, hug_counts):
    # Draw a black filled box to clear the image.
    # draw.rectangle((0, 0, width, height), outline=0, fill='#FED408')
    llama_image = Image.open(f'llama_text.png')
    image.paste(llama_image, (0, 0))
    
    # calculate
    hours = int(elapsed_time // 3600)
    mins = int(elapsed_time % 3600 // 60)
    # put text
    draw.text((145, 20), str(hug_counts), font=Sans_bold_40, fill=0)
    draw.text((75, 55), str(hours).zfill(2), font=Sans_bold, fill=0)
    draw.text((155, 55), str(mins).zfill(2), font=Sans_bold, fill=0)
    
    disp.image(image, rotation)



# Button configuration
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

# Configuration for CS and DC pins (these are PiTFT defaults):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = digitalio.DigitalInOut(board.D24)

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 24000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

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

# Prepare Fonts
Sans = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
Sans_bold = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansCondensed-Bold.ttf", 35)
Sans_bold_40 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansCondensed-Bold.ttf", 35)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True


#last_hug_time = datetime.now()
zero_date_str = '2023-09-17 9:00:00'
# Convert the zero date string to a datetime object
last_hug_time = datetime.strptime(zero_date_str, '%Y-%m-%d %H:%M:%S')
hug_counts = 3
while(1):
    # Get the current date and time
    current_date = datetime.now()
    if (not buttonA.value) or mpr121[6].value:
        hug_counts += 1
        print(hug_counts)
        last_hug_time = datetime.now()
        trigger_IFTTT(hug_counts)
        hugging_animation(hug_counts)
        while not buttonA.value:
            pass
    time_since_last_hug = current_date - last_hug_time
    standby_animation(time_since_last_hug.total_seconds(), hug_counts)
    
    sleep(0.2)