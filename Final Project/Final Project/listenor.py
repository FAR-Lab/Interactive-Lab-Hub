import textwrap
import paho.mqtt.client as mqtt
import uuid
import ssl

import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
import time
from adafruit_servokit import ServoKit
import threading


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

# the # wildcard means we subscribe to all subtopics of IDD
topic = 'IDD/Cube'

# some other examples
# topic = 'IDD/a/fun/topic'
kit = ServoKit(channels=16)
# servo mover hepler


def move_servo(channel, angle, delay=0.01):
    kit.servo[channel].angle = angle
    time.sleep(delay)
    print(f"Servo {channel} moved to {angle} degrees.")

# Function to move a group of 4 servos to a specified angle
def move_servo_group(start_channel, end_channel, angle):
    for channel in range(start_channel, end_channel):
        kit.servo[channel].angle = angle
    print(f"Servos {start_channel} to {end_channel - 1} moved to {angle} degrees.")

import threading


# Move servos top-down
def move_servos_top_down(angle):
    for start_channel in range(0, 16, 4):
        move_servo_group(start_channel, start_channel + 4, angle)
        
        # Check if we need to reset the previous group
        if start_channel >= 4:
            prev_group_start = start_channel - 4
            move_servo_group(prev_group_start, prev_group_start + 4, 60)
    
        time.sleep(0.1)
    move_servo_group(12, 16, 60)

# Move servos bottom-up
def move_servos_bottom_up(angle):
    for start_channel in range(12, -1, -4):
        move_servo_group(start_channel, start_channel + 4, angle)
        time.sleep(0.1)

# Move servos left-to-right
def move_servos_left_right(angle):
    for column_start in range(4):
        for row in range(4):
            servo_channel = column_start + row * 4
            move_servo(servo_channel, angle)
        time.sleep(0.1)


# Move servos right-to-left
def move_servos_right_left(angle):
    for column_start in range(3, -1, -1):  # Iterate over columns in reverse order
        for row in range(4):  # Iterate over rows
            servo_channel = column_start + row * 4  # Calculate the servo channel
            move_servo(servo_channel, angle)
        time.sleep(0.1)


def move_servos_center_out(angle):
    center_servos = [5, 6, 9, 10]
    outer_servos = [i for i in range(16) if i not in center_servos]

    for servo in center_servos:
        move_servo(servo, angle)
    time.sleep(0.1)

    for servo in outer_servos:
        move_servo(servo, angle)
    time.sleep(0.1)

# Move servos outer 12 to center 4
def move_servos_out_center(angle):
    center_servos = [5, 6, 9, 10]
    outer_servos = [i for i in range(16) if i not in center_servos]

    for servo in outer_servos:
        move_servo(servo, angle)
    time.sleep(0.1)

    for servo in center_servos:
        move_servo(servo, angle)
    time.sleep(0.1)


# Move servos in a left down diagonal pattern
def move_servos_left_down(angle):
    sequences = [[0], [1, 4], [2, 5, 8], [3, 6, 9, 12], [7, 10, 13], [11, 14], [15]]
    for group in sequences:
        for servo in group:
            move_servo(servo, angle)
        time.sleep(0.1)

# Move servos in a right down diagonal pattern
def move_servos_right_down(angle):
    sequences = [[3], [2, 7], [1, 6, 11], [0, 5, 10, 15], [4, 9, 14], [8, 13], [12]]
    for group in sequences:
        for servo in group:
            move_servo(servo, angle)
        time.sleep(0.1)

# Move servos in a left up diagonal pattern
def move_servos_left_up(angle):
    sequences = [[12], [8, 13], [4, 9, 14], [0, 5, 10, 15], [1, 6, 11], [2, 7], [3]]
    for group in sequences:
        for servo in group:
            move_servo(servo, angle)
        time.sleep(0.1)

# Move servos in a right up diagonal pattern
def move_servos_right_up(angle):
    sequences = [[15], [11, 14], [7, 10, 13], [3, 6, 9, 12], [2, 5, 8], [1, 4], [0]]
    for group in sequences:
        for servo in group:
            move_servo(servo, angle)
        time.sleep(0.1)

def move_servos_idd(angle, angle1):
    sequences = [[0, 4, 8, 12, 5, 6, 9, 10, 3, 7, 11, 15], [1, 2, 4, 8, 7, 11, 0, 13, 14, 3], [1, 2, 4, 8, 7, 11, 0, 13, 14, 3]]
    for group in sequences:
        # Move all servos in the group to the first angle
        for servo in group:
            move_servo(servo, angle)
        
        # Optional: Wait for some time after moving all servos in the group to the first angle
        time.sleep(0.6)  # Adjust the delay as needed

        # Move all servos in the group to the second angle
        for servo in group:
            move_servo(servo, angle1)
        
        # Wait for some time before proceeding to the next group
        time.sleep(0.6)  # Adjust the delay as needed


def move_servo_sequence(sequence, angle, angle1):
    for group in sequence:
        for servo in group:
            move_servo(servo, angle)
        time.sleep(0.6)
        for servo in group:
            move_servo(servo, angle1)
        time.sleep(0.6)

def move_servos_alphabet(angle, angle1):
    alphabet_sequences = {
    'A': [[1, 2, 3, 4, 6, 9, 10, 11]],
    'B': [[0, 1, 2, 3, 5, 7, 9, 10, 11]],
    'C': [[1, 2, 4, 7, 8, 11, 12, 15]],
    'D': [[1, 2, 4, 8, 7, 11, 0, 13, 14, 3]],
    'E': [[0, 1, 2, 3, 4, 8, 12, 7, 11, 15, 5]],
    'F': [[0, 1, 2, 3, 4, 8, 6, 10]],
    'G': [[1, 2, 4, 7, 8, 11, 12, 15, 10]],
    'H': [[0, 1, 2, 3, 5, 9, 14, 13, 12, 15]],
    'I': [[0, 4, 8, 12, 5, 6, 9, 10, 3, 7, 11, 15]],
    'J': [[2, 3, 7, 11, 8, 9, 10]],
    'K': [[0, 1, 2, 3, 6, 9, 12, 11]],
    'L': [[0, 1, 2, 3, 7, 11]],
    'M': [[2, 3, 4, 5, 10, 11, 12, 13]],
    'N': [[0, 1, 2, 3, 5, 10, 12, 13, 14, 15]],
    'O': [[1, 2, 4, 7, 8, 11, 13, 14]],
    'P': [[0, 1, 2, 3, 4, 6, 9]],
    'Q': [[1, 2, 4, 7, 8, 11, 13, 14, 15]],
    'R': [[0, 1, 2, 3, 4, 6, 9, 11]],
    'S': [[4, 8, 12, 5, 10, 3, 7]],
    'T': [[0, 4, 8, 12, 5, 6, 7]],
    'U': [[0, 1, 2, 12, 13, 14, 7, 11]],
    'V': [[1, 6, 11, 14]],
    'W': [[0, 1, 6, 7, 8, 9, 14, 15]],
    'X': [[0, 5, 10, 15, 12, 3]],
    'Y': [[1, 6, 7, 9, 12]],
    'Z': [[0, 4, 8, 12, 6, 9, 3, 7, 11, 15]]
}

    for letter, sequence in alphabet_sequences.items():
        print(f"Moving servos for letter: {letter}")
        move_servo_sequence(sequence, angle, angle1)



def move_servos_in_order(target_angle, speed_delay=0.1):
    # Define the order of servo movement
    servo_order = [0, 4, 8, 12, 13, 14, 15, 11, 7, 3, 2, 1, 5, 9, 6, 10]

    # Move each servo in the defined order
    for servo in servo_order:
        kit.servo[servo].angle = target_angle
        time.sleep(speed_delay) 

def move_servos_in_reverse_order(target_angle, speed_delay=0.1):
    # Define the order of servo movement
    servo_order = [0, 4, 8, 12, 13, 14, 15, 11, 7, 3, 2, 1, 5, 9, 6, 10]
    reversed_servo_order = servo_order[::-1]

    # Move each servo in the defined order
    for servo in reversed_servo_order:
        kit.servo[servo].angle = target_angle
        time.sleep(speed_delay) 
#this is the callback that gets called once we connect to the broker. 
#we should add our subscribe functions here as well
def on_connect(client, userdata, flags, rc):
	print(f"connected with result code {rc}")
	client.subscribe(topic)
	# you can subsribe to as many topics as you'd like
	# client.subscribe('some/other/topic')

def update_display_with_mqtt_message(message):
    """Updates the display with the received MQTT message."""
    # Clear the image with a black rectangle
    draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
    
    # Wrap the message to fit the display
    wrapped_text = textwrap.fill(message, width=20)  # Adjust width as needed
    
    # Draw the text on the display
    text_size = draw.textsize(wrapped_text, font=font)
    text_x = (width - text_size[0]) // 2
    text_y = (height - text_size[1]) // 2
    draw.text((text_x, text_y), wrapped_text, font=font, fill="#FFFFFF")
    
    # Update the display with the new image
    disp.image(image, rotation)

def servo_move_smile(target_angle):
    # Define the specific servos to move
    specific_servos = [0, 12, 2, 7, 11, 14]

    # Set the angle for each specific servo
    for servo in specific_servos:
        kit.servo[servo].angle = target_angle

    # Optionally, add a delay after setting the angles if needed
    time.sleep(0.3) 

def servo_move_cry(target_angle):
    # Define the specific servos to move
    specific_servos = [0, 12, 3, 6, 10, 15]

    # Set the angle for each specific servo
    for servo in specific_servos:
        kit.servo[servo].angle = target_angle

    # Optionally, add a delay after setting the angles if needed
    time.sleep(0.3) 
	
def update_servo_with_mqtt_message(message):
    if message == '1':
        move_servos_top_down(0)
        move_servos_top_down(60)
    elif message == '2':
        move_servos_bottom_up(0)
        move_servos_bottom_up(60)
    elif message == '3':
        move_servos_left_right(0)
        move_servos_left_right(60)
    elif message == '4':
        move_servos_right_left(0)
        move_servos_right_left(60)
    elif message == '5':
        move_servos_left_down(0)
        move_servos_left_down(60)
    elif message == '6':
        move_servos_right_down(0)
        move_servos_right_down(60)
    elif message == '7':
        move_servos_left_up(0)
        move_servos_left_up(60)
    elif message == '8':
        move_servos_right_up(0)
        move_servos_right_up(60)
    elif message == '11':
        move_servos_center_out(0)
        move_servos_center_out(60)
    elif message == '10':
        move_servos_out_center(0)
        move_servos_out_center(60)
    elif message == '9':
        move_servos_idd(0,60)
    elif message == '12':
        move_servos_idd(0,60)
    elif message == '99':
        move_servos_alphabet(0,60)
    elif message == '15':
        move_servos_in_order(0)
        move_servos_in_order(60)
    elif message == '14':
        move_servos_in_reverse_order(0)
        move_servos_in_reverse_order(60)
    elif message == '16':
        servo_move_smile(0)
        servo_move_smile(60)
    elif message == '17':
        servo_move_cry(0)
        servo_move_cry(60)
    elif message == 'reset':
        move_servos_top_down(60)
    else:
        print("Invalid message. Please enter a valid command.")



def on_message(client, userdata, msg):
    print(f"topic: {msg.topic} msg: {msg.payload.decode('UTF-8')}")
    
    update_display_with_mqtt_message(msg.payload.decode('UTF-8'))
    
    # Call update_servo_with_mqtt_message regardless of the topic
    update_servo_with_mqtt_message(msg.payload.decode('UTF-8'))


# Every client needs a random ID
client = mqtt.Client(str(uuid.uuid1()))
# configure network encryption etc
client.tls_set(cert_reqs=ssl.CERT_NONE)
# this is the username and pw we have setup for the class
client.username_pw_set('idd', 'device@theFarm')

# attach out callbacks to the client
client.on_connect = on_connect
client.on_message = on_message

#connect to the broker
client.connect(
    'farlab.infosci.cornell.edu',
    port=8883)

# this is blocking. to see other ways of dealing with the loop
#  https://www.eclipse.org/paho/index.php?page=clients/python/docs/index.php#network-loop
client.loop_forever()
