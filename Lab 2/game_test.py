import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789

from Box2D import *
from time import strftime

# Box2D setup: 
# 1) Download conda: wget https://github.com/conda-forge/miniforge/releases/download/23.3.1-1/Mambaforge-23.3.1-1-Linux-aarch64.sh
# 2) Make executable: chmod -v +x Mambaforge*.sh
# 3) Install: ./Mambaforge-23.3.1-1-Linux-aarch64.sh
# 4) Make conda env with Box2D: conda create -n pybox2d -c conda-forge python=3.9 box2d-py
# 5) Activate conda env: conda activate pybox2d
# 6) Install lab 2 requirements: pip install -r requirements.txt

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
# font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 50)
font = ImageFont.truetype("digital-dream/DIGITALDREAMNARROW.ttf", 40)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

# Setup buttons
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

# Write intro text
draw.text((width/2, height/2), "Select", font=font, fill="#1f1f1f", anchor = 'mm')
disp.image(image, rotation)

game_mode = 0

# Loop until user inputs game mode
while game_mode == 0:
    try:
        # convert user input to int within range
        game_mode = int(input('Choose game mode (1 = jump, 2 = static): '))
        if game_mode > 2 or game_mode < 1:
            raise ValueError
    except ValueError:
        # catch invalid game modes
        print("Invalid game mode, try again")
        game_mode = 0

# Clear screen
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)

# Box2D Setup

# Scale in pixels per world unit
scale = 15

class Object:
    name = ""

    def __init__(self, str):
        self.name = str

class myContactListener(b2ContactListener):
    can_jump = False

    def __init__(self):
        b2ContactListener.__init__(self)

    def BeginContact(self, contact):
        print('\n' + contact.fixtureA.body.userData.name + "-" + contact.fixtureB.body.userData.name + " Contact")
        print(contact.fixtureA.body.userData.name + " pos: (" + str(contact.fixtureA.body.position.x) + ", " + str(contact.fixtureA.body.position.y) + ")")
        print(contact.fixtureB.body.userData.name + " pos: (" + str(contact.fixtureB.body.position.x) + ", " + str(contact.fixtureB.body.position.y) + ")")
        self.can_jump = True
    def EndContact(self, contact):
        pass
    def PreSolve(self, contact, oldManifold):
        pass
    def PostSolve(self, contact, impulse):
        pass

def worldToScreen(x):
    return x * scale

def screenToWorld(x):
    return x / scale

fast_grav = (0,-500)
no_grav = (0,0)
# Choose input mode

listener = myContactListener()
world = b2World(contactListener = listener, gravity=fast_grav, doSleep=True)
if game_mode == 2:
    world.gravity = no_grav

p_width = 0.6
p_height = 0.6

p_body = world.CreateDynamicBody(position=(p_width * 2.5, screenToWorld(height)/2), userData = Object("Player"), fixedRotation = True)
p_fixture = p_body.CreatePolygonFixture(box=(p_width,p_height), density=1, friction=0.3)

g_width = screenToWorld(width)/2
g_height = 0.5

g_top = screenToWorld(height) + g_height
g_bot = g_height
if game_mode == 2:
    g_top = screenToWorld(height)
    g_bot = 0

g_body = world.CreateStaticBody(
    position=(screenToWorld(width) / 2, g_top),
    shapes=b2PolygonShape(box = (g_width, g_height)),
    userData = Object("Ceiling")
    )

g_body2 = world.CreateStaticBody(
    position=(screenToWorld(width) / 2, g_bot),
    shapes=b2PolygonShape(box = (g_width, g_height)),
    userData = Object("Floor")
    )

vel_iters, pos_iters = 6, 2
time_step = 1/30
up = (0,30)
down = (0,-30)
stop = (0,0)
jump = (0,100)

def drawRect(body,o_width,o_height,color):
    pos = (worldToScreen(body.position.x), height - worldToScreen(body.position.y))
    t_width = worldToScreen(o_width)
    t_height = worldToScreen(o_height)
    draw.rectangle((pos[0] - t_width, pos[1] - t_height, pos[0] + t_width, pos[1] + t_height), outline=0, fill=color)

while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill="#000000")

    # Static mode controls
    if game_mode == 2:
        if buttonB.value and not buttonA.value:
            p_body.linearVelocity = up 
        if buttonA.value and not buttonB.value:
            p_body.linearVelocity = down
        if not buttonA.value and not buttonB.value:
            p_body.linearVelocity = stop
        if buttonA.value and buttonB.value:
            p_body.linearVelocity = stop
    # Jump mode controls
    else:
        if buttonB.value and not buttonA.value:
            if listener.can_jump:
                listener.can_jump = False
                print('Jump!')
                p_body.linearVelocity = jump 
        if buttonA.value and not buttonB.value:
            pass
        if not buttonA.value and not buttonB.value:
            pass
        if buttonA.value and buttonB.value:
            pass

    world.Step(time_step, vel_iters, pos_iters)
    world.ClearForces()

    time_str = strftime("%I:%M:%S")
    # Draw time text
    draw.text((width/2, height/2), time_str, font=font, fill="#1f1f1f", anchor = 'mm')

    # Draw player
    drawRect(p_body,p_width,p_height,"#00ff00")

    # Draw ground (if visible)
    drawRect(g_body,g_width,g_height,"#36005c")
    drawRect(g_body2,g_width,g_height,"#36005c")

    # Display image.
    disp.image(image, rotation)
    time.sleep(time_step)
