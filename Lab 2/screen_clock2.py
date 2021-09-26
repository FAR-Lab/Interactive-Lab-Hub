import time
import datetime
import subprocess
import digitalio
import board
import json
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789

# The display uses a communication protocol called SPI.
# SPI will not be covered in depth in this course. 
# you can read more https://www.circuitbasics.com/basics-of-the-spi-communication-protocol/
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None
BAUDRATE = 64000000  # the rate  the screen talks to the pi
# Create the ST7789 display:
display = st7789.ST7789(
    board.SPI(),
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

# these setup the code for our buttons and the backlight and tell the pi to treat the GPIO pins as digitalIO vs analogIO
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = display.width  # we swap height/width to rotate it to landscape!
width = display.height
image = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
display.image(image, rotation)
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
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True


_cal={}
no_events="No more events today."
_year=int(time.strftime("%y"))
_month=int(time.strftime("%m"))
_day=int(time.strftime("%d"))
print("Checkpoint 1")
with open("calendar.json") as f:
    _cal=json.load(f)
print("Checkpoint 2")
while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    _time=datetime.datetime.now()
    y=top
    print("Checkpoint 3")
   # while input_mode=0:
        #if buttonA.value and buttonB.value: #both buttons pressed
            #backlight.value = False  # turn off backlight
        #else if buttonB.value and not buttonA.value:  # just button B pressed
            #display.fill(screenColor) # set the screen to the users color
        #else if buttonA.value and not buttonB.value:  # just button A pressed
            # input_mode=1
            #display.fill(color565(255, 255, 255))  # set the screen to white
    if buttonA.value and buttonB.value:  # none pressed
        print("Checkpoint 4")
        draw.text((x,y),"Does this work",font=font,fill='#A033FF')
        current_event=""
        next_event=""
        # Determine which event is current and which event is next:
        for i in range(len(_cal)):
            _event=_cal[i]
            _start=datetime.datetime(_year,_month,_day,hour=_event["start_h"], minute=_event["start_m"])
            _end=datetime.datetime(_year,_month,_day,hour=_event["end_h"], minute=_event["end_m"])
            if next_event=="":
                if _time < _end: # if current time is before event's end time
                    if _time >= _start: # if current time is after event's start time
                        current_event=_event
                    if _time < _start:
                        next_event=_event
        # Draw text
        print("Checkpoint 5")
        if current_event !="":
            time_left= str((current_event["end_m"]+current_event["end_h"]*60)-(int(time.strftime("%M"))+60*int(time.strftime("%H"))))
            current_words=time_left+" minutes left in\n"+current_event["name"]
            draw.text((x,y),current_words,font=font,fill='#A033FF')
            y += 2*font.getsize(current_words)[1]
        if next_event!="":
            time_until= str((int(time.strftime("%M"))+60*int(time.strftime("%H")))-(next_event["end_m"]+next_event["end_h"]*60))
            next_words=time_until+" minutes left in\n"+next_event["name"]
            draw.text((x,y),next_words,font=font,fill='#A033FF')
        else:
            draw.text((x,y),no_events,font=font,fill='#A033FF')
    print("Checkpoint 6")
    display.image(image, rotation)
    time.sleep(1)              
                       
                       
                       
                       
                       
                       
