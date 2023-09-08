import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
from time import strftime, sleep
from datetime import datetime

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

# Build Font
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)

# Turn On the Backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

def seconds(sec):
  return sec

def minutes(sec):
  return seconds(sec) // 60

def hours(sec):
  return minutes(sec) // 60

def days(sec):
  return hours(sec) // 24

states = {
  0:seconds,
  1:minutes,
  2:hours,
  3:days
}
units = {
  0:"seconds",
  1:"minutes",
  2:"hours",
  3:"days"
}
index = 0
index2 = 0

while True:

  today = datetime.now()
  start_year = datetime(today.year, 1, 1)
  next_year = datetime(today.year+1, 1, 1)

  time_since = today - start_year
  time_until = next_year - today

  seconds_since = time_since.seconds + (24*60*60*time_since.days)
  seconds_until = time_until.seconds + (24*60*60*time_until.days)

  if buttonA.value and buttonB.value:

    output_since = states[index](seconds_since)
    output_until = states[index](seconds_until)

  elif not buttonA.value and buttonB.value:

    index = int(index + 1) % len(states)
    output_since = states[index](seconds_since)
    output_until = states[index](seconds_until)
    time.sleep(0.5)

  elif not buttonB.value and buttonA.value:

    index = int(index - 1) % len(states)
    output_since = states[index](seconds_since)
    output_until = states[index](seconds_until)
    time.sleep(0.5)

  else:

    index2 += 1
    time.sleep(0.5)

  # Draw a black filled box to clear the image.
  draw.rectangle((0, 0, width, height), outline=0, fill=0)

  since = f"Time Since: {output_since:,d} {units[index]}"
  until = f"Time Until: {output_until:,d} {units[index]}"

  title = [f"Time Since 1/1/23: ", f"Time Until 1/1/24: "][index2 % 2]
  output = [f"{output_since:,d}",f"{output_until:,d}"][index2 % 2]
  unit = units[index]

  y = top
  draw.text((x,y), title, font=font, end="", flush=True, fill="#FFFFFF")
  y += 24
  draw.text((x,y), output, font=font, end="", flush=True, fill="#FFFFFF")
  y += 24
  draw.text((x,y), unit, font=font, end="", flush=True, fill="#FFFFFF")

  # Display image.
  disp.image(image, rotation)
  time.sleep(0.01)