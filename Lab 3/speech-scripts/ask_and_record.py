#!/usr/bin/env python3

import argparse
import queue
import sys
import sounddevice as sd
import numpy as np
import json
import re
from word2number import w2n

from vosk import Model, KaldiRecognizer

def convert_speech_text_to_numbers(speech_text):
    # Define a regular expression pattern for matching words representing numbers
    pattern = re.compile(r'\b(?:zero|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred|thousand|million|billion|trillion)\b', re.IGNORECASE)
    
    # Find all matching words in the input speech text
    matches = pattern.findall(speech_text)
    
    # Convert the matched words to numbers and store them in a list
    numbers = []
    for match in matches:
        try:
            number = w2n.word_to_num(match)
            numbers.append(number)
        except ValueError as e:
            print(f"Failed to convert {match} to a number: {e}")
    
    return numbers

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

try:
    if args.samplerate is None:
        device_info = sd.query_devices(args.device, "input")
        args.samplerate = int(device_info["default_samplerate"])
        
    if args.model is None:
        model = Model(lang="en-us")
    else:
        model = Model(lang=args.model)

    rec = KaldiRecognizer(model, args.samplerate)

    # Ask for input verbally
    print("Please provide your numerical input after the beep, for example, your phone number.")
    sd.play(np.sin(2 * np.pi * 440 * np.arange(args.samplerate) / args.samplerate), samplerate=args.samplerate)

    with sd.RawInputStream(samplerate=args.samplerate, blocksize = 8000, device=args.device, dtype="int16", channels=1, callback=callback):
        print("#" * 80)
        print("Recording for 5 seconds...")
        print("#" * 80)

        for _ in range(5 * args.samplerate // 8000):  # Record for 5 seconds
            data = q.get()
            if rec.AcceptWaveform(data):
                print(rec.Result())
            else:
                print(rec.PartialResult())
            if args.filename:
                with open(args.filename, "wb") as dump_fn:
                    dump_fn.write(data)

    print("Done recording. Here is your Number:")
    result = json.loads(rec.FinalResult())
    result = result.get("text", "")
    result = convert_speech_text_to_numbers(result)
    result = ''.join([str(item) for item in result])
    print(result)

except KeyboardInterrupt:
    print("\nDone")
    parser.exit(0)
except Exception as e:
    parser.exit(type(e).__name__ + ": " + str(e))
