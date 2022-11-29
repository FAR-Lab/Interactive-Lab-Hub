# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel
import digitalio
import busio

import adafruit_mpr121
i2c = busio.I2C(board.SCL, board.SDA)
mpr121 = adafruit_mpr121.MPR121(i2c)

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
y = 0
prev_index = 0

while True:
    print(mpr121[1].value)
    # index = int(input('number of steps: '))
    # for x in range (prev_index, prev_index + index):
    #     print('prev_index: ', prev_index)
    #     print('index: ', index)
    #     print(x%30)
    #     for y in range (0,85):
    #         pixels[(x-3)%30] = (85-y, 85-y, 85-y)
    #         pixels[(x-2)%30] = (170-y, 170-y, 170-y)
    #         pixels[(x-1)%30] = (255-y, 255-y, 255-y)
    #         pixels[(x%30)] = (170+y, 170+y, 170+y)
    #         pixels[(x+1)%30] = (85+y, 85+y, 85+y)
    #         pixels[(x+2)%30] = (y, y, y)
    #         #Add 1 to the counter
    #         #Add a small time pause which will translate to 'smoothly' changing colour
    #         pixels.show()
    #         time.sleep(0.001)
    # prev_index = prev_index + index
    