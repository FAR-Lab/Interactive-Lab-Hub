import RPi.GPIO as GPIO
import time

trigPin = 16
echoPin = 18
MAX_DISTANCE = 220          
timeOut = MAX_DISTANCE*60   

def pulseIn(pin,level,timeOut): 
    t0 = time.time()
    while(GPIO.input(pin) != level):
        if((time.time() - t0) > timeOut*0.000001):
            print("return 0 at whileloop 1")
            return 0;
    t0 = time.time()
    while(GPIO.input(pin) == level):
        if((time.time() - t0) > timeOut*0.000001):
            print("return 0 at whileloop 2")
            return 0;
    pulseTime = (time.time() - t0)*1000000
    print(pulseTime)
    return pulseTime
    
def getSonar():     
    GPIO.output(trigPin,GPIO.HIGH)       
    time.sleep(0.00001)
#    print("Current Mode: " + str(GPIO.getmode()))     
    GPIO.output(trigPin,GPIO.LOW)
    pingTime = pulseIn(echoPin,GPIO.HIGH,timeOut)
    print(pingTime) 
    distance = pingTime * 340.0 / 2.0 / 10000.0     
    return distance
    
def setup():
    print ('Program is starting...')
    mode = GPIO.getmode()
    if mode == GPIO.BCM:
        trigPin = 23
        echoPin = 24
    else:
        trigPin = 16
        echoPin = 18
        GPIO.setmode(GPIO.BOARD)       
    GPIO.setup(trigPin, GPIO.OUT)   
    GPIO.setup(echoPin, GPIO.IN)    

def loop():
    while(True):
        distance = getSonar()
        print ("The distance is : %.2f cm"%(distance))
        time.sleep(1)
        
if __name__ == '__main__':     
    setup()
    try:
        loop()
    except KeyboardInterrupt:  
        GPIO.cleanup()         


	
