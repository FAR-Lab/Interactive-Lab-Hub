import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
from time import strftime, sleep
import numpy as np
import board

import paho.mqtt.client as mqtt
import uuid

from adafruit_rgb_display.rgb import color565
import adafruit_rgb_display.st7789 as st7789
import webcolors


import os
# import pygame
# from camera import webCam
from mail import sendEmail


# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default Min is 24mhz):
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

backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape! 135
width = disp.height #240
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
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 44)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

def getFont(size):
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", size)
    return font



reset = True







#this is the callback that gets called once we connect to the broker. 
#we should add our subscribe functions here as well
def on_connect(client, userdata, flags, rc):
    print(f"connected with result code {rc}")
    client.subscribe(topic)
    # you can subsribe to as many topics as you'd like
    # client.subscribe('some/other/topic')


# this is the callback that gets called each time a message is recived
def on_message(cleint, userdata, msg):
    print(f"topic: {msg.topic} msg: {msg.payload.decode('UTF-8')}")
    alertCam.fall = ((msg.payload.decode('UTF-8'))=='True')
    
    # you can filter by topics
    # if msg.topic == 'IDD/some/other/topic': do thing



# attach out callbacks to the client
client = mqtt.Client(str(uuid.uuid1()))
client.tls_set()
client.username_pw_set('idd', 'device@theFarm')
client.on_connect = on_connect
client.on_message = on_message

client.connect(
    'farlab.infosci.cornell.edu',
    port=8883)

client.loop_start()
# pygame.mixer.init()
# pygame.mixer.music.load("./Graduate.wav")

def draw_text(fontsize,strDraw,bgcolor):
        draw.rectangle((0, 0, width, height), outline=0, fill=bgcolor)
        font = getFont(fontsize)
        x = width/2 - font.getsize(strDraw)[0]/2
        y = height/2 - font.getsize(strDraw)[1]/2
        draw.text((x, y), strDraw, font=font, fill="#FFFFFF")
        disp.image(image, rotation)

class App:
    def __init__(self):
        self.fall = False

# the # wildcard means we subscribe to all subtopics of IDD
topic = 'IDD/Fall/#'

alertCam = App()
# p = SoundPlayer("./Graduate.wav", 1) 

while True:

    if not alertCam.fall:
        draw.rectangle((0, 0, width, height), outline=0, fill='green')
        font = getFont(25)
        str1 = 'Status: Normal'
        x_1 = width/2 - font.getsize(str1)[0]/2
        y_1 = height/2 - font.getsize(str1)[1]
        draw.text((x_1, y_1), str1, font=font, fill="#FFFFFF")

        str2 = 'Stay Safe :)'
        x_2 = width/2 - font.getsize(str2)[0]/2
        y_1 += font.getsize(str2)[1]
        draw.text((x_2, y_1), str2, font=font, fill="#FFFFFF")
    else: 
        print('Fall detected')
        draw_text(25, 'Fall Detected', 'red')
        # pygame.mixer.music.play(1)
        # p.play(1)
        os.system('omxplayer Graduate.wav') 

        print('recording')
        draw_text(20,'Recording Video','green')

        # 
        os.system('rm recording.mp4')
        # os.system('ffmpeg -r 24 -f v4l2  -s 1280x720 -t 15 -i /dev/video0 recording.mp4')
        os.system('ffmpeg -r 25 -f v4l2  -s 640x480 -t 10 -i /dev/video0 -vf "hflip,vflip" recording.mp4')
        draw_text(20,'Video recorded','green')

        sendEmail()
        
        draw_text(20,'Video sent','green')
    
        break

    

    disp.image(image, rotation)
    time.sleep(0.01)
                
