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

There is an included [dspeech](./dspeech) demo that uses [Mozilla DeepSpeech](https://github.com/mozilla/DeepSpeech) for speech to text. If you're interested in trying it out we suggest you create a seperarate virutalenv. 



# Lab 3 Part 2

Create a system that runs on the Raspberry Pi that takes in one or more sensors and requires participants to speak to it. Document how the system works and include videos of both the system and the controller.

## Prep for Part 2

1. Sketch ideas for what you'll work on in lab on Wednesday.

I want to control my clock from lab2 with my voice. For example by saying "East" Beijing time will be displayed, by saying "West" NYC time will be displayed, by saying "Middle" Tel Aviv time will be displayed, by saying "Snow" Merry Christmas will be displayed.

Additionally, I want to implement the joystick. And since I like sushi, I want the joystick be represent a sushi wheel where four different types of sushi will be displayed according to the current coordinates of the joystick.

![alt text](https://github.com/williamzhang012998/Interactive-Lab-Hub/blob/Spring2021/Lab%203/speech.png)
![alt text](https://github.com/williamzhang012998/Interactive-Lab-Hub/blob/Spring2021/Lab%203/sushi_wheel.png)


## Share your idea sketches with Zoom Room mates and get feedback

*what was the feedback? Who did it come from?*
Feedback came from Jeanne Li and Jiadong Liu. They said that I should maybe include a button or some mechanism that indicated the start and the end of a voice recording. They also thought that the sushi wheel idea was very interesting.

## Prototype your system

The system should:
* use the Raspberry Pi 
* use one or more sensors
* require participants to speak to it. 

*Document how the system works*

You can control my lab2 clock with voice. For the system to listen to your voice, the red button must first be pressed down. After you have said your desired phrase, let go of the button. By saying "East" Beijing time will be displayed, by saying "West" NYC time will be displayed, by saying "Middle" Tel Aviv time will be displayed, by saying "Snow" Merry Christmas will be displayed.

Additionally, by moving the joystick in different directions, four different types of sushi will be displayed. The four different types are salmon, tuna, sea urchin and fatty tuna.

*Include videos or screencaptures of both the system and the controller.*

https://drive.google.com/file/d/1qT1YADKvDmYolcBbKoGKtXna_UPi28G5/view?usp=sharing

## Test the system
Try to get at least two people to interact with your system. (Ideally, you would inform them that there is a wizard _after_ the interaction, but we recognize that can be hard.)

Answer the following:

### What worked well about the system and what didn't?
Instead of having to press different buttons, now the whole system can be used through the pressing of only one button. This I thought was quite a big plus.

The latency of the whole system causes the system to not work as well as hoped. The user would not be able to speak immediately to the microphone right after the button was pressed. And the recording would not immediately come to a halt when the button was un-pressed. This issue sometimes caused confusion to the users.

### What worked well about the controller and what didn't?

The button that indicated the start and the end of a voice recording worked very well. I also made sure the button blinked while the voice was being recorded to make the recording experience more intuitive. 

Although the button would blink, it would be hard sometimes to see it blink because the user’s finger would be covering the whole button. As an improvement, maybe sound can also be used to indicate that the user is being recorded.

### What lessons can you take away from the WoZ interactions for designing a more autonomous version of the system?

A good microphone and a building a good system that can recognize different vocabulary is very important. With either of those missing, a decent voice recognition system will be very hard to produce.

### How could you use your system to create a dataset of interaction? What other sensing modalities would make sense to capture?

Other sensing modalities that we can potentially capture includes acceleration and torque. With the addition of these modalities and we can even make this a wearable watch for fall detection. This would be beneficial to the elderly who are living alone.
