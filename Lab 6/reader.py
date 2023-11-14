import paho.mqtt.client as mqtt
import uuid
import ssl
import board
import paho.mqtt.client as mqtt
import uuid


import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
# the # wildcard means we subscribe to all subtopics of IDD
topic = 'IDD/#'

# some other examples
# topic = 'IDD/a/fun/topic'
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
height =  disp.height
width = disp.width 
image = Image.new("RGB", (width, height))
draw = ImageDraw.Draw(image)


#this is the callback that gets called once we connect to the broker. 
#we should add our subscribe functions here as well
def on_connect(client, userdata, flags, rc):
	print(f"connected with result code {rc}")
	client.subscribe(topic)
	# you can subsribe to as many topics as you'd like
	# client.subscribe('some/other/topic')

# this is the callback that gets called each time a message is recived
def on_message(cleint, userdata, msg):
    print(f"topic: {msg.topic} msg: {msg.payload.decode('UTF-8')}")
    # you can filter by topics
    if msg.topic == 'IDD/colors':
        rgba = [int(c) for c in str(msg.payload.decode('UTF-8')).split(',')]
        color =tuple(map(lambda x: int(255*(1-(rgba[3]/65536))*255*(x/65536)) , rgba))
        draw.rectangle((0, 0, width, height), fill=color)
        disp.image(image)
    elif msg.topic == 'IDD/votes':
        votes = [int(c) for c in str(msg.payload.decode('UTF-8'))[1:-1].split(',')]
        print('**----------- Current votes -------------**')
        for i in range(len(votes)):
            print(f"Team{i+1}: {votes[i]} votes")
        

# Every client needs a random ID
client = mqtt.Client(str(uuid.uuid1()))
# configure network encryption etc
client.tls_set(cert_reqs=ssl.CERT_NONE)
# this is the username and pw we have setup for the class
client.username_pw_set('idd', 'device@theFarm')

# attach out callbacks to the client
client.on_connect = on_connect
client.on_message = on_message

# connect to the broker
client.connect(
    'farlab.infosci.cornell.edu',
    port=8883)

# this is blocking. to see other ways of dealing with the loop
# https://www.eclipse.org/paho/index.php?page=clients/python/docs/index.php#network-loop
client.loop_forever() 