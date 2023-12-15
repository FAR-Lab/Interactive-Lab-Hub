import time
import qwiic_vl53l1x
import subprocess

def main():
    mySensor = qwiic_vl53l1x.QwiicVL53L1X()
        
    mySensor.sensor_init()
    print(mySensor.address)
    while True:
        try:
            mySensor.start_ranging() # Write configuration bytes to initiate measurement
            time.sleep(.005)
            distance = mySensor.get_distance()         # Get the result of the measurement from the sensor
            time.sleep(.005)
            mySensor.stop_ranging()
            print("Distance(mm): %s" % distance)
            if (distance < 500):
                subprocess.call(['python', 'puzzle_prompting.py'])
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()
