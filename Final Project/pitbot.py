from display import draw_pibot
from Qwiic_Joystick import qwiicjoystick
from speak import speak_by_mode
from servo import oneturn

import smbus, time
bus = smbus.SMBus(1)
addr = 0x20

SLEEPMODE = 0
WAKEUPMODE = 1
ROTMODE = 2
QUESTIONMODE = 3
RESULTMODE = 4

if __name__ == '__main__':
	oneturn()
	mode = SLEEPMODE
	draw_pibot(mode)

	global bus_data, X, Y
	while True:
		direction, selected = qwiicjoystick()
		if selected == 0:
			if mode == RESULTMODE:
				mode = SLEEPMODE
			else:
				mode += 1
			draw_pibot(mode)
			speak_by_mode(mode)
