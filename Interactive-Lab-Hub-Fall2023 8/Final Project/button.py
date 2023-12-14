from __future__ import print_function
import qwiic_button
import time
import sys

def run_example():

    print("\nSparkFun Qwiic Button Example 1")
    my_button = qwiic_button.QwiicButton()
    my_button2 = qwiic_button.QwiicButton(address=0x6e)
    if my_button.begin() == False:
        print("\nThe Qwiic Button isn't connected to the system. Please check your connection", \
            file=sys.stderr)
        return
    if my_button2.begin() == False:
       print("\nButton 2 is not connected")
       return
    print("\nButton ready!")
   
    while True:   
        
       if my_button.is_button_pressed() == True:
            print("\nThe button is pressed!")

       #  else:    
       #      print("\nThe button is not pressed!")
       if my_button2.is_button_pressed():
            print("\nThe button 2 is pressed!")
       #  else:
       #      print("\nThe button 2 is not pressed!") 
    
       time.sleep(0.02)

if __name__ == '__main__':
    try:
        run_example()
    except (KeyboardInterrupt, SystemExit) as exErr:
        print("\nEnding Example 1")
        sys.exit(0)