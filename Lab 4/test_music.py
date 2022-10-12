from pynput import keyboard

#pip install pygame
from pygame import mixer
import pygame
import time
mixer.init() #Initialzing pyamge mixer

mixer.music.load('umeda.mp3') #Loading Music File

mixer.music.play() #Playing Music with Pygame

paused = False    # global to track if the audio is paused

def on_press(key):
    global paused
    print (key)
    if key == keyboard.Key.space:
        if paused == True:     # time to play audio
            print ('play pressed')
            pygame.mixer.music.unpause()
            paused = False
            return False
        elif paused == False:   # time to pause audio
            print ('pause pressed')
            pygame.mixer.music.pause()
            paused = True
            return False
    return False

while True:
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
    time.sleep(0.1)

# mixer.music.stop()

