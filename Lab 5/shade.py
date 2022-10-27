import numpy as np
import cv2
import sys

cv2.namedWindow('Resized Window', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Resized Window', 540, 540)

img = None
webCam = False

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

    if webCam:
        cv2.imshow('Resized Window', masked)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            break
        else:
            break

cv2.imwrite('contour_out.jpg', masked)
cv2.destroyAllWindows()