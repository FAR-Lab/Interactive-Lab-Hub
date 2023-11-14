import time
import board
import busio
import adafruit_mpr121
import ssl

import paho.mqtt.client as mqtt
import uuid

import qwiic_keypad
import sys

client = mqtt.Client(str(uuid.uuid1()))
client.tls_set(cert_reqs=ssl.CERT_NONE)
client.username_pw_set('idd', 'device@theFarm')

client.connect(
    'farlab.infosci.cornell.edu',
    port=8883)

topic = 'IDD/fsk/keypad'

# i2c = busio.I2C(board.SCL, board.SDA)
# 
# mpr121 = adafruit_mpr121.MPR121(i2c)
# 
# while True:
#     for i in range(12):
#         if mpr121[i].value:
#         	val = f"Twizzler {i} touched!"
#         	print(val)
#         	client.publish(topic, val)
#     time.sleep(0.25)

def runExample():

	print("\nSparkFun qwiic Keypad   Example 1\n")
	myKeypad = qwiic_keypad.QwiicKeypad()

	if myKeypad.is_connected() == False:
		print("The Qwiic Keypad device isn't connected to the system. Please check your connection", \
			file=sys.stderr)
		return

	myKeypad.begin()

	button = 0
	while True:

		# necessary for keypad to pull button from stack to readable register
		myKeypad.update_fifo()
		button = myKeypad.get_button()

		if button == -1:
			print("No keypad detected")
			time.sleep(1)

		elif button != 0:

			# Get the character version of this char
			charButton = chr(button)
			if charButton == '#':
				print()
			elif charButton == '*':
				print(" ", end="")
			else:
				print(charButton, end="")

			# Flush the stdout buffer to give immediate user feedback
			client.publish(topic, charButton)
			sys.stdout.flush()

		time.sleep(.25)
		# Development in progress

runExample()
