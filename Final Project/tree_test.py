import time
from adafruit_servokit import ServoKit
from random import random, randrange

# Set channels to the number of servo channels on your kit.
# There are 16 channels on the PCA9685 chip.
kit = ServoKit(channels=16)

# Name and set up the servo according to the channel you are using.
servo = kit.servo[2]

# Set the pulse width range of your servo for PWM control of rotating 0-180 degree (min_pulse, max_pulse)
# Each servo might be different, you can normally find this information in the servo datasheet
servo.set_pulse_width_range(500, 2500)

y = 0.75

def treeWind():
# Set the servo to 180 degree position
    servo.angle = 0
    time.sleep(randrange(20,200)/100)
    for x in range (1,randrange(2,6)):
        servo.angle = randrange(30,40)*y
        time.sleep(0.2)
        servo.angle = randrange(20,30)*y
        time.sleep(0.1)
        print(x)
    # Set the servo to 0 degree position
    servo.angle = 5
    time.sleep(randrange(20,200)/100)
    servo.angle = 10
    time.sleep(randrange(20,200)/100)


while True:
    try:
        treeWind()
    except KeyboardInterrupt:
        # Once interrupted, set the servo back to 0 degree position
        servo.angle = 0
        time.sleep(0.5)
        break
