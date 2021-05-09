#This example is directly copied from the Tensorflow examples provided from the Teachable Machine.

import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import cv2
import sys

import digitalio
import board

from adafruit_rgb_display.rgb import color565
import adafruit_rgb_display.st7789 as st7789
import webcolors

import pygame
import os
from time import strftime, sleep


# ----------------
# enable button on adafruit adafruit_rgb_display
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None
BAUDRATE = 64000000  # the rate  the screen talks to the pi
# Create the ST7789 display:
display = st7789.ST7789(
    board.SPI(),
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)
height = disp.width
width = disp.height

# these setup the code for our buttons and the backlight and tell the pi to treat the GPIO pins as digitalIO vs analogIO
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()
# Disable scientific notation for clarity
np.set_printoptions(suppress=True)
display.fill(color565(0, 255, 0))

# -----------------
# Load camera
img = None
camera = False

try:
    print("Trying to open the Webcam.")
    cap = cv2.VideoCapture(0) #capture through camera
    if cap is None or not cap.isOpened():
        raise("No camera")
    camera = True
except:
    print("no camera found, use default image")
    img = cv2.imread('/home/pi/openCV-examples/data/test.jpg')


# Load the model
model = tensorflow.keras.models.load_model('keras_model.h5')

labels=[]
f = open("labels.txt", "r")
for line in f.readlines():
    if(len(line)<1):
        continue
    labels.append(line.split(' ')[1].strip())


def detectKnot():
    if camera:
        ret, img = cap.read()

    rows, cols, channels = img.shape
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # image = Image.open('/home/pi/openCV-examples/data/test.jpg')
    size = (224, 224)
    img =  cv2.resize(img, size, interpolation = cv2.INTER_AREA)
    #turn the image into a numpy array
    image_array = np.asarray(img)

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)
    print("I think its a:",labels[np.argmax(prediction)])
    cv2.imwrite('detected_out.jpg',img)


    #display image on screen -------------
    image = Image.open("detected_out.jpg")
    # Scale the image to the smaller screen dimension
    image_ratio = image.width / image.height
    screen_ratio = width / height
    if screen_ratio < image_ratio:
        scaled_width = image.width * height // image.height
        scaled_height = height
    else:
        scaled_width = width
        scaled_height = image.height * width // image.width
    image = image.resize((scaled_width, scaled_height), Image.BICUBIC)

    # Crop and center the image
    x = scaled_width // 2 - width // 2
    y = scaled_height // 2 - height // 2
    image = image.crop((x, y, x + width, y + height))

    # Display image.

    # curTime = strftime("%H:%M:%S")
    draw = ImageDraw.Draw(image)
    disp.image(image, 90)



print("press up button to start detection")
while(True):

    if buttonB.value and not buttonA.value:  # just button A pressed
        print("start detecting knot")
        detectKnot()
        print("press button again if need another detection")

    if buttonA.value and not buttonB.value:  # just button B pressed
        cap.release() #quit
        break



# while(True):
#
#     if camera:
#         if sys.argv[-1] == "noWindow":
#            cv2.imwrite('detected_out.jpg',img)
#            continue
#         cv2.imshow('detected (press q to quit)',img)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             cap.release()
#             break
#     else:
#         break
