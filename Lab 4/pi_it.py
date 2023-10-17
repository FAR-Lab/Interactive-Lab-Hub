from __future__ import print_function

import time
import board
import busio
import qwiic_joystick
import sys

import adafruit_mpr121
from adafruit_apds9960.apds9960 import APDS9960
import os
import random
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import digitalio

import os
os.chdir('/home/ben/Interactive-Lab-Hub/Lab 4')


def init():
    global i2c
    global mpr121
    global apds
    global default_joystick_vals
    global oled
    global draw
    global font
    global font2
    global image
    
    default_joystick_vals = [508, 509, 511]
    
    i2c = busio.I2C(board.SCL, board.SDA)

    mpr121 = adafruit_mpr121.MPR121(i2c) #capacity

    apds = APDS9960(board.I2C()) #gesture
    apds.enable_proximity = True 
    apds.enable_gesture = True
    RESET_PIN = digitalio.DigitalInOut(board.D4)
    oled = adafruit_ssd1306.SSD1306_I2C(128, 64, board.I2C(), reset=RESET_PIN)
    # Clear display.
    oled.fill(0)
    oled.show()

    # Create blank image for drawing.
    image = Image.new("1", (oled.width, oled.height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 28)
    font2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
    oled.image(image)
    oled.show()
    
def pi_it():
    init()
    start = True
    if start:
        os.system('amixer sset Master 100% 100%')
        os.system('echo "Welcome to Pi-It" | festival --tts')
        time.sleep(0.2)
        os.system('echo "Prepare to play in" | festival --tts')
        for i in range(5):
            os.system(f'echo "{5-i}" | festival --tts')
            time.sleep(0.1)
    play()

def play():
    speed = 3
    lost = False
    i = 0
    os.system('mplayer -noconsolecontrols -volume 60 ./sounds/mega.mp3 &')
    while not lost:
        image = Image.new("1", (oled.width, oled.height))
        draw = ImageDraw.Draw(image)
        oled.image(image)
        action = random.randint(0, 2)
        #action = 0
        if action == 0:
            os.system('echo "Push it!" | festival --tts')
            draw.text((0, 0), "Push it!", font=font, fill=255)
        elif action == 1:
            os.system('echo "Cover it!" | festival --tts')
            draw.text((0, 0), "Cover it!", font=font, fill=255)
        else:
            os.system('echo "Move it!" | festival --tts')
            draw.text((0, 0), "Move it!", font=font, fill=255)
        draw.text((0, 35), f'Score: {i}', font=font2, fill=255)
        
        oled.image(image)
        oled.show()
        
        lost = detect(action, speed)
        i += 1
        if i%5 == 0:
            os.system(f'cvlc --play-and-exit ./sounds/cool.mp3')
            speed /= 1.33

    razz = random.randint(0, 5)
    os.system(f'cvlc --play-and-exit ./sounds/razz{razz}.mp3')
    os.system('echo "Game over!" | festival --tts')
    os.system(f'echo "Your score is {i-1}" | festival --tts')


def detect(action, speed):
    print('in detect')
    cap = False
    prox = False
    joystick = False
    lost = False

    start = time.time()
    
    if action == 0:
        try:
            while True:
                for i in range(12):
                    if mpr121[i].value:
                        cap = True
                if cap:
                    break
                now = time.time()
                if now - start > speed:
                    break
        except OSError:
            print('oh no')
            cap = True
            
    elif action == 1:
        while True:
            if apds.proximity >= 4:
                prox = True
                break
            now = time.time()
            if now - start > speed:
                break
    else:
        while True:
            myJoystick = qwiic_joystick.QwiicJoystick()
            myJoystick.begin()
            for x in [myJoystick.horizontal, myJoystick.vertical]:
                if not(x in default_joystick_vals):
                    joystick = True
            if joystick:
                break
            now = time.time()
            if now - start > speed:
                break
            
    if action == 0:
        if (cap == False) or (prox == True) or (joystick==True):
            lost = True
        else:
            os.system(f'cvlc --play-and-exit ./sounds/1.mp3')

    elif action == 1:
        if (cap == True) or (prox == False) or (joystick==True):
            lost = True
        else:
            os.system(f'cvlc --play-and-exit ./sounds/2.mp3')
    elif action == 2:
        if (cap == True) or (prox == True) or (joystick==False):
            lost = True
        else:
            os.system(f'cvlc --play-and-exit ./sounds/3.mp3')
    return lost



def mycap():
    
    while True:
        for i in range(12):
            if mpr121[i].value:
                print(f"Twizzler {i} touched!")
        time.sleep(0.25)  # Small delay to keep from spamming output messages.

# Uncomment and set the rotation if depending on how your sensor is mounted.
# apds.rotation = 270 # 270 for CLUE

#gesture
def mygesture():
    while True:
        gesture = apds.gesture()
        if gesture == 0x01:
            print("up")
        elif gesture == 0x02:
            print("down")
        elif gesture == 0x03:
            print("left")
        elif gesture == 0x04:
            print("right")
        
def myjoystick():
	print("\nSparkFun qwiic Joystick   Example 1\n")
	myJoystick = qwiic_joystick.QwiicJoystick()

	if myJoystick.connected == False:
		print("The Qwiic Joystick device isn't connected to the system. Please check your connection", \
			file=sys.stderr)
		return

	myJoystick.begin()

	print("Initialized. Firmware Version: %s" % myJoystick.version)

	while True:

		print("X: %d, Y: %d, Button: %d" % ( \
					myJoystick.horizontal, \
					myJoystick.vertical, \
					myJoystick.button))

		time.sleep(.5)