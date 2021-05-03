from os import system
import signal
import sys
import threading, queue
import paho.mqtt.client as mqtt
import re
import pyttsx3
import importlib

topic = "bbc/subtitles/bbc_news24/compacted"

q = queue.Queue()
running = True
def say(text):
    # Workaround because runAndWait() sometimes hangs on windows
    importlib.reload(pyttsx3)
    engine = pyttsx3.init()
    engine.say(text)
    print(str(text))
    engine.runAndWait()

def worker():
    sentence=" "
    while running:
        item = q.get()
        sentence += re.sub(r'[^A-Za-z0-9.,]+', '', item)+' '
        if '.' in sentence:
            say(sentence)
            sentence=""
        q.task_done()


threading.Thread(target=worker, daemon=True).start()


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(topic)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    if(running):
        for word in msg.payload.decode("utf-8").split(' '):
            q.put(word)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message



def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    running=False
    q.join()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

print("About to connect")
client.connect("mqtt.eclipseprojects.io", 1883, 60)
client.loop_forever()
