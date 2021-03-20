import eventlet
eventlet.monkey_patch()

import bomb_game as bg
from PIL import Image

import os
from flask import Flask,render_template
from flask_socketio import SocketIO, send, emit
from subprocess import Popen, call
import RPi.GPIO as GPIO
import time
from threading import Thread

import board
import busio
import adafruit_mpu6050
import socket

import signal
import sys

cwd = os.getcwd()

i2c = busio.I2C(board.SCL, board.SDA)
Servo, disp, disp_opts = bg.setup()

hostname = socket.gethostname()
hardware = 'plughw:2,0'

app = Flask(__name__)
socketio = SocketIO(app)
audio_stream = Popen("/usr/bin/cvlc alsa://"+hardware+" --sout='#transcode{vcodec=none,acodec=mp3,ab=256,channels=2,samplerate=44100,scodec=none}:http{mux=mp3,dst=:8080/}' --no-sout-all --sout-keep", shell=True)


@socketio.on('speak')
def handel_speak(val):
    bg.speak(val)

@socketio.on('start')
def start_game(continue_flag):
    continue_flag = False

    # bomb Game Introduction
    image = Image.open(bg.IMG_PATH + 'bomb_homescreen.png')
    image = bg.image_formatting(image)
    disp.image(image, disp_opts[0])

    Thread(target=bg.clock_tick(Servo)).start()

    bg.speak("Hello and welcome to the Bomb Game. I am a fake bomb. Diffuse me before the time runs out or die. You "
             "will have 5 minutes. Let's begin.")
    bg.speak("Do not touch me unless directed to. Breaking this rule will lead to detonation.")

    # Round 1: Answer some questions
    bg.speak("Round 1: Answer some initial questions so I know who I am talking to")
    bg.speak("Question 1: What is your name?")

@socketio.on('name')
def respond_to_name(choice):
    if choice == 'accept':
        bg.speak('Name Accepted.')
    else:
        bg.speak('That is not your name. Name Rejected. Detonating now')
        bg.detonate()

@app.route('/')
def index():
    return render_template('index.html', hostname=hostname)

def signal_handler(sig, frame):
    print('Closing Gracefully')
    audio_stream.terminate()
    GPIO.cleanup()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)


if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=5000)


