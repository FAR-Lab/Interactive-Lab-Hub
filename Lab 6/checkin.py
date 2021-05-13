#the elderly's end

import paho.mqtt.client as mqtt
import uuid
from subprocess import call
from datetime import datetime
import qwiic_button
import time
import pygame

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


p_button = qwiic_button.QwiicButton()
if p_button.is_connected():
    print("answer button detected!")

pygame.mixer.init()
pygame.mixer.music.load("./weather.wav")

reported = False
answered = False

def check_time():
    now = datetime.now()
    current_time = now.strftime("%H")
    # print("Current Time =", current_time)
    attime = False
    if current_time == "04":
        attime = True

    return attime

# reset reported detail at 12 everyday
def reset_time():
    now = datetime.now()
    current_time = now.strftime("%H")
    # print("Current Time =", current_time)
    attime = False
    if current_time == "12":
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

    timer = time.time()



while True:
    # if recieve button pressed, send to MQTT
    if p_button.is_button_pressed():
        answered = True
        val = "answered"
        client.publish("IDD/checkin", val)

    # reset every midnight
    if reset_time():
        answered = False
        reported = False

    #check if it is 9am
    if check_time() and not reported:
        # report()
        reported = True
        print("time to report")

        if pygame.mixer.music.get_busy() == True:
            print('playing music')
            continue
        else:
            pygame.mixer.music.play(1)
            print("start to play music")
