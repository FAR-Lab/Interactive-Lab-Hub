from display import draw_pibot

SLEEPMODE = 0
WAKEUPMODE = 1
ROTMODE = 2
QUESTIONMODE = 3
RESULTMODE = 4
if __name__ == '__main__':
	mode = SLEEPMODE
	while True:
		draw_pibot(1)
