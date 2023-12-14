import pydub
import os
files = os.listdir()
for file in files:
    if file.endswith(".wav"):
        sound = pydub.AudioSegment.from_wav(file)
        sound.export(file[:-4]+".mp3", format="mp3")