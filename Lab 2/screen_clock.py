import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
import math

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
    weight = 100
    weightStr = str(weight)
    AlcPercent = .05
    drinkCount = 0

    # Get drawing object to draw on image.
    draw = ImageDraw.Draw(image)
    x = 0
    exitBool = 0
    while exitBool < 1:
        if buttonA.value and buttonB.value:
            backlight.value = False  # turn off backlight
        else:
            backlight.value = True  # turn on backlight
        draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
        y = top
        draw.text((x, y), "Please Input your weight: ", font=font, fill="#FFFFFF") #display BAC
        y += font.getsize(weightStr)[1]
        draw.text((x, y), "Weight: " + str(weight),font_size = 5, font=font, fill="#FFFFFF") #display Time of Last Beer

        if buttonB.value and not buttonA.value:  # just button A pressed          
            weight += 1


        if buttonA.value and not buttonB.value:  # just button B pressed
            weight -= 1
            
        while buttonA.value and not buttonB.value:  # just button A pressed          
            if not buttonB.value and not buttonA.value:
                exitBool += 1
            
        disp.image(image, rotation)
        


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
            BACmetabolize = 0.015 #* int(time.strftime("%H")) #account for metabolism           
            BACmodifier =  round(round((BACmetabolize/(60 * 60)) *  int(time.strftime("%S")), 6), 6)
            clock = time.strftime("%H:%M:%S") #get current time
            beerTimes.append(timeLastBeer) #start list of prev beers
            timeTilDrive = 0

            BAC = round((150/weight)*(AlcPercent)*(drinkCount)*(0.25) * 2 , 6)  #update BAC
            if BAC < 0.08:
                timeTilDrive == 0
            else:
                timeTilDrive = round(((BAC - 0.08) / BACmetabolize)*60, 2)
            
            if BAC == 0:
                BACText = "BAC: " + str(BAC)
            else:
                BACText = "BAC: " + str(round(BAC - BACmodifier * 1.5, 5))
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
                if BAC > .12:
                    y += font.getsize(BACText)[1]
                    draw.text((x, y), "You've had one too many...", font=font, fill="#FFFFFF") #display Time of Last Beer
                    y += font.getsize(BACText)[1]
                    draw.text((x, y), "Just call #8294 for a cab", font=font, fill="#FFFFFF") #display Time of Last Beer

                else: 
                    timeTil = round(timeTilDrive - int(time.strftime("%S"))/60, 2)
                    draw.text((x, y), str( timeTil)  + "min", font=font, fill="#FFFFFF") #display Time of Last Beer
            
            
      #     timeUntilNextBeer = abs(.08 - BAC)    #this is not necessary anymore
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
