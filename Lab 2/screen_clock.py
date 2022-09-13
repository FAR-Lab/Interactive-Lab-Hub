import time
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

while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    #TODO: Lab 2 part D work should be filled in here. You should be able to look in cli_clock.py and stats.py 


    #adding image to be displayed
 #   image = Image.open("beerMug.jpg")
 #   image_ratio = (image.width / image.height)
 #   screen_ratio = width / height
 #   if screen_ratio < image_ratio:
 #       scaled_width = (image.width * height // image.height) 
 #       scaled_height = height 
 #   else:
 #       scaled_width = width
 #       scaled_height = (image.height * width // image.width)
 #   image = image.resize((scaled_width, scaled_height), Image.BICUBIC)

    # Crop and center the image
 #   x = scaled_width // 2 - width // 2
 #   y = scaled_height // 2 - height // 2
 #   image = image.crop((x, y, x + width, y + height))

    #setup button functionality
    backlight = digitalio.DigitalInOut(board.D22)
    backlight.switch_to_output()
    backlight.value = True
    buttonA = digitalio.DigitalInOut(board.D23)
    buttonB = digitalio.DigitalInOut(board.D24)
    buttonA.switch_to_input()
    buttonB.switch_to_input()

    #add logic to buttons
    weight = 150 
    AlcPercent = .05
    drinkCount = 0

    # Get drawing object to draw on image.
    draw = ImageDraw.Draw(image)
    x = 0

    while True:
        cmd = "hostname -I | cut -d' ' -f1"
        beerTimes = []
        if buttonA.value and buttonB.value:
            backlight.value = False  # turn off backlight

        else:
            backlight.value = True  # turn on backlight

        if buttonB.value and not buttonA.value:  # just button A pressed
#            image = Image.new("RGB", (width, height))
 #           rotation = 90
            draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
            timeLastBeer = time.strftime("%m/%d/%Y %H:%M:%S") # log time of last beer
            clock = time.strftime("%H:%M:%S") # log time of last beer
            beerTimes.append(timeLastBeer) #start list of prev beers
            timeTilDrive = 0
            BAC = (150/weight)*(AlcPercent)*(drinkCount)*(0.25) #dupdate BAC
            BACmetabolize = 0.015 #* int(time.strftime("%H")) #account for metabolism
            if BAC < 0.08:
                timeTilDrive == 0
            else:
                timeTilDrive = ((BAC - 0.08) / BACmetabolize)*60
            
            BACText = "BAC: " + str(BAC)
          #  timeTilDrive -= int(time.strftime("%S"))//60
            y = top
            draw.text((x, y), BACText, font=font, fill="#FFFFFF") #display BAC
            y += font.getsize(BACText)[1]
            draw.text((x, y), "Clock: " + clock, font=font, fill="#FFFFFF") #display Time of Last Beer
            y += font.getsize(BACText)[1]
            draw.text((x, y), "Drink Count:" + str(drinkCount), font=font, fill="#FFFFFF") #display Time of Last Beer
            y += font.getsize(BACText)[1]
            draw.text((x, y), "Wait Time to Drive: ", font=font, fill="#FFFFFF") #display Time of Last Beer
            y += font.getsize(BACText)[1]
            if timeTilDrive <= 0:
                draw.text((x, y), '0'  + "min", font=font, fill="#FFFFFF") #display Time of Last Beer
            else:
                draw.text((x, y), str(timeTilDrive - int(time.strftime("%S"))/60)  + "min", font=font, fill="#FFFFFF") #display Time of Last Beer
            timeUntilNextBeer = abs(.08 - BAC)

        if buttonA.value and not buttonB.value:  # just button B pressed
            draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))

            # Below code is commented out because I need to tweak it to make it work as desired"
 #           image = Image.open("beerMug.jpg")
  #          image_ratio = (image.width / image.height)
   #         screen_ratio = width / height
    #        if screen_ratio < image_ratio:
     #           scaled_width = (image.width * height // image.height) 
      #          scaled_height = height 
       #     else:
        #        scaled_width = width
         #       scaled_height = (image.height * width // image.width)
          #  image = image.resize((scaled_width, scaled_height), Image.BICUBIC)

            # Crop and center the image
  #          x = scaled_width // 2 - width // 2
   #         y = scaled_height // 2 - height // 2
    #        image = image.crop((x, y, x + width, y + height))
                        
            y = top
            draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
            draw.text((x, y), "Drink Logged", font=font, fill="#FFFFFF") #message that drink has been logged
            disp.image(image, rotation)
            time.sleep(1)
            drinkCount += 1
            
        disp.image(image, rotation)
        #if not buttonA.value and not buttonB.value:  # none pressed
        #    display.fill(color565(0, 255, 0))  # green

    #add text over image

    #COMMENTED OUT FOR TESTING FIX THIS LATER!!!!
    #timeNow = time.strftime("%m/%d/%Y %H:%M:%S")
    #y = top
    #draw.text((x, y), timeNow, font=font, fill="#FFFFFF")
    # Display image.

    #COMMENTED OUT FOR TESTING FIX THIS LATER!!!!
    
    #disp.image(image, rotation)

    #time.sleep(1)
