# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
# SPDX-License-Identifier: MIT
"""Example for connecting two NeoKey 1x4 breakouts. Requires bridging the A0 jumper on one board."""
import board
from rainbowio import colorwheel
from adafruit_neokey.neokey1x4 import NeoKey1x4
import time
import board
from adafruit_seesaw import seesaw, neopixel, rotaryio, digitalio
import qwiic_button
from adafruit_servokit import ServoKit
import sys

kit = ServoKit(channels=16)
servos = 2
for i in range(servos):
    kit.servo[i].set_pulse_width_range(500, 2500)

################################################################

servo_button = qwiic_button.QwiicButton()
reset_button = qwiic_button.QwiicButton(address=0x6e)

################################################################

i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
seesaw = seesaw.Seesaw(i2c, addr=0x36)

seesaw_product = (seesaw.get_version() >> 16) & 0xFFFF
# print("Found product {}".format(seesaw_product))
# if seesaw_product != 4991:
#     print("Wrong firmware loaded?  Expected 4991")

# Configure seesaw pin used to read knob button presses
# The internal pull up is enabled to prevent floating input
seesaw.pin_mode(24, seesaw.INPUT_PULLUP)
rotary_button = digitalio.DigitalIO(seesaw, 24)
encoder = rotaryio.IncrementalEncoder(seesaw)
pixel = neopixel.NeoPixel(seesaw, 6, 1)
pixel.brightness = 0.5
blue = colorwheel(170)
yellow = colorwheel(30)

################################################################

# Create a NeoKey object
neokey1 = NeoKey1x4(board.I2C())
neokey2 = NeoKey1x4(board.I2C(), addr=0x31)
neokey3 = NeoKey1x4(board.I2C(), addr=0x32)

keys = [
    (neokey1, 0, colorwheel(0)),
    (neokey1, 1, colorwheel(23)),
    (neokey1, 2, colorwheel(46)),
    (neokey1, 3, colorwheel(69)),
    (neokey2, 0, colorwheel(92)),
    (neokey2, 1, colorwheel(115)),
    (neokey2, 2, colorwheel(138)),
    (neokey2, 3, colorwheel(161)),
    (neokey3, 0, colorwheel(184)),
    (neokey3, 1, colorwheel(207)),
    (neokey3, 2, colorwheel(230)),
    # (neokey3, 3, colorwheel(352)),
]

pressed_keys = [-1] * len(keys)

off = (0, 0, 0)


import pygame
from pygame import mixer
pygame.init()


# sounds
'''
hi_hat = mixer.Sound('sounds\kit2\hi hat.wav')
snare = mixer.Sound('sounds\kit2\snare.wav')
kick = mixer.Sound('sounds\kit2\kick.wav')
crash = mixer.Sound('sounds\kit2\crash.wav')
clap = mixer.Sound('sounds\kit2\clap.wav')
tom = mixer.Sound("sounds\kit2\\tom.wav")
'''
beats = [
    mixer.Sound(f'sounds/{beat_name}.mp3') 
    for beat_name in ['hi hat', 'snare', 
                      'Acoustic Kick 29', 
                      'crash', 'clap', 
                    #   'tom',
                    'Acoustic Sticks 01',
                      'Acoustic Cowbell 01',
                      'Acoustic Crash 01',
                      'Acoustic Hat Bell 01',
                      'Acoustic High Tom 02',
                      'Acoustic Ride Short 04',
                    #   'Acoustic Ride Crash 01',
                      ]
]

# track = mixer.Sound(f'sounds/christmas-family-alfonso-gugliucci-main-version-21297-03-43.mp3')
track = mixer.Sound('sounds/springtime.mp3')

beat_changed = True
servo_on = True
timer = pygame.time.Clock()
fps = 60
nb_beats = 8
bpm = 240 * 8
# beat_length = 3600 // bpm
beat_length = 1
initial_volume = 0.5
instruments = len(beats)
playing = True
clicked = [[-1 for _ in range(nb_beats)] for _ in range(instruments)]
active_list = [1 for _ in range(instruments)]

active_length = 0
active_beat = 0
servo_button_time = time.time()

beat_offset = 0
volume_offset = 0

pygame.mixer.set_num_channels(instruments * 3)

cur_angle = 45
pixel.brightness = 2


def dance():
    if servo_on:
        for i in range(len(clicked)):
            if clicked[i][active_beat] == 1 and active_list[i] == 1:
                global cur_angle
                cur_angle = (180 - cur_angle)
                for i in range(servos):
                    # Set the servo to 180 degree position
                    kit.servo[i].angle = cur_angle
                break


    # for i in range(servos):
    #     # Set the servo to 0 degree position
    #     kit.servo[i].angle = 0

def reset():
    if reset_button.is_button_pressed():
        for i in range(len(clicked)):
            for j in range(len(clicked[i])):
                clicked[i][j] = -1
        for beat in beats:
            beat.stop()
        for i in range(len(pressed_keys)):
            pressed_keys[i] = -1
        for neokey, key_number, color in keys:
            neokey.pixels[key_number] = off

rotary_button_held = False
rotary_mode = 0

def rotary():
    global rotary_button_held
    global bpm, beat_length, rotary_mode

    if not rotary_button.value and not rotary_button_held:
        rotary_button_held = True
        rotary_mode = 1 - rotary_mode
        # if rotary_mode == 1:
        #     beat_offset = rotary_button.value
        # else:
        #     volume_offset = rotary_button.value
        print("Button pressed")

    if rotary_button.value and rotary_button_held:
        rotary_button_held = False

    if rotary_mode == 0:
        pixel.fill(yellow)
        position = -encoder.position
        # if position > 10:
        #     volume_offset = position - 10
        # elif position < -10:
        #     volume_offset = position + 10
        position = min(max(-10, position), 10)
        # bpm = max(0.1, 240 * 8 + (position - initial_position) * 50)
        volume = initial_volume + (position - volume_offset) / 20
        for beat in beats:
            beat.set_volume(volume)
        # track.set_volume(volume)

        print('set volume to ', volume)

    if rotary_mode == 1:
        pixel.fill(blue)
        position = -encoder.position
        position = min(max(1, position - beat_offset), 10)
        # bpm = max(0.1, 240 * 8 + (position - initial_position) * 50)
        beat_length = position
        print('set beat length to ', beat_length)


def play_keys():
    for i in range(len(keys)):
    # time_st_0 = time.time()
        neokey, key_number, color = keys[i]
        if neokey[key_number]:
            print("Button", i)
            neokey.pixels[key_number] = color
            try:
                clicked[i][active_beat] = 1
                if pressed_keys[i] == -1:
                    pressed_keys[i] = 1
                    beats[i].play()
            except:
                pass
        else:
            neokey.pixels[key_number] = off
            pressed_keys[i] = -1

    # print('key query: ', time.time() - time_st_0)


def play_notes():
    for i in range(len(clicked)):
        neokey, key_number, color = keys[i]
        if clicked[i][active_beat] == 1 and active_list[i] == 1:
            beats[i].play()
            neokey.pixels[key_number] = color
        else:
            neokey.pixels[key_number] = off

run = True

# Check each button, if pressed, light up the matching NeoPixel!

# track.play()
# track.set_volume(0.5)

while run:
    try:
        time_st = time.time()
        timer.tick(fps)
        if beat_changed:
            play_notes()
            dance()
            beat_changed = False

        # print(time.time() - time_st)

        play_keys()
        rotary()
        reset()

        # print(time.time() - time_st)

        # beat_length = 3600 // bpm
        # print(beat_length)
        if servo_button.is_button_pressed():
            pressed_time = time.time()
            if  pressed_time - servo_button_time > 0.5:
                servo_button_time = pressed_time
                servo_on = not servo_on

        if playing:
            # print(active_length, beat_length, active_beat, beat_changed)
            if active_length < beat_length: # measure time for a beat to play. This means the current beat is still playing.
                active_length += 1
            else:
                active_length = 0
                if active_beat < nb_beats - 1:
                    active_beat += 1
                else:
                    active_beat = 0
                beat_changed = True

        # print(time.time() - time_st)
        print()
    except (KeyboardInterrupt, SystemExit) as exErr:
        run = False
        pixel.brightness = 0
        pygame.quit()
        sys.exit(0)
    except:
        pass
    