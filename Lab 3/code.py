
from time import strftime, sleep
import time
import subprocess
import digitalio
import board
import PIL
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
import qwiic_button
import random 
import RPi.GPIO as GPIO
import time
import threading



#subprocess.call("~/Interactive-Lab-Hub/Lab\ 3/im.py", shell=True)
 # joystick = qwiic_joystick.QwiicJoystick()
import digitalio
import board
from PIL import Image, ImageDraw
import adafruit_rgb_display.ili9341 as ili9341
import adafruit_rgb_display.st7789 as st7789  # pylint: disable=unused-import
import adafruit_rgb_display.hx8357 as hx8357  # pylint: disable=unused-import
import adafruit_rgb_display.st7735 as st7735  # pylint: disable=unused-import
import adafruit_rgb_display.ssd1351 as ssd1351  # pylint: disable=unused-import
import adafruit_rgb_display.ssd1331 as ssd1331  # pylint: disable=unused-import

#cs_pin = digitalio.DigitalInOut(board.CE0)
#dc_pin = digitalio.DigitalInOut(board.D25)
#reset_pin = digitalio.DigitalInOut(board.D24)

# Setup SPI bus using hardware SPI:
#spi = board.SPI()

#disp = st7789.ST7789(
#    spi,
#    cs=cs_pin,
#    dc=dc_pin,
#    rst=reset_pin,
#    baudrate=BAUDRATE,
#    width=135,
#    height=240,
#    x_offset=53,
#    y_offset=40)
  
  #button = qwiic_button.QwiicButton()
#button.has_been_clicked
#if button.begin() == False:
        #print("\nThe Qwiic Button isn't connected to the system. Please check your connection")
# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
#cs_pin = digitalio.DigitalInOut(board.CE0)
#dc_pin = digitalio.DigitalInOut(board.D25)
#reset_pin = None

BtnPin = 40
to = 0.8
short_click = 0.65
long_click = 1.0 # length of a long click
very_long_click = 4.0 # length of a veeeery long click

# set up the GPIO pins to register the presses
#GPIO.setmode(GPIO.BOARD)
GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set BtnPin's mode is input

# returns the kind ok click
def pressed():
    start_time = time.time()
    while not GPIO.input(BtnPin):
        time.sleep(.1)
    pressed_time = time.time() - start_time
    if pressed_time < short_click:
        return 'short'
    elif pressed_time > very_long_click:
        return 'very long'
    else:
        return 'long'

# returns the kind of click event
def pressing():
    global clicks
    tmpclicks = []
    start_time = time.time()
    while time.time() - start_time < to:
        if not GPIO.input(BtnPin):
            tmpclicks.append(pressed())
            start_time = time.time()
    clicks = tmpclicks

clicks = [] # set up an empty list for the kind of clicks

lasting = 0

while True:
    #print (lasting) # just to show you can do other while getting the clicks
    lasting +=1
    # we create a thread for getting click events so we can other while waiting for the clicks
    try:
        t
    except NameError:
        if not GPIO.input(BtnPin):
            t= threading.Thread(target=pressing)
            t.start()
    else:
        if clicks:
            if clicks == ['short']:
                print ("Single click")
            elif clicks == ['short', 'short']:
                print ("Double click")
            elif clicks == ['short','short', 'short']:
                print ("Triple click")
            elif clicks == ['long']:
                print ("Long click")
            elif clicks == ['long', 'long']:
                print ("Double long click")
            elif clicks == ['very long']:
                print ("Very long click")
            clicks = []
            del t
