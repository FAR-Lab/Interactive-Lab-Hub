import time
import datetime
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789

# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

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

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
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

    

_cal={}
no_events="No more events today."
with open(calendar.json) as f:
    _cal=json.load(f)
   
while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    _time=int(time.strftime("%M"))+60*int(time.strftime("%H"))
   # while input_mode=0:
        #if buttonA.value and buttonB.value: #both buttons pressed
            #backlight.value = False  # turn off backlight
        #else if buttonB.value and not buttonA.value:  # just button B pressed
            #display.fill(screenColor) # set the screen to the users color
        #else if buttonA.value and not buttonB.value:  # just button A pressed
            # input_mode=1
            #display.fill(color565(255, 255, 255))  # set the screen to white
    if not buttonA.value and not buttonB.value:  # none pressed
        current_event=""
        next_event=""
        # Determine which event is current and which event is next:
        for date in _cal:
            if date==datetime.today():
                for event in _cal[date]:
                    _event=_cal[date][event]
                    if _time < int(time.strftime(_event["end"],"%M"))+60*int(time.strftime(_event["end"],"%H")):                # if current time is before event's end time
                        if _time>= int(time.strftime(_event["start"],"%M"))+60*int(time.strftime(_event["start"],"%H")):        # if current time is after event's start time
                            current_event=_event
                        if _time < int(time.strftime(_event["start"],"%M"))+60*int(time.strftime(_event["start"],"%H")):        # if current time is before event's start time
                            next_event=_event
                    if next_event!="": break
         # Write out default text
         if current_event!="":
            current_time = str(int(time.strftime(_event["end"],"%M"))+60*int(time.strftime(_event["end"],"%H"))-_time)+" minutes left in\n"+current_event["name"]
            y=top
            draw.text((x,y),current_time,font=font,fill='#A033FF')
            y += 2*font.getsize(current_time)[1]
         if next_event!="":
            next_time = str(int(time.strftime(_event["start"],"%M"))+60*int(time.strftime(_event["start"],"%H"))-_time)+" minutes until\n"+next_event["name"]
            draw.text((x,y),next_time,font=font,fill='#A033FF')
         else if next_event=="":
            draw.text((x,y),no_events,font=font,fill='#A033FF')
    disp.image(image, rotation)
    time.sleep(1)    
                                                                                      
    
 """ 
 def new_event():
    print("Please enter your new calendar event below:")
    event_name=input("What is the name of the event?")
    if event_name='': return input_mode=0
    new_date=input("Enter a date (MM/DD/YYYY): ")
    if new_date='': return input_mode=0
    time_start=input("Enter a start time (HH:MM): ")
    if time_start='': return input_mode=0
    time_end=input("Enter an end time (HH:MM): ")
    if time_end='': return input_mode=0
   
 input_mode=0
 
    if input_mode=1:
 """
                       
                       
                       
                       
                       
                       
                       
