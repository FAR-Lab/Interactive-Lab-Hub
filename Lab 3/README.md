# You're a wizard, Rui!! 😱🧙

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

![](simoncowell.jpeg)

The wizarding device is called the SimonCowell because it will judge a contestant's singing or dancing performance and provide feedback. If the performer gives a good performance, the SimonCowell will provide them with positive feedback and advance the contestant to the next round. If the performer gives a bad performance, the SimonCowell will provide them with negative feedback and tell them to leave. 

As a default, if the user does not press the button, the motion sensor will detect a dancing performance and the SimonCowell will watch the performance and provide them with feedback depending on whether the performance was good or not. If the user presses the red button, it will signal to the device that they are about to sing. The SimonCowell will then listen to the user sing and judge whether or not it is a good performance by providing feedback. 

In this lab, the accelerometer was used to detect the participant's motion/dancing and the Qwiic button was pressed to detect the participant's singing. 

## Share your idea sketches with Zoom Room mates and get feedback

*what was the feedback? Who did it come from?*

Brandt Beckerman: "Good idea! I like how it takes in movement and audio and the device will give a verbal response back." 

Antonio Mojena: "It's sort of like an 8 ball where you just shake it and you get a response. I wonder if you could make the device like a mic so that it senses how much you move while you sing and maybe base a response off of the movement as well."

## Prototype your system

The system should:
* use the Raspberry Pi 👍
* use one or more sensors 👍 (Qwiic Red Button and Accelerometer)
* require participants to speak to it. 👍 (Takes in contestant's singing!)

*Document how the system works*

*Include videos or screencaptures of both the system and the controller.*

The SimonCowell Lab Apparatus:
![](lab3.1.png)
![](lab3.2.png)
![](lab3.3.png)

Button to indicate singing: 
![](lab3.4.png)

[Video Walkthrough of the System](https://drive.google.com/file/d/1iZZjHekJbkAhmFUpk7fn5tYdL2Cp_7j1/view?usp=sharing)

## Test the system
Try to get at least two people to interact with your system. (Ideally, you would inform them that there is a wizard _after_ the interaction, but we recognize that can be hard.)

The system was tested out on Shreya Chandrasekar and Brandt Beckerman. The participant sat on a chair and put on headphones to listen to the speech from the wizarding device. 

Try to get at least two people to interact with your system. (Ideally, you would inform them that there is a wizard _after_ the interaction, but we recognize that can be hard.

Answer the following:

### What worked well about the system and what didn't?
*your answer here*

The wizarding system didn't have instructions in the beginning so Shreya wasn't sure what she was supposed to do as she put the headphones on. Although she saw a button connected to the device, she also didn't know whether or not she should push it. She seemed a little confused with what to do and then a few seconds later, the device gave feedback on her performance even though she didn't act. She found the overall system to be pretty amusing and fun to interact with but was just confused with what she should have done. Overall, this means that since there is no human in the front end of the device, it is especially important to make the directions on what to do to be very clear. It was important to set the stage for the participants on the context that they were in and then provide them with directions on what to do at the given time they should do it. 

Script for future reference:

Context: "You believe you have the X Factor and are auditioning for the SimonCowell by singing your favorite song to him. Today is your big day to see if you will advance to the next round of the competition! You will be judged by the SimonCowell after your performance and he will tell you whether or not you advance in the end. Good luck!" 

Directions: "When you are ready, please press the red button if you will be singing and do not press the red button if you will be dancing. Afterwards, start your audition." 

*If red button is pressed*: "Great! Please begin singing."
*If red button is NOT pressed*: "Since the button was not pressed, please begin dancing." 

After the performance: SimonCowell judgement from the wizarding device. 


### What worked well about the controller and what didn't?

*your answer here*

When Brandt interacted with the device, he briefly clicked on the button for one second to indicate singing but the SimonCowell ended up giving him dancing feedback. This showed that the controller only worked if it was pressed for an extended period of time, which may be confusing to the user if they do not know to do this. Next time, it will be important for the device to give further instructions telling the partcipant to press the button for X seconds. Overall, the button was easy to press and use. It was also good that the button was noticeable so that the participant automatically drew their attention to the button when they begin their audition. When Brandt was prompted to dance, he seemed to be a little confused with what exactly he should do to interact with the device, showing that we may need to include another button or sensor as a physical prompt so that the user knows to start dancing. 


### What lessons can you take away from the WoZ interactions for designing a more autonomous version of the system?

*your answer here*

For a future wizarding device, it will be very important to include very specific instructions on the context of the situation at the beginning so that the user generally understands what they should do. There should also be a direction given to the user before they are prompted to start any activity so that the user knows exactly when they should start and not end up waiting awkwardly around for the device to do something. It will also be important to make the sensor the user should interact with to be extremely noticeable so that the user will automatically draw their attention to this specific feature. A more autonomous version of the system will take in the user's motion and detect whenever the user has started and stopped moving. This way, feedback from the SimonCowell is given directly after the motion rather than after a set period of seconds (what it is currently programmed to do). Similarly, the more autonomous version of the system will take in the user's voice and detect whenever the user has started and stopped singing so that feedback is given at a natural time to the users. 


### How could you use your system to create a dataset of interaction? What other sensing modalities would make sense to capture?

*your answer here*

After more participants have interacted with the device and a dataset of various interactions is captured, it would be interesting to see the average length of time the user interacts with the device, the average length of time the user performs, the average length of time the user takes before performing any activity as directed by the device and the average length of time it takes for the user to press the button. By understanding the average length of time the user performs, the device would be better at predicting at what point in time the SimonCowell should be prepared to give feedback. By understanding the average length of time the user takes before performing any activity on the device, we can determine the user's general hesitation with the device and find ways to make the interactions more intuitive and clear. Finally, by understanding the average length of time it takes for the user to press the button, we can create a better controller system that actively takes in feedback from the user. 

It would also be interesting to see what types of performances participants usually give so that we can find some common indicators that would indicate whether or not the performance was good or bad so that the device can better determine whether the contestant should advance to the next round. After these indicators are identified from the growing dataset, the motion and voice detection sensor can recognize these patterns so that the SimonCowell can provide more accurate and relevant feedback in future interactions. 
