#!/usr/bin/env python3

from vosk import Model, KaldiRecognizer
import sys
import os
import wave

if not os.path.exists("model"):
    print ("Please download the model from https://github.com/alphacep/vosk-api/blob/master/doc/models.md and unpack as 'model' in the current folder.")
    exit (1)

wf = wave.open(sys.argv[1], "rb")
if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
    print ("Audio file must be WAV format mono PCM.")
    exit (1)

model = Model("model")
# You can also specify the possible word list
rec = KaldiRecognizer(model, wf.getframerate(), '["oh one two three four five six seven eight nine zero", "[unk]"]')

while True:
    data = wf.readframes(4000)
    # if len(data) == 0:
        # break
    if rec.AcceptWaveform(data):
        print(rec.Result()[14:-3]) # remove the dictionary syntax
    else:
        print(rec.PartialResult()[14:-3])

print(rec.FinalResult())
