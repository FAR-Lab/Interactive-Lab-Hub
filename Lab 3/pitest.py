#!/usr/bin/env python3

from vosk import Model, KaldiRecognizer
import sys
import os
import wave
import smbus, time
from screen_test import draw_text

# if not os.path.exists("model"):
#     print ("Please download the model from https://github.com/alphacep/vosk-api/blob/master/doc/models.md and unpack as 'model' in the current folder.")
#     exit (1)


# wf = wave.open("temp.wav", "rb")
# model = Model("model")
# rec = KaldiRecognizer(model, wf.getframerate(), "start test hi hello zero oh one two three four five six seven eight nine [unk]")

# record_command = "record -D hw:2,0 -f cd -c1 -r 48000 -d 5 -t wav temp.wav"

# #JoyStick Control
bus = smbus.SMBus(1)
addr = 0x20

# while True:

#     data = wf.readframes(4000)
#     if len(data) == 0:
#         break
#     if rec.AcceptWaveform(data):
#         print(rec.Result())
#     else:
#         print(rec.PartialResult())

def main():
	global bus_data,X,Y,mode
	while True:
    	# If joystick got pressed
		if qwiicjoystick():
        		mode = 0
        		draw_text(mode)


def qwiicjoystick():
	global bus_data, X, Y
	try:
    		bus_data = bus.read_i2c_block_data(addr, 0x03, 5)
	except Exception as e:
        	print(e)
	X = (bus_data[0]<<8 | bus_data[1])>>6
	Y = (bus_data[2]<<8 | bus_data[3])>>6
	selected = bus_data[4]
	return selected

if __name__ == '__main__':
    main()
