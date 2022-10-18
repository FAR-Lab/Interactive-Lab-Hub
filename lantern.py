import qwiic
import time
import qwiic_led_stick
import sys
import vlc


print("VL53L1X Qwiic Test\n")
ToF = qwiic.QwiicVL53L1X()
if (ToF.sensor_init() == None):					 # Begin returns 0 on a good init
	print("Sensor online!\n")

my_stick = qwiic_led_stick.QwiicLEDStick()
if my_stick.begin() == False:
    print("\nThe Qwiic LED Stick isn't connected to the sytsem. Please check your connection", file=sys.stderr)

my_stick.set_all_LED_brightness(15)
print("\nLED Stick ready!")
    
def do_led():
        my_stick.set_all_LED_color(255, 87, 51)
        p = vlc.MediaPlayer("laugh.mp3")
        p.play()
        
        time.sleep(5)
        
        # Turn off all LEDs
        my_stick.LED_off()
        time.sleep(1)
        p.stop()
    
while True:
    try:
        #print('hello world')
        ToF.start_ranging()
        time.sleep(.05)
        distance = ToF.get_distance()
        time.sleep(.05)
        ToF.stop_ranging()
        fe = (distance / 25.4)/ 12.0
        if fe < 3.0:
            do_led()
        
        
    except Exception as e:
        print(e)
	
    
