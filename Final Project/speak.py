import pyttsx3
import importlib

def say(text):
    importlib.reload(pyttsx3)
    engine = pyttsx3.init()
    engine.say(text)
    print(str(text))
    engine.runAndWait()

if __name__ == '__main__':
	t = "test test"
	say(t)
