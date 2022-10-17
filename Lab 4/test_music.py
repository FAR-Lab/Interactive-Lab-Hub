from pynput import keyboard

#pip install pygame
from pygame import mixer
import pygame
import time
import board

# Configuration for proximity sensor
import busio
import adafruit_apds9960.apds9960
from adafruit_apds9960.apds9960 import APDS9960
i2c = board.I2C()
apds = APDS9960(i2c)
apds.enable_proximity = True

# pygame.mixer.pre_init(44100, 16, 2, 4096)
mixer.init() #Initialzing pyamge mixer

# DISPLAYSURF = pygame.display.set_mode((400, 300))
# pygame.display.set_caption("Sound!!")

# song_1 = pygame.mixer.Sound('sample_1a.mp3')
s1 = pygame.mixer.Sound('s1.wav')
#s2 = pygame.mixer.Sound('s2.mp3')
#s3 = pygame.mixer.Sound('s3.mp3')
#s4 = pygame.mixer.Sound('s4.mp3')
#s5 = pygame.mixer.Sound('s5.mp3')
#s6 = pygame.mixer.Sound('s6.mp3')
#s7 = pygame.mixer.Sound('s7.mp3')
#s8 = pygame.mixer.Sound('s8.mp3')

mixer.music.load('umeda.wav') #Loading Music File

mixer.music.play() #Playing Music with Pygame

paused = False    # global to track if the audio is paused

def on_press(key):
    global paused
    print (key)
    if key == keyboard.Key.space:
        if paused == True:     # time to play audio
            print ('play pressed')
            pygame.mixer.music.unpause()
            # song_1.stop()
            paused = False
            return False
        elif paused == False:   # time to pause audio
            print ('pause pressed')
            pygame.mixer.music.pause()
            # song_1.play(0)
            paused = True
            return False
    elif key.char == 'z':
        s1.play(0)
    elif key.char == 'x':
        s2.play(0)
    elif key.char == 'c':
        s3.play(0)
    elif key.char == 'v':
        s4.play(0)
    elif key.char == 'b':
        s5.play(0)
    elif key.char == 'n':
        s6.play(0)
    elif key.char == 'm':
        s7.play(0)
    elif key.char == ',':
        s8.play(0)
    return False

while True:
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
        if apds.proximity > 0:
            s1.play(0)
            print("sensor")
    time.sleep(0.1)
    
# mixer.music.stop()

