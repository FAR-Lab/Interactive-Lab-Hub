import time
import board
import busio
import paho.mqtt.client as mqtt
import uuid

import adafruit_mpr121

i2c = busio.I2C(board.SCL, board.SDA)

mpr121 = adafruit_mpr121.MPR121(i2c)

# Every client needs a random ID
client = mqtt.Client(str(uuid.uuid1()))
# configure network encryption etc
client.tls_set()
# this is the username and pw we have setup for the class
client.username_pw_set('idd', 'device@theFarm')

#connect to the broker
client.connect(
    'farlab.infosci.cornell.edu',
    port=8883)


def main():
    topic = "IDD/package"
    
    prev_pack = 0
    total_pack = 0
    set_num = [6,8,10]
    while True:
        for num in set_num:
            if mpr121[num].value:
                prev_pack = total_pack
                total_pack += 1
                print(total_pack)
                time.sleep(0.5)
                if total_pack == 3:
                    text = str(total_pack) + " Packages Detected. Pick up your package!"
                    print(text)
                    client.publish(topic, text)
                    prev_pack = total_pack
                    total_pack = 0
                else: 
                    text = str(total_pack) + " Package(s) detected"
                    print(text)
                    client.publish(topic, text)
        
        
          # Small delay to keep from spamming output messages.


if __name__ == "__main__":
    main()