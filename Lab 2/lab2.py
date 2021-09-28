import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
from time import strftime, sleep
import adafruit_mpu6050
import board
from adafruit_rgb_display.rgb import color565
import webcolors
# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None
i2c = board.I2C()
mpu = adafruit_mpu6050.MPU6050(i2c)


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

buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

record = 10

while True:
    if record >= 0:
        record -= 0.1
        # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)




#TODO: Lab 2 part D work should be filled in here. You should be able to look in cli_clock.py and stats.py 
    H = int(strftime("%H"))
    M = int(strftime("%M"))
    S = int(strftime("%S"))
    t = H*60*60 + M*60 + S
    Repeat = str(int(t/2376))
    songCount = t%2376
    Time = Repeat + "th repeat of Album"
    Time2 = "<Sgt. Pepper's> today."
    if songCount <= 120:
        songname = "<Sgt.Pepper's Lonely Hearts Club Band>"
        songnum = "1"
        lastSong = "<A Day In The Life>"
        nextSong = "<With A Little Help From My Friend>"
        progress = (songCount)/120
    elif songCount > 120 and songCount <= 282:
        songname = "<With A Little Help From My Friend>"
        songnum = "2"
        lastSong = "<Sgt.Pepper's Lonely Hearts Club Band>"
        nextSong = "<Lucy In The Sky With Diamonds>"
        progress = (songCount-120)/(282-120)
    elif songCount > 282 and songCount <= 490:
        songname = "<Lucy In The Sky With Diamonds>"
        songnum = "3"
        lastSong ="<With A Little Help From My Friend>"
        nextSong = "<Getting Better>"
        progress = (songCount-282)/(490-282)
    elif songCount > 490 and songCount <= 658:
        songname = "<Getting Better>"
        songnum = "4"
        lastSong ="<Lucy In The Sky With Diamonds>"
        nextSong = "<Fixing A Hole>"
        progress = (songCount-490)/(658-490)
    elif songCount > 658 and songCount <= 814:
        songname = "<Fixing A Hole>"
        songnum = "5"
        lastSong ="<Getting Better>"
        nextSong = "<She's Leaving Home>"
        progress = (songCount-658)/(814-658)
    elif songCount > 814 and songCount <= 1019:
        songname = "<She's Leaving Home>"
        songnum = "6"
        lastSong ="<Fixing A Hole>"
        nextSong = "<Being For The Benefit Of Mr. Kite!>"
        progress = (songCount-814)/(1019-814)
    elif songCount > 1019 and songCount <= 1176:
        songname = "<Being For The Benefit Of Mr. Kite!>"
        songnum = "7"
        lastSong ="<She's Leaving Home>"
        nextSong = "<Within You Without You>"
        progress = (songCount-1019)/(1176-1019)
    elif songCount > 1176 and songCount <= 1481:
        songname = "<Within You Without You>"
        songnum = "8"
        lastSong ="<Being For The Benefit Of Mr. Kite!>"
        nextSong = "<When I'm Sixty Four>"
        progress = (songCount-1176)/(1481-1176)
    elif songCount > 1481 and songCount <= 1638:
        songname = "<When I'm Sixty Four>"
        songnum = "9"
        lastSong ="<Within You Without You>"
        nextSong = "<Lovely Rita>"
        progress = (songCount-1481)/(1638-1481)
    elif songCount > 1638 and songCount <= 1800:
        songname = "<Lovely Rita>"
        songnum = "10"
        lastSong ="<When I'm Sixty Four>"
        nextSong = "<Good Morning Good Morning>"
        progress = (songCount-1638)/(1800-1638)
    elif songCount > 1800 and songCount <= 1962:
        songname = "<Good Morning Good Morning>"
        songnum = "11"
        lastSong ="<Lovely Rita>"
        nextSong = "<Sgt.Pepper's Lonely Hearts Club Band>"
        progress = (songCount-1800)/(1962-1800)
    elif songCount > 1962 and songCount <= 2040:
        songname = "<Sgt.Pepper's Lonely Hearts Club Band>"
        songnum = "12"
        lastSong ="<Good Morning Good Morning>"
        nextSong = "<A Day In The Life>"
        progress = (songCount-1962)/(2040-1962)
    elif songCount>2040 and songCount<=2376:
        songname = "<A Day In The Life>"
        songnum = "13"
        lastSong ="<Sgt.Pepper's Lonely Hearts Club Band>"
        nextSong ="<Sgt.Pepper's Lonely Hearts Club Band>"
        progress = (songCount-2040)/(2376-2040)
    
    
    Song = "At the " + songnum +"th songs: "
    bar = "["+ ">"*int(14*progress) + "--"*(14-int(14*progress)) + "]"
    #bar = str(progress)
    uppage1 = "Last Song was:"
    uppage2 = "<"+ lastSong + ">"
    
    
    downpage1 = "Next Song will be:"
    downpage2 = "<"+ nextSong + ">"
    downpage3 = str(int((86400-t)/2376))+" repeats of the album"
    downpage4 = "And " + str(13-int(songnum)) +" songs"
    downpage5 = "till end of the day."
    
    
    gyroX, gyroY, gyroZ = mpu.gyro
    #sensordata = "Gyro x:"+ str(int(gyroX)) + ", Y:"+ str(int(gyroY)) +",Z: " + str(int(gyroZ))
    if(gyroX <= -3 or gyroY <= -3 or gyroZ <= -3):
        record = 10
        
        #Song  = "[>>>>>>>>>>>>>>]"
    if buttonA.value and buttonB.value:
        y = top
        draw.text((x, y), Time, font=font, fill="#FFFFFF")
        y += font.getsize(Time)[1]
        draw.text((x, y), Time2, font=font, fill="#FFFFFF")
        y += font.getsize(Time2)[1]
        draw.text((x, y), Song, font=font, fill="#FFFFFF")
        y += font.getsize(Song)[1]
        draw.text((x, y), songname, font=font, fill="#0000FF")
        y += font.getsize(songname)[1]
        draw.text((x, y), bar, font=font, fill="#FF00FF")
                    
    
    if buttonB.value and not buttonA.value:  # just button A pressed
        y = top
        draw.text((x, y), uppage1, font=font, fill="#FFFFFF")
        y += font.getsize(uppage1)[1]
        draw.text((x, y), uppage2, font=font, fill="#FFFF00")
             
        y += font.getsize(uppage1)[1]
        
        draw.ellipse((20,40,110,130), fill = "#FFFFFF")
        draw.ellipse((50,70,80,100), fill = "#000000")
        prog = (130-35)*((10-record)/10)
        draw.rectangle((0, y, 140, 35+int(prog)), outline=0, fill="#000000")
        #35 - 130
        y += font.getsize(uppage1)[1]

        if record <= 0.1:
            draw.text((x+130, y), "Time's Up!", font=font, fill="#FFFF00")
        
    if buttonA.value and not buttonB.value:  # just button B pressed
        y = top
        draw.text((x, y), downpage1, font=font, fill="#FFFFFF")
        y += font.getsize(downpage1)[1]
        draw.text((x, y), downpage2, font=font, fill="#FFFF00")
        y += font.getsize(downpage2)[1]
        draw.text((x, y), downpage3, font=font, fill="#FFFFFF")
        y += font.getsize(downpage3)[1]
        draw.text((x, y), downpage4, font=font, fill="#FFFFFF")
        y += font.getsize(downpage4)[1]
        draw.text((x, y), downpage5, font=font, fill="#FFFFFF")
    
    # Display image.
    disp.image(image, rotation)
    sleep(0.1)
