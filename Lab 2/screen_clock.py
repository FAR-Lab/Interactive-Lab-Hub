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
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 22)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

# Configuring button A (top) and button B (bottom)
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

morning_image = Image.open("morning.jpg")
morning_image = morning_image.resize((width,height))
# # Create a blank background image
# background_image = Image.new("RGB", (width, height))
while True:
    # # Paste your image onto the background image at the desired position
    # background_image.paste(morning_image, (0, 0))  # Adjust the position as needed

    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=400) #the fill 400 = red

    #TODO: Lab 2 part D work should be filled in here. You should be able to look in cli_clock.py and stats.py 
    # Get the current time in the format "mm/dd/yyyy hh:mm:ss"
    current_time = time.strftime("%m/%d/%Y %H:%M:%S")
    # current_time = time.strftime("%m/%d %H:%M:%S")
    # draw = ImageDraw.Draw(background_image)

    # Write the current time on the screen.
    x, y = 0, 0  # Adjust the coordinates as needed.
    draw.text((x, y), current_time, font=font, fill="#FFFFFF")

    # Display image.
    disp.image(image, rotation)

    time.sleep(1)

#______________ image attempt
# import time
# import digitalio
# import board
# from PIL import Image, ImageDraw, ImageFont
# import adafruit_rgb_display.st7789 as st7789

# # Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
# cs_pin = digitalio.DigitalInOut(board.CE0)
# dc_pin = digitalio.DigitalInOut(board.D25)
# reset_pin = None

# # Config for display baudrate (default max is 24mhz):
# BAUDRATE = 64000000

# # Setup SPI bus using hardware SPI:
# spi = board.SPI()

# # Create the ST7789 display:
# disp = st7789.ST7789(
#     spi,
#     cs=cs_pin,
#     dc=dc_pin,
#     rst=reset_pin,
#     baudrate=BAUDRATE,
#     width=135,
#     height=240,
#     x_offset=53,
#     y_offset=40,
# )

# # Create blank image for drawing.
# # Make sure to create an image with mode 'RGB' for full color.
# height = disp.width  # we swap height/width to rotate it to landscape!
# width = disp.height
# image = Image.new("RGB", (width, height))
# rotation = 90

# # Get drawing object to draw on the image.
# draw = ImageDraw.Draw(image)

# # Load images for different times of the day (e.g., morning, afternoon, evening)
# morning_image = Image.open("morning.jpg")  # Replace with your image file
# afternoon_image = Image.open("afternoon.jpg")  # Replace with your image file
# evening_image = Image.open("evening.jpg")  # Replace with your image file

# # Initialize button states
# buttonA = digitalio.DigitalInOut(board.D23) #top 
# buttonB = digitalio.DigitalInOut(board.D24) # bottom
# buttonA.switch_to_input()
# buttonB.switch_to_input()

# # Initialize time-based mode and image
# time_mode = "morning"  # Default to morning mode
# current_image = morning_image

# # Function to resize the image to fit the display dimensions
# def resize_image(image):
#     # Calculate the new size to fit the display
#     new_width, new_height = width, height
#     if image.width > width or image.height > height:
#         aspect_ratio = image.width / image.height
#         if aspect_ratio > 1:
#             new_width = width
#             new_height = int(width / aspect_ratio)
#         else:
#             new_height = height
#             new_width = int(height * aspect_ratio)
    
#     # Resize the image
#     return image.resize((new_width, new_height))

# # Function to update and display the current time on the image
# def display_current_time():
#     current_time = time.strftime("%H:%M:%S")
#     font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
#     draw.text((10, 10), current_time, font=font, fill="#FFFFFF")

# # Main loop:
# while True:
#     # Check button states
#     if buttonA.value and not buttonB.value:
#         # Button A pressed: Toggle between morning and afternoon modes
#         if time_mode == "morning":
#             time_mode = "afternoon"
#             current_image = afternoon_image
#         else:
#             time_mode = "morning"
#             current_image = morning_image

#     elif buttonB.value and not buttonA.value:
#         # Button B pressed: Toggle between afternoon and evening modes
#         if time_mode == "afternoon":
#             time_mode = "evening"
#             current_image = evening_image
#         else:
#             time_mode = "afternoon"
#             current_image = afternoon_image

#     # Resize the current image to fit the display
#     current_image = resize_image(current_image)

#     # Display the current image
#     disp.image(current_image, rotation)
    
#     # Display the current time on the image
#     display_current_time()

#     # Update the display
#     disp.display()

#     # Update every second
#     time.sleep(1)
