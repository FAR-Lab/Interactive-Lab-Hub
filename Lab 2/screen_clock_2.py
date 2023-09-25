import time
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789

# Configuration for CS and DC pins:
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate:
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

# Create blank image for drawing:
height = disp.width
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image:
draw = ImageDraw.Draw(image)

# Define font (ensure the font file is in the correct directory):
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)

# Turn on the backlight:
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

cycle_time = 10  # Cycle time in seconds
start_time = time.time()

def draw_sand_clock():
    current_time = time.time()
    elapsed_time = current_time - start_time
    phase = (elapsed_time % cycle_time) / cycle_time

    # Sand clock parameters:
    sand_clock_width = 40
    sand_clock_height = 80
    sand_clock_color = (255, 255, 255)

    # Calculate sand clock coordinates:
    sand_clock_x = (width - sand_clock_width) // 2
    sand_clock_y = (height - sand_clock_height) // 2

    # Draw upper and lower triangle outlines:
    draw.polygon([
        (sand_clock_x, sand_clock_y),
        (sand_clock_x + sand_clock_width, sand_clock_y),
        (sand_clock_x + sand_clock_width // 2, sand_clock_y + sand_clock_height // 2)
    ], outline=sand_clock_color)

    draw.polygon([
        (sand_clock_x, sand_clock_y + sand_clock_height),
        (sand_clock_x + sand_clock_width, sand_clock_y + sand_clock_height),
        (sand_clock_x + sand_clock_width // 2, sand_clock_y + sand_clock_height // 2)
    ], outline=sand_clock_color)

    # Calculate filling level based on elapsed time:
    fill_level = int(sand_clock_height // 2 * phase)

    # Draw filled upper triangle:
    draw.polygon([
        (sand_clock_x, sand_clock_y),
        (sand_clock_x + sand_clock_width, sand_clock_y),
        (sand_clock_x + sand_clock_width // 2, sand_clock_y + sand_clock_height // 2 - fill_level)
    ], outline=sand_clock_color, fill=sand_clock_color)

    # Draw filled lower triangle:
    draw.polygon([
        (sand_clock_x, sand_clock_y + sand_clock_height),
        (sand_clock_x + sand_clock_width, sand_clock_y + sand_clock_height),
        (sand_clock_x + sand_clock_width // 2, sand_clock_y + sand_clock_height // 2 + fill_level)
    ], outline=sand_clock_color, fill=sand_clock_color)

while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    current_time = time.time()
    elapsed_time = current_time - start_time
    phase = (elapsed_time % cycle_time) / cycle_time

    # Sand clock parameters
    sand_clock_width = 40
    sand_clock_height = 80
    sand_clock_color = (255, 255, 255)

    # Calculate sand clock coordinates
    sand_clock_x = (width - sand_clock_width) // 2
    sand_clock_y = (height - sand_clock_height) // 2

    # Draw upper and lower triangle outlines
    draw.polygon([
        (sand_clock_x, sand_clock_y),
        (sand_clock_x + sand_clock_width, sand_clock_y),
        (sand_clock_x + sand_clock_width // 2, sand_clock_y + sand_clock_height // 2)
    ], outline=sand_clock_color)
    draw.polygon([
        (sand_clock_x, sand_clock_y + sand_clock_height),
        (sand_clock_x + sand_clock_width, sand_clock_y + sand_clock_height),
        (sand_clock_x + sand_clock_width // 2, sand_clock_y + sand_clock_height // 2)
    ], outline=sand_clock_color)

    # Calculate filling level based on elapsed time:
    fill_level_upper = sand_clock_height // 2 - int(sand_clock_height // 2 * phase)
    fill_level_lower = int(sand_clock_height // 2 * phase)

    # Draw filled upper triangle:
    draw.polygon([
        (sand_clock_x, sand_clock_y),
        (sand_clock_x + sand_clock_width, sand_clock_y),
        (sand_clock_x + sand_clock_width // 2, sand_clock_y + fill_level_upper)
    ], outline=sand_clock_color, fill=sand_clock_color)

    # Draw filled lower triangle:
    draw.polygon([
        (sand_clock_x, sand_clock_y + sand_clock_height),
        (sand_clock_x + sand_clock_width, sand_clock_y + sand_clock_height),
        (sand_clock_x + sand_clock_width // 2, sand_clock_y + sand_clock_height - fill_level_lower)
    ], outline=sand_clock_color, fill=sand_clock_color)

    # Display the image:
    disp.image(image, rotation)

    # Pause before the next loop iteration:
    time.sleep(1)
