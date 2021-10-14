from vosk import Model, KaldiRecognizer
import subprocess
import os
import wave
import json
import board
from adafruit_seesaw import seesaw, rotaryio, digitalio

# For use with the STEMMA connector on QT Py RP2040
# import busio
# i2c = busio.I2C(board.SCL1, board.SDA1)
# seesaw = seesaw.Seesaw(i2c, 0x36)

seesaw = seesaw.Seesaw(board.I2C(), addr=0x36)

seesaw_product = (seesaw.get_version() >> 16) & 0xFFFF
print("Found product {}".format(seesaw_product))
if seesaw_product != 4991:
    print("Wrong firmware loaded?  Expected 4991")

seesaw.pin_mode(24, seesaw.INPUT_PULLUP)
button = digitalio.DigitalIO(seesaw, 24)
button_held = False

encoder = rotaryio.IncrementalEncoder(seesaw)
last_position = None

if not os.path.exists("../model"):
    print ("Please download the model from https://github.com/alphacep/vosk-api/blob/master/doc/models.md and unpack as 'model' in the current folder.")
    exit (1)

USER_INPUT_FILE = "user_input.wav"
model = Model("../model")

def speak(instruction):
    command = """
        say() { 
            local IFS=+;/usr/bin/mplayer -ao alsa -really-quiet -noconsolecontrols "http://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&q=$*&tl=en"; 
        } ; 
    """ + f"say '{instruction}'"
    subprocess.call(command, shell=True)

def dont_understand():
    speak("What, what are you saying? I don’t understand.")

def record_user_input():
    subprocess.call("arecord -D hw:2,0 -f cd -c1 -r 48000 -d 5 -t wav " + USER_INPUT_FILE, shell=True)


def recognize(pattern):
    wf = wave.open(USER_INPUT_FILE, "rb")
    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
        print ("Audio file must be WAV format mono PCM.")
        exit (1)

    rec = KaldiRecognizer(model, wf.getframerate(), pattern)

    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            res = json.loads(rec.Result())
            print("Result:", res['text'])
            return res['text']
        # else:
        #     print(rec.PartialResult())
    print("Failed to recognize")
    return ""



button_held = False
while True:
    subprocess.call("aplay ring.wav", shell=True)
    if not button.value and not button_held:
        button_held = True
        break
    if button.value and button_held:
        button_held = False
        break

speak("Is this 911? Hi, I need help, please! Can you help me?")
while True:
    record_user_input()
    result = recognize("yes sure yeah of course")
    if result != "":
        break
    dont_understand()
    speak("Can you help me?")

speak("I lost my memory and I’m now trapped in a room! There’s no one with me, and I don’t remember anything!")
speak("So um...I’m in a study I guess, there’s a door, let me see. It’s locked. There are many books on a bookshelf. There’s a painting on the wall. And it’s just like a regular study...")
speak("Which one should I check first?")
while True:
    record_user_input()
    result = recognize("door painting bookshelf")
    if "door" in result:
        speak("Ok I'm checking the door now...It’s still locked!")
    elif "painting" in result:
        speak("There is nothing special with the painting.")
    elif "bookshelf" in result:
        speak("Ok, I’ll check the bookshelf.")
        speak("Oh! There’s a book that looks strange, let me check." + 
        "Oh my god, the book is carved hollow inside and there’s a key in it!")
        break
    else:
        dont_understand()
    speak("Should I check the door, the painting, or the bookshelf?")

speak("What do you want me to do with the key?")
while True:
    record_user_input()
    result = recognize("door")
    if "door" in result:
        break
    else:
        dont_understand()
    speak("What do you want me to do with the key?")

speak("It openned the door! Ok, now I’m out, I’m in a hallway I think, quite a simple house. There’s no window though, let me see …… ")
speak("Are you still there? I see three rooms, other than the study, one to my left, it says, restroom, one to my right, I think is the kitchen, and one ahead, should be the bedroom?")
speak("Where should I go?")
while True:
    record_user_input()
    result = recognize("restroom kitchen bedroom")
    if "restroom" in result:
        speak("The door is open, god bless, it seems to be a normal restroom, quite small.")
        break
    elif "kitchen" in result:
        speak("Why not check the kitchen. I can smell something, it smells so good in it, the door is locked, I can’t go in, my god, I’m so hungry, how long has it been! Maybe I should try somewhere else?")
    elif "bedroom" in result:
        speak("Ok the bedroom. It’s weird, there’s not even a grip on the door, wait a minute, there’s something written on the door … What’s in the soup today? what? What does that mean? Maybe I should try somewhere else?")
    else:
        dont_understand()
    speak("Where should I go? Restroom, kitchen, or bedroom?")


speak("Wait... the connection is kinda unstable...")
while True:
    subprocess.call("aplay noise.wav", shell=True)

    # negate the position to make clockwise rotation positive
    position = -encoder.position

    if position != last_position:
        last_position = position
        print("Position: {}".format(position))
    if (position % 10) == 1:
        break
speak("Oh! thank god I have got you back")

speak("Now I’m in the restroom. There’s the bathtub, nothing unusual. The toilet. And a mirror ...")
speak("Which one should I check first?")
while True:
    record_user_input()
    result = recognize("bathtub mirror toilet")
    if "bathtub" in result:
        speak("It’s...just a regular bathtub I think...")
    elif "mirror" in result:
        speak("Ok, you are right, I should probably see what I look like, maybe I could remember something? Let me see. Oh My God!! Who am I, what’s wrong with this terrible face! I’m not looking at it anymore!")
    elif "toilet" in result:
        speak("Ok, It’s really dirty, but got to do whatever gets me out of this shithole ... Wait, it’s not flushing, maybe something is clogged, let me check...")
        speak("Who would have thought that! Are you like a detective or something? It’s a key! Probably opens the door to the kitchen!")
        break
    else:
        dont_understand()
    speak("Should I check the bathtub, mirror, or toilet?")


speak("Now that I have the key, where should I go? Bedroom, kitchen, or study?")
while True:
    record_user_input()
    result = recognize("bedroom study kitchen")
    if "bedroom" in result:
        speak("Ok, let me see, there’s no key hole on the door, really weird, just something written on the door … What’s in the soup today? What does that mean?")
    elif "study" in result:
        speak("Just like before, I don’t see anything useful, maybe I should do something with the key?")
    elif "kitchen" in result:
        speak("Ahh, there’s a keyhole, let me try.") 
        speak("Ok, the door’s open, let me see what’s inside, man, it smells so good!")
        break
    else:
        dont_understand()
    speak("Should I go to the bedroom, kitchen, or study?")

speak("So… Here’s the kitchen, some bowls … some bread, the stove is still on, and something is boiling in the pot. Dang, that smells so good.") 
speak("I wonder what’s in it… should I go check the pot?")
record_user_input()
result = recognize("yes pot check why not what inside")
if result == "":
    speak("Oh I’m too hungry, I need to know what smells that good")
speak("It’s soup! I need to have some…")
speak("Ok, it tastes like heaven, my lord, I think there’s tomatoes, chicken, onions, and chilies. I wish you could be here to taste it.")

speak("Ok, enough soup, what should I do now? Should I go to the restroom, study, or bedroom?")
while True:
    record_user_input()
    result = recognize("bedroom study restroom")
    if "bedroom" in result:
        speak("Sure! Why not check the bedroom.")
        break
    elif "study" in result:
        speak("Still the same old study, maybe I should check out other rooms?")
    elif "restroom" in result:
        speak("Eww, the restroom is dirty, not going back again")
    else:
        dont_understand()
    speak("Should I go to the restroom, study, or bedroom?")

speak("Ok, now I’m at the bedroom door. It’s hardly a door, no grip or anything, a question on it though...")
speak("What’s in the soup today? Oh man, I shouldn’t have finished it all, do you remember at least one of the ingredients?")
for i in range(3):
    record_user_input()
    result = recognize("tomato chicken onion chilli")
    if result == "":
        if i == 2:
            speak("Hmmm I think there’s tomato in it...")
            result = "tomato"
        else:
            dont_understand()
            speak("Do you remember at least one of the ingredients?")
    else:
        speak("Yes, yes, I still remember that taste! You are right!")
        break


speak("So… should I just say the word?" + result + result)
speak("Holy shit, it’s opening! The door opened automatically, is someone listening to me?")
speak("Ok, there’s the bed, of course, queen size I guess, looking cozy, a computer on the desk, and a book on the nightstand… What should I do?")
while True:
    record_user_input()
    result = recognize("bed desk computer book nightstand")
    if "book" in result or "nightstand" in result:
        speak("Sure, it’s never late to read, here’s a bookmarked page...")
        speak("Painting is always a good place for many private people to hide their secrets in their home")
        speak("many indoor designs leave a secret space on the wall that is covered by paintings and decorations … wait, that sounds real familiar... ")
        break
    elif "bed" in result:
        speak("I’m not going to sleep at this time, maybe something else?")
    elif "desk" in result or "computer" in result:
        speak("Ok You are right, maybe I can connect to the internet … ok it’s totally dead, just a decoration I guess. Maybe something else?")
    else:
        dont_understand()
    speak("Should I check the bed, computer, or the book?")

speak("Wait... the connection is lost again... hold on")
while True:
    subprocess.call("aplay noise.wav", shell=True)

    # negate the position to make clockwise rotation positive
    position = -encoder.position

    if position != last_position:
        last_position = position
        print("Position: {}".format(position))
    if (position % 10) == 3:
        break
speak("Wow you are a genius! How did you fix that?")

speak("Ok. So I think that’s it for the bedroom, where should I go next, I don’t see another new door")
speak("Should I go back to the kitchen, or restroom, or study?")
while True:
    record_user_input()
    result = recognize("study restroom kitchen")
    if "study" in result:
        speak("Wait, you are right, there’s a painting in the study! Maybe something hidden!")
        break
    elif "restroom" in result:
        speak("Eww, the restroom is dirty, not going back again!")
    elif "kitchen" in result:
        speak("No soup there anymore, maybe somewhere else?")
    else:
        dont_understand()
    speak("Should I go to the kitchen, or restroom, or study?")

speak("Ok, study, the painting, let’s see what’s behind it… My god, there is actually something!")
speak("Can you imagine that? There’s a half-full vile of some greenish fluid … and a note … Drink it and you will be free.")
speak("What does that mean? Should I drink it?")
record_user_input()
result = recognize("yes yeah of course no")
if "no" in result:
    speak("But I really want to get out of here...")
else:
    speak("Okay I’m drinking it")
speak("Shoot. The phone is going to die. Hey, hey can you still hear me...")
subprocess.call("aplay busy.wav", shell=True)

speak("The connection has been lost. After an hour or so, you received another call suddenly")

button_held = False
while True:
    subprocess.call("aplay ring.wav", shell=True)
    if not button.value and not button_held:
        button_held = True
        break
    if button.value and button_held:
        button_held = False
        break

speak("Is this 911, hi, I need help, please!")
speak("I lost my memory and I’m now trapped in a room! There’s no one with me, and I don’t remember anything!")