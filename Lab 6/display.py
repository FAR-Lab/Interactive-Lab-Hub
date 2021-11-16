import paho.mqtt.client as mqtt
import uuid
import board
import busio

import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789

# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

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

disp.rotation=90

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
if disp.rotation % 180 == 90:
    height = disp.width  # we swap height/width to rotate it to landscape!
    width = disp.height
else:
    width = disp.width  # we swap height/width to rotate it to landscape!
    height = disp.height

image = Image.new("RGB", (width, height))
draw = ImageDraw.Draw(image)

i2c = busio.I2C(board.SCL, board.SDA)

def add_text(text_1="", text_2=""):
    image = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(image)# Get drawing object to draw on image.
    draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))# Draw a black filled box to clear the image.
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)
    draw.text((10, 10), text_1, font=font, fill="#FFFFFF")
    draw.text((10, 50), text_2, font=font, fill="#FFFFFF")
    disp.image(image)

#this is the callback that gets called once we connect to the broker. 
#we should add our subscribe functions here as well
def on_connect(client, userdata, flags, rc):
    print(f"connected with result code {rc}")
    client.subscribe('IDD/syw/cap')
    client.subscribe('IDD/syw/multi-distance')
    # you can subsribe to as many topics as you'd like
    # client.subscribe('some/other/topic')

# this is the callback that gets called each time a message is recived
def on_message(client, userdata, msg):
    print(f"topic: {msg.topic} msg: {msg.payload.decode('UTF-8')}")
    
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
    disp.image(image)

    # you can filter by topics
    if msg.topic == 'IDD/syw/cap': 
        if '0' in msg.payload.decode('UTF-8'):
            add_text('EMERGENCY')
        elif '2' in msg.payload.decode('UTF-8'):
            add_text('move')
        elif '11' in msg.payload.decode('UTF-8'):
            add_text('food')
        elif '4' in msg.payload.decode('UTF-8'):
            add_text('meds')
        elif '8' in msg.payload.decode('UTF-8'):
            add_text('bathroom')
        elif '5' in msg.payload.decode('UTF-8'):
            add_text('water')
        elif '6' in msg.payload.decode('UTF-8'):
            add_text('assistance')
    elif msg.topic == 'IDD/syw/multi-distance':
        if 'Out of bed' in msg.payload.decode('UTF-8'):
            add_text('OUT OF BED')

# Every client needs a random ID
client = mqtt.Client(str(uuid.uuid1()))
# configure network encryption etc
client.tls_set()
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