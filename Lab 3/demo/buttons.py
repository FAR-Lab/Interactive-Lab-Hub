import qwiic_i2c
import math
import qwiic_button 
import time
import sys

brightness = 100

def run_example():

    print("\nSparkFun Qwiic Button Example 7")
    my_button1 = qwiic_button.QwiicButton()
    my_button2 = qwiic_button.QwiicButton(0x5b)

    if my_button1.begin() == False:
        print("\nThe Qwiic Button 1 isn't connected to the system. Please check your connection", \
            file=sys.stderr)
        return
    if my_button2.begin() == False:
        print("\nThe Qwiic Button 2 isn't connected to the system. Please check your connection", \
            file=sys.stderr)
        return
    
    print("\nButton's ready!")

    while 1:

        # Check if button 1 is pressed
        if my_button1.is_button_pressed() == True:
            print("\nButton 1 is pressed!")
            my_button1.LED_on(brightness)
        
        else:
            my_button1.LED_off()
        
        # Check if button2 is pressed
        if my_button2.is_button_pressed() == True:
            print("\nButton 2 is pressed!")
            my_button2.LED_on(brightness)
        
        else:
            my_button2.LED_off()
        
        time.sleep(0.5)    # Don't hammer too hard on the I2C bus

if __name__ == '__main__':
    try:
        run_example()
    except (KeyboardInterrupt, SystemExit) as exErr:
        print("\nEnding Example 7")
        sys.exit(0)