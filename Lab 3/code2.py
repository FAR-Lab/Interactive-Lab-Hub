import os
import time

import digitalio
import board
import adafruit_rgb_display.st7789 as st7789
import subprocess
import qwiic_button
import RPi.GPIO as GPIO

from PIL import Image, ImageDraw, ImageFont
from subprocess import call, Popen

cwd = os.getcwd()


def handle_speak(val):
    subprocess.run(["sh", "GoogleTTS_demo.sh", val])
    # call(f"espeak -ven -k5 -s150 --stdout '{val}' | aplay", shell=True)
    time.sleep(0.5)


def image_formatting(image2):
    image2 = image2.convert('RGB')
    # Scale the image to the smaller screen dimension
    image2 = image2.resize((240, 135), Image.BICUBIC)

    return image2


# Configuration for CS and DC pins (these are PiTFT defaults):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = digitalio.DigitalInOut(board.D24)

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

hardware = 'plughw:2,0'

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

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

redButton = qwiic_button.QwiicButton(address=0x68)
redButton.begin()

greenButton = qwiic_button.QwiicButton(address=0x6f)
greenButton.begin()

redButton.LED_off()
greenButton.LED_off()

if not redButton.begin():
    print("\nThe Red Qwiic Button isn't connected to the system. Please check your connection")
if not greenButton.begin():
    print("\nThe Green Qwiic Button isn't connected to the system. Please check your connection")

# Configure screen buttons
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

current = 0
while True:
    display_image = Image.open("welcome.jpeg")
    #display_img = image_formatting(display_img)
    display_image = display_image.convert('RGB')
    display_image = display_image.resize((width, height), Image.BICUBIC)
    #disp.image(display_image, rotation)

    if current == 0:
        subprocess.call("~/Interactive-Lab-Hub/Lab\ 3/welcome.sh", shell=True)
        time.sleep(0.8)
        current = 1

    if current == 1:
        subprocess.call("~/Interactive-Lab-Hub/Lab\ 3/registered.sh", shell=True)
        while not (redButton.is_button_pressed() or greenButton.is_button_pressed()):
            redButton.LED_on(155); greenButton.LED_on(155)
        red_clicked = redButton.is_button_pressed()
        green_clicked = greenButton.is_button_pressed()
        redButton.LED_off(); greenButton.LED_off()
        if red_clicked:
            current = 2
        else:
            handle_speak("So, you have already registered with us. Please say your 4 digit registration code.")
            time.sleep(1)
            handle_speak("I am sorry. I do not see that code in our system.")
            handle_speak("Please re register with us. I assure you the process is straight forward.")
            current = 2
        time.sleep(0.1)

    if current == 2:
        display_img = Image.open("NY.png")
        #display_img = image_formatting(display_img)
        #disp.image(display_img, rotation)
        handle_speak("To begin, are you a resident of New York State?")
        handle_speak("Press the red button for no, or press the green button for yes.")
        while not (redButton.is_button_pressed() or greenButton.is_button_pressed()):
            redButton.LED_on(200)
            greenButton.LED_on(200)
        red_clicked = redButton.is_button_pressed()
        redButton.LED_off()
        greenButton.LED_off()
        if red_clicked:
            handle_speak(
                "I am sorry but due to the high volume of inquiries we cannot create appointments for people residing "
                "outside of New York State.")
            handle_speak(
                "Please press the red button to disconnect, or the green button if you meant to say you are a "
                "resident of New York state.")
            current = 3
        else:
            current = 4

    if current == 3:
        while not (redButton.is_button_pressed() or greenButton.is_button_pressed()):
            redButton.LED_on(200);
            greenButton.LED_on(200)
        red_clicked = redButton.is_button_pressed()
        redButton.LED_off();
        greenButton.LED_off()
        if red_clicked:
            current = 10
        else:
            current = 4

    if current == 4:
        handle_speak("Thanks! Please state your county of residence.")
        time.sleep(1)
        handle_speak("Thanks! Please say your 10 digit mobile phone number including area code.")
        time.sleep(2)
        current = 5

    if current == 5:
        display_img = Image.open("text.gif")
        #display_img = image_formatting(display_img)
        #disp.image(display_img, rotation)
        handle_speak("Thanks! You should have received a confirmation text from us. Please press the green button to "
                     "confirm you have received the message. Press the red button to resend.")
        while not (redButton.is_button_pressed() or greenButton.is_button_pressed()):
            redButton.LED_on(200)
            greenButton.LED_on(200)
        red_clicked = redButton.is_button_pressed()
        redButton.LED_off()
        greenButton.LED_off()
        if red_clicked:
            current = 5
        else:
            current = 6

    if current == 6:
        display_img = Image.open("calendar.png")
        #display_img = image_formatting(display_img)
        #disp.image(display_img, rotation)
        handle_speak("Cool! What day would you like to come in to see the doctor?")
        time.sleep(0.8)
        handle_speak("Give me a moment to check the doctor's availability on this day.")
        time.sleep(0.5)
        handle_speak("The doctor is not available on this day. May I suggest his next available opening? Friday April "
                     "second at nine A M.")
        handle_speak("Press the green button to confirm this appointment. Press red for other options.")
        while not (redButton.is_button_pressed() or greenButton.is_button_pressed()):
            redButton.LED_on(200)
            greenButton.LED_on(200)
        red_clicked = redButton.is_button_pressed()
        redButton.LED_off()
        greenButton.LED_off()
        if red_clicked:
            current = 7
        else:
            current = 8

    if current == 7:
        handle_speak("I am sorry but the doctor has no other available appointments in the coming 8 days. Please call "
                     "again later to check for cancellations or to reschedule.")
        current = 10

    if current == 8:
        display_img = Image.open("friday.jpeg")
        #display_img = image_formatting(display_img)
        #disp.image(display_img, rotation)
        handle_speak("Great! You are confirmed for the appointment on ")
        handle_speak("Friday April second at")
        handle_speak("nine A M")
        handle_speak("We will send you a confirmation text the day before.")
        handle_speak("Is there anything else I can help you with? Please use the buttons.")
        while not (redButton.is_button_pressed() or greenButton.is_button_pressed()):
            redButton.LED_on(200)
            greenButton.LED_on(200)
        red_clicked = redButton.is_button_pressed()
        redButton.LED_off()
        greenButton.LED_off()
        if red_clicked:
            current = 10
        else:
            display_img = Image.open("phonering.jpeg")
            display_img = image_formatting(display_img)
            disp.image(display_img, rotation)
            handle_speak("Connecting you to an operator. Please stand by.")
            os.system('mpg321 ring.mp3 &')
            time.sleep(2)
            backlight.value = False
            break

    if current == 10:
        time.sleep(0.5)
        display_img = Image.open("welcome.jpeg")
        #display_img = image_formatting(display_img)
        #disp.image(display_img, rotation)
        handle_speak("Thanks for calling in to the Medical Hotline of Manhattan. Goodbye.")
        time.sleep(2)
        backlight.value = False
        break

    time.sleep(0.1)
    GPIO.cleanup()
