from __future__ import print_function
import qwiic_joystick
import time
import sys
from pydub import AudioSegment
from pydub.playback import _play_with_simpleaudio

import board
import busio

import adafruit_mpr121


notes = ['G3', 
        'Ab3',
        'A3',
        'Bb3',
        'B3',
        'C4',
        'Db4',
        'D4',
        'Eb4',
        'E4',
        'F4',
        'Gb4',
        'G4',
        'Ab4',
        'A4',
        'Bb4',
        'B4',
        'C5',
        'Db5',
        'D5',
        'Eb5',
        'E5',
        'F5',
        'Gb5',
        'G5',
        'Ab5']


sounds = {
    notes[i]: AudioSegment.from_file('notes/'+notes[i]+'.mp3') for i in range(len(notes))
}

# joystick
print("\nSparkFun qwiic Joystick   Example 1\n")
myJoystick = qwiic_joystick.QwiicJoystick()

if myJoystick.connected == False:
    print("The Qwiic Joystick device isn't connected to the system. Please check your connection", \
        file=sys.stderr)

myJoystick.begin()

print("Initialized. Firmware Version: %s" % myJoystick.version)

# twizzler
i2c = busio.I2C(board.SCL, board.SDA)
mpr121 = adafruit_mpr121.MPR121(i2c)

prev_x = None
prev_y = None
block = 0

while True:
    x = myJoystick.horizontal
    y = myJoystick.vertical

    block = 0
    for i in range(12):
        if mpr121[i].value:
            print(f"Twizzler {i} touched!")
            block = i + 1



    if prev_y != 1023 and y == 1023:
        _play_with_simpleaudio(sounds[notes[0 + block]])
        print('first string')
    if prev_x != 0 and x == 0:
        _play_with_simpleaudio(sounds[notes[5 + block]])
        print('second string')
    if prev_y != 0 and y == 0:
        _play_with_simpleaudio(sounds[notes[9 + block]])
        print('third string')
    if prev_x != 1023 and x == 1023:
        _play_with_simpleaudio(sounds[notes[14 + block]])
        print('fourth string')
    
    prev_x = x
    prev_y = y

    print("X: %d, Y: %d, Button: %d" % ( \
                x, \
                y, \
                myJoystick.button))

    time.sleep(.1)