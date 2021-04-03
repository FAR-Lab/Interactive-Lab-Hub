import time
import board
import busio
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import adafruit_mpr121

i2c = busio.I2C(board.SCL, board.SDA)

mpr121 = adafruit_mpr121.MPR121(i2c)

while True:
    for i in range(12):
        if mpr121[i].value:
            print(f"Banana {i} touched!")


        if mpr121[i].value == 1:
            # Setting some variables for our reset pin etc.
            RESET_PIN = digitalio.DigitalInOut(board.D4)

            i2c = board.I2C()
            oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

            # Clear display.
            oled.fill(0)
            oled.show()

            # Create blank image for drawing.
            image = Image.new("1", (oled.width, oled.height))
            draw = ImageDraw.Draw(image)

            # Load a font in 2 different sizes.
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 16)
            font2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)

            offset = 0  # flips between 0 and 32 for double buffering

            while True:
                # write the current time to the display after each scroll
                draw.rectangle((0, 0, oled.width, oled.height * 2), outline=0, fill=0)
                text = time.strftime("%A")
                draw.text((0, 0), text, font=font, fill=255)
                text = time.strftime("%e %b %Y")
                draw.text((0, 14), text, font=font, fill=255)
                text = time.strftime("%X")
                draw.text((0, 36), text, font=font2, fill=255)
                oled.image(image)
                oled.show()

                time.sleep(1)

                for i in range(0, oled.height // 2):
                    offset = (offset + 1) % oled.height
                    oled.write_cmd(adafruit_ssd1306.SET_DISP_START_LINE | offset)
                    oled.show()
                    time.sleep(0.001)


        if mpr121[i].value == 3:
            # Create the I2C interface.
            i2c = busio.I2C(SCL, SDA)

            # Create the SSD1306 OLED class.
            # The first two parameters are the pixel width and pixel height.  Change these
            # to the right size for your display!
            disp = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

            # Note you can change the I2C address, or add a reset pin:
            # disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c, addr=0x3c, reset=reset_pin)

            # Clear display.
            disp.fill(0)
            disp.show()

            # Load image based on OLED display height.  Note that image is converted to 1 bit color.
            if disp.height == 64:
                image = Image.open("happycat_oled_64.ppm").convert("1")
            else:
                image = Image.open("happycat_oled_32.ppm").convert("1")

            # Alternatively load a different format image, resize it, and convert to 1 bit color.
            # image = Image.open('happycat.png').resize((disp.width, disp.height), Image.ANTIALIAS).convert('1')

            # Display image.
            disp.image(image)
            disp.show()



        if mpr121[i].value == 10:
            disp.fill(0)
            disp.show()

            # Create blank image for drawing.
            # Make sure to create image with mode '1' for 1-bit color.
            width = disp.width
            height = disp.height
            image = Image.new("1", (width, height))

            # Get drawing object to draw on image.
            draw = ImageDraw.Draw(image)

            # Draw a black filled box to clear the image.
            draw.rectangle((0, 0, width, height), outline=0, fill=0)

            # Draw some shapes.
            # First define some constants to allow easy resizing of shapes.
            padding = 2
            shape_width = 20
            top = padding
            bottom = height - padding
            # Move left to right keeping track of the current x position for drawing shapes.
            x = padding
            # Draw an ellipse.
            draw.ellipse((x, top, x + shape_width, bottom), outline=255, fill=0)
            x += shape_width + padding
            # Draw a rectangle.
            draw.rectangle((x, top, x + shape_width, bottom), outline=255, fill=0)
            x += shape_width + padding
            # Draw a triangle.
            draw.polygon(
                [(x, bottom), (x + shape_width / 2, top), (x + shape_width, bottom)],
                outline=255,
                fill=0,
            )
            x += shape_width + padding
            # Draw an X.
            draw.line((x, bottom, x + shape_width, top), fill=255)
            draw.line((x, top, x + shape_width, bottom), fill=255)
            x += shape_width + padding

            # Load default font.
            font = ImageFont.load_default()

            # Alternatively load a TTF font.  Make sure the .ttf font file is in the
            # same directory as the python script!
            # Some other nice fonts to try: http://www.dafont.com/bitmap.php
            # font = ImageFont.truetype('Minecraftia.ttf', 8)

            # Write two lines of text.
            draw.text((x, top), "Hello", font=font, fill=255)
            draw.text((x, top + 20), "World!", font=font, fill=255)

            # Display image.
            disp.image(image)
            disp.show()


        if mpr121[i].value == 8:

            # Get display width and height.
            width = disp.width
            height = disp.height

            # Clear display.
            disp.fill(0)
            disp.show()

            # Create image buffer.
            # Make sure to create image with mode '1' for 1-bit color.
            image = Image.new("1", (width, height))

            # Load default font.
            font = ImageFont.load_default()

            # Alternatively load a TTF font.  Make sure the .ttf font file is in the
            # same directory as this python script!
            # Some nice fonts to try: http://www.dafont.com/bitmap.php
            # font = ImageFont.truetype('Minecraftia.ttf', 8)

            # Create drawing object.
            draw = ImageDraw.Draw(image)

            # Define text and get total width.
            text = (
                "William Zhang's Camera"
            )
            maxwidth, unused = draw.textsize(text, font=font)

            # Set animation and sine wave parameters.
            amplitude = height / 4
            offset = height / 2 - 4
            velocity = -2
            startpos = width

            # Animate text moving in sine wave.
            print("Press Ctrl-C to quit.")
            pos = startpos
            while True:
                # Clear image buffer by drawing a black filled box.
                draw.rectangle((0, 0, width, height), outline=0, fill=0)
                # Enumerate characters and draw them offset vertically based on a sine wave.
                x = pos
                for i, c in enumerate(text):
                    # Stop drawing if off the right side of screen.
                    if x > width:
                        break
                    # Calculate width but skip drawing if off the left side of screen.
                    if x < -10:
                        char_width, char_height = draw.textsize(c, font=font)
                        x += char_width
                        continue
                    # Calculate offset from sine wave.
                    y = offset + math.floor(amplitude * math.sin(x / float(width) * 2.0 * math.pi))
                    # Draw text.
                    draw.text((x, y), c, font=font, fill=255)
                    # Increment x position based on chacacter width.
                    char_width, char_height = draw.textsize(c, font=font)
                    x += char_width

                # Draw the image buffer.
                disp.image(image)
                disp.show()

                # Move position for next frame.
                pos += velocity
                # Start over if text has scrolled completely off left side of screen.
                if pos < -maxwidth:
                    pos = startpos

                # Pause briefly before drawing next frame.
                time.sleep(0.05)

    time.sleep(0.25)  # Small delay to keep from spamming output messages.

