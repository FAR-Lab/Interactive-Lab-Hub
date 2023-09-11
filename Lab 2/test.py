import time
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

# Load the background image
background = Image.open("red.jpg")

# Resize the background image to fit the display dimensions
background = background.resize((width, height))

# Display the background image.
disp.image(background, rotation)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
padding = -2
top = padding
while True:
    # Clear the text area.
    # draw.rectangle((0, 0, width, height), outline=0, fill=0)

    #TODO: Lab 2 part D work should be filled in here. You should be able to look in cli_clock.py and stats.py 
    current_time = time.strftime("%m/%d/%Y %H:%M:%S")
    y = top  # Adjust the y-coordinate as needed
    
    # # Display the updated image with text.
    # disp.image(background, rotation)
    # draw.text((10, y), current_time, font=font, fill="#00FF00")
    # print("here")
    # time.sleep(1)
    image.paste(background, (0, 0))
    
    # Draw the text onto the image
    draw.text((10, top), current_time, font=font, fill="#000000")
    
    # Display the updated image on the screen
    disp.image(image, rotation)
    
    time.sleep(1)
