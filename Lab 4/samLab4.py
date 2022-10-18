import musicalbeeps
import time
import board
import busio

import adafruit_mpr121

i2c = busio.I2C(board.SCL, board.SDA)

mpr121 = adafruit_mpr121.MPR121(i2c)

player = musicalbeeps.Player(volume = 1,
                            mute_output = False)

state = 0

while True:

#    button = qwiic_button.QwiicButton()

 #   if my_button.is_button_pressed() == True:
  #      print("\nThe button is pressed!")
   #     if (state % 2 == 0):
    #        espeak -ven+f2 -k5 -s150 --stdout  "Goodbye Macaully" | aplay
     #   else:
      #      espeak -ven+f2 -k5 -s150 --stdout  "Goodbye Macaully" | aplay
       # state += 1
        #time.sleep(1)
    for i in range(12):
        # Call is_touched and pass it then number of the input.  If it's touched
        # it will return True, otherwise it will return False.
        if mpr121[i].value:
            print("Input {} touched!".format(i))
            if("Input {} touched!".format(i) == "Input 0 touched!"):
                player.play_note("G", 0.2)
            if("Input {} touched!".format(i) == "Input 1 touched!"):
                player.play_note("Bb", 0.2)
            if("Input {} touched!".format(i) == "Input 4 touched!"):
                player.play_note("B", 0.2)
            if("Input {} touched!".format(i) == "Input 5 touched!"):
                player.play_note("C5", 0.2)
            if("Input {} touched!".format(i) == "Input 11 touched!"):
                player.play_note("G", 0.2)
            if("Input {} touched!".format(i) == "Input 10 touched!"):
                player.play_note("Bb", 0.2)
            if("Input {} touched!".format(i) == "Input 7 touched!"):
                player.play_note("B", 0.2)
            if("Input {} touched!".format(i) == "Input 6 touched!"):
                player.play_note("C5", 0.2)

# Examples:

# To play an A on default octave n°4 for 0.2 seconds
#player.play_note("A", 0.2)

# To play a G flat on octave n°3 for 1 seconds
#player.play_note("G3b", 1)

# To play a F sharp on octave n°5 for the default duration of 0.5 seconds
#player.play_note("F5#")

# To pause the player for 3.5 seconds
#player.play_note("pause", 3.5)