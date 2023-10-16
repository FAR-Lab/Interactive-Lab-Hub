import time
import board
import busio
import adafruit_mpr121
import os
from adafruit_seesaw import seesaw, rotaryio, digitalio

i2c = busio.I2C(board.SCL, board.SDA)
mpr121 = adafruit_mpr121.MPR121(i2c)

seesaw = seesaw.Seesaw(board.I2C(), addr=0x36)

seesaw_product = (seesaw.get_version() >> 16) & 0xFFFF
print("Found product {}".format(seesaw_product))
if seesaw_product != 4991:
    print("Wrong firmware loaded?  Expected 4991")

seesaw.pin_mode(24, seesaw.INPUT_PULLUP)
button = digitalio.DigitalIO(seesaw, 24)
button_held = False

encoder = rotaryio.IncrementalEncoder(seesaw)
last_position = None

soundtrack = {
    3: "GSound",
    2: "BSound",
    1: "Erightsound",
    8: "Dsound",
    9: "ASound",
    10: "Eleftsound",
}

def playnote(filename):
    os.system(f"mpg123 guitar/{filename}.mp3")

def adjustvolume(position):
    position += 50
    if position > 100:
        position = 100
    if position < 0:
        position = 0
    os.system(f"amixer sset 'Master' {position}%")

while True:
    position = -encoder.position
    if position != last_position:
        last_position = position
    if not button.value and not button_held:
        button_held = True
    if button.value and button_held:
        button_held = False
        adjustvolume(position)
    for i in range(12):
        if mpr121[i].value:
            print(f"Twizzler {i} touched!")
            playnote(soundtrack[i])
    time.sleep(0.05)  # Small delay to keep from spamming output messages.