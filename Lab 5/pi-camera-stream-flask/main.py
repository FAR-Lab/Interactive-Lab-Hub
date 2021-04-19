#Modified by smartbuilds.io
#Date: 27.09.20
#Desc: This web application serves a motion JPEG stream
# main.py
# import the necessary packages
from flask import Flask, render_template, Response, request
from camera import VideoCamera
import time
import threading
import os
from Qwiic_Joystick import qwiicjoystick

pi_camera = VideoCamera(flip=False) # flip pi camera if upside down.

# App Globals (do not edit)
app = Flask(__name__)

global n, m
n = 12
m = 0

@app.route('/')
def index():
    return render_template('index.html', numofface=n, numoflipstick=m)

# @app.route('/update_number')
# def update_number()
#     return render_template('index.html', numofface=n, numoflipstick=m)
        
def gen(camera):
    #get camera frame
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(pi_camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
    while True:
        direction = qwiicjoystick()
        if direction == "LEFT":
            n += 1
            render_template('index.html', numofface=n, numoflipstick=m)
        if direction == "RIGHT":
            m += 1
            render_template('index.html', numofface=n, numoflipstick=m)
    
    
    


