#the elderly's end

import paho.mqtt.client as mqtt
import uuid
from subprocess import call
from datetime import datetime


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




def check_time():
    now = datetime.now()
    current_time = now.strftime("%H")
    # print("Current Time =", current_time)
    attime = False
    if current_time == "04":
        attime = True

    return attime

def report():
    reported = True
    cmd_beg= 'espeak '
    cmd_end= ' | aplay /home/pi/Desktop/Text.wav  2>/dev/null' # To play back the stored .wav file and to dump the std errors to /dev/null
    cmd_out= '--stdout > /home/pi/Desktop/Text.wav ' # To store the voice file

    text = "today weather is"

    #Replacing ' ' with '_' to identify words in the text entered
    text = text.replace(' ', '_')

    #Calls the Espeak TTS Engine to read aloud a Text
    call([cmd_beg+cmd_out+text+cmd_end], shell=True)

reported = False

while True:

    if check_time() and not reported:
        report()
        reported = True
        val = "pressed"
        client.publish("IDD/checkin", val)

# while True:
# 	cmd = input('>> topic: IDD/')
# 	if ' ' in cmd:
# 		print('sorry white space is a no go for topics')
# 	else:
# 		topic = f"IDD/{cmd}"
# 		print(f"now writing to topic {topic}")
# 		print("type new-topic to swich topics")
# 		while True:
# 			val = input(">> message: ")
# 			if val =='new-topic':
# 				break
# 			else:
# 				client.publish(topic, val)
