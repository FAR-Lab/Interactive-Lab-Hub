from __future__ import print_function
import qwiic_joystick
import time
import sys
from subprocess import Popen, call

def speak2me(val):
    call(f"espeak '{val}'", shell=True)

def swing():

    print("Swing Your Club")
    myJoystick = qwiic_joystick.QwiicJoystick()
    myJoystick.begin()

   
    while True:
        
        if myJoystick.get_vertical() <= 205:
            speak2me("Your ball is in the right rough")
        if ((myJoystick.get_vertical() > 205) and (myJoystick.get_vertical() <= 409)):
            speak2me("Your ball is in the right side of the fairway")
        if ((myJoystick.get_vertical() > 409) and (myJoystick.get_vertical() <= 500)):
            speak2me("Your ball is in the middle of the fairway")
        if ((myJoystick.get_vertical() > 505) and (myJoystick.get_vertical() <= 614)):
            speak2me("Your ball is in the middle of the fairway")
        if ((myJoystick.get_vertical() > 614) and (myJoystick.get_vertical() <= 818)):
            speak2me("Your Ball is in the left side of the fairway")
        if myJoystick.get_vertical() > 818:
            speak2me("Your ball is in the left rough")
        else:
            pass

        print("X: %d, Y: %d, Button: %d" % ( \
                    myJoystick.get_horizontal(), \
                    myJoystick.get_vertical(), \
                    myJoystick.get_button()))

        time.sleep(.5)

if __name__ == '__main__':
    try:
        swing()
    except (KeyboardInterrupt, SystemExit) as exErr:
        print("Ending Swing Tracker")
        sys.exit(0)