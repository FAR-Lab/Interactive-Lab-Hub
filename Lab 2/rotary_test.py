import time
import board
import busio
import adafruit_apds9960.apds9960
from adafruit_apds9960.apds9960 import APDS9960

i2c = board.I2C()
apds = APDS9960(i2c)

apds.enable_proximity = True

while True:
    print(apds.proximity)
    time.sleep(0.2)