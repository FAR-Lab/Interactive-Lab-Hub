# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import board
from adafruit_apds9960.apds9960 import APDS9960
import time
import board
import busio
import adafruit_mpr121

import paho.mqtt.client as mqtt
import uuid

client = mqtt.Client(str(uuid.uuid1()))
client.tls_set()
client.username_pw_set('idd', 'device@theFarm')

client.connect(
    'farlab.infosci.cornell.edu',
    port=8883)
topic = 'IDD/your/topic/here'

i2c = board.I2C()

apds = APDS9960(i2c)
apds.enable_proximity = True
apds.enable_gesture = True
mpr121 = adafruit_mpr121.MPR121(i2c)

# Uncomment and set the rotation if depending on how your sensor is mounted.
# apds.rotation = 270 # 270 for CLUE

while True:
    gesture = apds.gesture()

    if gesture == 0x01:
        print("up")
        client.publish(topic, "up")
    elif gesture == 0x02:
        print("down")
        client.publish(topic, "down")
    elif gesture == 0x03:
        print("left")
        client.publish(topic, "left")
    elif gesture == 0x04:
        print("right")
        client.publish(topic, "right")