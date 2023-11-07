import qwiic_keypad
import time
import sys

def runExample():
    myKeypad = qwiic_keypad.QwiicKeypad(0x4b)

    if myKeypad.is_connected() == False:
        print("The Qwiic Keypad device isn't connected to the system. Please check your connection", file=sys.stderr)
        return

    myKeypad.begin()

    button = 0
    while True:

        # necessary for keypad to pull button from stack to readable register
        myKeypad.update_fifo()
        button = myKeypad.get_button()

        if button == -1:
            print("No keypad detected")
            time.sleep(1)

        elif button != 0:

            # Get the character version of this char
            charButton = chr(button)
            if charButton == '#':
                print()
            elif charButton == '*':
                print(" ", end="")
            else: 
                print(charButton, end="")

            # Flush the stdout buffer to give immediate user feedback
            sys.stdout.flush()

        time.sleep(.25) 
runExample()





