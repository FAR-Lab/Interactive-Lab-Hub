import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
import busio
import qwiic_twist
import qwiic_joystick
import qwiic_button

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

# Set up the rotary pin
twist = qwiic_twist.QwiicTwist()
twist.begin()
twist_count = 0
twist.set_blue(150)
twist.set_red(0)
twist.set_green(0)

# Set up the joystick
joystick = qwiic_joystick.QwiicJoystick()
joystick.begin()

# Set up first button
redButton = qwiic_button.QwiicButton()
redButton.begin()

greenButton = qwiic_button.QwiicButton(0x63)
greenButton.begin()

dates = ['Sunday\nFebruary 28, 2021',
         'Monday\nMarch 1, 2021',
         'Tuesday\nMarch 2, 2021',
         'Wednesday\nMarch 3, 2021',
         'Thursday\nMarch 4, 2021',
         'Friday\nMarch 5, 2021',
         'Saturday\nMarch 6, 2021']
times = ['12:00 AM', '12:30 AM', '01:00 AM', '01:30 AM', '02:00 AM', '02:30 AM', '03:00 AM', '03:30 AM',
         '04:00 AM', '04:30 AM', '05:00 AM', '05:30 AM', '06:00 AM', '06:30 AM', '07:00 AM', '07:30 AM',
         '08:00 AM', '08:30 AM', '09:00 AM', '09:30 AM', '10:00 AM', '10:30 AM', '11:00 AM', '11:30 AM',
         '12:00 PM', '12:30 PM', '01:00 PM', '01:30 PM', '02:00 PM', '02:30 PM', '03:00 PM', '03:30 PM',
         '04:00 PM', '04:30 PM', '05:00 PM', '05:30 PM', '06:00 PM', '06:30 PM', '07:00 PM', '07:30 PM',
         '08:00 PM', '08:30 PM', '09:00 PM', '09:30 PM', '10:00 PM', '10:30 PM', '11:00 PM', '11:30 PM']

def image_formatting(image2, width, height):
    image2 = image2.convert('RGB')
    # Scale the image to the smaller screen dimension
    image2 = image2.resize((240, 135), Image.BICUBIC)

    return image2

while True:
    # Draw a black filled box to clear the image.
    twist_time = twist.count
    twist_date = twist_time // 48
    clock_time = twist_time % 48

    # Start wine time if it is 5pm on Friday
    if twist_date == 5 and clock_time == 34:
        while not redButton.is_button_pressed():
            image3 = Image.open("/home/pi/Documents/Interactive-Lab-Hub/Lab 2/imgs/winetime.png")
            image3 = image_formatting(image3, width, height)
            disp.image(image3, rotation)

            redButton.LED_on(255)
            time.sleep(1)
            redButton.LED_off()
            time.sleep(1)

        for i in range(0, 9):
            image4 = Image.open(f"/home/pi/Documents/Interactive-Lab-Hub/Lab 2/imgs/cheers{i}.png")
            image4 = image_formatting(image4, width, height)
            disp.image(image4, rotation)

            time.sleep(0.5)
        twist.set_count(twist.count + 1)

    image2 = Image.open("/home/pi/Documents/Interactive-Lab-Hub/Lab 2/imgs/" + times[clock_time].replace(':','').replace(' ','').replace('AM','am').replace('PM','pm') + '.png')
    image2 = image_formatting(image2, width, height)

    # Get drawing object to draw on image.
    draw = ImageDraw.Draw(image2)

    # Write the time
    y = top
    x = 4
    draw.text((x, y), dates[twist_date], font=font, fill="#000000")
    y += 2 * font.getsize(dates[twist_date])[1]
    draw.text((x, y), times[clock_time], font=font, fill="#000000")
    #draw.text((x, y), time.strftime("%m/%d/%Y %H:%M:%S"), font=font, fill="#FFFFFF")

    #print(f"Rotary Count: {twist.count}")
    #print(f"Joystick Position: X: {joystick.get_horizontal()}, Y: {joystick.get_vertical()}, Button: {joystick.check_button()}")
    #print(f"Red Button: {redButton.is_button_pressed()}")
    #print(f"Green Button: {greenButton.is_button_pressed()}")

    # Display image.
    disp.image(image2, rotation)
    time.sleep(0.1)
