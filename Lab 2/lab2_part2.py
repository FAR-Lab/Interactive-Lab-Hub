import time
import pytz
import datetime
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
from binary_time import *

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



rect_x = width
# Height of the rect
rect_height = 65
# Wideth of the rect
rect_width = 25


hour_list = [1,0,0,1,1,1]
min_list = [1,1,1,1,1,1]
second_list = [0,1,0,1,1,1]

binary_list = [[1,1,1,1,1,1],[0,1,0,1,1,1],[1,0,0,1,1,1]]


rect_spacing = 100
rect_init_position = 240
second_rect_init_position = 240 + 6 * rect_spacing
score = [[0]* 6,[0]*6,[0]*6]
position = [[0]* 6,[0]*6,[0]*6]
game_status = 1
def sum2d(input):
    my_sum = 0
    for row in input:
        my_sum += sum(row)
    return my_sum

def init_position(min_list,second_list,hour_list,position):
    for i in range(len(min_list)):
        position[0][i] = (rect_init_position + i * rect_spacing )
    for i in range(len(second_list)):
        position[1][i] = (rect_init_position + i * rect_spacing )
    for i in range(len(hour_list)):
        position[2][i] = (second_rect_init_position + i * rect_spacing)

def restore_position(position,score):
    for i in range(len(position)):
        for j in range(len(position[i])):
            position[i][j] = -100
            score[i][j]=0

def update_position(position_list):
    update_pixel = 2
    for i in range(len(position_list)):
        for j in range(len(position_list[i])):
            position_list[i][j] -= update_pixel

def Game_over(intended_score, user_score,dead_time):
    global game_status
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

    current_time = dead_time

    # Create a new blank image with the desired dimensions
    text_image = bg_image

    # Create a draw object for the text image
    text_draw = ImageDraw.Draw(text_image)

    # Define a space-themed font (you can replace 'path_to_your_font.ttf' with your font file)
    space_font_t = ImageFont.truetype('future_font.ttf', size=18)
    space_font = ImageFont.truetype('future_font.ttf', size=25)
    # Define font color (you can use any color that matches your space theme)

    # Define background color (you can use any color that matches your space theme)
    background_color = "#000000"  # Black

    # Draw the current_time text at the top of the screen
    text_draw.text((10, 0), current_time, font=space_font_t, fill="#FFFFFF" )

    # Break the message into new lines at every space
    message_lines = message.split(" ")
    wrapped_message = "\n".join(message_lines)

    # Draw the wrapped message below the current_time
    text_draw.multiline_text((10, height // 2 - text_offset), wrapped_message, font=space_font, fill="#FFFFFF" )

    # Rotate the text image by 270 degrees
    text_image = text_image.transpose(Image.ROTATE_270)

    # Paste the rotated text image onto the original image
    y = top
    draw.text((x, y), "", fill="#000000")  # Clear any previous text
    image.paste(text_image, (x, y))

    # Display the result on your screen
    disp.image(image, rotation)
    time.sleep(7)
    game_status = 3


def draw_rec_list(position,binary_list):
    global game_status
    global score
    for i in range(len(position)):
        for j in range(len(position[i])):
            #check if the rect is in screen
            if binary_list[i][j] == 1 and position[i][j] < 240 and position[i][j] > - rect_width:
                if i == 0 :
                    draw.rectangle((position[i][j], center_y_rotated - rect_height, position[i][j] + rect_width, center_y_rotated), fill="blue", outline="blue")
                
                elif i == 1:
                    draw.rectangle((position[i][j], center_y_rotated, position[i][j] + rect_width, center_y_rotated + rect_height), fill="red", outline="red")
                
                else:
                    draw.rectangle((position[i][j], center_y_rotated - rect_height, position[i][j] + rect_width, center_y_rotated), fill="green", outline="green")
                    draw.rectangle((position[i][j], center_y_rotated, position[i][j] + rect_width, center_y_rotated + rect_height), fill="green", outline="green")
                
                if position[i][j] < 0:
                    if i == 0:
                        if not buttonA.value:
                            # pop the light
                            draw.ellipse((15, center_y_rotated - 125, 80, center_y_rotated - 50), fill="yellow", outline="yellow")
                            score[i][j] = 1
                    if i == 1:
                        if not buttonB.value:
                            # pop the light
                            draw.ellipse((15, center_y_rotated + 50, 80, center_y_rotated + 125), fill="yellow", outline="yellow")
                            score[i][j] = 1 

                    if i == 2:
                        if not buttonA.value and not buttonB.value:
                            draw.ellipse((15, center_y_rotated - 125, 80, center_y_rotated - 50), fill="yellow", outline="yellow")
                            draw.ellipse((15, center_y_rotated + 50, 80, center_y_rotated + 125), fill="yellow", outline="yellow")
                            score[i][j] = 1

    if position[2][5]< - rect_width:
        global num_block
        global total_score
        num_block=sum2d(binary_list)
        print(score)
        total_score = sum2d(score)
        print(num_block)
        print(total_score)
        game_status = 2
        restore_position(position,score)
        #print(game_status)
        print(position)

        
def start_screen():     
    bg_image = Image.open("bg.jpg")
    bg_image = bg_image.resize((width, height))

    draw = ImageDraw.Draw(bg_image)
    
    arrow_lower_left = [(30, height//4 - 10), (10, height//4), (30, height//4 + 10)]
    arrow_upper_left = [(30, 3*height//4 - 10), (10, 3*height//4), (30, 3*height//4 + 10)]    
    draw.polygon(arrow_lower_left, outline="white", fill="white")
    draw.polygon(arrow_upper_left, outline="white", fill="white")

    current_time = time.strftime("%m/%d/%Y \n %H:%M:%S")
    space_font_t = ImageFont.truetype('future_font.ttf', size=18)
    draw.text((70, 50), current_time, font=space_font_t, fill="#FFFFFF" )
    disp.image(bg_image, rotation)

    bg_image = Image.open("bg.jpg")
    bg_image = bg_image.resize((width, height))
    draw = ImageDraw.Draw(bg_image)
    draw.text((70, 50), current_time, font=space_font_t, fill="#FFFFFF" )
    
   #disp.image(bg_image, rotation)




center_y_rotated = height // 2

while True:
    # Clear the screen
    draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))

    # Draw the link, breaking the screen into two parts
    
    # Draw the rectangles on both screens
    #draw.rectangle((rect_x, center_y_rotated - rect_height, rect_x + rect_width, center_y_rotated), fill="blue", outline="blue")
    #draw.rectangle((rect_x, center_y_rotated, rect_x + rect_width, center_y_rotated + rect_height), fill="red", outline="red")
    print("GAME",game_status)
    if game_status==0:
        draw.line((0, center_y_rotated, width, center_y_rotated), fill="white", width=1)
        draw_rec_list(position,binary_list)
        update_position(position)
        disp.image(image, rotation)
    elif game_status==1:
        start_screen()
        if not buttonA.value and not buttonB.value:
            global dead_time
            dead_time, binary_list = convert_binary_to_2d()
            init_position(binary_list[0],binary_list[1],binary_list[2],position)
            game_status=0
    elif game_status==2:
        Game_over(num_block,total_score,dead_time)
    elif game_status==3:
        game_status=1
    else:
        pass
    






    #rect_x -= 5
    #if rect_x < -rect_width:
    #    rect_x = width
    time.sleep(0.00001)

