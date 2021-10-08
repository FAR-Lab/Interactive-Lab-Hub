# Chatterboxes
[![Watch the video](https://user-images.githubusercontent.com/1128669/135009222-111fe522-e6ba-46ad-b6dc-d1633d21129c.png)](https://www.youtube.com/embed/Q8FWzLMobx0?start=19)

In this lab, we want you to design interaction with a speech-enabled device--something that listens and talks to you. This device can do anything *but* control lights (since we already did that in Lab 1).  First, we want you first to storyboard what you imagine the conversational interaction to be like. Then, you will use wizarding techniques to elicit examples of what people might say, ask, or respond.  We then want you to use the examples collected from at least two other people to inform the redesign of the device.

We will focus on **audio** as the main modality for interaction to start; these general techniques can be extended to **video**, **haptics** or other interactive mechanisms in the second part of the Lab.

## Prep for Part 1: Get the Latest Content and Pick up Additional Parts 

### Pick up Additional Parts

As mentioned during the class, we ordered additional mini microphone for Lab 3. Also, a new part that has finally arrived is encoder! Please remember to pick them up from the TA.

### Get the Latest Content

As always, pull updates from the class Interactive-Lab-Hub to both your Pi and your own GitHub repo. As we discussed in the class, there are 2 ways you can do so:

**\[recommended\]**Option 1: On the Pi, `cd` to your `Interactive-Lab-Hub`, pull the updates from upstream (class lab-hub) and push the updates back to your own GitHub repo. You will need the *personal access token* for this.

```
pi@ixe00:~$ cd Interactive-Lab-Hub
pi@ixe00:~/Interactive-Lab-Hub $ git pull upstream Fall2021
pi@ixe00:~/Interactive-Lab-Hub $ git add .
pi@ixe00:~/Interactive-Lab-Hub $ git commit -m "get lab3 updates"
pi@ixe00:~/Interactive-Lab-Hub $ git push
```

Option 2: On your your own GitHub repo, [create pull request](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2021Fall/readings/Submitting%20Labs.md) to get updates from the class Interactive-Lab-Hub. After you have latest updates online, go on your Pi, `cd` to your `Interactive-Lab-Hub` and use `git pull` to get updates from your own GitHub repo.

## Part 1.
### Text to Speech 

\*\***Write your own shell file to use your favorite of these TTS engines to have your Pi greet you by name.**\*\* <br />
I followed the instruction I found on adafruit (https://learn.adafruit.com/speech-synthesis-on-the-raspberry-pi/speak-easier-flite) to install the synthesis engine on my pi. By using the commands below, I was able to build my own Flite.
```
cd ~/Downloads
sudo apt-get install libasound2-dev

wget http://www.festvox.org/flite/packed/flite-2.1/flite-2.1-release.tar.bz2

tar -xvf flite-2.1-release.tar.bz2
cd flite-2.1-release
./configure --with-audio=alsa --with-vox=awb

make

sudo make install
```
After successfully installing the flite, I created another file ```greet.sh``` which can be found in the Lab 3 repo. I then had the flite to speak the content of the file, "How are you doing, Kristy", using the following command line.
```
flite -f greet.sh
```

### Speech to Text

Running ```./vosk_demo_mic.sh``` and saying ```one, two, three``` generated us the following result.
![P1:speech2text-1](https://github.com/kchen1009/Interactive-Lab-Hub/blob/Fall2021/Lab%203/images/speech2text-1.png)


\*\***Write your own shell file that verbally asks for a numerical based input (such as a phone number, zipcode, number of pets, etc) and records the answer the respondent provides.**\*\* <br />
I wrote a shell file ```zipcode.sh``` to ask for zipcode. The answer respondent provides would be recorded and printed out in the terminal. ```zipcode.sh```is in the ```speech2text``` folder, and it looks like this:
```
#adapted from https://learn.adafruit.com/speech-synthesis-on-the-raspberry-pi/speak-easier-flite

#arecord -f cd -r 16000 -d 5 -t wav recorded.wav && sox recorded.wav recorded_mono.wav remix 1,2

flite -voice slt -t "What is your zipcode?"

arecord -D hw:2,0 -f cd -c1 -r 48000 -d 5 -t wav recorded_mono.wav
python3 test_words.py recorded_mono.wav
```
The result from answering ```11101``` is shown in the image. <br />
![P2:speech2text-2](https://github.com/kchen1009/Interactive-Lab-Hub/blob/Fall2021/Lab%203/images/speech2text-2.png)

Bonus Activity:

If you are really excited about Speech to Text, you can try out [Mozilla DeepSpeech](https://github.com/mozilla/DeepSpeech) and [voice2json](http://voice2json.org/install.html)
There is an included [dspeech](./dspeech) demo  on the Pi. If you're interested in trying it out, we suggest you create a seperarate virutal environment for it . Create a new Python virtual environment by typing the following commands.

```
pi@ixe00:~ $ virtualenv dspeechexercise
pi@ixe00:~ $ source dspeechexercise/bin/activate
(dspeechexercise) pi@ixe00:~ $ 
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

\*\***Post your storyboard and diagram here.**\*\*
![P3:storyboard](https://github.com/kchen1009/Interactive-Lab-Hub/blob/Fall2021/Lab%203/images/storyboard.JPG)

Write out what you imagine the dialogue to be. Use cards, post-its, or whatever method helps you develop alternatives or group responses. 

\*\***Please describe and document your process.**\*\* <br />
![P4:dialogue](https://github.com/kchen1009/Interactive-Lab-Hub/blob/Fall2021/Lab%203/images/dialogue.jpg) <br />
The scenario I depicted in my storyboard above is that a cat walks to the door to welcome her owner and asks for dinner. The speech-enabled device bascially is a translator in this case, bridging the conversation between the owner and the cat so they are able to understand and communicate with each other with ease. The dialogue that I imagined would occur in this scenario is as described below. I use post-its notes to help me generate ideas.

```
Cat owner
   "Hey I am back!"
Device (cat)
   "Why are you so late today? I am starving!!"
   "But how's school today?"
Cat owner
   "Hey, thank you for asking! It was okay, and I am super exhausted right now."
   "I'm gonna fix myself something for dinner"
Device (cat)
   "But how about MY dinner? I am starving I told you! I didn't even have treats for toady's afternoon tea"
Cat owner
   "Sorry, my poor pal. What do you want for tonight? Fish or chicken?"
Device (cat)
   "Fish is fine!"
Cat owner
   "Then tuna or salmon?"
Device (cat)
   "SALMON PLEASE!!! It's my fav <3"
```

### Acting out the dialogue

Find a partner, and *without sharing the script with your partner* try out the dialogue you've designed, where you (as the device designer) act as the device you are designing.  Please record this interaction (for example, using Zoom's record feature).

The interaction can be found here: https://drive.google.com/file/d/1GiDDY7BRCE8N_lmsjGV4FVUA1_LPkBzw/view?usp=sharing. I acted as the device that helped Nunu (the cat featured in the video) translate her conversation with her owner. 

\*\***Describe if the dialogue seemed different than what you imagined when it was acted out, and how.**\*\* <br />
The dialogue was every different - without giving my partner guidance and content of the sciprt, the conversation flew freely. Even though I was trying my best to swing the convo back to what I initially designed, it was fairly difficult as I wasn't the cat owner himself. Frankly speaking, I wasn't even sure if I was doing the assignment correctly. For the next part, I think I would need to narrow down the scope of the scenario to make the dialogue more focused and interactive.

### Wizarding with the Pi (optional)
Running ```app.py```, I was able to open the controller interface, having the Pi to stream audio and even speak.
![P4:wizardinterface](https://github.com/kchen1009/Interactive-Lab-Hub/blob/Fall2021/Lab%203/images/wizardinterface.png)


# Lab 3 Part 2

For Part 2, you will redesign the interaction with the speech-enabled device using the data collected, as well as feedback from part 1.

## Prep for Part 2

1. What are concrete things that could use improvement in the design of your device? For example: wording, timing, anticipation of misunderstandings... <br />
I would focus on the scenario of meal selection in part 2 so as to have a more concrete theme and limit the length of the conversation. In this way, the purpose of the device can be more clearly communicated, allowing users to intuitively perceive what it does and how to interact with it. Also, the initial language design was fairly casual since I imagined a friendly dialogue between an owner and his cat. However, in the new design of the device, I decided to pivot a little bit; instead of making a cat translator, I'd like to design an interactive device that helps pick meal items for a cat. The device should speak more like a robot and faciliate the selection process.

2. What are other modes of interaction _beyond speech_ that you might also use to clarify how to interact? <br />
Since it's about meal selection, I'd like to add joystick to make the interaciton beyond speech and text, which is more fun and engaging. Users could the joystick as a controller to pick either "salmon" or "tune" for the cat's dinner meal.

3. Make a new storyboard, diagram and/or script based on these reflections.
![P5:diagram](https://github.com/kchen1009/Interactive-Lab-Hub/blob/Fall2021/Lab%203/images/diagram.JPG)

## Prototype your system

The system should:
* use the Raspberry Pi 
* use one or more sensors
* require participants to speak to it. 

*Document how the system works*

*Include videos or screencaptures of both the system and the controller.*

## Test the system
Try to get at least two people to interact with your system. (Ideally, you would inform them that there is a wizard _after_ the interaction, but we recognize that can be hard.)

Answer the following:

### What worked well about the system and what didn't?
\*\**your answer here*\*\*

### What worked well about the controller and what didn't?

\*\**your answer here*\*\*

### What lessons can you take away from the WoZ interactions for designing a more autonomous version of the system?
The reaction time of the device is fairly important in such an interactive game. If the system takes a while to repsond, users might lose interest in it or think the device is broken. Therefore, to deliver a better UX and make the game more engaging, it is critical to ensure that the system respond to users' selections and speech right away. Also, when having the system talk, it is imperative to use an easy-to-understand voice and make sure that the system communicates clearly to prevent confusions.


### How could you use your system to create a dataset of interaction? What other sensing modalities would make sense to capture?
I could use the system to record the participation rate of the game - how many people say yes vs no? I could also use the system to record how users speak to the device to indicate their willingness based on their tone (happy vs upset), pitch (high vs low), langugage (Yes vs Yeah!), etc. I think it'd also be interesting to capture users' facial expressions and body languages of which when they play with the joystick.

