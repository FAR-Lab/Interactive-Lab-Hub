#pip install pygame
import pygame
from pygame import mixer

mixer.init() #Initialzing pyamge mixer
mixer.music.load('umeda.wav') #Loading Music File
mixer.music.play() #Playing Music with Pygame

while True:
    mixer.music.play()



