
#This example is directly copied from the Tensorflow examples provided from the Teachable Machine.
import random

import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import cv2
import time
import sys

winning_combo = {
    ('Rock', 'Lizard'),
    ('Lizard', 'Spock'),
    ('Spock', 'Scissor'),
    ('Scissor', 'Paper'),
    ('Paper', 'Rock'),
    ('Rock', 'Scissor'),
    ('Lizard', 'Paper'),
    ('Spock', 'Rock'),
    ('Scissor', 'Lizard'),
    ('Paper', 'Spock')
}

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


# Load the model
model = tensorflow.keras.models.load_model('keras_model.h5')
# Load Labels:
labels=[]
f = open("labels.txt", "r")
for line in f.readlines():
    if(len(line)<1):
        continue
    labels.append(line.split(' ')[1].strip())
computer_score = 0
user_score = 0

# has 3 modes, Start, play, and result
mode = 0
won = False
counter = 0
main_size = (720, 1080)
while True:
    if webCam:
        ret, img = cap.read()
    print("Img size: ", cap.get(cv2.CAP_PROP_FRAME_WIDTH), cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    font = cv2.FONT_HERSHEY_SIMPLEX

    # Play mode
    if mode == 0:
        img = cv2.imread('img/start.png')
    elif mode == 1:
        size = (224, 224)
        rows, cols, channels = img.shape
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        filter_img = cv2.resize(img, size, interpolation=cv2.INTER_AREA)
        counter = int(time.time() - start)
        print(counter)
        if counter < 4:
            cv2.putText(img, str(3 - counter), (360, 540), font, 10, (200, 255, 155), 5, cv2.LINE_AA)
        # cv2.putText(img, 'Computer', (25, 60), font, 1, (200, 255, 155), 2, cv2.LINE_AA)
        # cv2.putText(img, 'User', (200, 60), font, 1, (200, 255, 155), 2, cv2.LINE_AA)

        # turn the image into a numpy array
        image_array = np.asarray(filter_img)
        print(image_array.shape, image_array.size)
        # Normalize the image
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
        # Load the image into the array
        data[0] = normalized_image_array

        # run the inference
        prediction = model.predict(data)
        print("I think its a:", labels[np.argmax(prediction)])
        if counter > 3:
            computer_selections = random.choice(['Rock', 'Scissor', 'Lizard', 'Spock', 'Paper'])
            final_prediction = labels[np.argmax(prediction)]
            mode = 2
    elif mode == 2:
        print(final_prediction, computer_selections)
        if final_prediction == computer_selections:
            img = cv2.imread('img/tie.png')
            cv2.putText(img, f'You choose {final_prediction} and computer choose {computer_selections}', (50, 100),
                        font, 3, (0, 0, 0), 2, cv2.LINE_AA)
        if (final_prediction, computer_selections) in winning_combo:
            img = cv2.imread('img/you_won.png')
            cv2.putText(img, f'You choose {final_prediction} and computer choose {computer_selections}', (50, 100), font, 3, (0, 0, 0), 2, cv2.LINE_AA)
        else:
            img = cv2.imread('img/you_lost.png')
            cv2.putText(img, f'You choose {final_prediction} and computer choose {computer_selections}', (50, 100), font,
                        3, (255, 255, 255), 2, cv2.LINE_AA)

    cv2.imshow('detected (press q to quit)', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cap.release()
        exit()
    elif cv2.waitKey(1) & 0xFF == ord('s'):
        mode = 1
        start = time.time()
    elif cv2.waitKey(1) & 0xFF == ord('r'):
        mode = 0


exit()


cv2.imwrite('detected_out.jpg',img)
cv2.destroyAllWindows()
