import eventlet
eventlet.monkey_patch()

import bomb_game as bg

import os
from flask import Flask,render_template
from flask_socketio import SocketIO
from subprocess import Popen
import RPi.GPIO as GPIO
from threading import Thread
import socket
import signal
import sys

cwd = os.getcwd()

hostname = socket.gethostname()
hardware = 'plughw:2,0'

app = Flask(__name__)
socketio = SocketIO(app)
audio_stream = Popen("/usr/bin/cvlc alsa://"+hardware+" --sout='#transcode{vcodec=none,acodec=mp3,ab=256,channels=2,samplerate=44100,scodec=none}:http{mux=mp3,dst=:8080/}' --no-sout-all --sout-keep", shell=True)


@socketio.on('speak')
def handel_speak(val):
    bg.speak(val)

@socketio.on('start')
def start_game():
    Thread(target=bg.clock_tick).start()

    bg.speak("Hello and welcome to the Bomb Game. I am a fake bomb. Diffuse me before the time runs out or die. You "
             "will have 5 minutes. Let's begin.")

    # Round 1: Answer some questions
    bg.speak("Round 1: Answer some initial questions so I know who I am talking to")
    bg.speak("Question 1: What is your name?")

@socketio.on('detonate')
def detonate():
    bg.detonate()

@socketio.on('name')
def respond_to_name(choice):
    if choice == 'accept':
        bg.speak('Name Accepted.')

        # Round 1 continues
        bg.speak("Question 2: What is your favorite color?")
    else:
        bg.speak('That is not your name. Name rejected.')
        bg.detonate()

@socketio.on('color')
def respond_to_color(choice):
    if choice == 'accept':
        bg.speak('Color Accepted.')
        bg.speak("You have passed Round 1.")
        bg.speak("Round 2: Answer the following riddle.")
        bg.speak("What has to be broken before you can use it?")
        #egg
    else:
        bg.speak("How do you not know your favorite color? Color rejected.")
        bg.detonate()

@socketio.on('riddle1')
def riddle1(choice):
    if choice == 'accept':
        bg.speak('Answer correct.')
        bg.speak("You have passed Round 2")
        bg.speak("Round 3: In order to access my controls, you must first unlock the system. To unlock the system, you will need to solve a series of math questions. Once you know the answer, say the number aloud and turn the turn dial on The Lock that many times.")
        bg.speak("Question 1: Turn the lock clockwise this many times. 2 times 2 plus 3")
        bg.show_image('q1.png')
        is_passed = bg.math_question(1)
        if is_passed:
            bg.speak('Correct. Question 2: Turn the lock counter-clockwise this many times. 6 modulus 3 plus 2')
            bg.show_image('q2.png')
            is_passed = bg.math_question(2)
            if is_passed:
                bg.speak(
                    'Correct. Question 3: Turn the lock clockwise this many times. 10 times 2 plus 4 all divided by 8')
                bg.show_image('q3.png')
                is_passed = bg.math_question(3)
                if is_passed:
                    bg.speak(
                        'Correct. Question 4: Turn the lock counter-clockwise this many times. 6 times 6 divided by 3 minus 7')
                    bg.show_image('q4.png')
                    is_passed = bg.math_question(4)
                    if is_passed:
                        bg.speak('Answer correct.')
                        bg.speak("You have passed Round 3")
                        bg.speak("Round 4: Answer the following riddle")
                        bg.speak("I’m tall when I’m young, and I’m short when I’m old. What am I?")
                        # candle
                    else:
                        bg.speak('That is incorrect.')
                        bg.detonate()
                else:
                    bg.speak('That is incorrect. This is just algebra, buddy.')
                    bg.detonate()
            else:
                bg.speak('That is incorrect. This is just algebra, buddy.')
                bg.detonate()
        else:
            bg.speak('That is incorrect. This is just algebra, buddy.')
            bg.detonate()
    else:
        bg.speak('That is incorrect. And that was the easy one...awkward')
        bg.detonate()

@socketio.on('riddle2')
def riddle2(choice):
    if choice == 'accept':
        bg.speak('Correct.')
        bg.speak('You have passed Round 4')
        bg.speak('Round 5: Follow the arrows to decode the system. When an arrow appears on the screen, push the joystick in that direction.')
        is_passed = bg.arrow_question()
        if is_passed:
            bg.speak('You have correctly decoded the system and passed Round 5.')
            bg.speak('Round 6: Answer the following riddle.')
            bg.speak('What is full of holes but still holds water?')
            # sponge
        else:
            bg.speak('You were unsuccessful at decoding the system.')
            bg.detonate()
    else:
        bg.speak('Incorrect.')
        bg.detonate()

@socketio.on('riddle3')
def riddle3(choice):
    if choice == 'accept':
        bg.speak("That is correct. You have passed Round 6")
        bg.speak("Round 7: Bring me objects of a certain color and show them to my eye")
        bg.speak("Object 1: Show me a red object")
        is_passed = bg.show_and_tell('red')
        if is_passed:
            bg.speak("Well done. Object 2: Show me a blue object")
            is_passed = bg.show_and_tell('blue')
            if is_passed:
                bg.speak("Well done. Object 3: Show me a green object")
                is_passed = bg.show_and_tell('green')
                if is_passed:
                    bg.speak('You have passed round 6')
                    bg.speak(
                        "Time is almosst up. Cut the red wire near the blinking red light to diffuse. Detonation will occur in 10 seconds")
                    is_passed = bg.cut_wire()
                    if is_passed:
                        bg.speak('Detonation averted. Thank you for playing.')
                        print('Closing Gracefully')
                        audio_stream.terminate()
                        GPIO.cleanup()
                        sys.exit(0)
                    else:
                        bg.speak('You cut the wrong wire')
                        bg.detonate()
                else:
                    bg.speak('You have failed')
                    bg.detonate()
            else:
                bg.speak('Incorrect')
                bg.detonate()
        else:
            bg.speak('Incorrect')
            bg.detonate()
    else:
        bg.speak('That is incorrect.')
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


