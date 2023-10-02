#!/usr/bin/env python3

# prerequisites: as described in https://alphacephei.com/vosk/install and also python module `sounddevice` (simply run command `pip install sounddevice`)
# Example usage using Dutch (nl) recognition model: `python test_microphone.py -m nl`
# For more help run: `python test_microphone.py -h`

import argparse
import queue
import sys
import json
import time
# import keyboard
import sounddevice as sd

from vosk import Model, KaldiRecognizer
# from playsound import playsound
from pydub import AudioSegment
from pydub.playback import _play_with_simpleaudio
from gtts import gTTS
from io import BytesIO

import board
import busio
import adafruit_mpr121

i2c = busio.I2C(board.SCL, board.SDA)
mpr121 = adafruit_mpr121.MPR121(i2c)

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
tts = gTTS('Hello! I am a drum machine that can play hi hat, bass drum and snare drum sounds. If you say start, I can record your beats and repeat them. Say clear to stop the recording.', lang='en')
# tts = gTTS('Hello!', lang='en')
tts.save('hello.mp3')

# tts = gTTS("Sorry, I don't recognize the instrument you are saying.", lang='en')
# tts = gTTS("Sorry.", lang='en')
# tts.save('sorry.wav')

##################################
# SOUNDS
sounds = {
    'hi-hat': AudioSegment.from_file('short-open-hi-hat.wav'),
    'snare-drum': AudioSegment.from_file('wide-snare-drum_B_minor.wav'),
    'bass-drum': AudioSegment.from_file('bass-drum-hit.wav'),
    'hello': AudioSegment.from_file('hello.mp3'),
    'sorry': AudioSegment.from_file('sorry.mp3')
}

# playsound("hello.mp3")
_play_with_simpleaudio(sounds['hello'])

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

        rec = KaldiRecognizer(model, args.samplerate, '["bass", "snare", "drum", "hi", "hat", "start", "clear", "[unk]"]')
        last_sorry_playback_time = 0

        sound_name = ""
        recording = False
        playback = False
        start_time = 0
        i = 0
        time_list = []

        while True:
            data = q.get()
            clear = False
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())["text"]
                if (result.find("hi hat") != -1):
                    print("Switching to hi hat.")
                    sound_name = "hi-hat"
                    # playsound("short-open-hi-hat.wav")
                elif (result.find("snare drum") != -1):
                    print("Switching to snare drum.")
                    sound_name = "snare-drum"
                    # playsound("wide-snare-drum_B_minor.wav")
                elif (result.find("bass drum") != -1):
                    print("Switching to bass drum.")
                    sound_name = "bass-drum"
                    # playsound("bass-drum-hit.wav")
                elif (result.find("start") != -1):
                    recording = True
                    start_time = time.time()
                elif (result.find("clear") != -1):
                    recording = False
                    time_list = []
                elif sound_name == "":
                    # sound_name = ""
                    current_time = time.time()
                    # if current_time - last_sorry_playback_time > 10:
                        # playsound('sorry.mp3', True)
                        # _play_with_simpleaudio(sounds['sorry'])
                    last_sorry_playback_time = current_time
                print(result)
            else:
                pass
                # print(rec.PartialResult())
            if playback:
                if (time.time() - playback_time > 4):
                    # Loop recording
                    playback_time = time.time()
                    start_time = playback_time
                    i = 0
                    print("loop")
                elif (i < len(time_list) and time.time() - playback_time >= time_list[i][0]):
                    _play_with_simpleaudio(sounds[time_list[i][1]])
                    # playsound(time_list[i][1], False)
                    i = i + 1
            elif recording and time.time() - start_time > 4:
                # play back
                playback = True
                playback_time = time.time()
                print("start playback")

            if sound_name != "" and mpr121[2].value:
                if recording and time.time() - start_time < 4:
                    time_list.append((time.time() - start_time, sound_name))
                    time_list = sorted(time_list, key=lambda tup: tup[0]) # sort time_list by time (first entry)
                    print(time_list)
                    if not playback:
                        _play_with_simpleaudio(sounds[sound_name])
                        # playsound(sound_name, False)
                else:
                    _play_with_simpleaudio(sounds[sound_name])
                    # playsound(sound_name, False)



            if dump_fn is not None:
                dump_fn.write(data)
            # time.sleep(1)

except KeyboardInterrupt:
    print("\nDone")
    parser.exit(0)
except Exception as e:
    parser.exit(type(e).__name__ + ": " + str(e))
