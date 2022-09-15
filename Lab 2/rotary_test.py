import time
import board
import busio
import adafruit_apds9960.apds9960
from adafruit_apds9960.apds9960 import APDS9960

i2c = board.I2C()
apds = APDS9960(i2c)

apds.enable_proximity = True

while True:

    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    # TODO: Lab 2 part D work should be filled in here. You should be able to look in cli_clock.py and stats.py 
    y = top
    IP = "Proximity: " + str(apds.proximity)
    draw.text((x, y), IP, font=font, fill="#FFFFFF")

    # Display image.
    disp.image(image, rotation)
    time.sleep(0.2)