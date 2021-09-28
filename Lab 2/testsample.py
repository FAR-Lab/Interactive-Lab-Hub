import adafruit_mpu6050
import board
import time

i2c = board.I2C()
mpu = adafruit_mpu6050.MPU6050(i2c)

while True:
    print("Acceleration: X: %.2f, Y: %.2f, Z: %.2f m/s^2" % (mpu.acceleration))
    print("Gyro x: %.2f, Y: %.2f Z: %.2f rad/s" % (mpu.gyro))
    print("Temperature : %.2f C" % mpu.temperature)
    print("")
    time.sleep(0.1)