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

import board
import busio
import adafruit_mpu6050
import socket

import signal
import sys

cwd = os.getcwd()

i2c = busio.I2C(board.SCL, board.SDA)
mpu = adafruit_mpu6050.MPU6050(i2c)

detonate_flag = False
continue_flag = False


hostname = socket.gethostname()
hardware = 'plughw:2,0'

app = Flask(__name__)
socketio = SocketIO(app)
audio_stream = Popen("/usr/bin/cvlc alsa://"+hardware+" --sout='#transcode{vcodec=none,acodec=mp3,ab=256,channels=2,samplerate=44100,scodec=none}:http{mux=mp3,dst=:8080/}' --no-sout-all --sout-keep", shell=True)


@socketio.on('speak')
def handel_speak(val):
    bg.speak(val)

@socketio.on('connect')
def test_connect():
    print('connected')
    emit('after connect',  {'data':'Lets dance'})

@socketio.on('ping-gps')
def handle_message(val):
    # print(mpu.acceleration)
    emit('pong-gps', mpu.acceleration)


@socketio.on('name')
def respond_to_name(choice):
    if choice == 'accept':
        bg.speak('Name Accepted.')
        continue_flag = True
    else:
        bg.speak('That is not your name. Name Rejected. Detonating now')
        detonate_flag = True

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
    Servo, disp, disp_opts = bg.setup()

    # bomb Game Introduction
    image = Image.open(bg.IMG_PATH + 'bomb_homescreen.png')
    image = bg.image_formatting(image)
    disp.image(image, disp_opts[0])

    bg.clock_tick(Servo)

    bg.speak("Hello and welcome to the Bomb Game. I am a fake bomb. Diffuse me before the time runs out or die. You "
          "will have 5 minutes. Let's begin.")
    bg.speak("Do not touch me unless directed to. Breaking this rule will lead to detonation.")

    # Round 1: Answer some questions
    bg.speak("What is your name?")
    while not continue_flag:
        time.sleep(0.1)

    continue_flag = False

    bg.speak("What is your favorite color?")
    while not continue_flag:
        time.sleep(0.1)

    continue_flag = False

    # Round 2

    for i in range(10):
        bg.led_tick(bg.LED_PIN)


