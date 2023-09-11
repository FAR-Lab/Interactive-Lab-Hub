import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont, ImageSequence
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
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 25)
font2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)
font_current_time = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True
# # _________________________________________________________________________Individual
# # Configuring button A (top) and button B (bottom)
# buttonA = digitalio.DigitalInOut(board.D23)
# buttonB = digitalio.DigitalInOut(board.D24)
# buttonA.switch_to_input()
# buttonB.switch_to_input()

# morning_image = Image.open("morning.jpg")
# morning_image = morning_image.resize((width,height))
# afternoon_image = Image.open("afternoon.jpg") # might use in the future
# afternoon_image = afternoon_image.resize((width,height))
# evening_image = Image.open("evening.jpg")
# evening_image = evening_image.resize((width,height))
# gif_image_blow_kiss = Image.open("blow_kiss.gif") # this is for the time (seconds)
# gif_iterator = ImageSequence.Iterator(gif_image_blow_kiss)
# # Define the desired frame switching interval in seconds
# frame_switch_interval = 0.0001  # Switch frames every 0.1 second (adjust as needed)
# # Initialize the last frame switch time
# last_frame_switch_time = time.time()

# # jumping interaction for buttonB 
# # Define variables for controlling the current_time text position
# current_time_x = 75
# current_time_y = 45
# current_time_jump = False
# jump_counter = 0

# # Timer for the "Current Time" text color change
# current_time_color_change_timer = 0
# # Initialize the current_time_color variable
# current_time_color = "#f41f1f"

# while True:
#     # Create a copy of the background image (morning image as default)
#     display_image = morning_image.copy()
#     display_image_evening = evening_image.copy()
#     # TODO: Lab 2 part D work should be filled in here. You should be able to look in cli_clock.py and stats.py 
#     # Get the current time in the format "mm/dd/yyyy hh:mm:ss"
#     date = time.strftime("%m/%d/%Y")
#     current_time = time.strftime("%H:%M")
#     seconds = time.strftime("%S")

#     if not buttonA.value:  # button A is pressed, see screen_test.py
#         x, y = 70, 80  # Adjust the coordinates as needed.
#         draw_on_image = ImageDraw.Draw(display_image_evening)
#         draw_on_image.text((0, 0), "Today's Date", font=font2, fill="#FFFFFF")
#         draw_on_image.text((x, y), date, font=font, fill="#FFFFFF")
#         # Display the modified images with the time on the screen
#         disp.image(display_image_evening, rotation)
#     else:  # The default screen
#         # Handle button B press to make current_time text jump up and down
#         if not buttonB.value:
#             current_time_jump = True  # button B is pressed

#         if current_time_jump:
#             if jump_counter < 3:  # controlling jump speed 
#                 current_time_y -= 4  # increase the jump distance
#                 jump_counter += 1
#             elif jump_counter < 6:
#                 current_time_y += 4
#                 jump_counter += 1
#             else:
#                 current_time_jump = False
#                 jump_counter = 0
#                 current_time_color_change_timer = time.time()  # Start the color change timer

#         # Check if it's time to change the "Current Time" text color
#         if current_time_color_change_timer != 0:
#             current_time_color = "#FFFFFF"  # White color
#             if time.time() - current_time_color_change_timer >= 1:  # Change color for 1 second
#                 current_time_color = "#f41f1f"  # Default color
#                 current_time_color_change_timer = 0
#             else:
#                 current_time_color_change_timer = time.time()

#         # Draw the "Current Time" text with the selected color
#         draw_on_image = ImageDraw.Draw(display_image)
#         draw_on_image.text((current_time_x, current_time_y), current_time, font=font2, fill="#f41f1f")  # Default color
#         draw_on_image.text((130, 90), seconds, font=font2, fill="#FFFFFF")  # 134f5c
#         draw_on_image.text((0, 0), "Current Time", font=font_current_time, fill=current_time_color)

#         # Displaying the gif: had to reduce frames to make it run faster...
#         current_datetime = time.time()
#         time_difference = current_datetime - last_frame_switch_time

#         if time_difference >= frame_switch_interval:
#             try:
#                 frame = next(gif_iterator)
#                 frame = frame.convert("RGBA").resize((45, 45))
#                 display_image.paste(frame, (80, 85), frame)
#             except StopIteration:
#                 gif_iterator = ImageSequence.Iterator(gif_image_blow_kiss)

#             last_frame_switch_time = current_datetime

#         # Display the modified image with the time on the screen
#         disp.image(display_image, rotation)

#     time.sleep(0.0001)

#     #__________________________________________________________________________


# _________________________________________________________________________Group Part
# Configuring button A (top) and button B (bottom)
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

white_background_image = Image.open("white.jpg")
white_background_image = white_background_image.resize((width,height))
afternoon_image = Image.open("afternoon.jpg") # might use in the future
afternoon_image = afternoon_image.resize((width,height))
evening_image = Image.open("evening.jpg")
evening_image = evening_image.resize((width,height))
gif_image_dog = Image.open("dog.gif") # this is for the time (seconds)
gif_iterator = ImageSequence.Iterator(gif_image_dog)
# Define the desired frame switching interval in seconds
frame_switch_interval = 0.0001  # Switch frames every 0.1 second (adjust as needed)
# Initialize the last frame switch time
last_frame_switch_time = time.time()


# Timer for the "Current Time" text color change
current_time_color_change_timer = 0
# Initialize the current_time_color variable
current_time_color = "#f41f1f"



while True:
    # Create a copy of the background image (morning image as default)
    display_image = white_background_image.copy()
    display_image_evening = evening_image.copy()
    # TODO: Lab 2 part D work should be filled in here. You should be able to look in cli_clock.py and stats.py 
    # Get the current time in the format "mm/dd/yyyy hh:mm:ss"
    date = time.strftime("%m/%d/%Y")
    current_time = time.strftime("%H:%M:%S")
    seconds = time.strftime("%S")

    if not buttonA.value:  # button A is pressed, see screen_test.py
        x, y = 70, 80  # Adjust the coordinates as needed.
        draw_on_image = ImageDraw.Draw(display_image_evening)
        draw_on_image.text((0, 0), "Today's Date", font=font2, fill="#FFFFFF")
        draw_on_image.text((x, y), date, font=font, fill="#FFFFFF")
        # Display the modified images with the time on the screen
        disp.image(display_image_evening, rotation)
    else:  # The default screen
        # Handle button B press to make current_time text jump up and down
        if not buttonB.value:
            current_time_jump = True  # button B is pressed

        # if current_time_jump:
        #     if jump_counter < 3:  # controlling jump speed 
        #         current_time_y -= 4  # increase the jump distance
        #         jump_counter += 1
        #     elif jump_counter < 6:
        #         current_time_y += 4
        #         jump_counter += 1
        #     else:
        #         current_time_jump = False
        #         jump_counter = 0
        #         current_time_color_change_timer = time.time()  # Start the color change timer

        # Check if it's time to change the "Current Time" text color
        if current_time_color_change_timer != 0:
            current_time_color = "#FFFFFF"  # White color
            if time.time() - current_time_color_change_timer >= 1:  # Change color for 1 second
                current_time_color = "#f41f1f"  # Default color
                current_time_color_change_timer = 0
            else:
                current_time_color_change_timer = time.time()

        # Draw the "Current Time" text with the selected color
        draw_on_image = ImageDraw.Draw(display_image)
        # draw_on_image.text((current_time_x, current_time_y), current_time, font=font2, fill="#f41f1f")  # Default color
        draw_on_image.text((0, 0), current_time, font=font2, fill="#f41f1f")  # Default color
        draw_on_image.text((130, 90), seconds, font=font2, fill="#FFFFFF")  # 134f5c
        # draw_on_image.text((0, 0), "Current Time", font=font_current_time, fill=current_time_color)

        # Displaying the gif: had to reduce frames to make it run faster...
        current_datetime = time.time()
        time_difference = current_datetime - last_frame_switch_time

        if time_difference >= frame_switch_interval:
            try:
                frame = next(gif_iterator)
                frame = frame.convert("RGBA").resize((120, 80))
                display_image.paste(frame, (20, 55), frame)
            except StopIteration:
                gif_iterator = ImageSequence.Iterator(gif_image_dog)

            last_frame_switch_time = current_datetime

        # Display the modified image with the time on the screen
        disp.image(display_image, rotation)

    time.sleep(0.0001)

    #__________________________________________________________________________