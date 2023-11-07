import cv2
import time
import numpy as np
import HandTrackingModule as htm
import math
from ctypes import cast, POINTER
import subprocess
import mouse
from adafruit_servokit import ServoKit
from multiprocessing import Process, shared_memory, Queue


#####
#servo setup
kit = ServoKit(channels=16)
servo_left = kit.servo[0]
servo_left.set_pulse_width_range(500, 2500)

servo_right = kit.servo[1]
servo_right.set_pulse_width_range(500, 2500)
#####



################################
wCam, hCam = 640, 480
wScreen, hScreen = 1276, 791
################################

global left_hit,right_hit
left_hit = 0
right_hit = 0

left_q = Queue()
right_q = Queue()

def cv_capture(left_q, right_q):
    cap = cv2.VideoCapture(0)
    cap.set(3, wCam)
    cap.set(4, hCam)
    pTime = 0
    detector = htm.handDetector(detectionCon=int(0.7))
    pre_left_len = 0
    pre_right_len = 0
    left_len = 0
    right_len = 0
    while True:
        success, img = cap.read()
        img = cv2.flip(img, 1)
        img = detector.findHands(img)
        lmList = detector.findPosition(img, draw=False)
        if len(lmList) != 0:
    
            thumbX, thumbY = lmList[4][1], lmList[4][2] #thumb
            pointerX, pointerY = lmList[8][1], lmList[8][2] #pointer
            middleX, middleY = lmList[12][1], lmList[12][2]
            ringX, ringY = lmList[16][1], lmList[16][2]
            pinkyX, pinkyY = lmList[20][1], lmList[20][2]
            baseX, baseY = lmList[0][1], lmList[0][2]


            len_calc = lambda x1,y1,x2,y2: math.hypot(x2 - x1, y2 - y1)
            pre_left_len = left_len
            pre_right_len = right_len
            left_len = len_calc(baseX,baseY,pointerX,pointerY)
            right_len = len_calc(baseX,baseY,middleX,middleY)
            #print(left_len,"##",right_len)
            global left_hit, right_hit
            threshhold_len = 200
            
            left_hit = 1 if left_len >threshhold_len and pre_left_len<=threshhold_len else 0
            right_hit  = 1 if right_len > threshhold_len and pre_right_len<=threshhold_len else 0
            #print(left_hit,"##",right_hit)
            #if left_hit == 1:
            left_q.put(left_hit)
            #if right_hit == 1:
            right_q.put(right_hit)

            #cx, cy = (thumbX + pointerX) // 2, (thumbY + pointerY) // 2

            #cv2.circle(img, (thumbX, thumbY), 15, (255, 0, 255), cv2.FILLED)
            #cv2.circle(img, (pointerX, pointerY), 15, (0, 255, 255), cv2.FILLED)
            #cv2.circle(img, (middleX, middleY), 15, (255, 0, 255), cv2.FILLED)
            #cv2.circle(img, (ringX, ringY), 15, (255, 0, 255), cv2.FILLED)
            #cv2.circle(img, (pinkyX, pinkyY), 15, (255, 0, 255), cv2.FILLED)
            #cv2.line(img, (baseX, baseY), (pointerX, pointerY), (255, 0, 255), 3)
            #cv2.line(img, (baseX, baseY), (middleX, middleY), (255, 0, 255), 3)
            #cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
            
            #conv_x = int(np.interp(pointerX, (0, wCam), (0, wScreen)))
            #conv_y = int(np.interp(pointerY, (0, hCam), (0, hScreen)))
            
            #mouse.move(conv_x, conv_y)
        #cTime = time.time()
        #fps = 1 / (cTime - pTime)
        #pTime = cTime
        #cv2.putText(img, f'FPS: {int(fps)}', (40, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)

        #cv2.imshow("Img", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()






def servo_action(left_q, right_q):
    while True:
        # Set the servo to 180 degree position
        #global left_hit, right_hit
        #print(left_q.get(),"SERVO",right_q.get())
        left_get = left_q.get()
        right_get = right_q.get()
        print(left_get,"##",right_get)
        if left_get == 1 and right_get == 1:
            print("both")
            servo_left.angle = 60
            servo_right.angle = 0
            time.sleep(0.2)
            servo_left.angle = 0
            servo_right.angle = 60
        elif left_get == 1: 
            print("left")
            servo_left.angle = 60
            time.sleep(0.2)
            servo_left.angle = 0
        elif right_get == 1: 
            print("right")
            servo_right.angle = 0
            time.sleep(0.2)
            servo_right.angle = 60
        else:
            pass

        #servo.angle = 180
        #time.sleep(2)
        # Set the servo to 0 degree position
        #servo.angle = 0
        #time.sleep(2)

process1 = Process(target=cv_capture, args=(left_q, right_q))
process2 = Process(target=servo_action,  args=(left_q, right_q))

process1.start()
process2.start()









