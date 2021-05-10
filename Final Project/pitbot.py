from display import draw_pibot
from Qwiic_Joystick import qwiicjoystick
from speak import speak_by_mode
from servo import oneturn, setup, destroy
import board
import busio
import adafruit_mpr121
import smbus, time

bus = smbus.SMBus(1)
addr = 0x20

i2c = busio.I2C(board.SCL, board.SDA)
mpr121 = adafruit_mpr121.MPR121(i2c)

SLEEPMODE = 0
WAKEUPMODE = 1
ROTMODE = 2
QUESTIONMODE = 3
RESULTMODE = 4

def act(mode):
	if mode == RESULTMODE:
		mode = SLEEPMODE
	else:
		mode += 1
	draw_pibot(mode)
	if mode == ROTMODE:
		setup()
		oneturn()
	speak_by_mode(mode)
	return mode

if __name__ == '__main__':
	mode = SLEEPMODE
	draw_pibot(mode)
	
	global bus_data, X, Y
	while True:
		direction, selected = qwiicjoystick()
		if selected == 0:
			mode = act(mode)
		if mpr121[6].value:
			mode = act(mode)
	destroy()
	
