from pynput import keyboard

#pip install pygame
from pygame import mixer
import pygame
import time
import board

# Configuration for proximity sensor
import busio
# import adafruit_apds9960.apds9960
# from adafruit_apds9960.apds9960 import APDS9960
# i2c = board.I2C()
# apds = APDS9960(i2c)
# apds.enable_proximity = True

# import qwiic_oled_display
# import sys

def runExample():
    #  These lines of code are all you need to initialize the OLED display and print text on the screen.
    print("\nSparkFun Qwiic OLED Display - Hello Example\n")
    myOLED = qwiic_oled_display.QwiicOledDisplay()
    if myOLED.is_connected() == False:
        print("The Qwiic OLED Display isn't connected to the system. Please check your connection", \
            file=sys.stderr)
        return
    
    #  Before you can start using the OLED, call begin() to init all of the pins and configure the OLED.
    myOLED.begin()
    myOLED.clear(myOLED.PAGE)  #  Clear the display's buffer
    myOLED.print("Umeda Cypher: Umeda Night Fever 19")  #  Add "Hello World" to buffer
    #  To actually draw anything on the display, you must call the display() function. 
    myOLED.display()

# runExample()

# pygame.mixer.pre_init(44100, 16, 2, 4096)
mixer.init() #Initialzing pyamge mixer

# DISPLAYSURF = pygame.display.set_mode((400, 300))
# pygame.display.set_caption("Sound!!")

# song_1 = pygame.mixer.Sound('sample_1a.mp3')
# s1 = pygame.mixer.Sound('s1.wav')
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
    return False

while True:
    s1.play()
    time.sleep(0.5)
    
# mixer.music.stop()

