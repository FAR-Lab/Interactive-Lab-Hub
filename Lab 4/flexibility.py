import time
import subprocess
import digitalio
import board
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
from time import  strftime, sleep
from datetime import datetime, timedelta
import busio
from i2c_button import I2C_Button

import qwiic

# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()
i2c = busio.I2C(board.SCL, board.SDA)



ToF = qwiic.QwiicVL53L1X()
if (ToF.sensor_init() == None):					 # Begin returns 0 on a good init
	print("Sensor online!\n")


# scan the I2C bus for devices
while not i2c.try_lock():
	pass
devices = i2c.scan()
i2c.unlock()
print("I2C devices found:", [hex(n) for n in devices])
default_addr = 0x6F
if default_addr not in devices:
	print("warning: no device at the default button address", default_addr)

# Create the ST7789 display:
disp = st7789.ST7789(
	spi,
	cs=cs_pin,
	dc=dc_pin,
	rst=reset_pin,
	baudrate=BAUDRATE,
	width=135,
	height=240,
	x_offset=53,
	y_offset=40,
)


# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

#def countdown(int: t):
#	while t:
#		mins, secs = divmod(t,60)
#		timer = '%02d:%02d'.format(mins,secs)
#		print(timer, end="\r")
#		time.sleep(1)
#		t -= 1


# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width-10, height-10), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font_size =20
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", font_size)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

# these setup the code for our buttons and tell the pi to treat the GPIO pins as digitalIO vs analogIO
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()


## draw to start
current_text = "How flexible are you? \n" 
print_str = current_text
y = top
draw.text((x+width/2-font_size/2,y+height/2-font_size/2),(current_text),font=font,fill="#FFFFFF")
y += font.getsize(print_str)[1]
	
# Display image.
disp.image(image, rotation)
past_laps = ""




while True:
  
	try:
		ToF.start_ranging()						 # Write configuration bytes to initiate measurement
		time.sleep(.005)
		distance = ToF.get_distance()	 # Get the result of the measurement from the sensor
		time.sleep(.005)
		ToF.stop_ranging()
		distanceInches = distance / 25.4
		distanceFeet = distanceInches / 12.0
		print_str = " How flexible are you? \n \n" 
		print_str = print_str + ("Inches from toes: %s" % ( round(distanceInches-5,1)))

	except Exception as e:
		print(e)

	if buttonB.value and not buttonA.value:  
		print("here")
		# just button A pressed
		##lap_times = lap_times.append(str(current_lap_time))
		## Increment the current lap

		## Print out line with that total lap time 
		## Start a new line with the new time in between   
	draw.rectangle((0, 0, width, height), outline=0, fill=0)
	y = top
	draw.text((x+12,y+35),print_str,font=font,fill="#FFFFFF")
	#y += font.getsize(print_str)[1]
	print("here1")
	# Display image.
	disp.image(image, rotation)
	sleep(.05)

 



