from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
import socket
import RPi.GPIO as GPIO
import time

port=5000

app = Flask(__name__)
socketio = SocketIO(app)

def broadcast(name, value):
	emit(name, value, broadcast=True, include_self=False)

@socketio.on('connect')
def test_connect():
	print('connected')
	emit('after connect',  {'data':'Lets dance'})

@socketio.on('message')
def handle_message(data):
    print('received message: ' + data)

@socketio.on('hex')
def handle_hex(val):
	broadcast('hex', val)

@socketio.on('audio')
def handle_audio(val): 
	broadcast('audio', val)

@socketio.on('pauseAudio')
def handle_pause(val):
	broadcast('pauseAudio', val)

# Couldn't seem to get this working
@socketio.on('clock')
def handle_clock():
	broadcast('clockTime', {'description': '2h 0m'})

@socketio.on('shake')
def handle_servo():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(12, GPIO.OUT)
	Servo = GPIO.PWM(12, 50)
	Servo.start(2.5)
	time.sleep(0.5)
	Servo.ChangeDutyCycle(2.7)
	time.sleep(0.5)
	Servo.ChangeDutyCycle(2.5)
	time.sleep(0.5)
	Servo.ChangeDutyCycle(2.7)
	time.sleep(0.5)
	Servo.ChangeDutyCycle(2.5)
	time.sleep(0.5)
	Servo.ChangeDutyCycle(2.7)
	time.sleep(0.5)
	Servo.ChangeDutyCycle(2.5)
	time.sleep(0.5)
	Servo.ChangeDutyCycle(2.7)
	time.sleep(0.5)
	Servo.ChangeDutyCycle(2.5)
	Servo.stop()


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
# 	The way of getting the ip address is dumb but works https://stackoverflow.com/questions/166506/finding-local-ip-addresses-using-pythons-stdlib
	print(f"access at http://100.64.6.64:{port}")
	socketio.run(app, host='0.0.0.0', debug=True, port=port)
