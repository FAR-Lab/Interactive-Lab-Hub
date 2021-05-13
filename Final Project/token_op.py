import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
from adafruit_rgb_display.rgb import color565
import adafruit_rgb_display.st7789 as st7789
import sys
import random
import os
import time
import json

from playsound import playsound
from picamera import PiCamera
import qwiic_twist
import qwiic_button
import qwiic_keypad

import speech_recognition as sr
import pyaudio

# The display uses a communication protocol called SPI.
# SPI will not be covered in depth in this course. 
# you can read more https://www.circuitbasics.com/basics-of-the-spi-communication-protocol/
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None
BAUDRATE = 64000000  # the rate  the screen talks to the pi
# Create the ST7789 display:
disp = st7789.ST7789(
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

# Params
# Screen
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = False
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

# Display
height = disp.width
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
font_big = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 32)


draw = ImageDraw.Draw(image)

pwd = "3428"
count_pwd = 15

emergency_pwd = "9716"
emergency_count_pwd = 28

emergency_color = (50, 205, 50)

# Sounds
token_num = 'audio/token_num.mp3'
get_token = 'audio/get_token.mp3'
deleted = 'audio/deleted.mp3'

x = 0

class Tokens:
    def __init__(self, keypad, emergency_mode=False):        
        self.tokens = []
        with open('tokens.json') as json_file:
            data = json.load(json_file)
        for t in data['C']:
            self.tokens.append(t)
        if not emergency_mode:
            for t in data['E']:
                self.tokens.append(t)
        self.keypad = keypad
        self.token_number = ""
        self.keypad.begin()

    def get_token(self):
        self.keypad.update_fifo()
        x = self.keypad.get_button()
        if x != 0:
            if chr(x) == "#":
                return True
            elif chr(x) != "*":
                self.token_number += chr(x)
            return False
        #self.tokens[int(self.token_number)-1]

    def delete_token(self):
        self.tokens.pop(int(self.token_number)-1)
        self.token_number = ""
        playsound(deleted)

        
