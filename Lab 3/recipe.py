import digitalio
import board

from adafruit_rgb_display.rgb import color565
import adafruit_rgb_display.st7789 as st7789
import webcolors

import pygame
import os


cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None
BAUDRATE = 64000000  # the rate  the screen talks to the pi
# Create the ST7789 display:
display = st7789.ST7789(
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


# these setup the code for our buttons and the backlight and tell the pi to treat the GPIO pins as digitalIO vs analogIO
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

# get a color from the user
display.fill(color565(0, 255, 0))

pygame.mixer.init()

# states = ["step1", "step2", "step3", "step4", "step5"]
curstate = 0
musics=[]
#iterate files in audios
for filename in os.listdir("audios"):
    if filename.endswith(".wav"):
        curmusic = 'audios/' +filename
        # musics.append[curmusic]
        print('find audio %s'%filename)


pygame.mixer.music.load("audios/Step1.wav")
# pygame.mixer.music.play()
# while pygame.mixer.music.get_busy() == True:
#     continue

# Main loop:
while True:
    if buttonA.value and buttonB.value:
        backlight.value = False  # turn off backlight
    else:
        backlight.value = True  # turn on backlight
    if buttonB.value and not buttonA.value:  # just button A pressed
        if curstate>0:
            curstate = curstate - 1
            pygame.mixer.music.load(musics[curstate-1])

        print(curstate)

    if buttonA.value and not buttonB.value:  # just button B pressed
        if curstate<5:
            curstate = curstate + 1
            pygame.mixer.music.load(musics[curstate-1])

        print(curstate)


    if curstate == 0:
        continue
    else:
        pygame.mixer.music.play()

        if pygame.mixer.music.get_busy() == True:
            continue
