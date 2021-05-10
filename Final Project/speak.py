import pyttsx3
import importlib
import time

def say(text):
    importlib.reload(pyttsx3)
    engine = pyttsx3.init()
    engine.say(text)
    print(str(text))
    engine.runAndWait()

def speak_by_mode(mode):
	if(mode == 1):
		say("Oh hey, hello!")
	elif(mode == 2):
		say("Who's touching me!")
	elif(mode == 3):
		say("Do you want to know the room tempeture and humidity?")
	elif(mode == 4):
		say("Anyway I will just let you know!")
		time.sleep(0.3)
		say("Since this is the only thing I know!") 
		time.sleep(0.3)
		say("The current tempeture is ...")
	else:
		pass

if __name__ == '__main__':
	t = "test test"
	say(t)
