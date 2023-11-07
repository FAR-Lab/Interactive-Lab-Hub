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
