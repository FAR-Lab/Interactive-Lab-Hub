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

The script 'name.sh' can be found in the scripts folder of this repo: https://github.com/rohangreddy/Interactive-Lab-Hub/blob/Fall2021/Lab%203/scripts/name.sh 

Bonus: If this topic is very exciting to you, you can try out this new TTS system we recently learned about: https://github.com/rhasspy/larynx

### Speech to Text

Now examine the `speech2text` folder. We are using a speech recognition engine, [Vosk](https://alphacephei.com/vosk/), which is made by researchers at Carnegie Mellon University. Vosk is amazing because it is an offline speech recognition engine; that is, all the processing for the speech recognition is happening onboard the Raspberry Pi. 

In particular, look at `test_words.py` and make sure you understand how the vocab is defined. Then try `./vosk_demo_mic.sh`

One thing you might need to pay attention to is the audio input setting of Pi. Since you are plugging the USB cable of your webcam to your Pi at the same time to act as speaker, the default input might be set to the webcam microphone, which will not be working for recording.

\*\***Write your own shell file that verbally asks for a numerical based input (such as a phone number, zipcode, number of pets, etc) and records the answer the respondent provides.**\*\*

The shell file zipcode_test.sh can be found in the scripts folder of this repo: https://github.com/rohangreddy/Interactive-Lab-Hub/blob/Fall2021/Lab%203/scripts/name.sh 

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

\*\***Post your storyboard and diagram here.**\*\*

The idea is to have the Pi act as an auditory checklist for various covid-19 related precautions and symptom checks. For example, as Cornell Tech students, we have to get tested for covid weekly but I frequently find myself forgetting to go and end up rushing to get tested at the last possible minute. The first question the Pi could ask is "Have you been tested for covid this week" and accept a simple yes or no response. The Pi could then go through a standard list of covid-19 related symptoms, asking "Do you have a fever or chills", "Do you have a headache", "Do you have a cough", etc. and listen for responses from the user. I anticipate that most responses will be in yes or no form. The Pi can then provide responses/guidance when all questions have been asked (or provide questions by question responses). For example, if the answer to "Have you been tested this week?" is "No", the Pi could remind the user of the testing schedule for the week. 

Finally, the Pi could assess the answers to the symptom questions and provide a summary of the users responses. It could end with recommending the user to quarantine, see their physician, or go about their day.

These questions have been adapted from the OSHA employee COVID-19 screening questionnaire: https://www.osha.gov/sites/default/files/publications/OSHA4132.pdf

![alt text](https://github.com/rohangreddy/Interactive-Lab-Hub/blob/Fall2021/Lab%203/storyboard.JPG)

Write out what you imagine the dialogue to be. Use cards, post-its, or whatever method helps you develop alternatives or group responses. 

\*\***Please describe and document your process.**\*\*

![alt text](https://github.com/rohangreddy/Interactive-Lab-Hub/blob/Fall2021/Lab%203/checklist.JPG)

I initially anticipated that most responses would be yes or no answers. However, many of the questions are in either-or format. For example, "Do you have fever or chills". While the standard yes or no responses would work here, some people would answer "fever" or "chills". Additionally, people might provide even more information such as their temperature value. There are many different answers to anticipate, and it might be simplest to structure the questions to purely accept yes or no answers.

### Acting out the dialogue

Find a partner, and *without sharing the script with your partner* try out the dialogue you've designed, where you (as the device designer) act as the device you are designing.  Please record this interaction (for example, using Zoom's record feature).

\*\***Describe if the dialogue seemed different than what you imagined when it was acted out, and how.**\*\*

Video link: https://youtu.be/_s3BVtuhlvw

Special thanks to Marissa for allowing me to test out the script with her!

The dialogue was a lot different from what I imagined. Some of the questions were answered with a straightforward yes or no, but for many of the symptom questions, there was a tendency to describe the symptom in further detail. For instance, when I asked Marissa if she had a fever, she responded with "a little". Also, when asked about multiple symptoms, there was a tendency to choose the symptom that was experienced. It will be difficult to anticipate all of the nuances of the answers to these questions, so I might try to structure them to try and elicit a straightforward yes or no response.

### Wizarding with the Pi (optional)
In the [demo directory](./demo), you will find an example Wizard of Oz project. In that project, you can see how audio and sensor data is streamed from the Pi to a wizard controller that runs in the browser.  You may use this demo code as a template. By running the `app.py` script, you can see how audio and sensor data (Adafruit MPU-6050 6-DoF Accel and Gyro Sensor) is streamed from the Pi to a wizard controller that runs in the browser `http://<YouPiIPAddress>:5000`. You can control what the system says from the controller as well!

\*\***Describe if the dialogue seemed different than what you imagined, or when acted out, when it was wizarded, and how.**\*\*

# Lab 3 Part 2

For Part 2, you will redesign the interaction with the speech-enabled device using the data collected, as well as feedback from part 1.

## Prep for Part 2

1. What are concrete things that could use improvement in the design of your device? For example: wording, timing, anticipation of misunderstandings...

From acting out the dialogue, I found that some of the questions were structured to be too complicated. For example, some questions were in either-or format (i.e. do you have a fever or chills?). These types of questions confused the participant, as they were not sure to answer with a yes or no or to identify the symptom that they have been experiencing. Structuring the questions to accept yes or no answers would be much clearer for participants.

The timing of the dialogue felt a bit rushed. Adding a pause in between questions and responses would be useful to give participants time to think about their responses and give a well thought out answer to the question.

One other point of feedback was that it was a bit jarring for participants to immediately jump in to answering questions about medical information. Some introductory statements from the Pi would be useful to prep participants on what they should expect.

Additionally, I received good feedback from the peer critiques. One person mentioned that I should consider the setting further. Therefore, I have decided to design the pi as a digital medical assistant that is used in doctors offices. There is usually downtime when a patient is in the examining room but still waiting for the doctor. This represents a moment where a digital medical assistant can collect important information from the patient and send the patient's responses directly to the EMR. Therefore, when the doctor arrives, they do not need to waste time asking the patient basic questions and can see the responses to the questions they would have asked. 

Some other feedback I received is that there should be some follow up to questions that participants answer yes to. For example, if a participant answers yes to having a cough, a follow up question could be "On a scale of 1-10, how bad is the cough?". Follow up questions would provide the doctor with more information about the patient's experience of the symptom. 

2. What are other modes of interaction _beyond speech_ that you might also use to clarify how to interact?

I received some feedback that participants may not be comfortable speaking about sensitive medical information verbally outloud where this information could possibly be overheard by others. Therefore, I will be adding 2 led buttons that participants can use to indicate whether they are experiencing the symptom (green LED) or not (red LED). These two buttons also indicate to the participants that the answer to the questions should be binary (yes or no). 

Additionally, as the device is now a digital medical assistant, it needs to display a modicum of professionalism appropriate for a physician's office. An accelerometer will be incorporated with the device that will allow for patients to "shake the hand" of the assistant when it first introduces itself. This should allow patients to become more comfortable with the assistant and better answer questions about their symptoms. It will also indicate to the system (and the wizard) that the participant is ready to interact. 

5. Make a new storyboard, diagram and/or script based on these reflections.

![alt text](https://github.com/rohangreddy/Interactive-Lab-Hub/blob/Fall2021/Lab%203/Capture.PNG)

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

\*\**your answer here*\*\*


### How could you use your system to create a dataset of interaction? What other sensing modalities would make sense to capture?

\*\**your answer here*\*\*

