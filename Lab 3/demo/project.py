import eventlet
eventlet.monkey_patch()

from flask import Flask, Response,render_template
from flask_socketio import SocketIO, send, emit
from subprocess import Popen, call

import time
import board
import busio
import adafruit_apds9960.apds9960
import adafruit_mpu6050
import json
import socket
import digitalio
import os

import signal
import sys
from queue import Queue
from adafruit_apds9960.apds9960 import APDS9960

i2c = busio.I2C(board.SCL, board.SDA)
mpu = adafruit_mpu6050.MPU6050(i2c)
int_pin = digitalio.DigitalInOut(board.D5)
apds = APDS9960(i2c, interrupt_pin=int_pin)

hostname = socket.gethostname()
hardware = 'plughw:2,0'

app = Flask(__name__)
socketio = SocketIO(app)
audio_stream = Popen("/usr/bin/cvlc alsa://"+hardware+" --sout='#transcode{vcodec=none,acodec=mp3,ab=256,channels=2,samplerate=44100,scodec=none}:http{mux=mp3,dst=:8080/}' --no-sout-all --sout-keep", shell=True)

apds.enable_proximity = True
apds.proximity_interrupt_threshold = (0, 175)
apds.enable_proximity_interrupt = True

def speak2me(val):
    call(f"espeak '{val}'", shell=True)
    
speak2me("Welcome to your navigation buddy, Please tell me where you would like to go")

def Speech2Text():
    wf = wave.open("recording.wav", "rb")
    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
        print ("Audio file must be WAV format mono PCM.")
        exit (1)

    model = Model("model")
    # You can also specify the possible word list
    rec = KaldiRecognizer(model, wf.getframerate(), "east west middle snow")

    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            print(rec.Result())
        else:
            print(rec.PartialResult())
    res = json.loads(rec.FinalResult())
    print ("Speech2Text: "+ res['text'])
    return res['text']

os.system('arecord -D hw:2,0 -f cd -c1 -r 48000 -d 10 -t wav recorded_mono.wav')
print("testing2")
#python3 test_words.py recorded_mono.wav
#print("testing3")

@socketio.on('speak')
def handel_speak(val):
    call(f"espeak '{val}'", shell=True)

@socketio.on('connect')
def test_connect():
    print('connected')
    emit('after connect',  {'data':'Lets dance'})

@socketio.on('ping-gps')
def handle_message(val):
    # print(mpu.acceleration)
    emit('pong-gps', mpu.acceleration) 
    
@app.route('/')
def index():
    return render_template('index.html', hostname=hostname)

while True:
    #print(apds.proximity)
    if apds.proximity > 150:
    #print(apds.proximity) #printing out the proximity of the sensor from 0-255 where 0 is nothing is near and 255 is its touching
        print ("You are too close!")
        speak2me("You are too close to an object")

def signal_handler(sig, frame):
    print('Closing Gracefully')
    audio_stream.terminate()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)


if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=5000)
    
