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

acc_history = list(np.zeros((10000,3)))
avg_history = list(np.zeros((10000,3)))

img = None
webCam = None
cap = cv2.VideoCapture()

np.set_printoptions(suppress=True)
model = tensorflow.keras.model.load_model("converted_keras/keras_model.h5")

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
    print(prediction)

    global acc_history
    global avg_history
    acc_history = acc_history[1:]
    acc_history += [list(mpu.acceleration)]
    avg_history = avg_history[1:]
    avg_history += [np.mean(acc_history[-10:], axis=0)]
    tmp = np.array(avg_history)
    x_peaks, _ = find_peaks(tmp[:,0])
    y_peaks, _ = find_peaks(tmp[:,1])
    z_peaks, _ = find_peaks(tmp[:,2])
    if x_peaks[-1] > 950 or y_peaks[-1] > 950 or z_peaks[-1] > 950:
        emit('peak-detected', {'data': 'PEAK!!!'})
    else:
        emit('peak-detected', {'data': ''})
    if sum(np.where(np.array(mpu.acceleration) > 10)) > 0:
        emit('thresh-passed', {'data': 'BOAT!!!'})
    else:
        emit('thresh-passed', {'data': ''})
    emit('pong-gps', tuple(np.mean(acc_history[-10:], axis=0))) 




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


