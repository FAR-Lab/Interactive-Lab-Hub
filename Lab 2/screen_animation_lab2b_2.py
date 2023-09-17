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
height = disp.width
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)

padding = -2
top = padding
bottom = height - padding
x = 0

font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)

backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

# Define the initial size of the diamond
diamond_size = 20

while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
    
    # Draw a diamond shape with decreasing size
    for i in range(diamond_size):
        draw.line([(width//2 - i, height//2 - diamond_size + i), 
                   (width//2 + i, height//2 - diamond_size + i)], 
                   fill=(255, 255, 255))
        
        draw.line([(width//2 - i, height//2 + diamond_size - i), 
                   (width//2 + i, height//2 + diamond_size - i)], 
                   fill=(255, 255, 255))
    
    # Decrease the size of the diamond for the next iteration
    diamond_size -= 1
    
    # Reset the diamond size once it has disappeared
    if diamond_size <= 0:
        diamond_size = 20
    
    # Display the image
    disp.image(image, rotation)
    time.sleep(0.1)  # Adjust the sleep time to control the speed of the animation
