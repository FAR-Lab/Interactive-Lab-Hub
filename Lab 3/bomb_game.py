import
import time
import RPi.GPIO as GPIO

LED_PIN = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

MOTOR_PIN = 12
GPIO.setup(MOTOR_PIN, GPIO.OUT)
Servo = GPIO.PWM(MOTOR_PIN, 50)

def led_tick(LED_PIN):
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(1)

def clock_tick(Servo):
    Servo.start(2.5)
    for i in range(0, 90, 3):
        Servo.ChangeDutyCycle(i / 18 + 2)
        time.sleep(0.5)
        Servo.ChangeDutyCycle(0)
        time.sleep(0.1)
    Servo.stop()

for i in range(10):
    led_tick(LED_PIN)
    clock_tick(Servo)

GPIO.cleanup()
