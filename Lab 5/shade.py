import numpy as np
import cv2
import sys
import time

cv2.namedWindow('Resized Window', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Resized Window', 540, 540)

img = None
webCam = False

def draw_label(img, text, pos, bg_color):
  font_face = cv2.FONT_HERSHEY_SIMPLEX
  scale = 0.4
  color = (0,0,0)
  thickness = cv2.FILLED
  margin = 2
  txt_size = cv2.getTextSize(text, font_face, scale, thickness)

  end_x = pos[0] + txt_size[0][0] + margin
  end_y = pos[1] - txt_size[0][1] - margin

  cv2.rectangle(img, pos, (end_x, end_y), bg_color, thickness)
  cv2.putText(img, text, pos, font_face, scale, color, 1, cv2.LINE_AA)

if(len(sys.argv)>1):
    try:
        print("I'll try to read your image")
        img = cv2.imread(sys.argv[1])
        if img is None:
            print("Failed to load image file:", sys.argv[1])
    except:
        print("Failed, make sure it is a path to an image")
else:
    try:
        print("Trying to open the Webcam.")
        cap = cv2.VideoCapture(0)
        if cap is None or not cap.isOpened():
            raise("No camera")
        webCam = True
    except:
        img = cv2.imread("../data/test.jpg")
        print("Using default image.")

while(True):
    if webCam:
        ret, img = cap.read()
    
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(imgray, (7,7), 0)
    ret, thresh = cv2.threshold(blurred,100,255,0)

    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    img_c = cv2.drawContours(img, contours, -1, (0,255,0), 3)
    masked = cv2.bitwise_and(img_c, img_c, mask=thresh)

    num_dark_px = sum(masked[masked < 110])
    num_total_px = masked.shape[0] * masked.shape[1]
    dark_area_pcnt = num_dark_px / num_total_px
    print(dark_area_pcnt)

    if webCam:
        # draw_label(masked, 'Hello', (20,20), (255,0,0))
        cv2.putText(masked, str(round(dark_area_pcnt, 1)), (200, 200), cv2.FONT_HERSHEY_SIMPLEX, 5, (0, 255, 255), 2, cv2.LINE_4)
        cv2.imshow('Resized Window', masked)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            break
    else:
        break

    time.sleep(1)

cv2.imwrite('contour_out.jpg', masked)
cv2.destroyAllWindows()

