import eventlet
eventlet.monkey_patch()

from flask import Flask, Response,render_template
from flask_socketio import SocketIO, send, emit
from subprocess import Popen, call

import time
import board
import busio
#import adafruit_mpu6050
from adafruit_msa3xx import MSA311
import json
import socket


import signal
import sys
from queue import Queue

app = Flask(__name__)


hostname = socket.gethostname()
hardware = 'plughw:2,0'

app = Flask(__name__)

socketio = SocketIO(app)
socketio.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#sock=socket(app)
#sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
audio_stream = Popen("/usr/bin/cvlc alsa://"+hardware+" --sout='#transcode{vcodec=none,acodec=mp3,ab=256,channels=2,samplerate=44100,scodec=none}:http{mux=mp3,dst=:8080/}' --no-sout-all --sout-keep", shell=True)

#@app.route('/')
#def index():
#    return 'Hello world'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


@socketio.on('speak')
def handel_speak(val):
    call(f"espeak '{val}'", shell=True)

@socketio.on('connect')
def test_connect():
    print('connected')
    emit('after connect',  {'data':'Lets dance'})


@app.route('/')
def index():
    return 'Hello world'

def signal_handler(sig, frame):
    print('Closing Gracefully')
    audio_stream.terminate()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)


if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=5000)