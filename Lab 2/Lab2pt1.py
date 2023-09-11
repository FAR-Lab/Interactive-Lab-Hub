import time
from time import strftime, sleep
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

#Configure Buttons:
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

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

buttonA_lastState = False

Hprev = 0
Mprev = 0
Sprev = 0


while True:
    
    draw.rectangle((0, 0, width, height), outline = 0, fill = 0)
    
    # Getting the values of time
    theTime = datetime.datetime.now()
    hour = theTime.hour
    minute = theTime.minute
    second = theTime.second
    
    if buttonB.value == 0 and buttonA.value == 1:
        draw.rectangle((0, 0, width, height), outline=0, fill="#FF0000")
        dateTime = strftime("%H:%M:%S")
        y = 10
        x = 85
        draw.text((x,y), dateTime, font=font, fill="#FFFFFF")
        
        #For debugging
        #print("red")
    
    
    if buttonA.value == 0 and buttonB.value == 1:
        draw.rectangle((0, 0, width, height), outline=0, fill="#FFFFFF")
        dateTime = strftime("%H:%M:%S")
        y = 10
        x = 85
        draw.text((x,y), dateTime, font=font, fill="#000000")
        
        #For debugging
        #print("white")
    
    else:
        dateTime = strftime("%H:%M:%S")
        #print(buttonA.value)
        y = 10
        x = 85
        draw.text((x,y), dateTime, font=font, fill="#FFFFFF")
    
    if  buttonA.value + buttonB.value == 0:
        draw.rectangle((0, 0, width, height), outline=0, fill="#add8e6")
        dateTime = strftime("%H:%M:%S")
        y = 10
        x = 85
        draw.text((x,y), dateTime, font=font, fill="#FFFFFF")
        
        #For debugging
        #print("blue")
        


        
    #----------------------------------------------------------
    #Fixed parameters
    fixedWidth = 20

    #----------------------------------------------------------
    #This section is for the top bar that represents the hours
    
    
    Hy1 = 40
    Hy2 = Hy1 + fixedWidth
    HtoDay = 24
    Hcolor = "#808080"
    
    Hscale = (hour*(width-fixedWidth))/HtoDay
   
    Hx1 = 0
    Hx2 = fixedWidth + Hscale
    #Hprev = Hx2
    
    Hshape = [Hx1, Hy1, Hx2, Hy2]
    #test
    #Hshape = [Hx1, Hy1, 50, Hy2]
    draw.rectangle(Hshape, outline=0, fill=Hcolor)
        
        
        
    #----------------------------------------------------------
    #This section is for the middle bar that represents the minutes
    
    My1 = 60
    My2 = My1 + fixedWidth
    MtoHour = 60
    Mcolor = "#FFD700"
    
    Mscale = (minute*(width-fixedWidth))/MtoHour
    
    Mx1 = 0
    Mx2 =  fixedWidth + Mscale
    #Mprev = Mx2
    
    Mshape = [Mx1, My1, Mx2, My2]
    
    draw.rectangle(Mshape, outline=0, fill=Mcolor)

        
    #----------------------------------------------------------
    #This section is for the bottom bar that represents the seconds
    
    Sy1 = 80
    Sy2 = Sy1 + fixedWidth
    StoMinute = 60
    Scolor = "#B87333"
    
    Sscale = (second*(width-fixedWidth))/StoMinute
    
    Sx1 = 0
    Sx2 = fixedWidth + Sscale
    
    Sshape = [Sx1, Sy1, Sx2, Sy2]
    
    draw.rectangle(Sshape, outline=0, fill=Scolor)
        
        
        
    #----------------------------------------------------------
           
        
    disp.image(image, rotation)
    time.sleep(0.0001)


