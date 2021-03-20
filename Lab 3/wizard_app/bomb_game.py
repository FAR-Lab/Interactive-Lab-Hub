from gtts import gTTS
import time
import RPi.GPIO as GPIO
from multiprocessing import Pool
import os
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import busio
import qwiic_twist
import qwiic_button
from adafruit_apds9960.apds9960 import APDS9960
import adafruit_rgb_display.st7789 as st7789

cwd = os.getcwd()

LED_PIN = 26
MOTOR_PIN = 12
IMG_PATH = "/home/pi/Documents/Interactive-Lab-Hub/Lab 3/wizard_app/imgs/"
live_flag = True

def setup():
    # Setup the LED
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_PIN, GPIO.OUT)

    # Setup the servo
    GPIO.setup(MOTOR_PIN, GPIO.OUT)
    Servo = GPIO.PWM(MOTOR_PIN, 50)

    # Setup the display
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
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)

    # Turn on the backlight
    backlight = digitalio.DigitalInOut(board.D22)
    backlight.switch_to_output()
    backlight.value = True

    # Set up the rotary pin
    twist = qwiic_twist.QwiicTwist()
    twist.begin()
    twist_count = 0
    twist.set_blue(255)
    twist.set_red(100)
    twist.set_green(255)

    return Servo, disp, [rotation, top]

def led_tick(LED_PIN):
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(1)

def clock_tick(Servo):
    Servo.start(2.5)
    for i in range(0, 60, 3):
        Servo.ChangeDutyCycle(i / 18 + 2)
        time.sleep(0.5)
        Servo.ChangeDutyCycle(0)
        time.sleep(0.1)
    Servo.stop()

def detonate():
    speak('You have failed. Detonating in 3...2...1...')
    GPIO.cleanup()

def speak(m):
    filename = 'tmp.mp3'

    tts = gTTS(m, lang='en')
    tts.save(filename)
    os.system("/usr/bin/mplayer " + filename)


def image_formatting(image2):
    image2 = image2.convert('RGB')
    # Scale the image to the smaller screen dimension
    image2 = image2.resize((240, 135), Image.BICUBIC)

    return image2
