import RPi.GPIO as GPIO
import signal
import time
import board
import busio
from subprocess import Popen, call
import digitalio



import paho.mqtt.client as mqtt
import uuid

cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# these setup the code for our buttons and the backlight and tell the pi to treat the GPIO pins as digitalIO vs analogIO
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

i2c = busio.I2C(board.SCL, board.SDA)

send_topic = 'IDD/foodserv/button'
read_topic = 'IDD/foodserv/food'


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
client.connect(
    'farlab.infosci.cornell.edu',
    port=8883)

# client.loop_forever()

while True:
        client.loop()
        if buttonA.value:
                buttonSts = 'Do not touch my food'
                client.publish(send_topic, buttonSts)
                # call(f"espeak -s125 '{buttonSts}'", shell=True)
        if buttonB.value:
                buttonSts = 'Go ahead and enjoy it'
                client.publish(send_topic, buttonSts)
                # call(f"espeak -s125 '{buttonSts}'", shell=True)