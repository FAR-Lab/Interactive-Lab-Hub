#pip install pygame
from pygame import mixer
import pygame
import time

mixer.init() #Initialzing pyamge mixer
mixer.music.load('victoria.wav') #Loading Music File
mixer.music.play() #Playing Music with Pygame

while True:
    print("test")
    time.sleep(0.5)



