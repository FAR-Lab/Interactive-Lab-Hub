
#This example is directly copied from the Tensorflow examples provided from the Teachable Machine.

import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import cv2
import sys
import time
import qwiic_button 
from statistics import mode
import subprocess
import shlex

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

img = None
webCam = False
if(len(sys.argv)>1 and not sys.argv[-1]== "noWindow"):
   try:
      print("I'll try to read your image");
      img = cv2.imread(sys.argv[1])
      if img is None:
         print("Failed to load image file:", sys.argv[1])
   except:
      print("Failed to load the image are you sure that:", sys.argv[1],"is a path to an image?")
else:
   try:
      print("Trying to open the Webcam.")
      cap = cv2.VideoCapture(0)
      if cap is None or not cap.isOpened():
         raise("No camera")
      webCam = True
   except:
      print("Unable to access webcam.")

my_button1 = qwiic_button.QwiicButton()
my_button2 = qwiic_button.QwiicButton(0x5b)

if my_button1.begin() == False:
    print("\nThe Qwiic Button 1 isn't connected to the system. Please check your connection", \
            file=sys.stderr)
if my_button2.begin() == False:
    print("\nThe Qwiic Button 2 isn't connected to the system. Please check your connection", \
            file=sys.stderr)
# Load the model
model = tensorflow.keras.models.load_model('./sign_lang3/keras_model.h5')
# Load Labels:
labels=[]
f = open("./sign_lang3/labels.txt", "r")
for line in f.readlines():
    if(len(line)<1):
        continue
    labels.append(line.split(' ')[1].strip())

predictions = []
while(True):
    curr_predict = []
    while True:
        if my_button1.is_button_pressed() == True:
            if webCam:
                ret, img = cap.read()

            rows, cols, channels = img.shape
            data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

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
            curr_predict.append(np.argmax(prediction))
                
            if webCam:
                if sys.argv[-1] == "noWindow":
                   cv2.imwrite('detected_out.jpg',img)
                   continue
                cv2.imshow('detected (press q to quit)',img)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    cap.release()
                    print('double condition true, breaking')
                    break
            else:
                print('webcam not here, breaking')
                break
        if my_button2.is_button_pressed() == True:
            my_button2.LED_on(10)
            print('captured letter, breaking')
            time.sleep(0.5)
            break
    if curr_predict:
        predictions.append(labels[mode(curr_predict)])
    if len(predictions) >= 14:
        print('reached sentence length, breaking')
        break
sentence = ''
for letter in predictions:
    if letter == 'Background':
        sentence+= ' '
    else:
        sentence += letter
print(sentence)
subprocess.call(['sh', './tts.sh', sentence])
cv2.imwrite('detected_out.jpg',img)
cv2.destroyAllWindows()

