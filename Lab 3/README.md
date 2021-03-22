# You're a wizard, [Student Name Here]

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

I want to build a device for golfers that tells you where your ball went if you hit it and can't see it. You swing and hit your ball, and then if you're not sure where it went you say "Where did my ball go?". Then, based on tracking your swing, the device tells you where it is, answering something like "your ball went 280 yards to the left".

![Device](https://github.com/rkleinro-CT/Interactive-Lab-Hub/blob/Spring2021/Lab%203/IMG_3797.jpg)

## Share your idea sketches with Zoom Room mates and get feedback

*what was the feedback? Who did it come from?*

Rob Gentul: "sweet idea, definitely see a valuable application for it. would be really cool if you could select a club type to start off the program (i imagine that would impact where the ball would go)"

Niki Agrawal: seems like a helpful tool but its not entirely clear what exactly the device is and how it will be measuring where your ball went, are there sensors at the end of the course, or in the tee or in the club?

## Prototype your system

The system should:
* use the Raspberry Pi 
* use one or more sensors
* require participants to speak to it. 

*Document how the system works*

*Include videos or screencaptures of both the system and the controller.*
https://drive.google.com/file/d/1FpqbzFQT_Ovi9ZoR1nsagoWAlWgEVL0D/view?usp=sharing
https://drive.google.com/file/d/193YiEM_ZR9YCQ77YxAkxOe7pKyJlmXrI/view?usp=sharing

I got significant help from Ilan, Rob, Niki, and Snigdha in getting set up, and leveraged Willam Zhang’s code for my joystick and Niki's code in my test2speech. I also leverage the website below for info:

https://stackoverflow.com/questions/2485466/pythons-equivalent-of-logical-and-in-an-if-statement

https://github.com/sparkfun/Qwiic_Joystick_Py

https://learn.sparkfun.com/tutorials/qwiic-joystick-hookup-guide/all#python-examples

https://www.geeksforgeeks.org/check-multiple-conditions-in-if-statement-python/

## Test the system
Try to get at least two people to interact with your system. (Ideally, you would inform them that there is a wizard _after_ the interaction, but we recognize that can be hard.)

Answer the following:

One tester: Niki Agrawal

### What worked well about the system and what didn't?
The simulation of swinging a club and the explanation of where the ball went seemed to be very clear.

### What worked well about the controller and what didn't?

The sensitivity was a bit off. Sometimes the user swung the club and the device didnt respond because it was too in the middle (I tampered this down so it woulnd't constantly speak if the person wasn't swinging, because of the starting position of the joystick). Additionally the timing was a bit off, sometimes the user would swing and was confused when they weren’t getting immediate feedback - time may be too long. Although, they said the speed of the reponse seemed good.

### What lessons can you take away from the WoZ interactions for designing a more autonomous version of the system?

The device will need to respond to the user within an acceptable time window when called upon, so as not to seem to quick to feel "fake" but not take too long to feel like it's not being responsive or working correctly.


### How could you use your system to create a dataset of interaction? What other sensing modalities would make sense to capture?

I'd like to capture how long after a swing the person asks the device where the ball went, how long it takes to respond after asking, and where the ball actually goes. Additionally, i've gotten some feedback regarding wind, course conditions, club type, swing speed, hazards, and different courses. It would be great to capture all this, more specifically tracking the force and angle of the club at impact to help determine how far and where it went, in additional to the direction which ended up being what I tested in this lab.

