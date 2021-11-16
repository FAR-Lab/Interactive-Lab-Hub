import time
import board
import busio
#import adafruit_mpr121

import paho.mqtt.client as mqtt
import uuid

import qwiic_button
import time

my_button1 = qwiic_button.QwiicButton()
my_button2 = qwiic_button.QwiicButton(0x5b)

if my_button1.begin() == False:
    print("\nThe Qwiic Button 1 isn't connected to the system. Please check your connection")
if my_button2.begin() == False:
    print("\nThe Qwiic Button 1 isn't connected to the system. Please check your connection")

client = mqtt.Client(str(uuid.uuid1()))
client.tls_set()
client.username_pw_set('idd', 'device@theFarm')

client.connect(
    'farlab.infosci.cornell.edu',
    port=8883)

def on_connect(client, userdata, flags, rc):
    print(f"connected with result code {rc}")
    client.subscribe('IDD/syw/cap')


# this is the callback that gets called each time a message is recived
def on_message(client, userdata, msg):
    print(f"topic: {msg.topic} msg: {msg.payload.decode('UTF-8')}")
    # you can filter by topics
    if any(char.isdigit() for char in msg.payload.decode('UTF-8')):
        if '0' in msg.payload.decode('UTF-8'):
            my_button2.LED_on(10)
        else: 
            my_button1.LED_on(10)
    

# attach out callbacks to the client
client.on_connect = on_connect
client.on_message = on_message

i2c = busio.I2C(board.SCL, board.SDA)

#mpr121 = adafruit_mpr121.MPR121(i2c)
count = on_message
while True:
    client.loop()
    if my_button1.is_button_pressed() == True:
        print('Responded to patient request')
        client.publish('IDD/syw/cap', 'request cleared')
        my_button1.LED_off()
    # Check if button 1 is pressed
    if my_button2.is_button_pressed() == True:
        print('Responded to patient SOS')
        my_button2.LED_off()
        client.publish('IDD/syw/cap', 'request cleared')
    time.sleep(0.5)    # Don't hammer too hard on the I2C bus