# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
"""NeoKey simpletest."""
import board
from adafruit_neokey.neokey1x4 import NeoKey1x4

# use default I2C bus
i2c_bus = board.I2C()

# Create a NeoKey object
neokey = NeoKey1x4(i2c_bus, addr=0x30)

print("Adafruit NeoKey simple test")

# Check each button, if pressed, light up the matching neopixel!
last_pressed = None
while True:
    if neokey[0]:
        if not last_pressed == 0:
            print("Button A")
        neokey.pixels[0] = 0xFF0000
        last_pressed = 0
    else:
        neokey.pixels[0] = 0x0

    if neokey[1]:
        if not last_pressed == 1:
            print("Button B")
        neokey.pixels[1] = 0xFFFF00
        last_pressed = 1
    else:
        neokey.pixels[1] = 0x0

    if neokey[2]:
        if not last_pressed == 2:
            print("Button C")
        last_pressed = 2
        neokey.pixels[2] = 0x00FF00
    else:
        neokey.pixels[2] = 0x0

    if neokey[3]:
        if not last_pressed == 3:
            print("Button D")
        last_pressed = 3
        neokey.pixels[3] = 0x00FFFF
    else:
        neokey.pixels[3] = 0x0
