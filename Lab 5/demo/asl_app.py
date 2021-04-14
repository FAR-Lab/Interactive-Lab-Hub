import eventlet
eventlet.monkey_patch()

from flask import Flask, Response,render_template
from flask_socketio import SocketIO, send, emit
from subprocess import Popen, call

import time
import board
import busio
import adafruit_mpu6050
import json
import socket

import signal
import sys
from queue import Queue

import numpy as np
from scipy.signal import find_peaks

import cv2
import tensorflow.keras

i2c = busio.I2C(board.SCL, board.SDA)
mpu = adafruit_mpu6050.MPU6050(i2c)

hostname = socket.gethostname()
hardware = 'plughw:2,0'

app = Flask(__name__)
socketio = SocketIO(app)

img = None
webCam = None
cap = cv2.VideoCapture()

np.set_printoptions(suppress=True)
model = tensorflow.keras.model.load_model("converted_keras/keras_model.h5")
labels = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ']

@socketio.on('connect')
def test_connect():
    print('connected')
    emit('after connect',  {'data':'Lets dance'})

@socketio.on('ping-gps')
def handle_message(val):
    global cap
    ret, img = cap.read()
    size = (224, 224)
    img = ImageOps.fit(img, size, Image. ANTIALIAS)

    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    data[0] = normalized_image_array

    prediction = model.predict(data)
    pred_ind = np.argmax(prediction)
    #print(prediction)

    emit('new_letter', {'letter': labels[pred_ind]})


@app.route('/')
def index():
    return render_template('index.html', hostname=hostname)

def signal_handler(sig, frame):
    print('Closing Gracefully')
    audio_stream.terminate()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)


if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=5000)


