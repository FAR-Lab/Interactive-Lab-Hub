import cv2
import time
import HandTrackingModule as htm
import math
import pygame
import board
import busio
from adafruit_seesaw import seesaw, rotaryio
import adafruit_seesaw.digitalio
import digitalio
from PIL import Image, ImageDraw, ImageFont #, ImageSequence
import adafruit_mpr121
import adafruit_rgb_display.st7789 as st7789
import qwiic_button  # sudo pip install sparkfun-qwiic-button
import os

TOPIC = "IDD/playList"
N_GENRE = 4
N_SONG = 3
N_BACKGROUNDS = 4

################################
wCam, hCam = 640, 480
################################

pygame.init()

# init twizzler
i2c = busio.I2C(board.SCL, board.SDA)
mpr121 = adafruit_mpr121.MPR121(i2c)

# init volButton
seesaw = seesaw.Seesaw(board.I2C(), addr=0x36)
seesaw_product = (seesaw.get_version() >> 16) & 0xFFFF
print("Found product {}".format(seesaw_product))
if seesaw_product != 4991:
    print("Wrong firmware loaded?  Expected 4991")
seesaw.pin_mode(24, seesaw.INPUT_PULLUP)
volButton = adafruit_seesaw.digitalio.DigitalIO(seesaw, 24)
button_held = False
encoder = rotaryio.IncrementalEncoder(seesaw)
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

# init qwicc button
qwiicButton = qwiic_button.QwiicButton()
if qwiicButton.begin() == False:
    print(
        "The Qwiic Button isn't connected to the system. Please check your connection"
    )
print("Qwicc Button ready!")

################################
# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
# image = Image.new("RGB", (width, height))
rotation = 90

################################

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0

detector = htm.handDetector(detectionCon=int(0.7))
# minVol = 0
# maxVol = 100
vol = 0
volBar = 213
volPer = 75

conditions = {
            (True, False, False, False): "play/pause", #1
            (True, False, True, True): "play/pause", #1
            (True, False, False, True): "play/pause", #1
            (True, False, True, False): "play/pause", #1
            (True, True, False, False): "next", #2
            (True, True, True, False): "prev" #3
            }

genres = ["pop", "r&b", "kpop","dance"]

playList = {
            "pop": ["Justin Bieber - Peaches ft. Daniel Caesar, Giveon", 
                    "Kehlani - Gangsta (Audio)", 
                    "Rihanna - Umbrella (Lyrics) ft. JAY-Z"],
            "r&b": ["H.E.R - Come Through ft. Chris Brown (Lyrics)", 
                    "John Mayer - New Light (Lyrics)", 
                    "Sasha Sloan - Dancing With Your Ghost (Lyrics)"],
            "kpop": ["ENHYPEN - Sweet Venom", 
                     "IVE - LOVE DIVE", 
                     "NewJeans - Ditto"],
            "dance": ["Sam Smith - Unholy (Lyrics) ft. Kim Petras", 
                      "SZA - Snooze-_Audio_", 
                      "Tyla Water - Official Audio"]
            }

backgrounds =  [Image.open("backgrounds/Light.png").resize((width,height)), 
                Image.open("backgrounds/Mountain.png").resize((width,height)), 
                Image.open("backgrounds/Retro.png").resize((width,height)), 
                Image.open("backgrounds/Sunset.png").resize((width,height))
                ]

curGenre = curSongNumber = curBackground = 0
paused = False
playing = False
lastVolPosition = -encoder.position
initsongtime = -1

################################

def playSong(genre, song_number):
    global playing, paused, initsongtime
    pygame.mixer.music.load(f"songGenre/{genres[genre]}/{playList[genres[genre]][song_number]}.wav")
    pygame.mixer.music.play()
    initsongtime = pygame.mixer.music.get_pos()
    playing = True
    paused = False

def pauseSong():
    global paused
    pygame.mixer.music.pause()
    print("Music Paused")
    paused = not paused
    

def unpauseSong():
    global paused
    pygame.mixer.music.unpause()
    print("Music Unpaused")
    paused = not paused

def stopSong():
    global playing
    pygame.mixer.music.stop()
    print("Music Stopped")
    playing = False
    

def setVolume(vol):
    global volBar
    global volPer
    curVol = pygame.mixer.music.get_volume()
    curVol += (vol / 100)
    if curVol < 0:
        curVol = 0
    if curVol > 1:
        curVol = 1
    pygame.mixer.music.set_volume(curVol)        
    os.system(f"amixer sset 'Master' {curVol * 100}%")
    print(f"Current volume: {curVol * 100}%")
    volBar = 400 - (curVol * 250)
    volPer = curVol * 100

def nextSong():
    global curSongNumber
    curSongNumber += 1
    curSongNumber %= N_SONG
    stopSong()
    playSong(curGenre, curSongNumber)
    print("Next Song")
     
def prevSong():
    global curSongNumber
    curSongNumber -= 1
    curSongNumber %= N_SONG
    stopSong()
    playSong(curGenre, curSongNumber)
    print("Prev Song")
     
def detectAction(action):
    global paused, playing
    if action == "play/pause":
        if not playing:
           playSong(curGenre, curSongNumber)
        elif not paused:
            pauseSong()
        else:
            unpauseSong()

    elif action == "next":
        nextSong()
    elif action == "prev":
        prevSong()


def checkBackground():
    global curBackground
    if qwiicButton.is_button_pressed():
       curBackground += 1
       curBackground %= N_BACKGROUNDS
       print("Background changed")
    
def checkGenre():
    global curGenre, curSongNumber
    try:
        for i in range(N_GENRE):
            if mpr121[i].value:
                if i != curGenre: 
                    curGenre = i
                    curSongNumber = 0
                    print(f"Changed to {genres[i]} genre")
                    playSong(curGenre, curSongNumber)
                else:
                    print(f"Already playing {genres[i]} genre") 
                break
    except IOError as e:
        return

def checkVolume():
    global lastVolPosition
    # if buttonB.value and not buttonA.value:
    #     setVolume(10)
    # if buttonA.value and not buttonB.value:
    #     setVolume(-10)
    # global button_held
    # if not volButton.value and not button_held:
    #     button_held = True
    # if volButton.value and button_held:
    #     button_held = False
    #     print(lastVolPosition, position)
    #     lastVolPosition = position
    #     setVolume(10)
    try:
        position = -encoder.position
        if position >= 100 or lastVolPosition >= 100: # handle seesaw sudden very large position
            return
        if position != lastVolPosition:
            adjust_vol = (position - lastVolPosition) * 5
            setVolume(adjust_vol)
            # print(lastVolPosition, position)
            lastVolPosition = position                
    except IOError as e:
        return

################################
frame_cnt = 0
start_time = time.time()
pygame.mixer.music.set_volume(0.75)
vol_change = 0
font = ImageFont.truetype("font/SundayGrapes.ttf", size=20)
time_font = ImageFont.truetype("font/SundayGrapes.ttf", size=38)
while True:
    checkGenre()
    checkBackground()
    checkVolume()

    display_image = backgrounds[curBackground].copy()
    draw_on_image = ImageDraw.Draw(display_image)
    split_song_name = playList[genres[curGenre]][curSongNumber].split(' - ')
    
    draw_on_image.text((10, 10), split_song_name[0], fill="#fff", font=font)  # might need to assign font
    draw_on_image.text((10, 30), split_song_name[1], fill="#fff", font=font)  # might need to assign font
    played_millis = pygame.mixer.music.get_pos()-initsongtime // 1000
    seconds = int((played_millis / 1000) % 60)
    minutes = int((played_millis / (1000 * 60)) % 60)
    draw_on_image.text((55, 62), '{:02d}:{:02d}'.format(minutes, seconds), fill="#fff", font=time_font)  # might need to assign font 
    success, img = cap.read()
    if frame_cnt % 2 == 0:
        img = detector.findHands(img)
        lmList = detector.findPosition(img, draw=False)
        end_time = time.time()
        
        if len(lmList) != 0:
    
            thumbX, thumbY = lmList[4][1], lmList[4][2] #thumb
            pointerX, pointerY = lmList[8][1], lmList[8][2] #pointer

            middleX, middleY = lmList[12][1], lmList[12][2]
            ringX, ringY = lmList[16][1], lmList[16][2]
            pinkyX, pinkyY = lmList[20][1], lmList[20][2]
            
            # cx, cy = (thumbX + pointerX) // 2, (thumbY + pointerY) // 2   
            # cv2.circle(img, (thumbX, thumbY), 15, (255, 0, 255), cv2.FILLED)
            # cv2.circle(img, (pointerX, pointerY), 15, (255, 0, 255), cv2.FILLED)
            # cv2.circle(img, (middleX, middleY), 15, (255, 0, 255), cv2.FILLED)
            # cv2.circle(img, (ringX, ringY), 15, (255, 0, 255), cv2.FILLED)
            # cv2.circle(img, (pinkyX, pinkyY), 15, (255, 0, 255), cv2.FILLED)
            # cv2.line(img, (thumbX, thumbY), (pointerX, pointerY), (255, 0, 255), 3)
            # cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

            len_calc = lambda x1,y1,x2,y2: math.hypot(x2 - x1, y2 - y1)
            length = len_calc(thumbX, thumbY, pointerX, pointerY)
            length1 = len_calc(thumbX, thumbY, middleX, middleY)
            length2 = len_calc(thumbX, thumbY, ringX, ringY)
            length3 = len_calc(thumbX, thumbY, pinkyX, pinkyY)
            base = min([length, length1, length2, length3]) * 2
            key = (length>base, length1>base, length2>base, length3>base)
            # One operation within per 3 seconds
            if end_time - start_time > 3:
                # print(key)
                if key in conditions:
                    detectAction(conditions[key])
                start_time = time.time()

            # if length < 50:
            #     cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED)
        cv2.rectangle(img, (50, 150), (85, 400), (255, 0, 0), 3)
        cv2.rectangle(img, (50, int(volBar)), (85, 400), (255, 0, 0), cv2.FILLED)
        cv2.putText(img, f'{int(volPer)} %', (40, 450), cv2.FONT_HERSHEY_COMPLEX,
                    1, (255, 0, 0), 3)
        
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, f'current playing: {playList[genres[curGenre]][curSongNumber]}', (40, 50), cv2.FONT_HERSHEY_COMPLEX,
                    1, (255, 0, 0), 3)

        cv2.imshow("Img", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit
            break
        
    # Display image
    disp.image(display_image, rotation)
    frame_cnt += 1
cap.release()
cv2.destroyAllWindows()
