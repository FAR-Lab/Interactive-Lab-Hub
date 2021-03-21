from gtts import gTTS
import time
import RPi.GPIO as GPIO
import os
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import busio
import qwiic_twist
import qwiic_joystick
from adafruit_apds9960.apds9960 import APDS9960
import adafruit_rgb_display.st7789 as st7789
from threading import Thread

cwd = os.getcwd()
i2c = busio.I2C(board.SCL, board.SDA)

LED_PIN = 26
MOTOR_PIN = 12
IMG_PATH = "/home/pi/Documents/Interactive-Lab-Hub/Lab 3/wizard_app/imgs/"
live_flag = True

def image_formatting(image2):
    image2 = image2.convert('RGB')
    # Scale the image to the smaller screen dimension
    image2 = image2.resize((240, 135), Image.BICUBIC)

    return image2

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
    twist.set_count(20)
    twist.set_blue(255)
    twist.set_red(100)
    twist.set_green(255)

    # bomb Game Introduction
    image = Image.open(IMG_PATH + 'bomb_homescreen.png')
    image = image_formatting(image)
    disp.image(image, rotation)

    # Set up the joystick
    joystick = qwiic_joystick.QwiicJoystick()
    joystick.begin()

    # Configure the light sensor
    apds = APDS9960(i2c)
    apds.enable_proximity = True
    apds.enable_color = True

    return Servo, disp, [rotation, top], twist, joystick, apds

Servo, disp, disp_opts, twist, joystick, apds = setup()

def twist_tick(num_blinks):
    for i in range(num_blinks):
        twist.set_red(255)
        time.sleep(1)
        twist.set_red(100)
        time.sleep(1)

def led_tick(num_blinks):
    for i in range(num_blinks):
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(1)

def clock_tick():
    Servo.start(2.5)
    while True:
        for i in range(0, 60, 3):
            Servo.ChangeDutyCycle(i / 18 + 2)
            time.sleep(0.5)
            Servo.ChangeDutyCycle(0)
            time.sleep(0.1)
    Servo.stop()

def show_image(filename):
    image = Image.open(IMG_PATH + filename)
    image = image_formatting(image)
    disp.image(image, disp_opts[0])

def detonate():
    Thread(target=led_tick, args=(7,)).start()
    Thread(target=twist_tick, args=(7,)).start()
    time.sleep(0.5)
    speak('You have failed. Detonating in 3')
    time.sleep(1)
    speak('2')
    time.sleep(1)
    speak('1')
    time.sleep(1)
    speak('Boom')
    for i in range(0, 37):
        show_image(f'boom{i}.png')
        time.sleep(0.1)

    show_image('game_over.png')

    speak('Game Over. Would you like to play again?')

    time.sleep(1)
    show_image('bomb_homescreen.png')

def speak(m):
    filename = 'tmp.mp3'

    tts = gTTS(m, lang='en')
    tts.save(filename)
    os.system("/usr/bin/mplayer " + filename)

def math_question(q_num):
    time_ind = 0
    while True:
        if q_num == 1:
            if twist.count == 27:
                return True
            elif twist.count > 27 or time_ind > 60:
                return False
        elif q_num == 2:
            if twist.count == 25:
                return True
            elif twist.count < 25 or time_ind > 60:
                return False
        elif q_num == 3:
            if twist.count == 28:
                return True
            elif twist.count > 28 or time_ind > 60:
                return False
        elif q_num == 4:
            if twist.count == 23:
                show_image('bomb_homescreen.png')
                return True
            elif twist.count < 23 or time_ind > 60:
                return False

        time.sleep(0.5)
        time_ind += 1

def arrow_question():
    directions = ['up', 'down', 'left', 'up', 'down', 'right', 'up']
    for i, direction in enumerate(directions):
        speak(direction)
        show_image(f'{direction}_arrow.png')
        passed = arrow_wait(direction)
        if passed:
            if i == 6:
                show_image('bomb_homescreen.png')
                return True
        else:
            return False

def arrow_wait(direction):
    time_ind = 0
    while True:
        if time_ind > 10:
            return False
        x = joystick.horizontal
        y = joystick.vertical
        print(f'x: {x}, y: {y}')
        j_direction = 'neutral'
        if x > 575:
            j_direction = "down"
        elif x < 450:
            j_direction = 'up'

        if y > 575:
            j_direction = 'left'
        elif y < 450:
            j_direction = 'right'

        if j_direction not in (['neutral', direction]):
            return False
        elif j_direction == direction:
            return True

        time.sleep(0.5)
        time_ind += 1

def show_and_tell(color):
    time_ind = 0
    while True:
        if time_ind > 60:
            return False
        if apds.color_data_ready:
            r, g, b, c = apds.color_data
            total = r + g + b

            # normalize the colors
            r = round(r / total, 2)
            g = round(g / total, 2)
            b = round(b / total, 2)
            s_color = 'wrong'
            print(f'r: {r}, b: {b}: g: {g}')
            if r > 155 and g < 155 and b < 155:
                s_color = 'red'
            elif r < 155 and g > 155 and b < 155:
                s_color = 'green'
            elif r < 155 and g < 155 and b > 155:
                s_color = 'blue'

            if s_color == color:
                return True
            #else:
            #    return False

        time.sleep(0.5)
        #time_ind += 1

def cut_wire():
    time_ind = 0
    while True:
        try:
            if time_ind > 20:
                return False
            _ = apds.proximity
            time.sleep(0.5)
            time_ind += 1
        except:
            return True


