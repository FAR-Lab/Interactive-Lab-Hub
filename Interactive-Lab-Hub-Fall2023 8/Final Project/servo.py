import time
from adafruit_servokit import ServoKit

# Set channels to the number of servo channels on your kit.
# There are 16 channels on the PCA9685 chip.
kit = ServoKit(channels=16)

# Name and set up the servo according to the channel you are using.
servos = 2

# Set the pulse width range of your servo for PWM control of rotating 0-180 degree (min_pulse, max_pulse)
# Each servo might be different, you can normally find this information in the servo datasheet
for i in range(servos):
    kit.servo[i].set_pulse_width_range(500, 2500)

while True:
    try:
        for i in range(servos):
            # Set the servo to 180 degree position
            kit.servo[i].angle = 180
        time.sleep(0.5)
        for i in range(servos):
            # Set the servo to 0 degree position
            kit.servo[i].angle = 0
        time.sleep(0.5)
        
    except KeyboardInterrupt:
        # Once interrupted, set the servo back to 0 degree position
        servo.angle = 0
        time.sleep(0.5)
        break