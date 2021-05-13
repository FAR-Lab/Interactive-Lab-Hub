import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
from adafruit_rgb_display.rgb import color565
import adafruit_rgb_display.st7789 as st7789
import sys
import random
import os
import time

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
failed_1 = 'audio/failed_1.mp3'
failed_2 = 'audio/failed_2.mp3'
failed_3 = 'audio/failed_3.mp3'

x = 0

class PassWordMod:
    def __init__(self, twist, keypad):
        self.entered_pwd = ""
        self.entered_count = 0
        self.emergency_mode = False
        self.count_down = False
        self.count_down_times = 10
        self.failed_times = 0
        self.twist = twist
        self.keypad = keypad
        self.keypad.begin()


    def get_input(self):
        self.entered_count = self.twist.get_count()
        self.keypad.update_fifo()
        x = self.keypad.get_button()
        if x != 0:
            self.entered_pwd += chr(x)
        time.sleep(.25)


    def check_password(self):
        if len(self.entered_pwd) != len(pwd):
            return False

        if self.entered_pwd == pwd and int(self.twist.get_count()) == count_pwd:
            return True
        elif self.entered_pwd == emergency_pwd and int(self.twist.get_count()) == emergency_count_pwd:
            self.emergency_mode = True
            return True
        else:
            self.failed_times += 1
            self.entered_pwd = ""
            if self.failed_times == 1:
                playsound(failed_1)
            elif self.failed_times == 2:
                playsound(failed_2)
            elif self.failed_times >= 3:
                playsound(failed_3)
                self.count_down = True  
            return False

