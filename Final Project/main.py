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
from password import PassWordMod
from token_op import Tokens

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

# Twist
twist = qwiic_twist.QwiicTwist()
if twist.is_connected():
    print("twist detected!")

# Power button
p_button = qwiic_button.QwiicButton()
if p_button.is_connected():
    print("power button detected!")

# Keypad
keypad = qwiic_keypad.QwiicKeypad()
if keypad.is_connected():
    print("keypad detected!")

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

emergency_pwd = "9316"
emergency_count_pwd = 28

emergency_color = (50, 205, 50)

# Audio
wc_sound = 'audio/welcome.mp3'
wc_e_sound = 'audio/welcome_emergency.mp3'
token_num = 'audio/token_num.mp3'
get_token = 'audio/get_token.mp3'
goodbye = 'audio/goodbye.mp3'

# Images
logo_1 = Image.open('img/CT_logo1.png')
logo_1 = logo_1.resize((70, 70))
logo_2 = Image.open('img/CT_logo2.png')
logo_2 = logo_2.resize((70, 70))
logo_3 = Image.open('img/CT_logo3.png')
logo_3 = logo_3.resize((70, 70))
logo_4 = Image.open('img/CT_logo4.png')
logo_4 = logo_4.resize((70, 70))



def screen_init():
    entered_pwd = ""
    twist.clear_interrupts()
    draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
    draw.text((0.5, 10), "Enter password", font=font, fill="#FFFFFF")
    draw.text((0.5, 50), "to access the safe", font=font, fill="#FFFFFF")     
    draw.text((20, 90), str(twist.count), font=font_big, fill="#FFFFFF")
    disp.image(image, rotation)


def display_token(token):
    draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
    draw.text((5, 5), token[:16], font=font, fill="#FFFFFF")
    draw.text((5, 35), token[16:32], font=font, fill="#FFFFFF")
    draw.text((5, 65), token[32:48], font=font, fill="#FFFFFF")
    draw.text((5, 95), token[48:], font=font, fill="#FFFFFF")
    disp.image(image, rotation)


def listen_return():
    answer = ""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        answer = r.recognize_google(audio).lower()
        print(answer)
    except sr.UnknownValueError:
        print("Google could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    if answer == "return":
        return True
    else:
        return False


def animation():
    chars = "CORNELL TECH"
    for i in range(10):
        draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0, i*25))
        disp.image(image, rotation)
    for i in range(21):
        blend_image = Image.blend(logo_2, logo_4, i / 20)
        image.paste(blend_image, (30, 30, 100, 100))
        draw.text((120, 30), chars[:min(i, len(chars))], font=font, fill="#B22222")
        disp.image(image, rotation)
        time.sleep(0.02)


    


def token_process():
    tk = Tokens(keypad, PWDM.emergency_mode)
    animation()
    draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
    draw.text((0.5, 10), "YOU HAVE ", font=font, fill="#FFFFFF")
    draw.text((50, 50), str(len(tk.tokens)), font=font_big, fill="#FFFFFF")
    draw.text((90, 60), " TOKENS", font=font, fill="#98FB98")
    draw.text((0.5, 90), "Input a number end with # to view", font=font, fill="#FFFFFF")
    disp.image(image, rotation)
    playsound(token_num)
    while check_button() and backlight.value:
        draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
        draw.text((0.5, 10), "YOU HAVE ", font=font, fill="#FFFFFF")
        draw.text((50, 50), str(len(tk.tokens)), font=font_big, fill="#FFFFFF")
        draw.text((90, 60), " TOKENS", font=font, fill="#98FB98")
        draw.text((0.5, 90), "Input a number end with # to view", font=font, fill="#FFFFFF")
        disp.image(image, rotation)
        if tk.get_token():
            playsound(get_token)
            display_token(tk.tokens[int(tk.token_number)-1])
            while not listen_return():
                pass
            tk.token_number = ""


def check_button():
    if p_button.is_button_pressed():
        if backlight.value:
            animation()
            playsound(goodbye)
        screen_init()
        backlight.value = not backlight.value
        twist.set_count(0)
        twist.set_limit(100)
        screen_init()
    return True



while True:
    check_button()
    while backlight.value:
        PWDM = PassWordMod(twist, keypad)
        while len(PWDM.entered_pwd) != len(pwd):
            PWDM.get_input()
            draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
            draw.text((0.5, 10), "Enter password", font=font, fill="#FFFFFF")
            draw.text((0.5, 50), "to access the safe", font=font, fill="#FFFFFF")     
            draw.text((20, 90), str(PWDM.entered_count), font=font_big, fill="#FFFFFF")
            draw.text((80, 90), "*"*len(PWDM.entered_pwd), font=font_big, fill="#FFFFFF")
            disp.image(image, rotation)

            PWDM.get_input()

            draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
            draw.text((0.5, 10), "Enter password", font=font, fill="#FFFFFF")
            draw.text((0.5, 50), "to access the safe", font=font, fill="#FFFFFF")     
            draw.text((20, 90), str(PWDM.entered_count), font=font_big, fill="#FFFFFF")
            draw.text((80, 90), "*"*len(PWDM.entered_pwd), font=font_big, fill="#FFFFFF")
            disp.image(image, rotation)

            if PWDM.check_password():
                # TODO
                draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
                time.sleep(0.5)
                if PWDM.emergency_mode:
                    playsound(wc_e_sound)
                    twist.set_color(*emergency_color)
                    camera = PiCamera()                        
                    camera.capture('/home/pi/final_emergency/image'+time.strftime("%m-%d-%y %H %M %S")+'.jpg')
                else:
                    playsound(wc_sound)
                token_process()
                break

            if PWDM.count_down:
                while PWDM.count_down_times > 0:
                    draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
                    draw.text((0.5, 10), "Safe LOCKED due to", font=font, fill="#FFFFFF")
                    draw.text((0.5, 50), "too many wrong inputs", font=font, fill="#FFFFFF")
                    draw.text((70, 90), str(PWDM.count_down_times)+" S", font=font_big, fill="#FFFFFF")
                    disp.image(image, rotation)
                    PWDM.count_down_times -= 1
                    time.sleep(1)
                PWDM.count_down = False