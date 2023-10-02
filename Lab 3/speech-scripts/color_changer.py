#!/usr/bin/env python3

# prerequisites: as described in https://alphacephei.com/vosk/install and also python module `sounddevice` (simply run command `pip install sounddevice`)
# Example usage using Dutch (nl) recognition model: `python test_microphone.py -m nl`
# For more help run: `python test_microphone.py -h`

import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789

import argparse
import queue
import sys
import sounddevice as sd

from vosk import Model, KaldiRecognizer

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

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True


q = queue.Queue()

def int_or_str(text):
    """Helper function for argument parsing."""
    try:
        return int(text)
    except ValueError:
        return text

def callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))

parser = argparse.ArgumentParser(add_help=False)
parser.add_argument(
    "-l", "--list-devices", action="store_true",
    help="show list of audio devices and exit")
args, remaining = parser.parse_known_args()
if args.list_devices:
    print(sd.query_devices())
    parser.exit(0)
parser = argparse.ArgumentParser(
    description=__doc__,
    formatter_class=argparse.RawDescriptionHelpFormatter,
    parents=[parser])
parser.add_argument(
    "-f", "--filename", type=str, metavar="FILENAME",
    help="audio file to store recording to")
parser.add_argument(
    "-d", "--device", type=int_or_str,
    help="input device (numeric ID or substring)")
parser.add_argument(
    "-r", "--samplerate", type=int, help="sampling rate")
parser.add_argument(
    "-m", "--model", type=str, help="language model; e.g. en-us, fr, nl; default is en-us")
args = parser.parse_args(remaining)

try:
    if args.samplerate is None:
        device_info = sd.query_devices(args.device, "input")
        # soundfile expects an int, sounddevice provides a float:
        args.samplerate = int(device_info["default_samplerate"])
        
    if args.model is None:
        model = Model(lang="en-us")
    else:
        model = Model(lang=args.model)

    if args.filename:
        #dump_fn = open(args.filename, "wb")
        text_fn = open(args.filename, 'w+')
    else:
        #dump_fn = None
        text_fn = None
    with sd.RawInputStream(samplerate=args.samplerate, blocksize = 8000, device=args.device,
            dtype="int16", channels=1, callback=callback):
        print("#" * 80)
        print("Press Ctrl+C to stop the recording")
        print("#" * 80)

        rec = KaldiRecognizer(model, args.samplerate)
        start = time.time()
        
        color = ""
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                # print(rec.Result())
                text_fn.write(rec.Result())
            else:
                print(rec.PartialResult())
                text_fn.write(rec.PartialResult())

            if ("red" in(rec.PartialResult()) or "read" in(rec.PartialResult())): 
                color = "#FF0000"
                # print(color)
                draw.rectangle((0, 0, width, height), outline=0, fill= color)
                disp.image(image, rotation)
                # break
           
            if ("blue" in(rec.PartialResult())): 
                color = "#0335fc"
                # print(color)
                draw.rectangle((0, 0, width, height), outline=0, fill= color)
                disp.image(image, rotation)
                # break
           
            if ("green" in(rec.PartialResult())):
                color = "#05781e"
                # print(color)
                draw.rectangle((0, 0, width, height), outline=0, fill= color)
                disp.image(image, rotation)
                # break
            
            if ("yellow" in(rec.PartialResult())):
                color = "#f2ee02"
                # print(color)
                draw.rectangle((0, 0, width, height), outline=0, fill= color)
                disp.image(image, rotation)
                # break

            if ("orange" in(rec.PartialResult())):
                color = "#e69812"
                # print(color)
                draw.rectangle((0, 0, width, height), outline=0, fill= color)
                disp.image(image, rotation)
                # break

            if ("purple" in(rec.PartialResult())):
                color = "#821bb5"
                # print(color)
                draw.rectangle((0, 0, width, height), outline=0, fill= color)
                disp.image(image, rotation)
                # break
            
            if ("white" in(rec.PartialResult())): 
                color = "#FFFFFF"
                # print(color)
                draw.rectangle((0, 0, width, height), outline=0, fill= color)
                disp.image(image, rotation)
                # break

            if ("black" in(rec.PartialResult())):
                color = "#000000"
                # print(color)
                draw.rectangle((0, 0, width, height), outline=0, fill= color)
                disp.image(image, rotation)
                # break

            if ("pink" in(rec.PartialResult()) or "thank" in(rec.PartialResult()) or "paint" in(rec.PartialResult()) or "think" in(rec.PartialResult())):
                color = "#f781c6"
                # print(color)
                draw.rectangle((0, 0, width, height), outline=0, fill= color)
                disp.image(image, rotation)
                # break
            
            if ("stop" in(rec.PartialResult())): 
                color = "#000000"
                draw.rectangle((0, 0, width, height), outline=0, fill= color)
                disp.image(image, rotation)  
                break

        

                  

except KeyboardInterrupt:
    print("\nDone")
    parser.exit(0)
except Exception as e:
    parser.exit(type(e).__name__ + ": " + str(e))

