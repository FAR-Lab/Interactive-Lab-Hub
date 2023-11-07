# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import board
import busio
import time
import qwiic_button
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont

i2c = busio.I2C(board.SCL, board.SDA)

oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
start_button = qwiic_button.QwiicButton()

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
    x = 16
    y = height // 2 - 5
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

# states = ["start", "game", "end"]
curr_state = "end"

while True:
    print(curr_state)
    if curr_state == "start":
        draw_start()
    elif curr_state == "game":
        draw_game(1)
    elif curr_state == "end":
        draw_end()
    if start_button.is_button_pressed():
        if curr_state == "start":
            curr_state = "game"
        if curr_state == "end":
            curr_state = "start"
        time.sleep(0.1)