from __future__ import print_function
import time
import board
import busio
import adafruit_mpr121
import musicalbeeps
import qwiic_button 
import sys



player = musicalbeeps.Player(volume = 0.3,
                            mute_output = False)

i2c = busio.I2C(board.SCL, board.SDA)
mpr121 = adafruit_mpr121.MPR121(i2c)


def run_example():

    #print("\nSparkFun Qwiic Button Example 1")
    my_button = qwiic_button.QwiicButton()

    if my_button.begin() == False:
        print("\nThe Qwiic Button isn't connected to the system. Please check your connection", \
            file=sys.stderr)
        return
    #print("\nButton ready!")
    index = 0
    while True:
        #I need to put the button code in here
        Octave = ["3","4","5","6"]
        
        
        if my_button.is_button_pressed() == True:
            print("\nThe button is pressed!")
            index = index+1
            if (index >4):
                index = 0
            print(index)
            time.sleep(1)
           
        # Loop through all 12 inputs (0-11).   
        for i in range(12):
            # Call is_touched and pass it then number of the input.  If it's touched
            # it will return True, otherwise it will return False.
            if mpr121[i].value:
                print("Input {} touched!".format(i))
                if("Input {} touched!".format(i) == "Input 0 touched!"):
                    player.play_note("C"+ Octave[index], 0.2)
                    print("C"+ Octave[index])
                if("Input {} touched!".format(i) == "Input 1 touched!"):
                    player.play_note("D"+ Octave[index], 0.2)
                    
                if("Input {} touched!".format(i) == "Input 2 touched!"):
                    player.play_note("E"+ Octave[index], 0.2)
                    
                if("Input {} touched!".format(i) == "Input 3 touched!"):
                    player.play_note("F"+ Octave[index], 0.2)
                    
                if("Input {} touched!".format(i) == "Input 4 touched!"):
                    player.play_note("G"+ Octave[index], 0.2)
                    
                if("Input {} touched!".format(i) == "Input 5 touched!"):
                    player.play_note("A"+ Octave[index], 0.2)
                    
                if("Input {} touched!".format(i) == "Input 6 touched!"):
                    player.play_note("B"+ Octave[index], 0.2)
                    
                if("Input {} touched!".format(i) == "Input 7 touched!"):
                    player.play_note("C"+ Octave[index+1], 0.2)
                
                
            time.sleep(0.02)
            
    #time.sleep(0.1)  # Small delay to keep from spamming output messages.


if __name__ == '__main__':
    try:
        run_example()
    except (KeyboardInterrupt, SystemExit) as exErr:
        print("\nEnding Example 1")
        sys.exit(0)