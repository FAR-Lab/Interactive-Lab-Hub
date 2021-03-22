# You're a wizard, Joy.

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

![alt text](https://github.com/iamyuchy/Interactive-Lab-Hub/blob/Spring2021/Lab%203/test.jpg)

## Share your idea sketches with Zoom Room mates and get feedback

Feedback from Jiadong Lou and Chelsea Luo: 


"Great sketch. You can add extra buttons to start and reset the personality test. The voice input includes not only numbers but also other categories, which is good. "


"Instead of speaking out the questions and the results, the pi can also use text display so it is easier for user to follow. Maybe also using buttons and joysticks to show rolling texts."


"I think it is an interesting an idea, and I am thinking that you can use both speaker and text display to clearly convey the message."


## Prototype your system

The system should:
* use the Raspberry Pi 
* use one or more sensors
* require participants to speak to it. 

*Document how the system works*
![alt text](https://github.com/iamyuchy/Interactive-Lab-Hub/blob/Spring2021/Lab%203/system.JPG)


The system will have 3 stages: Idle, Start Test, Present Results.

### Idle
During the idle stage, the display will show a emoticon like this "(-_-) zzzZZZ"

### Start Test
When a user says "Start Test" or "Start" or "Test" or "Hi" or "Hello", the system will enter the next stage.

The display will show a wake-up emoticon "╭( ๐ _๐)╮" and start to display questions. The user will enter the result by answering the questions vocally and then pressing the joystick.

### Present Results
After finishing a series of questions, the system will present the results. The results will accompanied with a random emoticon. The results will stay for 10 seconds and then the system will return back to the Idle stage.

*Include videos or screencaptures of both the system and the controller.*

Full video link:
https://drive.google.com/file/d/1SE1ETttaJaDRAs7LzBmJGKKse9qkzk-3/view?usp=sharing

## Test the system
Try to get at least two people to interact with your system. (Ideally, you would inform them that there is a wizard _after_ the interaction, but we recognize that can be hard.)

Answer the following:

### What worked well about the system and what didn't?
The voice command to start the test works well. The text on the display also helps since it gives some visual feedback to the user.
However, the other voice commands to answer the questions did not work smoothly.

### What worked well about the controller and what didn't?
The button clicking and directional controlling of the JoyStick is very intuitive: no extra explaination needed. However, in this system we don't need many directional data. As a result, the JoyStick hasn't been fully utilized, especially with the voice control.

### What lessons can you take away from the WoZ interactions for designing a more autonomous version of the system?
I learnt that multimodal user interface needs extra consideration about what type of interactions suit which modality. Voice control has its own strength for providing humanized responses, while JoyStick itself is a power input source and controller. For some simple task, like the personality test I designed here, the multimodality may simply increases the complexity without creating additional value.


### How could you use your system to create a dataset of interaction? What other sensing modalities would make sense to capture?
For the dataset of interaction, I can classfifed them based on what modalities are most suitable for it. The other modality I want to capture is definitely using a camera to do face or object recognization. The other modality could be a motion sensor.

