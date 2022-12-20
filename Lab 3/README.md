# Chatterboxes

## Part 1.
### Text to Speech 

In this part of lab, we are going to start peeking into the world of audio on your Pi! 

We will be using the microphone and speaker on your webcamera. In the home directory of your Pi, there is a folder called `text2speech` containing several shell scripts. `cd` to the folder and list out all the files by `ls`:

```
pi@ixe00:~/text2speech $ ls
Download        festival_demo.sh  GoogleTTS_demo.sh  pico2text_demo.sh
espeak_demo.sh  flite_demo.sh     lookdave.wav
```

You can run these shell files by typing `./filename`, for example, typing `./espeak_demo.sh` and see what happens. Take some time to look at each script and see how it works. You can see a script by typing `cat filename`. For instance:

```
pi@ixe00:~/text2speech $ cat festival_demo.sh 
#from: https://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)#Festival_Text_to_Speech

echo "Just what do you think you're doing, Dave?" | festival --tts
```

Now, you might wonder what exactly is a `.sh` file? Typically, a `.sh` file is a shell script which you can execute in a terminal. The example files we offer here are for you to figure out the ways to play with audio on your Pi!

You can also play audio files directly with `aplay filename`. Try typing `aplay lookdave.wav`.

\*\***Write your own shell file to use your favorite of these TTS engines to have your Pi greet you by name.**\*\*

```
espeak -ven+f2 -k5 -s150 –stdout “Hey Olena” | aplay 
```

Bonus: If this topic is very exciting to you, you can try out this new TTS system we recently learned about: https://github.com/rhasspy/larynx

### Speech to Text

Now examine the `speech2text` folder. We are using a speech recognition engine, [Vosk](https://alphacephei.com/vosk/), which is made by researchers at Carnegie Mellon University. Vosk is amazing because it is an offline speech recognition engine; that is, all the processing for the speech recognition is happening onboard the Raspberry Pi. 

In particular, look at `test_words.py` and make sure you understand how the vocab is defined. 
Now, we need to find out where your webcam's audio device is connected to the Pi. Use `arecord -l` to get the card and device number:
```
pi@ixe00:~/speech2text $ arecord -l
**** List of CAPTURE Hardware Devices ****
card 1: Device [Usb Audio Device], device 0: USB Audio [USB Audio]
  Subdevices: 1/1
  Subdevice #0: subdevice #0
```
The example above shows a scenario where the audio device is at card 1, device 0. Now, use `nano vosk_demo_mic.sh` and change the `hw` parameter. In the case as shown above, change it to `hw:1,0`, which stands for card 1, device 0.  

Now, look at which camera you have. Do you have the cylinder camera (likely the case if you received it when we first handed out kits), change the `-r 16000` parameter to `-r 44100`. If you have the IMISES camera, check if your rate parameter says `-r 16000`. Save the file using Write Out and press enter.

Then try `./vosk_demo_mic.sh`

\*\***Write your own shell file that verbally asks for a numerical based input (such as a phone number, zipcode, number of pets, etc) and records the answer the respondent provides.**\*\*
```
#!/bin/bash
echo "What year is it?" | festival --tts
arecord -D hw:1,0 -f cd -c1 -r 16000 -d 5 -t wav recorded_mono.wav
```

### Serving Pages

In Lab 1, we served a webpage with flask. In this lab, you may find it useful to serve a webpage for the controller on a remote device. Here is a simple example of a webserver.

```
pi@ixe00:~/Interactive-Lab-Hub/Lab 3 $ python server.py
 * Serving Flask app "server" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 162-573-883
```
From a remote browser on the same network, check to make sure your webserver is working by going to `http://<YourPiIPAddress>:5000`. You should be able to see "Hello World" on the webpage.

### Storyboard

Storyboard and/or use a Verplank diagram to design a speech-enabled device. (Stuck? Make a device that talks for dogs. If that is too stupid, find an application that is better than that.) 

\*\***Post your storyboard and diagram here.**\*\*

![](https://github.com/ob234/ob234s-Interactive-Lab-Hub/blob/Fall2022/Lab%203/board_one.png)

Write out what you imagine the dialogue to be. Use cards, post-its, or whatever method helps you develop alternatives or group responses. 

\*\***Please describe and document your process.**\*\*

![](https://github.com/ob234/ob234s-Interactive-Lab-Hub/blob/d1af4a77c143a07ff709b8bd5b14c7bfcb76aeea/Lab%203/diagram_one.png)

### Acting out the dialogue

Find a partner, and *without sharing the script with your partner* try out the dialogue you've designed, where you (as the device designer) act as the device you are designing.  Please record this interaction (for example, using Zoom's record feature).

\*\***Describe if the dialogue seemed different than what you imagined when it was acted out, and how.**\*\*
The dialogue ended up being a bit tricky! Even for a simple interaction such as this one, the keywords used were really important. For example, a user would say something like “play something random” without specifically saying whether or not they wanted to hear a song or playlist. 


# Lab 3 Part 2

For Part 2, you will redesign the interaction with the speech-enabled device using the data collected, as well as feedback from part 1.

## Prep for Part 2

1. What are concrete things that could use improvement in the design of your device? For example: wording, timing, anticipation of misunderstandings...

Improving the dialogue is definitely important. I think the user should have a better understanding of how the system works so they can better interact with it. 

2. What are other modes of interaction _beyond speech_ that you might also use to clarify how to interact?

Having a sensor track the type of environment the music is playing in would be interesting. Technically a sensor could pick up things like how much light there is, if there are a lot of people in a room, if people are talking loudly and so on. The way the Spotify dataset was built would be really helpful in bridging this visual/audio understanding of surroundings with selecting the best music. 


3. Make a new storyboard, diagram and/or script based on these reflections.

![](https://github.com/ob234/ob234s-Interactive-Lab-Hub/blob/Fall2022/Lab%203/board_two.png)

![](https://github.com/ob234/ob234s-Interactive-Lab-Hub/blob/Fall2022/Lab%203/board_three.png)



## Prototype your system

The system should:
* use the Raspberry Pi 
* use one or more sensors
* require participants to speak to it. 

*Document how the system works*

*Include videos or screencaptures of both the system and the controller.*

For the prototype, I decided to link the pi using [this](https://pimylifeup.com/raspberry-pi-spotify/) tutorial. This will create a live speaker using the pi. Interactions will rely on wizard of oz method, however voice recording & processing can be setup using the speech2text examples. 

## Test the system
Try to get at least two people to interact with your system. (Ideally, you would inform them that there is a wizard _after_ the interaction, but we recognize that can be hard.)

Answer the following:

### What worked well about the system and what didn't?
→ When the specific instructions were followed, the system worked well 
→ However, when no response was recorded, the system didn’t really work at all 
→ The more sensors that are connected to the pi, the longer the wait time. It would take a while to buffer. Integrating motion detection also caused the same issue. 

### What worked well about the controller and what didn't?
→ Picking up random (or different) instructions wasn’t easy. 
→ Voice commands took a while to buffer, and sometimes the command wasn’t underwood. 

### What lessons can you take away from the WoZ interactions for designing a more autonomous version of the system?

→ The system needs to better adapt to what the user says.
→ Not much could be done about speeding up the hardware at this point, so we are limited by the compute power of the pi. 


### How could you use your system to create a dataset of interaction? What other sensing modalities would make sense to capture?

→ Different interactions could lead to better results. It would be interesting to see which set of commands work best. A dataset could definitely be helpful in this case. 
→ What if the user relied on something like a series of shortcuts? That might be more understandable for the pi, however more work ends up being placed on the user. Testing out different commands would be interesting. 
→ Future work could integrate work that has already been done on the spotify dataset, such as this text to song application: https://github.com/possan/playlistcreator-example
