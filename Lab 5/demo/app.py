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

i2c = busio.I2C(board.SCL, board.SDA)
mpu = adafruit_mpu6050.MPU6050(i2c)

hostname = socket.gethostname()
hardware = 'plughw:2,0'

app = Flask(__name__)
socketio = SocketIO(app)

acc_history = list(np.zeros((10000,3)))
avg_history = list(np.zeros((10000,3)))

np.set_printoptions(suppress=True)
model = tensorflow.keras.models.load_model("../models/converted_keras/keras_model.h5")
labels = list(pd.read_csv('../models/converted_keras/labels.txt', header=None)[0])
labels = [x.split(' ')[1] for x in labels]
labels[-1] = ' '

@socketio.on('connect')
def test_connect():
    print('connected')
    emit('after connect',  {'data':'Lets dance'})

@socketio.on('ping-gps')
def handle_message(val):
    global acc_history
    global avg_history
    acc_history = acc_history[1:]
    acc_history += [list(mpu.acceleration)]
    avg_history = avg_history[1:]
    avg_history += [np.mean(acc_history[-10:], axis=0)]
    tmp = np.array(avg_history)
    x_peaks, _ = find_peaks(tmp[:,0], prominence=0.1, distance=5)
    y_peaks, _ = find_peaks(tmp[:,1], prominence=0.1, distance=5)
    z_peaks, _ = find_peaks(tmp[:,2], prominence=0.1, distance=5)
    x_peaks = list(np.zeros(10)) + list(x_peaks)
    y_peaks = list(np.zeros(10)) + list(y_peaks)
    z_peaks = list(np.zeros(10)) + list(z_peaks)
    if x_peaks[-1] > 9997 or y_peaks[-1] > 9997 or z_peaks[-1] > 9997:
        emit('peak-detected', {'data': 'peak-detected'})
    else:
        emit('peak-detected', {'data': ''})
    if sum(np.where(np.array(mpu.acceleration) > 10)) > 0:
        emit('thresh-passed', {'data': 'thresh-passed'})
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


