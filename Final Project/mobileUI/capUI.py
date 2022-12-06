import time
import board
import os
import RPi.GPIO as GPIO
import pygame
import adafruit_mpr121
import busio
import json

i2c = busio.I2C(board.SCL, board.SDA)

mpr121 = adafruit_mpr121.MPR121(i2c)

# Triggers capacitive sensor and sends out data
def sensor_update_json(num):
    if mpr121[1].value:
        return (num, 1)
    elif mpr121[2].value:
        return (num, 2)
    elif mpr121[3].value:
        return (num, 3)
    elif mpr121[4].value:
        return (num, 4)
    elif mpr121[5].value:
        return (num, 5)
    else: return (num, num)


def main():
    cur_index = 0

    while True: 
        
        cur_index, triggered = sensor_update_json(cur_index)
        if cur_index != triggered:
            cur_index = triggered
            json_value = cur_index
            print(json_value)
            time.sleep(0.5)
            json_list = [{"layer":json_value}]
            json_string = json.dumps(json_list)
            json_file = open("data.json", "w")
            json_file.write(json_string)





if __name__ == "__main__":
    main()