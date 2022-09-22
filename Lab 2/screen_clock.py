import time
import subprocess
import digitalio
import board
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
from time import  strftime, sleep
from datetime import datetime, timedelta
import busio
from i2c_button import I2C_Button
# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()
i2c = busio.I2C(board.SCL, board.SDA)

# scan the I2C bus for devices
while not i2c.try_lock():
    pass
devices = i2c.scan()
i2c.unlock()
print("I2C devices found:", [hex(n) for n in devices])
default_addr = 0x6F
if default_addr not in devices:
    print("warning: no device at the default button address", default_addr)

# Create the ST7789 display:
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

# initialize the button
button = I2C_Button(i2c)

# print some stuff
print("firmware version", button.version)
# print("interrupts", button.interrupts)
print("debounce ms", button.debounce_ms)

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)
def leaderboard() -> str:
    print_string = "Fastest lap time ever: \n"
    print(alltime_lap_times)
    best_time = timedelta(days =100)
    for i in range(len(alltime_lap_times)):
        time = alltime_lap_times[i]
        print(time)
        print(time.days)
        print(best_time.days)
        print(time.days)
        print(best_time.seconds)
        if  best_time.days > time.days :
            best_time = alltime_lap_times[i]
        elif ((best_time.days == time.days) and (time.seconds < best_time.seconds)):
            best_time = alltime_lap_times[i]
        elif ((best_time.days == time.days) and (time.seconds < best_time.seconds) and (time.microseconds > best_time.microseconds)):
            best_time = alltime_lap_times[i]
                    

    print(print_string+str(best_time.seconds)+"."+str(best_time.microseconds))
    return print_string+str(best_time)  

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width-10, height-10), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

# these setup the code for our buttons and tell the pi to treat the GPIO pins as digitalIO vs analogIO
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()



## GET CURRENT TIME

time_real = datetime.now()
time_str = time_real.strftime("%d %H:%M:%S")

## SET CURRENT LAP TIME
lap_time_start = time_real
lap_times = []
alltime_lap_times = []
lap_number = 0
pause = True
first_time = True

## draw to start
current_text = "Start time: " + time_str
y = top
draw.text((x,y),(current_text),font=font,fill="#FFFFFF")
y += font.getsize(time_str)[1]
    
# Display image.
disp.image(image, rotation)
past_laps = ""

button.led_bright = 0

while True:
    while( pause == True):
        if not buttonA.value and not buttonB.value:  # just button B pressed

            pause = not pause
            past_laps = ""
            draw.rectangle((0, 0, width-160, height-50), outline='white', fill=0)
            lap_times = []
            draw.text((x,y),"RESET",font=font,fill="#FFFFFF")
            disp.image(image, rotation)
            sleep(0.5)
            button.led_bright = 0
            sleep(0.5)
            button.led_bright = 255
            sleep(0.5)
            button.led_bright = 0
            sleep(0.5)
            button.led_bright = 255
            sleep(0.5)
            button.led_bright = 0
            first_time = True
            time_loop = datetime.now()

    time_loop = datetime.now()
    if(first_time):
        current_lap_time = (datetime.now()-datetime.now())
        time_loop = datetime.now()
        first_time = False
    else:
        current_lap_time = (time_loop-lap_time_start)

    print_str =  "Current lap:\n" + str((lap_number +1)) +": "  +str(current_lap_time)+ "\n"+ "Past laps:"+ "\n"+past_laps    

    if buttonB.value and not buttonA.value:  # just button A pressed
        ##lap_times = lap_times.append(str(current_lap_time))
        ## Increment the current lap
        past_laps = str((lap_number +1)) + ": " + str(current_lap_time)  +"\n" + past_laps 
        lap_number += 1
        lap_times.append(current_lap_time)
        alltime_lap_times.append(current_lap_time)
        print(lap_number)
        print(past_laps)
        lap_time_start = time_loop
        
        ## Print out line with that total lap time 
        ## Start a new line with the new time in between   
    
    if buttonA.value and not buttonB.value:  # just button B pressed - show leaderboard
        alltime_lap_times.append(current_lap_time)
        draw.rectangle((0, 0, width-20, height-10), outline='white', fill=0)
        draw.text((x,y),leaderboard(),font=font,fill="#FFFFFF")
        disp.image(image, rotation)
        sleep(3)

    if not buttonA.value and not buttonB.value:  # just button B pressed

        pause = not pause
        past_laps = ""
        lap_number = 0
        draw.rectangle((0, 0, width-160, height-50), outline='white', fill=0)   
        draw.text((x,y),"RESET",font=font,fill="#FFFFFF")
        disp.image(image, rotation)
        first_time = True
        sleep(0.5)
        time_loop = datetime.now()
        lap_times = []
        lap_time_start = time_loop
        button.led_bright = 0

    ## if not buttonA.value and not buttonB.value:  # none pressed
    ##    display.fill(color565(0, 255, 0))  # green
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    #TODO: Lab 2 part D work should be filled in here. You should be able to look in cli_clock.py and stats.py 
    y = top
    draw.text((x,y),print_str,font=font,fill="#FFFFFF")
    y += font.getsize(print_str)[1]
    
    # Display image.
    disp.image(image, rotation)
    button.led_bright = 0
    sleep(.05)

 



