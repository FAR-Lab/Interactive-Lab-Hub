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
import adafruit_mpu6050
from adafruit_apds9960.apds9960 import APDS9960
import os

cwd = os.getcwd()

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
twist.set_blue(255)
twist.set_red(100)
twist.set_green(255)

# Set up the joystick
joystick = qwiic_joystick.QwiicJoystick()
joystick.begin()

# Set up first button
redButton = qwiic_button.QwiicButton()
redButton.begin()

greenButton = qwiic_button.QwiicButton(0x62)
greenButton.begin()

# Configure the accelerometer
i2c = busio.I2C(board.SCL, board.SDA)
mpu = adafruit_mpu6050.MPU6050(i2c)

# Configure the light sensor
int_pin = digitalio.DigitalInOut(board.D21)
apds = APDS9960(i2c, interrupt_pin=int_pin)
apds.enable_proximity = True
apds.proximity_interrupt_threshold = (0, 175)
apds.enable_proximity_interrupt = True

# Configure screen buttons
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

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

    # Check into work at 9am on weekdays
    """    if twist_date in [1,2,3,4,5] and clock_time == 18:
        while buttonA.value:
            image8 = Image.open("/home/pi/Documents/Interactive-Lab-Hub/Lab 2/imgs/gotowork.png")
            image8 = image_formatting(image8, width, height)

            # Get drawing object to draw on image.
            draw = ImageDraw.Draw(image8)

            # Write the time
            y = 50
            x = 50
            draw.text((x, y), "Check in to work", font=font, fill="#000000")

            disp.image(image8, rotation)
        twist.set_count(twist.count + 1)

    # Check out of work at 5pm on weekdays
    if twist_date in [1,2,3,4,5] and clock_time == 34:
        while buttonB.value:
            image9 = Image.open("/home/pi/Documents/Interactive-Lab-Hub/Lab 2/imgs/leavework.png")
            image9 = image_formatting(image9, width, height)

            # Get drawing object to draw on image.
            draw = ImageDraw.Draw(image9)

            # Write the time
            y = 50
            x = 50
            draw.text((x, y), "Check out of work", font=font, fill="#000000")

            disp.image(image9, rotation)
        twist.set_count(twist.count + 1)
    """
    # Start wine time if it is 5pm on Friday
    if twist_date == 5 and clock_time == 35:
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

    if greenButton.is_button_pressed():
        accel_move = False
        accel_quota = 0
        image4 = Image.open("/home/pi/Documents/Interactive-Lab-Hub/Lab 2/imgs/dinnertime.png")
        image4 = image_formatting(image4, width, height)
        disp.image(image4, rotation)

        while not accel_move:
            greenButton.LED_on(255)
            time.sleep(1)
            greenButton.LED_off()
            time.sleep(1)

            accel_value = (mpu.acceleration[0]**2 + mpu.acceleration[1]**2 + mpu.acceleration[2]**2)**0.5
            print(accel_value)
            if accel_value > 14:
                accel_quota += 1

            if accel_quota > 2:
                accel_move = True

        image5 = Image.open("/home/pi/Documents/Interactive-Lab-Hub/Lab 2/imgs/yum.png")
        image5 = image_formatting(image5, width, height)
        disp.image(image5, rotation)
        time.sleep(1)

    if not int_pin.value:
        image6 = Image.open("/home/pi/Documents/Interactive-Lab-Hub/Lab 2/imgs/bedtime.png")
        image6 = image_formatting(image6, width, height)
        disp.image(image6, rotation)

        time.sleep(2)
        twist.set_count(twist.count + 14)
        twist_time = twist.count
        twist_date = twist_time // 48
        clock_time = twist_time % 48

        while apds.proximity > 100:
            pass

        apds.clear_interrupt()

    if twist_date == 0 and clock_time == 20:
        soccer_time_img = Image.open(f"{cwd}/imgs/soccer_time.jpg")
        soccer_time_img = image_formatting(soccer_time_img, width, height)
        disp.image(soccer_time_img, rotation)
        time.sleep(2)

        while joystick.get_horizontal() == 510 and joystick.get_vertical() == 505:
            soccer_start_img = Image.open(f"{cwd}/imgs/kick0.png")
            soccer_start_img = image_formatting(soccer_start_img, width, height)
            disp.image(soccer_start_img, rotation)
            time.sleep(0.5)

        for i in range(1, 12):
            kick_img = Image.open(f"{cwd}/imgs/kick{i}.png")
            kick_img = image_formatting(kick_img, width, height)
            disp.image(kick_img, rotation)
            time.sleep(0.05)

        goal_img = Image.open(f"{cwd}/imgs/goooooal.png")
        goal_img = image_formatting(goal_img, width, height)
        disp.image(goal_img, rotation)
        time.sleep(2)
        while joystick.get_horizontal() != 510 and joystick.get_vertical() != 505:
            time.sleep(1)
        twist.set_count(twist.count + 2)

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
    #if redButton.is_button_pressed():
    #    print('Red Button Pressed')
    #if greenButton.is_button_pressed():
    #    print('Green Button Pressed')

    # Display image.
    disp.image(image2, rotation)
    time.sleep(0.01)
