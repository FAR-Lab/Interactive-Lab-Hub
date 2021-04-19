import eventlet
eventlet.monkey_patch()

from flask import Flask, Response,render_template, jsonify
from flask_socketio import SocketIO, send, emit
from subprocess import Popen, call
from threading import Thread
from gtts import gTTS
import os

import time
import board
import busio
import json
import socket

import signal
import sys
from queue import Queue

import numpy as np
from scipy.signal import find_peaks
from scipy import stats

import cv2
import tensorflow.keras
import tensorflow as tf

hostname = socket.gethostname()
hardware = 'plughw:2,0'

app = Flask(__name__)
socketio = SocketIO(app)

cap = cv2.VideoCapture(0)

np.set_printoptions(suppress=True)
model = tensorflow.keras.models.load_model("../models/sides_of_sam/keras_model.h5")
labels = ['Studious Sam',
          'Sporty Sam',
          'Incognito Sam',
          'Cool Sam',
          'Music Snob Sam']

studious_model = tensorflow.keras.models.load_model('../models/counting/keras_model.h5')
studious_labels = ['normal', 'counting']

sporty_model = tensorflow.keras.models.load_model('../models/play_ball/keras_model.h5')
sporty_labels = ['catch', 'throw']

incognito_model = tensorflow.keras.models.load_model('../models/incognito/keras_model.h5')
incognito_labels = ['normal', 'reveal']

cool_model = tensorflow.keras.models.load_model('../models/half_nod/keras_model.h5')
cool_labels = ['normal', 'nod']

music_model = tensorflow.keras.models.load_model('../models/dancing/keras_model.h5')
music_labels = ['normal', 'dancing']

sam_state = 'Studious Sam'

def load_frame():
    global cap
    ret, img = cap.read()
    size = (298, 224)
    img = cv2.resize(img, size)
    img = img[:, 37:-37]

    return img

def format_frame(img):
    image_array = np.asarray(img)
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    data[0] = normalized_image_array

    return data

@socketio.on('connect')
def test_connect():
    print('connected')
    emit('after connect',  {'data':'Lets dance'})

@socketio.on('ping-video')
def stream_video():
    img = load_frame()

    cv2.imwrite('static/tmp.jpg', img)
    emit('new_frame', {'data': ''})

def run_studious():
    handle_speak('You are looking awfully studious today, Sam. Let us see if you are studious after all. Count as quickly as you can for the next 5 seconds.')
    end = time.time() + 5
    while time.time() < end:
        img = load_frame()
        data = format_frame(img)

        prediction = studious_model.predict(data)
        pred_ind = np.argmax(prediction)

        prediction = studious_labels[pred_ind]
        if prediction == 'normal':
            handle_speak('You are not counting. Not so studious today after all')
    handle_speak('5 seconds is up. How much did you count?')
    time.sleep(2)
    handle_speak('That is not much. You will have to count faster next time.')

def run_sporty():
    handle_speak('You are looking sporty today, Sam. Let us play ball. Throw a ball in the air 5 times.')
    throw_count = 0
    catch_state = 'catch'
    while throw_count < 5:
        img = load_frame()
        data = format_frame(img)

        prediction = sporty_model.predict(data)
        pred_ind = np.argmax(prediction)

        prediction = sporty_labels[pred_ind]
        if prediction == 'catch' and catch_state == 'throw':
            catch_state = 'catch'
            throw_count += 1
            handle_speak(str(throw_count))
        elif prediction == 'throw' and catch_state == 'catch':
            catch_state = 'throw'
    handle_speak('Well done. I did not expect you to be able to do it. Miracles do happen.')

def run_incognito():
    handle_speak('Wait you are not Sam. Who are you?')
    incognito_state = 'normal'
    while incognito_state == 'normal':
        img = load_frame()
        data = format_frame(img)

        prediction = incognito_model.predict(data)
        pred_ind = np.argmax(prediction)

        prediction = incognito_labels[pred_ind]
        if prediction == 'reveal':
            handle_speak('You tricked me, Sam. What a convincing disguise.')
            incognito_state = 'reveal'

def run_cool():
    handle_speak('You look like you think you are cool, Sam. Let us put that to the test. How would a cool person greet another cool person?')
    cool_state = 'normal'
    while cool_state == 'normal':
        img = load_frame()
        data = format_frame(img)

        prediction = cool_model.predict(data)
        pred_ind = np.argmax(prediction)

        prediction = cool_labels[pred_ind]
        if prediction == 'nod':
            handle_speak('I am doing well, thank you. You have passed the cool test. I applaud your coolness.')
            cool_state = 'cool'

def run_music():
    handle_speak('You look like you are enjoying some music. Let us have a dance party.')
    end = time.time() + 5
    while time.time() < end:
        img = load_frame()
        data = format_frame(img)

        prediction = music_model.predict(data)
        pred_ind = np.argmax(prediction)

        prediction = music_labels[pred_ind]
        if prediction == 'normal':
            handle_speak('You are not dancing. That is very lame.')
    handle_speak('Your dancing is inferior.')

@socketio.on('check_state')
def check_sam_state():
    global sam_state
    handle_speak("Hi, Sam")
    if sam_state == 'Studious Sam':
        run_studious()
    elif sam_state == 'Sporty Sam':
        run_sporty()
    elif sam_state == 'Incognito Sam':
        run_incognito()
    elif sam_state == 'Cool Sam':
        run_cool()
    else:
        run_music()

@socketio.on('speak')
def handle_speak(m):
    filename = 'tmp.mp3'

    tts = gTTS(m, lang='en')
    tts.save(filename)
    os.system("/usr/bin/mplayer " + filename)

@socketio.on('ping-gps')
def handle_message(val):
    global sam_state
    pred_history = []
    for ind, i in enumerate(range(3)):
        img = load_frame()
        data = format_frame(img)

        prediction = model.predict(data)
        pred_ind = np.argmax(prediction)

        pred_history += [pred_ind]

    prediction = labels[stats.mode(pred_history)[0][0]]
    sam_state = prediction

    emit('new_letter', {'letter': prediction})


@app.route('/')
def index():
    return render_template('asl.html', hostname=hostname)

def signal_handler(sig, frame):
    print('Closing Gracefully')
    audio_stream.terminate()
    cv2.destroyAllWindows()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)


if __name__ == "__main__":
    socketio.run(app, host='100.64.4.253', port=8888)


