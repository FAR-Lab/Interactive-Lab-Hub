import time
import board
import busio
import adafruit_mpr121

import RPi.GPIO as GPIO
import signal
import time
import board
import busio
from subprocess import Popen, call

import paho.mqtt.client as mqtt
import uuid

i2c = busio.I2C(board.SCL, board.SDA)

mpr121 = adafruit_mpr121.MPR121(i2c)

read_topic = 'IDD/tools/response'
send_topic = 'IDD/tools/guess'


def on_connect(client, userdata, flags, rc):
        print(f"connected with result code {rc}")
        client.subscribe(read_topic)
        # you can subsribe to as many topics as you'd like
        # client.subscribe('some/other/topic')


# this is the callback that gets called each time a message is recived
def on_message(cleint, userdata, msg):
        message = msg.payload.decode('UTF-8')
        print(f"topic: {msg.topic} msg: {message}")
        call(f"espeak -s125 '{message}'", shell=True)

client = mqtt.Client(str(uuid.uuid1()))
# configure network encryption etc
client.tls_set()
# this is the username and pw we have setup for the class
client.username_pw_set('idd', 'device@theFarm')

client.on_connect = on_connect
client.on_message = on_message

#connect to the broker
client.connect('farlab.infosci.cornell.edu',port=8883)

# food_list = {0:'milk',1:'orange'}

while True:
    if mpr121[0].value:
        val = "screwdriver"
        print(val)
        client.publish(send_topic, val)
    if mpr121[1].value:
        val = "wrench"
        print(val)
        client.publish(send_topic, val)
    if mpr121[2].value:
        val = "hex wrench"
        print(val)
        client.publish(send_topic, val)
    if mpr121[3].value:
        val = "protractor"
        print(val)
        client.publish(send_topic, val)
    if mpr121[4].value:
        val = "ruler"
        print(val)
        client.publish(send_topic, val)
    if mpr121[5].value:
        val = "pliers"
        print(val)
        client.publish(send_topic, val)

client.loop_forever()