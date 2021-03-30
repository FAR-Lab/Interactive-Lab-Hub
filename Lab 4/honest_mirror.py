from gtts import gTTS
import RPi.GPIO as GPIO
import os
from random import randrange
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import busio
import time
from adafruit_apds9960.apds9960 import APDS9960
import adafruit_rgb_display.st7789 as st7789
from threading import Thread

cwd = os.getcwd()
i2c = busio.I2C(board.SCL, board.SDA)

MOTOR_PIN = 13
IMG_PATH = "/home/pi/Documents/Interactive-Lab-Hub/Lab 4/imgs/"

def image_formatting(image2):
    image2 = image2.convert('RGB')
    # Scale the image to the smaller screen dimension
    image2 = image2.resize((240, 135), Image.BICUBIC)

    return image2

def setup():
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
    rotation = 270

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
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 40)

    # Turn on the backlight
    backlight = digitalio.DigitalInOut(board.D22)
    backlight.switch_to_output()
    backlight.value = True

    # Configure the light sensor
    apds = APDS9960(i2c)
    apds.enable_proximity = True
    apds.enable_proximity_interrupt = True

    return Servo, disp, [rotation, top], apds, font

Servo, disp, disp_opts, apds, font = setup()

def face_move(num_moves):
    Servo.start(2.5)
    for i in range(num_moves):
        Servo.ChangeDutyCycle(80 / 18 + 2)
        time.sleep(0.5)
        Servo.ChangeDutyCycle(60 / 18 + 2)
        time.sleep(0.5)

    Servo.stop()

def show_image(filename, temp):
    image = Image.open(IMG_PATH + filename)
    image = image_formatting(image)

    draw = ImageDraw.Draw(image)
    draw.text((40, 10), str(temp) + " degF", font=font, fill="#000000")

    disp.image(image, disp_opts[0])

def speak(m):
    filename = 'tmp.mp3'

    tts = gTTS(m, lang='en')
    tts.save(filename)
    os.system("/usr/bin/mplayer " + filename)


temp = 76.0
weather = 50
while True:
    rand_change = randrange(10)
    temp += (.05 - rand_change / 100)
    weather += (.5 - rand_change / 10)
    weather_class = ""
    if weather > 30 and weather < 70:
        weather_class = 'sunny'
        show_image('sunny.png', round(temp, 1))
    elif weather > 10 and weather <= 30:
        weather_class = 'rainy'
        show_image('rainy.png', round(temp, 1))
    elif weather <= 10 and weather > 0:
        weather_class = 'stormy'
        show_image('stormy.png', round(temp, 1))
    elif weather >= 70 and weather < 100:
        weather_class = 'cloudy'
        show_image('cloudy.png', round(temp, 1))
    else:
        weather = 50
        weather_class = 'sunny'
        show_image('sunny.png', temp)
    if apds.proximity > 100:
        Thread(target=face_move, args=(10,)).start()
        speak("Heading out? Don't forget your mask. The pandemic hasn't ended yet!")
        speak(f"It is {weather_class} out and {round(temp, 1)} degrees farenheit.")
        rand_val = randrange(10)
        if rand_val == 0:
            speak("Looking good. Go get them, tiger.")
        elif rand_val < 5:
            speak("Are you really going to wear your hair like that?")
        else:
            speak("What happened to your face?")

    print(apds.proximity)
    time.sleep(0.1)
