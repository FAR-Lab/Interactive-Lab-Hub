from pynput import keyboard

#pip install pygame
from pygame import mixer
import pygame
import time
import board

import busio

mixer.init() #Initialzing pyamge mixer

mixer.music.load('umeda.wav') #Loading Music File

mixer.music.play() #Playing Music with Pygame



