# How to load a Tensorflow model using OpenCV
# Jean Vitor de Paulo Blog - https://jeanvitor.com/tensorflow-object-detecion-opencv/
# David edited some stuff

import numpy as np
import cv2
import sys
# Load a model imported from Tensorflow
tensorflowNet = cv2.dnn.readNetFromTensorflow('frozen_inference_graph.pb', 'ssd_mobilenet_v2_coco_2018_03_29.pbtxt')
classes = ['person','bicycle','car','motorbike','aeroplane','bus','train','truck','boat','traffic light','fire hydrant','stop sign','parking meter','bench','bird','cat','dog','horse','sheep','cow','elephant','bear','zebra','giraffe','backpack','umbrella','handbag','tie','suitcase','frisbee','skis','snowboard','sports ball','kite','baseball bat','baseball glove','skateboard','surfboard','tennis racket','bottle','wine glass','cup','fork','knife','spoon','bowl','banana','apple','sandwich','orange','broccoli','carrot','hot dog','pizza','donut','cake','chair','sofa','pottedplant','bed','diningtable','toilet','tv monitor','laptop','mouse','remote','keyboard','cell phone','microwave','oven','toaster','sink','refrigerator','book','clock','vase','scissors','teddy bear','hair drier','toothbrush']

personCount=0

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
      img = cv2.imread("../data/test.jpg")
      print("Using default image.")


while(True):
    if webCam:
        ret, img = cap.read()

    rows, cols, channels = img.shape

    # Use the given image as input, which needs to be blob(s).
    tensorflowNet.setInput(cv2.dnn.blobFromImage(img, size=(300, 300), swapRB=True, crop=False))

    # Runs a forward pass to compute the net output
    networkOutput = tensorflowNet.forward()
    FoundAPerson = False
    # Loop on the outputs
    for detection in networkOutput[0,0]:
        score = float(detection[2])
        if score > 0.2 and len(classes)>detection[1]:
            detectclass= classes[int(detection[1])-1]
            if 'person' in detectclass:
                FoundAPerson=True
            left = detection[3] * cols + 5000 
            top = detection[4] * rows + 2000
            right = detection[5] * cols + 2000
            bottom = detection[6] * rows + 5000

            #draw a red rectangle around detected objects
            cv2.rectangle(img, (int(left), int(top)), (int(right), int(bottom)), (0, 0, 255), thickness=2)
            cv2.putText(img,detectclass,(int(left),int(top)),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2,cv2.LINE_AA)
    if FoundAPerson:
        cv2.putText(img,"The Spot Is Currently Taken :(".format(personCount),(20,45),cv2.FONT_HERSHEY_COMPLEX,1,(36,29,245),3,cv2.LINE_AA)
    else:
        cv2.putText(img,"The Spot is Open! :)".format(personCount),(20,45),cv2.FONT_HERSHEY_COMPLEX,1,(91,245,44),3,cv2.LINE_AA)
    if webCam:
        if sys.argv[-1] == "noWindow":
           print("Finished a frame")
           cv2.imwrite('detected_out.jpg',img)
           continue
        cv2.imshow('detected (press q to quit)',img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            break
    else:
        break

cv2.imwrite('detected_out.jpg',img)
cv2.destroyAllWindows()


