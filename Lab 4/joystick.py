from __future__ import print_function
import qwiic_joystick
import time
import sys

def runExample():
    print("\nSparkFun qwiic Joystick Example 1\n")
    myJoystick = qwiic_joystick.QwiicJoystick()

    if myJoystick.connected == False:
        print("The Qwiic Joystick device isn't connected to the system. Please check your connection", \
            file=sys.stderr)
        return

    myJoystick.begin()

    print("Initialized. Firmware Version: %s" % myJoystick.version)
    
    pull = False
    while True:
        if myJoystick.vertical < 10:
            print("pulled")
            pull = True
        else:
            pull = False
        print("X: %d, Y: %d, Button: %d" % ( \
                myJoystick.horizontal, \
                myJoystick.vertical, \
                myJoystick.button))

if __name__ == '__main__':
    try:
        runExample()
    except (KeyboardInterrupt, SystemExit) as exErr:
        print("\nEnding Example 1")
        sys.exit(0)
