<<<<<<< HEAD
import qwiic_button
import pygame
import sys
import time

def play_sound(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    time.sleep(0.5) 

def main():
    button = qwiic_button.QwiicButton()
    if button.begin() == False:
        print("The Qwiic Button isn't connected to the system. Please check your connection", \
            file=sys.stderr)
        return
    
    print("Press the button to play the sound!")

    while True:
        if button.is_button_pressed():
            print("Button Pressed!")
            play_sound("gunshot.wav")
            time.sleep(1)  

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        pass
=======
import time
import qwiic_button

button = qwiic_button.QwiicButton()

while True:
    # Check if the button is pressed and tell us if it is!
    if button.is_button_pressed():
        print("The button is pressed!")
        while button.is_button_pressed():
            time.sleep(1)  # Wait for the user to stop pressing
    time.sleep(0.02)  # Don't hammer too hard on the I2C bus
>>>>>>> 9da52b82651b8398438900b0b78bae99c5f8c30a
