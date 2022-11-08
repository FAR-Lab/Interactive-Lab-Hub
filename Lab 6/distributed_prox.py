import time
import board
from adafruit_apds9960.apds9960 import APDS9960

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

while True:
    client.publish(topic, apds.proximity)
    print(apds.proximity)
    time.sleep(0.2)