import pyaudio
import numpy as np
from scipy.fft import rfft, rfftfreq
from scipy.signal.windows import hann
from numpy_ringbuffer import RingBuffer

import queue
import time


import digitalio
import board
from PIL import Image, ImageDraw
import adafruit_rgb_display.ili9341 as ili9341
import adafruit_rgb_display.st7789 as st7789  # pylint: disable=unused-import
import adafruit_rgb_display.hx8357 as hx8357  # pylint: disable=unused-import
import adafruit_rgb_display.st7735 as st7735  # pylint: disable=unused-import
import adafruit_rgb_display.ssd1351 as ssd1351  # pylint: disable=unused-import
import adafruit_rgb_display.ssd1331 as ssd1331  # pylint: disable=unused-import

# Configuration for CS and DC pins (these are PiTFT defaults):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = digitalio.DigitalInOut(board.D24)

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 24000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# pylint: disable=line-too-long
# Create the display:
# disp = st7789.ST7789(spi, rotation=90,                            # 2.0" ST7789
# disp = st7789.ST7789(spi, height=240, y_offset=80, rotation=180,  # 1.3", 1.54" ST7789
# disp = st7789.ST7789(spi, rotation=90, width=135, height=240, x_offset=53, y_offset=40, # 1.14" ST7789
# disp = hx8357.HX8357(spi, rotation=180,                           # 3.5" HX8357
# disp = st7735.ST7735R(spi, rotation=90,                           # 1.8" ST7735R
# disp = st7735.ST7735R(spi, rotation=270, height=128, x_offset=2, y_offset=3,   # 1.44" ST7735R
# disp = st7735.ST7735R(spi, rotation=90, bgr=True,                 # 0.96" MiniTFT ST7735R
# disp = ssd1351.SSD1351(spi, rotation=180,                         # 1.5" SSD1351
# disp = ssd1351.SSD1351(spi, height=96, y_offset=32, rotation=180, # 1.27" SSD1351
# disp = ssd1331.SSD1331(spi, rotation=180,                         # 0.96" SSD1331
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
# pylint: enable=line-too-long

#height = disp.width  # we swap height/width to rotate it to landscape!
#width = disp.height
#image = Image.new("RGB", (width, height))
rotation = 90

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
if disp.rotation % 180 == 90:
    height = disp.width  # we swap height/width to rotate it to landscape!
    width = disp.height
else:
    width = disp.width  # we swap height/width to rotate it to landscape!
    height = disp.height
image = Image.new("RGB", (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image)

padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

#font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)

#FIX THIS ABOVE TO GET FONTS^^^^


## Please change the following number so that it matches to the microphone that you are using. 
DEVICE_INDEX = 1

## Compute the audio statistics every `UPDATE_INTERVAL` seconds.
UPDATE_INTERVAL = 1.0



### Things you probably don't need to change
FORMAT=np.float32
SAMPLING_RATE = 44100
CHANNELS=1


def main():
    ### Setting up all required software elements: 
    audioQueue = queue.Queue() #In this queue stores the incoming audio data before processing.
    pyaudio_instance = pyaudio.PyAudio() #This is the AudioDriver that connects to the microphone for us.

    def _callback(in_data, frame_count, time_info, status): # This "callbackfunction" stores the incoming audio data in the `audioQueue`
        audioQueue.put(in_data)
        return None, pyaudio.paContinue

    stream = pyaudio_instance.open(input=True,start=False,format=pyaudio.paFloat32,channels=CHANNELS,rate=SAMPLING_RATE,frames_per_buffer=int(SAMPLING_RATE/2),stream_callback=_callback,input_device_index=DEVICE_INDEX)
    
    
    # One essential way to keep track of variables overtime is with a ringbuffer. 
    # As an example the `AudioBuffer` it stores always the last second of audio data. 
    AudioBuffer = RingBuffer(capacity=SAMPLING_RATE*1, dtype=FORMAT) # 1 second long buffer.
    
    # Another example is the `VolumeHistory` ringbuffer. 
    VolumeHistory = RingBuffer(capacity=int(20/UPDATE_INTERVAL), dtype=FORMAT) ## This is how you can compute a history to record changes over time
    ### Here  is a good spot to extend other buffers  aswell that keeps track of varailbes over a certain period of time. 

    nextTimeStamp = time.time()
    stream.start_stream()
    warningCount = 0
    if True:
        while True:
            frames = audioQueue.get() #Get DataFrom the audioDriver (see _callbackfunction how the data arrives)
            if not frames:
                continue

            framesData = np.frombuffer(frames, dtype=FORMAT) 
            AudioBuffer.extend(framesData[0::CHANNELS]) #Pick one audio channel and fill the ringbuffer. 
            
            if(AudioBuffer.is_full and  # Waiting for the ringbuffer to be full at the beginning.
                audioQueue.qsize()<2 and # Make sure there is not alot more new data that should be used. 
                time.time()>nextTimeStamp): # See `UPDATE_INTERVAL` above.

                buffer  = np.array(AudioBuffer) #Get the last second of audio. 


                volume = np.rint(np.sqrt(np.mean(buffer**2))*10000) # Compute the rms volume
                
                
                VolumeHistory.append(volume)
                volumneSlow = volume
                volumechange = 0.0
                if VolumeHistory.is_full:
                    HalfLength = int(np.round(VolumeHistory.maxlen/2)) 
                    vnew = np.array(VolumeHistory)[HalfLength:].mean()
                    vold = np.array(VolumeHistory)[:VolumeHistory.maxlen-HalfLength].mean()
                    volumechange =vnew-vold
                    volumneSlow = np.array(VolumeHistory).mean()
                
                ## Computes the Frequency Foruier analysis on the Audio Signal.
                N = buffer.shape[0] 
                window = hann(N) 
                amplitudes = np.abs(rfft(buffer*window))[25:] #Contains the volume for the different frequency bin.
                frequencies = (rfftfreq(N, 1/SAMPLING_RATE)[:N//2])[25:] #Contains the Hz frequency values. for the different frequency bin.
                '''
                Combining  the `amplitudes` and `frequencies` varialbes allows you to understand how loud a certain frequency is.

                e.g. If you'd like to know the volume for 500Hz you could do the following. 
                1. Find the frequency bin in which 500Hz belis closest to with:
                FrequencyBin = np.abs(frequencies - 500).argmin()
                
                2. Look up the volume in that bin:
                amplitudes[FrequencyBin]


                The example below does something similar, just in revers.
                It finds the loudest amplitued and its coresponding bin  with `argmax()`. 
                The uses the index to look up the Freqeucny value.
                '''


                LoudestFrequency = frequencies[amplitudes.argmax()]
                
                #print("Loudest Frqeuncy:",LoudestFrequency)
                #print("RMS volume:",volumneSlow)
                #print("Volume Change:",volumechange)
                
                nextTimeStamp = UPDATE_INTERVAL+time.time() # See `UPDATE_INTERVAL` above
                
                if 1750 > LoudestFrequency > 750:
                    print("quiet down a little")
                    print("Loudest Frqeuncy:",LoudestFrequency)
                    warningCount+=1
                    print("you have been warned", warningCount, "times")
                    

                elif LoudestFrequency > 1750:
                    print("quiet down a lot!!!")
                    print("Loudest Frqeuncy:",LoudestFrequency)
                    warningCount+=1
                    print("you have been warned", warningCount, "times")

                  #  y = top
                  #  draw.rectangle((x, y, width, height), outline=0, fill=0)
                  #  draw.text((x, y), "Quiet down", fill="#FFFFFF")
                    #draw.text((x, y), "Quiet down", font=font, fill="#FFFFFF") MUST FIX FONT ISSUE
                    #y += font.getsize(drawText)[1] FIX FONT ISSUE 

               ### draw.text((x, y), "You snored. \n Severity : \n4.5 out of 10 \n" + str(volumneSlow), font=font, fill="#FFFFFF")
                   # disp.image(image, rotation)
                   # time.sleep(0.1)

                   #FIX FONT ISSUES TO ADD CODE ABOVE^^^^


if __name__ == '__main__':
    main()
    print("Something happend with the audio example. Stopping!") 





