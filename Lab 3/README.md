# You're a wizard, Niki

<img src="https://pbs.twimg.com/media/Cen7qkHWIAAdKsB.jpg" height="400">

In this lab, we want you to practice wizarding an interactive device as discussed in class. We will focus on audio as the main modality for interaction but there is no reason these general techniques can't extend to video, haptics or other interactive mechanisms. In fact, you are welcome to add those to your project if they enhance your design.


## Text to Speech and Speech to Text

In the home directory of your Pi there is a folder called `text2speech` containing some shell scripts.

```
pi@ixe00:~/text2speech $ ls
Download        festival_demo.sh  GoogleTTS_demo.sh  pico2text_demo.sh
espeak_demo.sh  flite_demo.sh     lookdave.wav

```

you can run these examples by typing 
`./espeakdeom.sh`. Take some time to look at each script and see how it works. You can see a script by typing `cat filename`

```
pi@ixe00:~/text2speech $ cat festival_demo.sh 
#from: https://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)#Festival_Text_to_Speech

echo "Just what do you think you're doing, Dave?" | festival --tts

```

You can also play audio files directly with `aplay filename`.

After looking through this folder do the same for the `speech2text` folder. In particular, look at `test_words.py` and make sure you understand how the vocab is defined. Then try `./vosk_demo_mic.sh`

## Serving Pages

In Lab 1 we served a webpage with flask. In this lab you may find it useful to serve a webpage for the controller on a remote device. Here is a simple example of a webserver.

```
pi@ixe00:~/$ python server.py
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
From a remote browser on the same network, check to make sure your webserver is working by going to [http://ixe00.local:5000]()


## Demo

In the [demo directory](./demo), you will find an example wizard of oz project you may use as a template. **You do not have to** feel free to get creative. In that project, you can see how audio and sensor data is streamed from the Pi to a wizard controller that runs in the browser. You can control what system says from the controller as well.

## Optional

There is an included [dspeech](.dspeech) demo that uses [Mozilla DeepSpeech](https://github.com/mozilla/DeepSpeech) for speech to text. If you're interested in trying it out we suggest you create a seperarate virutalenv. 



# Lab 3 Part 2

Create a system that runs on the Raspberry Pi that takes in one or more sensors and requires participants to speak to it. Document how the system works and include videos of both the system and the controller.

## Prep for Part 2

1. Sketch ideas for what you'll work on in lab on Wednesday.

https://github.com/nagrawal44/Interactive-Lab-Hub/blob/master/Lab%203/sketch.JPG

I'm am using my friend's studio project for my prototype for Lab 3. I am creating a wearable device that helps blind people navigate through a mall or school building by giving them voice instructions on how to get somewhere. For example, if they say "Take me to Ilan's lab" then it has information populated by people that do have sight and responds back with "Take the elevator to the third floor, then turn right, and its the second door on the left". So the pi will ask the person where they want to go, and then give them voice instructions. It also has a sensor so that if you are too close to an object, like a wall, it will alert you with audio warning.


## Share your idea sketches with Zoom Room mates and get feedback

*what was the feedback? Who did it come from?*
Rob - this is a solid idea that uses all the components of the class
Shivani - When you record this demo, you should hold the sensor in front of you because the sensor only has a small radius so you might bump your head if you are "wearing it". This way you have a full arms length before the object potentiall hits you.

## Prototype your system

The system should:
* use the Raspberry Pi 
* use one or more sensors
* require participants to speak to it. 

*Document how the system works*
1) The system welcomes you and asks you where you want to go. 
2) You then tell it "I want to go to Ilan's lab". It will look through the database of directions it has to find the one that matches yours
3) For the purposes of this demo, I will use my fridge and the instructions will appear once you say "done" and press one of the buttons on the Pi
4) It first says "Walk straight and turn left". Then the person tells the pi "Done"
5) Once it hears "done", it gives the next step of "Walk 2 steps forward and then turn left"
6) If a person is approaching a wall, it will warn them and say "You are too close to an object" 

*Include videos or screencaptures of both the system and the controller.*
https://drive.google.com/file/d/1mVyckoidQbm5ALzmIW6bXTdvRDLXtJV_/view?usp=sharing

## Test the system
Try to get at least two people to interact with your system. (Ideally, you would inform them that there is a wizard _after_ the interaction, but we recognize that can be hard.)

Answer the following:

### What worked well about the system and what didn't?
This worked well as a navigator for a blind person by giving them voice directions and having a two-sided conversation on whether they have completed the steps or not. But what would be difficult is that if the blind person thinks they have turned correctly, but they actually didn't then it would keep leading them down a stray path. Ideally, if this has some GPS component to tell the blind person where to go by tracking their location. I also liked that I was able to incorporate one of the sensors and have it tell the person if they are about to hit something.


### What worked well about the controller and what didn't?
From a device prototyping perspective, since the computer had to be connected to the pi as a power source and the speaker, it was a very bulky interaction and didn't feel natural. Also, this should be used as a wearable device or at the end of the white cane, not something you have to hold in your hands. Lastly, when I was showing the capabilities of the proximity sensor, I had to purposefully tap it against a wall so that was not natural.


### What lessons can you take away from the WoZ interactions for designing a more autonomous version of the system?
Next time with a less bulky system to carry around and actually running into an object, it will feel more natural. Also if we have enough directions programmed into the device, we could really direct a person to a place with these directions. Lastly, I should make the voice sound a bit more pleasant and easier to understand.


### How could you use your system to create a dataset of interaction? What other sensing modalities would make sense to capture?
We could make a library of different directions that the system can provide. For example, it only has directions to these 10 places in Tata or Bloomberg, and then create if/else statements so that it automatically speaks once you've said where you want to go or once you've said "done"

