import paho.mqtt.client as mqtt
import uuid
import ssl
import cv2 as cv
import time

# the # wildcard means we subscribe to all subtopics of IDD
topic = 'IDD/fsk/remote_camera'

# some other examples
# topic = 'IDD/a/fun/topic'

#this is the callback that gets called once we connect to the broker. 
#we should add our subscribe functions here as well
def on_connect(client, userdata, flags, rc):
	print(f"connected with result code {rc}")
	client.subscribe(topic)
	# you can subsribe to as many topics as you'd like
	# client.subscribe('some/other/topic')

MOST_RECENT_MSG = [None]

# this is the callback that gets called each time a message is recived
def on_message(cleint, userdata, msg):
	print(f"topic: {msg.topic} msg: {msg.payload.decode('UTF-8')}")
	MOST_RECENT_MSG[0] = msg.payload.decode('UTF-8')
	# you can filter by topics
	# if msg.topic == 'IDD/some/other/topic': do thing


# Every client needs a random ID
client = mqtt.Client(str(uuid.uuid1()))
# configure network encryption etc
client.tls_set(cert_reqs=ssl.CERT_NONE)
# this is the username and pw we have setup for the class
client.username_pw_set('idd', 'device@theFarm')

# attach out callbacks to the client
client.on_connect = on_connect
client.on_message = on_message

#connect to the broker
client.connect(
    'farlab.infosci.cornell.edu',
    port=8883)

# this is blocking. to see other ways of dealing with the loop
#  https://www.eclipse.org/paho/index.php?page=clients/python/docs/index.php#network-loop
# client.loop_forever()

# import numpy as np
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

client.loop_start()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    # image = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame
    # cv.imshow('frame', gray)

    timestr = time.strftime("%Y%m%d-%H%M%S")

    if MOST_RECENT_MSG[0] is not None:
        print(MOST_RECENT_MSG[-1])
    if MOST_RECENT_MSG[0] == 'take':
        cv.imwrite(timestr+'.png', frame)

    MOST_RECENT_MSG[0] = None
    
    if cv.waitKey(1) == ord('q'):
        break
# When everything done, release the capture

cap.release()
cv.destroyAllWindows()