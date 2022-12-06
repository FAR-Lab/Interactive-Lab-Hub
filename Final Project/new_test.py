# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel
import digitalio
import busio

# import adafruit_mpr121
# i2c = busio.I2C(board.SCL, board.SDA)
# mpr121 = adafruit_mpr121.MPR121(i2c)

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

def move_to_target (target_index):
    global prev_index
    target_index = target_index
    steps = (target_index - prev_index)%30
    for x in range (prev_index, prev_index + steps):
        print('prev_index: ', prev_index)
        print('steps: ', steps)
        print(x%30)
        for y in range (0,85):
            pixels[(x-3)%30] = (85-y, 85-y, 85-y)
            pixels[(x-2)%30] = (170-y, 170-y, 170-y)
            pixels[(x-1)%30] = (255-y, 255-y, 255-y)
            pixels[(x%30)] = (170+y, 170+y, 170+y)
            pixels[(x+1)%30] = (85+y, 85+y, 85+y)
            pixels[(x+2)%30] = (y, y, y)
            #Add 1 to the counter
            #Add a small time pause which will translate to 'smoothly' changing colour
            pixels.show()
            time.sleep(0.001)
    prev_index = (prev_index + steps)%30

def loop_white ():
    while True:
        global x
        x = x + 1
        for y in range (0,85):
            pixels[(x-3)%30] = (85-y, 85-y, 85-y)
            pixels[(x-2)%30] = (170-y, 170-y, 170-y)
            pixels[(x-1)%30] = (255-y, 255-y, 255-y)
            pixels[(x%30)] = (170+y, 170+y, 170+y)
            pixels[(x+1)%30] = (85+y, 85+y, 85+y)
            pixels[(x+2)%30] = (y, y, y)
            #Add 1 to the counter
            #Add a small time pause which will translate to 'smoothly' changing colour
            pixels.show()
            time.sleep(0.001)

def wheel(pos):
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = pos * 3
        g = 255 - pos * 3
        b = 0
    elif pos < 170:
        pos -= 85
        r = 255 - pos * 3
        g = 0
        b = pos * 3
    else:
        pos -= 170
        r = 0
        g = pos * 3
        b = 255 - pos * 3
    return (r, g, b)

def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)

while True:
    # rainbow_cycle(0.01)
    # loop_white()
    if mpr121[1].value:
        move_to_target(8)
    elif mpr121[3].value:
        move_to_target(15)
    elif mpr121[5].value:
        move_to_target(20)
    elif mpr121[8].value:
        move_to_target(25)
    elif mpr121[10].value:
        move_to_target(3)