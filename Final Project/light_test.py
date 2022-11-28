### Light feature of the installation ###

# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel
from adafruit_seesaw import seesaw, rotaryio, digitalio


# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D21

# The number of NeoPixels
num_pixels = 30

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)

seesaw = seesaw.Seesaw(board.I2C(), addr=0x36)

seesaw_product = (seesaw.get_version() >> 16) & 0xFFFF
print("Found product {}".format(seesaw_product))
if seesaw_product != 4991:
    print("Wrong firmware loaded?  Expected 4991")

seesaw.pin_mode(24, seesaw.INPUT_PULLUP)
button = digitalio.DigitalIO(seesaw, 24)
button_held = False

encoder = rotaryio.IncrementalEncoder(seesaw)
last_position = 0
lights = 0

blank = ((0,0,0))
white = ((248,255,220))
orange = ((253,80,0))
yellow = ((160,90,0))
colour_val = 0

def colorWipe(pixels, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(num_pixels):
        pixels[i] = color
        pixels.show()
        time.sleep(wait_ms/1000.0)

while True:
    position = encoder.position

    if position > last_position:
        last_position = position
        print("Position: {}".format(position))
        if lights < 30:
            lights += 1
        else:
            if colour_val == 0 or colour_val == 1:
                colour_val += 1
            else:
                colour_val = 0
    elif position < last_position:
        last_position = position
        print("Position: {}".format(position))
        lights -= 1

    else:
        lights = lights
    
    if colour_val == 1:
        colour = white
    elif colour_val == 2:
        colour = yellow
    else:
        colour = orange

    for i in range(30):
        if i in range(lights):
            pixels[i] = colour
        else:
            pixels[i] = blank

    pixels.show()


    # # Comment this line out if you have RGBW/GRBW NeoPixels
    # position = encoder.position
    # if (encoder.position < 0):
    #     position = 0

    # pixels[last_position] = ((253,80,0))

    # if position > last_position and position <= (num_pixels - 1):
    #     last_position = position
    #     print("Position: {}".format(position))
    #     pixels[position] = ((253,80,0))
    # elif position < last_position and position <= (num_pixels - 1):
    #     pixels[last_position] = ((0,0,0))
    #     last_position = position
    #     print("Position: {}".format(position))
    # else: 
    #     position %= num_pixels

    # pixels.show()


    # # Uncomment this line if you have RGBW/GRBW NeoPixels
    # # pixels.fill((255, 0, 0, 0))

    # # Comment this line out if you have RGBW/GRBW NeoPixels