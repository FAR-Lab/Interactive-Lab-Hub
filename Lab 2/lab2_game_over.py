import textwrap
import time
import pytz
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
buttonA = digitalio.DigitalInOut(board.D23)	
buttonB = digitalio.DigitalInOut(board.D24)	
buttonA.switch_to_input()	
buttonB.switch_to_input()

background_list = ["liberty.jpg", "paris.jpg", "au.jpg", "china.jpg"]

background_image = []
for image_name in background_list:
    bg_image = Image.open(image_name)	
    bg_image = bg_image.resize((width, height))
    background_image.append(bg_image)

def get_current_time_in_timezone(timezone_str):
    """Return the current time in the specified timezone."""
    local_timezone = pytz.timezone(timezone_str)
    local_time = datetime.datetime.now(local_timezone)
    return local_time

location_list = ['America/New_York', 
                 'Europe/Paris',
                 'Australia/Canberra',
                 'Asia/Shanghai'
                ]

index = 0
count = 0
intended_score = 30
user_score = 25
def update_display(background_image, index, format_12_hour=True):
    """Updates the display with the given background and time format."""
    image.paste(background_image[index], (0, 0))
    if format_12_hour:
        Game_over(intended_score, user_score)
    else:
        Game_over(1, 1)
    
    

index = 0
format_12_hour = True

buttonA_pressed_last = False
buttonB_pressed_last = False

game_state = False

game_state = False

def Game_over(intended_score, user_score):
    """Updates the display with the given futuristic space-themed text format."""
    # Define text_offset and other variables
    text_offset = 10
    bg_image = Image.open("bg.jpg")
    bg_image = bg_image.resize((width, height))
    bg_image = bg_image.rotate(90, expand=True)

    # Define the text to display
    if intended_score == user_score:
        message = "Congrats! You have Won the Game!"
    else:
        mis_Score = str(intended_score - user_score)
        message = "GG! You have missed " + mis_Score + " hit"

    current_time = time.strftime("%m/%d/%Y \n %H:%M:%S")

    # Create a new blank image with the desired dimensions
    text_image = bg_image

    # Create a draw object for the text image
    text_draw = ImageDraw.Draw(text_image)

    # Define a space-themed font (you can replace 'path_to_your_font.ttf' with your font file)
    space_font_t = ImageFont.truetype('future_font.ttf', size=18)
    space_font = ImageFont.truetype('future_font.ttf', size=25)
    # Define font color (you can use any color that matches your space theme)
    font_color = "#FFFFFF" 

    # Define background color (you can use any color that matches your space theme)
    background_color = "#000000"  # Black

    # Draw the current_time text at the top of the screen
    text_draw.text((10, 0), current_time, font=space_font_t, fill=font_color)

    # Break the message into new lines at every space
    message_lines = message.split(" ")
    wrapped_message = "\n".join(message_lines)

    # Draw the wrapped message below the current_time
    text_draw.multiline_text((10, height // 2 - text_offset), wrapped_message, font=space_font, fill=font_color)

    # Rotate the text image by 270 degrees
    text_image = text_image.transpose(Image.ROTATE_270)

    # Paste the rotated text image onto the original image
    y = top
    draw.text((x, y), "", fill="#000000")  # Clear any previous text
    image.paste(text_image, (x, y))

    # Display the result on your screen
    disp.image(image, rotation)

    game_state = False

while True:
    
    if not buttonB.value and not buttonB_pressed_last:
        index = (index + 1) % len(background_list)
        buttonB_pressed_last = True
    elif buttonB.value:
        buttonB_pressed_last = False

    if not buttonA.value and not buttonA_pressed_last:
        format_12_hour = not format_12_hour
        buttonA_pressed_last = True
    elif buttonA.value:
        buttonA_pressed_last = False

    update_display(background_image, index, format_12_hour)
    time.sleep(0.1)