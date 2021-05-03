import paho.mqtt.client as mqtt
import uuid
import smbus, time
import sys
import os

# Every client needs a random ID
client = mqtt.Client(str(uuid.uuid1()))
# configure network encryption etc
client.tls_set()
# this is the username and pw we have setup for the class
client.username_pw_set('idd', 'device@theFarm')

#connect to the broker
client.connect(
    'farlab.infosci.cornell.edu',
    port=8883)

radio_text = """I have a slight fear we  got so excited about this season  that the next one we could get so  anticipatory fit and then were
going to get let down. For me, Im  sorry if you havent seen the last  episode because we are spoiling it  for you, but the last one was a bit  
of a damp squid. At least they  didnt go ridiculous, but I was  like, oh, is that it But the  problem is that we know that H and I is not great 
and we know that people allowed him to be  promoted to that level so we know  there are senior people. There were  too many obections to the idea of
systemic option for me. Follow the  money. Yeah, exactly."""

radio_list = radio_text.split()

def qwiicjoystick():
	global bus_data,X,Y,mode
	try:
		bus_data = bus.read_i2c_block_data(addr, 0x03, 5)
	except Exception as e:
		print(e)
	X = (bus_data[0]<<8 | bus_data[1])>>6
	Y = (bus_data[2]<<8 | bus_data[3])>>6
	selected = bus_data[4]
	return selected

bus = smbus.SMBus(1)
addr = 0x20
radio_flag = 0
while True:
	topic = f"IDD/mmmradio"
	if not qwiicjoystick():
		print("Button Pressed.")
		radio_flag ^= 1
		if radio_flag:
			print("Radio broadcast started.")
			
	while radio_flag:
		for val in radio_list:
			client.publish(topic, val)
			if not qwiicjoystick():
				radio_flag ^= 1
				print("Radio broadcast ended.")
