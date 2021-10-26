import qwiic_button 
import time
import sys

import board
import busio
import adafruit_ssd1306

from PIL import Image, ImageDraw, ImageFont
from adafruit_apds9960.apds9960 import APDS9960

brightness = 10

# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)

apds = APDS9960(i2c)

# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.  Change these
# to the right size for your display!
oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

def run_example():

    print("\nSparkFun Qwiic Button Example 7")
    my_button1 = qwiic_button.QwiicButton()

    if my_button1.begin() == False:
        print("\nThe Qwiic Button 1 isn't connected to the system. Please check your connection", \
            file=sys.stderr)
        return
    print("\nButton ready!")
    
    # Initialize font for text
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 16)

    # start with a blank screen
    oled.fill(0)
    # we just blanked the framebuffer. to push the framebuffer onto the display, we call show()
    oled.show()
    
    # Create blank image for drawing.
    image = Image.new("1", (oled.width, oled.height))
    draw = ImageDraw.Draw(image)

    while 1:
        draw.rectangle((0, 0, oled.width, oled.height * 2), outline=0, fill=0)
        text = 'Press Start!'
        draw.text((0, 0), text, font=font, fill=255)
        oled.image(image)
        oled.show()
        # Check if button 1 is pressed
        if my_button1.is_button_pressed() == True:
            print("\nButton 1 is pressed!")
            # start with a blank screen
            oled.fill(0)
            # we just blanked the framebuffer. to push the framebuffer onto the display, we call show()
            oled.show()
            apds.enable_proximity = True
            start_time = time.time()
            my_button1.LED_on(brightness)
            while True:
                # If proximity sensor triggers, break out of the loop
                if apds.proximity > 0:
                    time.sleep(3)
                    break
                # undraw the previous circle
                draw.rectangle((0, 0, oled.width, oled.height * 2), outline=0, fill=0)
                text = 'Time: '+str(round(time.time()-start_time, 2))
                draw.text((0, 0), text, font=font, fill=255)
                oled.image(image)
                oled.show()
                time.sleep(0.1)
        else:
            my_button1.LED_on(brightness)
            time.sleep(0.5)
            my_button1.LED_off()
        time.sleep(0.5)
    
    # Clear screen
    oled.fill(0)
    # we just blanked the framebuffer. to push the framebuffer onto the display, we call show()
    oled.show()
if __name__ == '__main__':
    try:
        run_example()
    except (KeyboardInterrupt, SystemExit) as exErr:
        print("\nEnding Example 7")
        sys.exit(0)
