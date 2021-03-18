from gtts import gTTS
import os

text = 'Hello, I am a (fake) bomb. Diffuse me before the time runs out (or die)'
filename = 'test.mp3'

tts = gTTS(text, lang='en')
tts.save(filename)
os.system("/usr/bin/mplayer " + filename)
