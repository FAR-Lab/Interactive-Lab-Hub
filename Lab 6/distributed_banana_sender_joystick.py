import time
import board
import busio
import adafruit_mpr121
import qwiic_joystick

import paho.mqtt.client as mqtt
import uuid

client = mqtt.Client(str(uuid.uuid1()))
client.tls_set()
client.username_pw_set('idd', 'device@theFarm')

client.connect(
    'farlab.infosci.cornell.edu',
    port=8883)

topic = 'IDD/cake'

i2c = busio.I2C(board.SCL, board.SDA)

mpr121 = adafruit_mpr121.MPR121(i2c)

while True:
    myJoystick = qwiic_joystick.QwiicJoystick()
    myJoystick.begin()
    amount = myTwist.count*10
    if myJoystick.get_vertical() <= 205:
        val = f"mixing!"
        print(val, amount)
        client.publish(topic, val)
    time.sleep(0.25)
