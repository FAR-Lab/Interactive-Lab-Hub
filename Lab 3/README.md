# Chatterboxes
**NAMES OF COLLABORATORS HERE**
[![Watch the video](https://user-images.githubusercontent.com/1128669/135009222-111fe522-e6ba-46ad-b6dc-d1633d21129c.png)](https://www.youtube.com/embed/Q8FWzLMobx0?start=19)

In this lab, we want you to design interaction with a speech-enabled device--something that listens and talks to you. This device can do anything *but* control lights (since we already did that in Lab 1).  First, we want you first to storyboard what you imagine the conversational interaction to be like. Then, you will use wizarding techniques to elicit examples of what people might say, ask, or respond.  We then want you to use the examples collected from at least two other people to inform the redesign of the device.

We will focus on **audio** as the main modality for interaction to start; these general techniques can be extended to **video**, **haptics** or other interactive mechanisms in the second part of the Lab.

## Prep for Part 1: Get the Latest Content and Pick up Additional Parts 

### Pick up Web Camera If You Don't Have One

Students who have not already received a web camera will receive their [IMISES web cameras](https://www.amazon.com/Microphone-Speaker-Balance-Conference-Streaming/dp/B0B7B7SYSY/ref=sr_1_3?keywords=webcam%2Bwith%2Bmicrophone%2Band%2Bspeaker&qid=1663090960&s=electronics&sprefix=webcam%2Bwith%2Bmicrophone%2Band%2Bsp%2Celectronics%2C123&sr=1-3&th=1) on Thursday at the beginning of lab. If you cannot make it to class on Thursday, please contact the TAs to ensure you get your web camera. 

### Get the Latest Content

As always, pull updates from the class Interactive-Lab-Hub to both your Pi and your own GitHub repo. There are 2 ways you can do so:

**\[recommended\]**Option 1: On the Pi, `cd` to your `Interactive-Lab-Hub`, pull the updates from upstream (class lab-hub) and push the updates back to your own GitHub repo. You will need the *personal access token* for this.

```
pi@ixe00:~$ cd Interactive-Lab-Hub
pi@ixe00:~/Interactive-Lab-Hub $ git pull upstream Fall2022
pi@ixe00:~/Interactive-Lab-Hub $ git add .
pi@ixe00:~/Interactive-Lab-Hub $ git commit -m "get lab3 updates"
pi@ixe00:~/Interactive-Lab-Hub $ git push
```

Option 2: On your your own GitHub repo, [create pull request](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2022Fall/readings/Submitting%20Labs.md) to get updates from the class Interactive-Lab-Hub. After you have latest updates online, go on your Pi, `cd` to your `Interactive-Lab-Hub` and use `git pull` to get updates from your own GitHub repo.

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
(This shell file should be saved to your own repo for this lab.)

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

My custom shell file is saved on the Pi but I had trouble pushing it to github due to access restrictions. I will have this sorted out after talking to prof/TA.

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

My device is a music recommendation device. It asks the user what mood they are in and then asks the user to specify their preferred genre. Depending on the mood and genre requested, the device will narrow down the possible selection of songs until it is ready to output only songs of a specific genre and mood. Essentially, the device will take some of the work out of picking a song that matches the current mood you are in. This can be a frustrating process, and many of us do not put in the effort to make playlists according to moods. This device will automatically append each song the user listens to for over 1 min into a playlist that is built over time, each time the user uses the device.

\*\***Post your storyboard and diagram here.**\*\*

![storyboardcropped](https://user-images.githubusercontent.com/112603386/192417637-66b717ff-c6a8-464f-84f6-edae8639381b.png)


Write out what you imagine the dialogue to be. Use cards, post-its, or whatever method helps you develop alternatives or group responses. 

\*\***Please describe and document your process.**\*\*
![flowchart](https://user-images.githubusercontent.com/112603386/192417670-4e6931d9-7d3d-4f2a-af8b-06bf935f7b2c.jpg)



### Acting out the dialogue

Find a partner, and *without sharing the script with your partner* try out the dialogue you've designed, where you (as the device designer) act as the device you are designing.  Please record this interaction (for example, using Zoom's record feature).

\*\***Describe if the dialogue seemed different than what you imagined when it was acted out, and how.**\*\*



https://user-images.githubusercontent.com/112603386/192417774-df4695bd-ddd5-42ea-9f4f-b219b57a5011.mp4



### Wizarding with the Pi (optional)
In the [demo directory](./demo), you will find an example Wizard of Oz project. In that project, you can see how audio and sensor data is streamed from the Pi to a wizard controller that runs in the browser.  You may use this demo code as a template. By running the `app.py` script, you can see how audio and sensor data (Adafruit MPU-6050 6-DoF Accel and Gyro Sensor) is streamed from the Pi to a wizard controller that runs in the browser `http://<YouPiIPAddress>:5000`. You can control what the system says from the controller as well!

\*\***Describe if the dialogue seemed different than what you imagined, or when acted out, when it was wizarded, and how.**\*\*

Jackson Reimer was my test user for this device. The dialogue was fairly similar to what I expected. Because I prompted him with the device dialogue at each step, there were only so many responses that could be given. However I realized that when he requested to hear a new Punk song, I didn't have any more Punk songs available in my playlist database ready to go. I had to make a small pivot playing a Metal song instead. Because Jackson is nice, he was fine with the song. However someone who is angry may be even more angered at the mistake in the nuanced genres. This made me realize I need to have more songs in my database so I can have atleast 5 different options for each genre in each mood bucket.

I also realized that my dialogue was a little too wordy. This is because I was trying to account for every possible option and was covering too much ground with my device. It would be better if my device got straight to the point and immidiately played music. If the user wants to listen to their saved playlist they can request that without being prompted. For a similar reason I have made the device automatically add the song to the playlist after the user listens without requesting a new song for 1 minute. This is a more streamlined implementation.

# Lab 3 Part 2

For Part 2, you will redesign the interaction with the speech-enabled device using the data collected, as well as feedback from part 1.

## Prep for Part 2

1. What are concrete things that could use improvement in the design of your device? For example: wording, timing, anticipation of misunderstandings...

The wording of the first iteration of my device was good, but almost too comprehensive. To actually start listening to music, the user first had to go through multiple questions. When I listen to music, I want to listen as quickly as possible, so I have cut down on several of my questions such as "Do you want to discover new music or listen to your XXX playlist?" Now the device will immidiately start playing your saved playlist for whatever mood you say you are in; if that playlist is empty it will switching into discovery mode. The user can also prompt the device by saying discover new music at any time.

Because I removed some of the questions, this device will need an instruction manual to get started. I believe this is a better implementation because devices nowadays do not prompt you with how to use the device, but rather expect you to know certain options you have with your device before usage. My device will work like this, and will have a manual that tells users how to interact with the device before they start for the first time. This will include gestures and voice commands that work, as well as how to add different phrases or gestures for commands to perform currently implemented features (for example if they would prefer to swipe their hand up instead of to the right for go to next song command). The manual will also include information on what to expect in terms of when songs are added to user playlists (currently the device adds songs to playlists if the user listens for more than 30 seconds), how to change the threshold of when the songs are added, or change how far into a song the skip forward command actually moves you into a song, for example if you want the default skip ahead feature to skip forward 15 seconds instead of 30 seconds.

2. What are other modes of interaction _beyond speech_ that you might also use to clarify how to interact?

Another improvement form my first iteration of the device is the accessibility of the device. In the first iteration the only option users had to interact with the device was using voice commands, but in this second iteration the user can use gesturing commands with their hands to have more choices of how to interact with the device. The users can now skip to next song, skip back a song, skip forward 30 seconds in a song they are listening to, and skip backwards 30 seconds in a song they are listening to. Of course the voice commands will also still work.

3. Make a new storyboard, diagram and/or script based on these reflections.

## Prototype your system

The system should:
* use the Raspberry Pi 
* use one or more sensors
* require participants to speak to it. 

*Document how the system works*

*Include videos or screencaptures of both the system and the controller.*

## Test the system
Try to get at least two people to interact with your system. (Ideally, you would inform them that there is a wizard _after_ the interaction, but we recognize that can be hard.)

User Test 1, user was given verbal version of user manual describing how to use gesture features and voice commands, as well as how to enter discover mode or go straight into playlist.



https://user-images.githubusercontent.com/112603386/193732168-2e83cf9e-86c1-4b34-b644-04adfa4d705f.mov




Answer the following:

### What worked well about the system and what didn't?
\*\**your answer here*\*\*

### What worked well about the controller and what didn't?

\*\**your answer here*\*\*

### What lessons can you take away from the WoZ interactions for designing a more autonomous version of the system?

\*\**your answer here*\*\*


### How could you use your system to create a dataset of interaction? What other sensing modalities would make sense to capture?

\*\**your answer here*\*\*

