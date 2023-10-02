#!/usr/bin/env python3

# prerequisites: as described in https://alphacephei.com/vosk/install and also python module `sounddevice` (simply run command `pip install sounddevice`)
# Example usage using Dutch (nl) recognition model: `python test_microphone.py -m nl`
# For more help run: `python test_microphone.py -h`

import argparse
import queue
import sys
import json
import time
import sounddevice as sd

from vosk import Model, KaldiRecognizer
from gtts import gTTS
from io import BytesIO
from pydub import AudioSegment
from pydub.playback import _play_with_simpleaudio, play

q = queue.Queue()

def int_or_str(text):
    """Helper function for argument parsing."""
    try:
        return int(text)
    except ValueError:
        return text

def callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))

parser = argparse.ArgumentParser(add_help=False)
parser.add_argument(
    "-l", "--list-devices", action="store_true",
    help="show list of audio devices and exit")
args, remaining = parser.parse_known_args()
if args.list_devices:
    print(sd.query_devices())
    parser.exit(0)
parser = argparse.ArgumentParser(
    description=__doc__,
    formatter_class=argparse.RawDescriptionHelpFormatter,
    parents=[parser])
parser.add_argument(
    "-f", "--filename", type=str, metavar="FILENAME",
    help="audio file to store recording to")
parser.add_argument(
    "-d", "--device", type=int_or_str,
    help="input device (numeric ID or substring)")
parser.add_argument(
    "-r", "--samplerate", type=int, help="sampling rate")
parser.add_argument(
    "-m", "--model", type=str, help="language model; e.g. en-us, fr, nl; default is en-us")
args = parser.parse_args(remaining)

mp3_fp = BytesIO()
tts = gTTS('Hello! I am a drum machine that can play hi hat, bass drum and snare drum sounds. ', lang='en')
tts.save('hello.mp3')


tts = gTTS("Sorry, I don't recognize the instrument you are saying.", lang='en')
tts.save('sorry.mp3')

##################################
# SOUNDS
sounds = {
    'hi-hat': AudioSegment.from_file('short-open-hi-hat.wav'),
    'snare-drum': AudioSegment.from_file('wide-snare-drum_B_minor.wav'),
    'bass-drum': AudioSegment.from_file('bass-drum-hit.wav'),
    'hello': AudioSegment.from_file('hello.mp3'),
    'sorry': AudioSegment.from_file('sorry.mp3')
}

play(sounds['hello'])

try:
    if args.samplerate is None:
        device_info = sd.query_devices(args.device, "input")
        # soundfile expects an int, sounddevice provides a float:
        args.samplerate = int(device_info["default_samplerate"])
        
    if args.model is None:
        model = Model(lang="en-us")
    else:
        model = Model(lang=args.model)

    if args.filename:
        dump_fn = open(args.filename, "wb")
    else:
        dump_fn = None

    with sd.RawInputStream(samplerate=args.samplerate, blocksize = 8000, device=args.device,
            dtype="int16", channels=1, callback=callback):
        print("#" * 80)
        print("Press Ctrl+C to stop the recording")
        print("#" * 80)

        rec = KaldiRecognizer(model, args.samplerate, '["bass", "snare", "drum", "hi", "hat", "[unk]"]')
        last_sorry_playback_time = 0
        while True:
            data = q.get()
            clear = False
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())["text"]
                if (result.find("hi hat") != -1):
                    print("Now playing hi hat.")
                    # playsound("short-open-hi-hat.wav")
                    _play_with_simpleaudio(sounds["hi-hat"])
                elif (result.find("snare drum") != -1): 
                    print("Now playing snare drum.")
                    # playsound("wide-snare-drum_B_minor.wav")
                    _play_with_simpleaudio(sounds["snare-drum"])
                elif (result.find("bass drum") != -1):
                    print("Now playing bass drum.")
                    # playsound("bass-drum-hit.wav")
                    _play_with_simpleaudio(sounds["bass-drum"])
                else:
                    pass
                    # current_time = time.time()
                    # if current_time - last_sorry_playback_time > 10:
                    #     # playsound('sorry.mp3', True)
                    #     _play_with_simpleaudio(sounds["snare-drum"])
                    # last_sorry_playback_time = current_time
                print(result)
            else:
                pass
                # print(rec.PartialResult())
            
            if dump_fn is not None:
                dump_fn.write(data)
            # time.sleep(1)

except KeyboardInterrupt:
    print("\nDone")
    parser.exit(0)
except Exception as e:
    parser.exit(type(e).__name__ + ": " + str(e))
