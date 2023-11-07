from __future__ import print_function
import qwiic_joystick
import random
import sys
import time
import pygame
import board
import busio
import time
import qwiic_button
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont

i2c = busio.I2C(board.SCL, board.SDA)

oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
myButton = qwiic_button.QwiicButton()

width = oled.width
height = oled.height
image = Image.new("1", (width, height))

draw = ImageDraw.Draw(image)

padding = -2
top = padding
bottom = height - padding

font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 12)

oled.fill(0)
oled.show()

def draw_start():
    global image
    image = Image.new("1", (width, height))
    draw = ImageDraw.Draw(image)
    x = 12
    y = height // 2 - 4
    draw.text((x, y), "Russian Roulette", font=font, fill="#DFC58D")
    oled.image(image)
    oled.show()

def draw_end():
    global image
    image = Image.new("1", (width, height))
    draw = ImageDraw.Draw(image)
    draw.text((8, height // 2 - 10), "You just got served.", font=font, fill="#DFC58D")
    draw.text((30, height // 2 + 2), "Game over.", font=font, fill="#DFC58D")
    oled.image(image)
    oled.show()

def draw_game(pull):
    global image
    image = Image.new("1", (width, height))
    draw = ImageDraw.Draw(image)
    x = 15
    y = height // 2 - 5
    draw.text((x, y), "Triggers pulled: " + str(pull), font=font, fill="#DFC58D")
    oled.image(image)
    oled.show()

def play_sound(file_path, time_to_sleep=1):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    time.sleep(time_to_sleep) 

def runGame():
    pygame.mixer.init()

    myJoystick = qwiic_joystick.QwiicJoystick()
    if myJoystick.connected == False:
            print("The Qwiic Joystick device isn't connected to the system. Please check your connection", \
                file=sys.stderr)
            sys.exit(1)
    myJoystick.begin()
    print("Joystick Initialized. Firmware Version: %s" % myJoystick.version)

    draw_start()
    chambers_input = input("Please enter the number of chambers (default = 6): ")
    if chambers_input and chambers_input.isdigit():
        chambers = int(chambers_input)
        if chambers < 2 or chambers > 10:
            print("You have entered an invalid number of chambers. Please enter a number between 2 and 10.")
            sys.exit(1)
        print("You have chosen to play with " + str(chambers) + " chamber.")
    else:
        chambers = 6
        print("Invalid input, the game has been set to play with 6 chambers by default.")

    fatal_bullet = random.randint(0, chambers - 1)
    current_bullet = 0
    current_shots = 0
    brightness = 250    # The maximum brightness of the pulsing LED. Can be between 0 and 255
    cycle_time = 1000    # The total time for the pulse to take. Set to a bigger number for a slower pulse or a smaller number for a faster pulse
    off_time = 200       # The total time to stay off between pulses. Set to 0 to be pulsing continuously.


    trigger_pulled = False

    print("Press the Button to start!")

    myButton.LED_config(brightness, cycle_time, off_time)
    
    while True:
        if myButton.is_button_pressed():
            myButton.LED_off()
            play_sound("reload.mp3", 1.0)
            time.sleep(0.1)
            break

    while True:

        draw_game(current_shots)

        # print("You have pulled the trigger " + str(current_shots) + " time(s) in the current round.")
        # keypress = input("Pull the trigger or type 'r' to reset the chamber: ")
        
        if myJoystick.vertical < 10 and not trigger_pulled:
            trigger_pulled == True
            current_bullet = (current_bullet + 1) % chambers
            current_shots += 1
            print("You have pulled the trigger " + str(current_shots) + " time(s) in the current round.")
            if current_bullet == fatal_bullet:
                print("You just got served!")
                play_sound("gunshot.mp3", 1)
                print("Game Over")
                draw_end()
                break
            print("You will live to see another day")
            draw_game(current_shots)
            time.sleep(2)

        elif myJoystick.vertical > 500 and trigger_pulled:
            trigger_pulled == False

        elif myJoystick.horizontal < 400:
            print("You spun the chamber!")
            play_sound("reload.mp3", 1.4)
            current_shots = 0
            fatal_bullet = random.randint(0, chambers - 1)

    play_sound("GG.mp3", 214)


if __name__ == '__main__':
    try:
        runGame()
    except (KeyboardInterrupt, SystemExit) as exErr:
        print("\nEnding Game")
        myButton.LED_off()
        sys.exit(0)