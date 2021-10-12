import RPi.GPIO as GPIO
import time

# Setup GPIO for servo, 1) output, 2) power management.
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
servo = GPIO.PWM(11, 50) # At pin 11.
servo.start(0)

# Ask user for angle, and convert into Duty Cycle for servo.
try:
  while True:
    user_input = float(input('Enter angle between 0 and 180: '))
    angle = 2 + (user_input/18)
    servo.ChangeDutyCycle(angle)
    time.sleep(.5)
    servo.ChangeDutyCycle(0)
finally:
    servo.stop()
    GPIO.cleanup() 
    
