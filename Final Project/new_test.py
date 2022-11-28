# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel
import digitalio
import busio

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D21

# The number of NeoPixels
num_pixels = 30

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
# ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False
)

blank = ((0,0,0))
white = ((248,255,220))
orange = ((253,80,0))
yellow = ((160,90,0))

x = 0

pixels.fill((0, 220, 0))

while True:
    while x < 40:
        pixels[x] = (255, 0, 0)
        pixels[x-5] = (255, 0, 100)
        pixels[x-10] = (0, 0, 255)
        #Add 1 to the counter
        x=x+1
        #Add a small time pause which will translate to 'smoothly' changing colour
        print(x)
        time.sleep(0.1)