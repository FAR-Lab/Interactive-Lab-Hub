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

In this part of lab, we are going to start peeking into the world of audio on your Pi! 

We will be using a USB microphone, and the speaker on your webcamera. (Originally we intended to use the microphone on the web camera, but it does not seem to work on Linux.) In the home directory of your Pi, there is a folder called `text2speech` containing several shell scripts. `cd` to the folder and list out all the files by `ls`:

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
(This shell file should be saved to your own repo for this lab.)

Bonus: If this topic is very exciting to you, you can try out this new TTS system we recently learned about: https://github.com/rhasspy/larynx

### Speech to Text

Now examine the `speech2text` folder. We are using a speech recognition engine, [Vosk](https://alphacephei.com/vosk/), which is made by researchers at Carnegie Mellon University. Vosk is amazing because it is an offline speech recognition engine; that is, all the processing for the speech recognition is happening onboard the Raspberry Pi. 

In particular, look at `test_words.py` and make sure you understand how the vocab is defined. Then try `./vosk_demo_mic.sh`

One thing you might need to pay attention to is the audio input setting of Pi. Since you are plugging the USB cable of your webcam to your Pi at the same time to act as speaker, the default input might be set to the webcam microphone, which will not be working for recording.

\*\***Write your own shell file that verbally asks for a numerical based input (such as a phone number, zipcode, number of pets, etc) and records the answer the respondent provides.**\*\*

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

Storyboard and/or use a Verplank diagram to design a speech-enabled device. (Stuck? Make a device that talks for dogs. If that is too stupid, find an application that is better than that.) 

![verplanck](https://github.com/standardnormal/Interactive-Lab-Hub/blob/Fall2021/Lab%203/lab3verplanck.png?raw=true)

Write out what you imagine the dialogue to be. Use cards, post-its, or whatever method helps you develop alternatives or group responses. 

<img src="https://github.com/standardnormal/Interactive-Lab-Hub/blob/Fall2021/Lab%203/lab3notes.png?raw=true" width="500" />

### Acting out the dialogue

Find a partner, and *without sharing the script with your partner* try out the dialogue you've designed, where you (as the device designer) act as the device you are designing.  Please record this interaction (for example, using Zoom's record feature).

\*\***One thing I didn't prepare for was the amount of distinct variations to the phrases I planned for. For example, I planned for "Pause" but got "Hold on a sec." I realized I forgot to add a question to the script asking for the number of users, which means it is unclear when a second person is supposed to speak. **\*\*

### Wizarding with the Pi (optional)
In the [demo directory](./demo), you will find an example Wizard of Oz project. In that project, you can see how audio and sensor data is streamed from the Pi to a wizard controller that runs in the browser.  You may use this demo code as a template. By running the `app.py` script, you can see how audio and sensor data (Adafruit MPU-6050 6-DoF Accel and Gyro Sensor) is streamed from the Pi to a wizard controller that runs in the browser `http://<YouPiIPAddress>:5000`. You can control what the system says from the controller as well!

\*\***Describe if the dialogue seemed different than what you imagined, or when acted out, when it was wizarded, and how.**\*\*

# Lab 3 Part 2

For Part 2, you will redesign the interaction with the speech-enabled device using the data collected, as well as feedback from part 1.

## Prep for Part 2

1. What are concrete things that could use improvement in the design of your device? For example: wording, timing, anticipation of misunderstandings...

I only received one feedback note from David O. He suggested I expand to "something like language study, where the machine listens to your conjugations and pronunciations and assists you." His idea got me thinking of other ways the system could help an actor prepare for a role. I particularly liked his thought that "perhaps the device could be trained to do improv." Unfortunately this is beyond my skill level, but still definitely cool to think about.

2. What are other modes of interaction _beyond speech_ that you might also use to clarify how to interact?

A visual of the device moving through a script could certainly help. Or some kind of virtual manifestation of the line-reading partner. Alternatively, physical buttons with arrows that help the user move back or forward through the script.

3. Make a new storyboard, diagram and/or script based on these reflections.

As all of my ideas are too challenging for me to implement, I'll be working with the same ideas from part 1.

## Prototype your system

The system should:
* use the Raspberry Pi 
* use one or more sensors
* require participants to speak to it. 

*Document how the system works*

My first step was figuring out how to get the Pi to speak at all, which I was able to do through the steps given above. I knew I wanted to do a two-person scene as scenes with more than one role might be more complicated to implement, so I went with the balcony scene from Romeo and Juliet. That said, some of the longer lines still take a while to format.

![First Video: the Pi does a Romeo Monologue](https://github.com/standardnormal/Interactive-Lab-Hub/blob/Fall2021/Lab%203/vid1.mp4)

Once I got through a bunch of github issues and understood how to do text to speech from the command line, I had to figure out how to do the same thing within Python. Unfortunately there were no instructions here or in class about how to call terminal commands from a Python program. After a lot of Googling and some help from James Parsons, I found the OS module which I use in my scriptread.py file to make the Pi speak.

<img src="https://github.com/standardnormal/Interactive-Lab-Hub/blob/Fall2021/Lab%203/pgmV1.JPG?raw=true" />

As with the previous lab, I used a .json file (script.json) to simulate uploading a real script. The file contains a dictionary pairing each character's name with an array containing their lines in order.

Because of the complications of combining Speech-to-Text and Text-to-Speech as specified by the original design, I decided to focus entirely on Text-to-Speech and simply Wizard the device's choice of response. After running the program in the command line it asks for a line number. Pressing Ctrl+C ends the line early and allows you to enter another line number.

<img src="https://github.com/standardnormal/Interactive-Lab-Hub/blob/Fall2021/Lab%203/pgmV2.JPG?raw=true" />

Next I added an opening line that has the device ask the user which part they are going to play. The response is, again, Wizard of Oz. The operator types in the part the computer is playing and the device asks "Would you like to begin or should I?" After another operator input, the device says an initiation message and waits for the user to either say their first line or tell the device which line to start with. I decided to exclude asking which play the user wants to read as I was only working with Romeo and Juliet.

<a href="https://www.youtube.com/watch?v=aYpIQY9AVt0">Line-Reader Demo Video</a>

## Test the system
Try to get at least two people to interact with your system. (Ideally, you would inform them that there is a wizard _after_ the interaction, but we recognize that can be hard.)

Answer the following:

### What worked well about the system and what didn't?

I had to delete and re-add my entire github repo to the Pi because of github issues that I couldn't diagnose. Because some lines were longer than others, I learned the system needed more time between the command input and beginning speech for longer lines. That could definitely be an issue in a product that needs to keep up with a human's pace.

Once I got rid of any apostrophes in the script which affected how the python script interpreted the strings, text to speech worked very well. The controller worked entirely as intended.

### What worked well about the controller and what didn't?

I didn't account for input errors so typing in something wrong could crash the program. Assuming the operator was careful, they would still have to keep track of which line the user was up to. I added a line to the python script to print the previously read line's number to the command line to make it easier for the operator.

### What lessons can you take away from the WoZ interactions for designing a more autonomous version of the system?

I need to account for a wider variety of responses, especially to the simpler commands like "repeat" and "go back X lines." My original plan was for a speech-to-text platform to listen to the user's spoken line and figure out which line to read next, but if the user makes a mistake or improvises then the device may not know what to do. A more autonomous version of the system will need to be more flexible, perhaps only needing to recognize part of the line and some synonyms. It will also need to know to wait until the user is finished speaking before it continues on to the next line.

### How could you use your system to create a dataset of interaction? What other sensing modalities would make sense to capture?

Staying in the realm of audio and in line with some of David's feedback, the device could actively listen to not just your words but your pronunciation and enunciation and then provide suggestions. It could also use a camera to measure the user's emotional expressions to adjust its own tone or to provide feedback on an actor's physical performance. Some kind of health sensor for heart rate and breathing may also enable improved functionality in the device.
