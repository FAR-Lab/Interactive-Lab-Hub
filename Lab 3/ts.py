import sys
import os
import wave
import subprocess
import speech_recognition as sr
import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
from time import strftime, sleep
from adafruit_rgb_display.rgb import color565


cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None
BAUDRATE = 64000000
spi = board.SPI()
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
height = disp.width  
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90
draw = ImageDraw.Draw(image)
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)
padding = -2
top = padding
bottom = height - padding
x = 0
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

while True:
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    t = "Top button for en \n\nBottom Button for es "
    y = top
    draw.text((x, y), t, font=font, fill="#FFFFFF")
    y += font.getsize(t)[1]
    disp.image(image, rotation)
    
    # Display image.
    disp.image(image, rotation)
    if buttonB.value and not buttonA.value: 
        # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            disp.fill(color565(0, 255, 0))
            audio = r.listen(source)
            disp.fill(color565(255, 0, 0))
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))


        from translate import Translator
        translator= Translator(to_lang="es")
        translation = translator.translate(r.recognize_google(audio))
        print(translation)
        cmd = f'''
        #https://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)

        #!/bin/bash
        say() {{ local IFS=+;/usr/bin/mplayer -ao alsa -really-quiet -noconsolecontrols "http://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&q=$*&tl=es"; }}
        #say $*
        say {str(translation)}
        '''
        subprocess.check_output(cmd, shell=True)
        
    if not buttonB.value and buttonA.value: 
        # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            disp.fill(color565(0, 255, 0))
            audio = r.listen(source)
            disp.fill(color565(255, 0, 0))
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            print("Google Speech Recognition thinks you said " + r.recognize_google(audio, language = 'es'))
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))


        from translate import Translator
        translator= Translator(from_lang = "es", to_lang="en")
        translation = translator.translate(r.recognize_google(audio))
        print(translation)
        cmd = f'''
        #https://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)

        #!/bin/bash
        say() {{ local IFS=+;/usr/bin/mplayer -ao alsa -really-quiet -noconsolecontrols "http://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&q=$*&tl=en"; }}
        #say $*
        say {str(translation)}
        '''
        subprocess.check_output(cmd, shell=True)

