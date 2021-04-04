import time
import os
from time import strftime, sleep

import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789

import board
import busio
import adafruit_ssd1306

# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)

# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.  Change these
# to the right size for your display!
oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

image = Image.new("1", (oled.width, oled.height))
draw = ImageDraw.Draw(image)
emoticon_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 10)


def draw_pibot(xpos, ypos, mode, col):
	
	pibot_face = None
	sleep_emoticon = "(-_-) zzzZZZ"
	wakeup_emoticon = "╭( ๐ _๐)╮"
	result_emoticon = "٩( ᐛ )و"

	if(mode == 1):
		pibot_face = wakeup_emoticon
	elif(mode == 2):
		pibot_face = result_emoticon
	else:
		pibot_face = sleep_emoticon

	draw.text((xpos, ypos), pibot_face, font=emoticon_font, fill=col)

def main():
	center_x = 63
	center_y = 15

	oled.fill(0)
	oled.show()

	while True:
		draw_pibot(center_x, center_y, 0, '#cef716')
		oled.image(image)
		oled.show()
		
if __name__ == '__main__':
	main()
