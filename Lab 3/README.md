# Chatterboxes
**NAMES OF COLLABORATORS HERE**
John Li (jl4239), Shiying Wu (sw2298), Mingze Gao (mg2454), Crystal Chong (cc2795), Qianxin(Carl) Gan (qg72), Mingzhe Sun (ms3636)

[![Watch the video](https://user-images.githubusercontent.com/1128669/135009222-111fe522-e6ba-46ad-b6dc-d1633d21129c.png)](https://www.youtube.com/embed/Q8FWzLMobx0?start=19)

In this lab, we want you to design interaction with a speech-enabled device--something that listens and talks to you. This device can do anything *but* control lights (since we already did that in Lab 1).  First, we want you first to storyboard what you imagine the conversational interaction to be like. Then, you will use wizarding techniques to elicit examples of what people might say, ask, or respond.  We then want you to use the examples collected from at least two other people to inform the redesign of the device.


## Prep for Part 1: Get the Latest Content and Pick up Additional Parts 

### Pick up Web Camera If You Don't Have One

Students who have not already received a web camera will receive their [IMISES web cameras](https://www.amazon.com/Microphone-Speaker-Balance-Conference-Streaming/dp/B0B7B7SYSY/ref=sr_1_3?keywords=webcam%2Bwith%2Bmicrophone%2Band%2Bspeaker&qid=1663090960&s=electronics&sprefix=webcam%2Bwith%2Bmicrophone%2Band%2Bsp%2Celectronics%2C123&sr=1-3&th=1) on Thursday at the beginning of lab. If you cannot make it to class on Thursday, please contact the TAs to ensure you get your web camera. 

**Please note:** connect the webcam/speaker/microphone while the pi is *off*. 

### Get the Latest Content

As always, pull updates from the class Interactive-Lab-Hub to both your Pi and your own GitHub repo. There are 2 ways you can do so:

**[recommended]** Option 1: On the Pi, `cd` to your `Interactive-Lab-Hub`, pull the updates from upstream (class lab-hub) and push the updates back to your own GitHub repo. You will need the *personal access token* for this.

```
pi@ixe00:~$ cd Interactive-Lab-Hub
pi@ixe00:~/Interactive-Lab-Hub $ git pull upstream Fall2023
pi@ixe00:~/Interactive-Lab-Hub $ git add .
pi@ixe00:~/Interactive-Lab-Hub $ git commit -m "get lab3 updates"
pi@ixe00:~/Interactive-Lab-Hub $ git push
```

Option 2: On your your own GitHub repo, [create pull request](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2022Fall/readings/Submitting%20Labs.md) to get updates from the class Interactive-Lab-Hub. After you have latest updates online, go on your Pi, `cd` to your `Interactive-Lab-Hub` and use `git pull` to get updates from your own GitHub repo.

## Part 1.
### Setup 

*DO NOT* forget to work on your virtual environment! 

Run the setup script
```chmod u+x setup.sh && sudo ./setup.sh  ```

### Text to Speech 

In this part of lab, we are going to start peeking into the world of audio on your Pi! 

We will be using the microphone and speaker on your webcamera. In the directory is a folder called `speech-scripts` containing several shell scripts. `cd` to the folder and list out all the files by `ls`:

```
pi@ixe00:~/speech-scripts $ ls
Download        festival_demo.sh  GoogleTTS_demo.sh  pico2text_demo.sh
espeak_demo.sh  flite_demo.sh     lookdave.wav
```

You can run these shell files `.sh` by typing `./filename`, for example, typing `./espeak_demo.sh` and see what happens. Take some time to look at each script and see how it works. You can see a script by typing `cat filename`. For instance:

```
pi@ixe00:~/speech-scripts $ cat festival_demo.sh 
#from: https://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)#Festival_Text_to_Speech
```
You can test the commands by running
```
echo "Just what do you think you're doing, Dave?" | festival --tts
```

Now, you might wonder what exactly is a `.sh` file? 
Typically, a `.sh` file is a shell script which you can execute in a terminal. The example files we offer here are for you to figure out the ways to play with audio on your Pi!

You can also play audio files directly with `aplay filename`. Try typing `aplay lookdave.wav`.

\*\***Write your own shell file to use your favorite of these TTS engines to have your Pi greet you by name.**\*\*
(This shell file should be saved to your own repo for this lab.)
Here's the [shell file](./speech-scripts/greetings.sh) greeting us in our favorite TTS engine - the GoogleTTS.

Greeting shell file located in `\speech-scripts\greetings.sh`.

---
Bonus:
[Piper](https://github.com/rhasspy/piper) is another fast neural based text to speech package for raspberry pi which can be installed easily through python with:
```
pip install piper-tts
```
and used from the command line. Running the command below the first time will download the model, concurrent runs will be faster. 
```
echo 'Welcome to the world of speech synthesis!' | piper \
  --model en_US-lessac-medium \
  --output_file welcome.wav
```
Check the file that was created by running `aplay welcome.wav`. Many more languages are supported and audio can be streamed dirctly to an audio output, rather than into an file by:

```
echo 'This sentence is spoken first. This sentence is synthesized while the first sentence is spoken.' | \
  piper --model en_US-lessac-medium --output-raw | \
  aplay -r 22050 -f S16_LE -t raw -
```
  
### Speech to Text

Next setup speech to text. We are using a speech recognition engine, [Vosk](https://alphacephei.com/vosk/), which is made by researchers at Carnegie Mellon University. Vosk is amazing because it is an offline speech recognition engine; that is, all the processing for the speech recognition is happening onboard the Raspberry Pi. 
```
pip install vosk
pip install sounddevice
```

Test if vosk works by transcribing text:

```
vosk-transcriber -i recorded_mono.wav -o test.txt
```

You can use vosk with the microphone by running 
```
python test_microphone.py -m en
```

\*\***Write your own shell file that verbally asks for a numerical based input (such as a phone number, zipcode, number of pets, etc) and records the answer the respondent provides.**\*\*

Here's the [shell file](./speech-scripts/transcribe.sh) that acts as a voicemail message asking for a callback number, records the inputs, and transcribes to numerical outputs. The shell file also invokes a python script [ask_and_record.py](./speech-scripts/ask_and_record.py) that uses `vosk` to transcribe the audio.

[![Voice Mail](https://hackmd.io/_uploads/SyaHD7Je6.jpg)](https://www.youtube.com/watch?v=cD3JbQLfFVg)



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
![](https://hackmd.io/_uploads/B1RiW_yep.jpg)



Write out what you imagine the dialogue to be. Use cards, post-its, or whatever method helps you develop alternatives or group responses. 

\*\***Please describe and document your process.**\*\*

The Hotel Robot Butler, affectionately known as "TT", is an innovative and advanced speech-enabled device designed to revolutionize the guest experience within hospitality establishments, particularly hotels and resorts. TT is a cutting-edge fusion of artificial intelligence and robotics, seamlessly integrated into the hotel's environment to provide personalized and efficient service to guests.

To interact with "TT", the customer will need to say a sentence that includes the keyword "TT." We chose this name because it is not a word commonly used in conversation. Therefore, the device will not be activated accidentally. The device can provide any services offered by the hotel, such as breakfast options, locating objects in the room, ordering towels, room service, and more. It has an embedded AI language model that enables it to process and respond to conversations.


### Acting out the dialogue

Find a partner, and *without sharing the script with your partner* try out the dialogue you've designed, where you (as the device designer) act as the device you are designing.  Please record this interaction (for example, using Zoom's record feature).

Intended Script:
Question: what is the weather today?
Robot: Today is sunny, tempature of 75F
Question: Can you replace the towel?
Robot: For sure, A servant will come shortly.
Question: what is the time now?
Robot: Now is 9:30AM Sep 23rd
Question: Can you tell me a joke?
Robot: for sure, XXXX hahahahaha
Question: when does breakfast time end?
Robot: The breakfast hours is 6:30 to 9:30 everyday at floor 2nd
Question: can you connect me to front desk?
Robot: Calling Front Desk...

Actual Script
Kevin: Morning TT.
Robot Butler: Morning Kevin, how I can help you?
Kevin: What you get for breakfast today?
Robot Butler: For breakfast today, we have a selection of options. You can choose from a variety of cereals, fresh fruits, and toast with your choice of spreads. Additionally, there are some hot options like scrambled eggs, bacon, and pancakes. Please let me know your preference, and I'll prepare it for you.
Kevin: Can you give me a French toast with wipped cream and two bacons, and some blueberry please.
Robot Butler: No problem, I will send them your way. What else can I help you with?
Kevin: Yes TT, can you let me know where is my glasses?
Robot Butler: Let me check. Your glass are on the sink of the bathroom.
Kevin: Thank you, TT. 

<<<<<<< HEAD
=======
Click to watch the video:
>>>>>>> MingzheSun-Fall2023
[![Act Out](https://hackmd.io/_uploads/rk0TPmke6.jpg)](https://www.youtube.com/watch?v=MXm7EFBcMv8)

\*\***Describe if the dialogue seemed different than what you imagined when it was acted out, and how.**\*\*
    Before the dialogue, Our script was preping for questions like can you replace the towel or put do not disturbe, or some questions like weather or tempature. 
    But when we acted out, the first question was on what breakfast does the hotel provides and none of the question was expact, that was really surpising. 
    We figured it would be extremely hard to 'hard code' a script to fullfill it's designed purpose. NLP or big data model will be essanital for the chat bot to be  comprehensive in practise.


### Wizarding with the Pi (optional)
In the [demo directory](./demo), you will find an example Wizard of Oz project. In that project, you can see how audio and sensor data is streamed from the Pi to a wizard controller that runs in the browser.  You may use this demo code as a template. By running the `app.py` script, you can see how audio and sensor data (Adafruit MPU-6050 6-DoF Accel and Gyro Sensor) is streamed from the Pi to a wizard controller that runs in the browser `http://<YouPiIPAddress>:5000`. You can control what the system says from the controller as well!

\*\***Describe if the dialogue seemed different than what you imagined, or when acted out, when it was wizarded, and how.**\*\*


# Lab 3 Part 2

For Part 2, you will redesign the interaction with the speech-enabled device using the data collected, as well as feedback from part 1.

## Prep for Part 2

1. What are concrete things that could use improvement in the design of your device? For example: wording, timing, anticipation of misunderstandings

With our Part 1 creation, the Hotel Robot Butler, there exists a requirement for users to possess some prior knowledge or instructions to effectively engage with the device. Moreover, it can be uncertain as to the range of services the device is equipped to handle. In light of the upcoming Halloween season, we have chosen to craft a device that seamlessly integrates into Halloween decorations and offers an intuitive and straightforward interaction experience for users.


2. What are other modes of interaction _beyond speech_ that you might also use to clarify how to interact?

In the context of our Halloween device, we are contemplating the incorporation of additional interaction modes beyond speech to enhance user clarity. One approach involves utilizing a sensor that can detect when someone is approaching our door, subsequently triggering our speech detection feature. Additionally, we are considering the utilization of a servo motor mechanism to deliver an element of surprise or scare to the user, complementing the overall interaction experience.

3. Make a new storyboard, diagram and/or script based on these reflections.
![](https://hackmd.io/_uploads/BJN_X2_la.jpg)


Brainstorming Ideas:
- A doorbell trick-or-treat

## Prototype your system

The system should:
* use the Raspberry Pi 
* use one or more sensors
* require participants to speak to it. 

*Document how the system works*

**The system operates as follows:**

**Distance Sensor Activation:** A distance sensor is employed to monitor the proximity of individuals approaching the door. When a person comes within 0.5 meters of the door, where the device is securely attached, this sensor triggers the activation of the interaction system.

**Speech Detection:** Upon activation, the system initiates its speech detection feature, actively listening for the specific keyword, "trick or treat." This keyword serves as the trigger for further interaction.

**Random Puzzle Generation:** Subsequently, the system randomly selects one of the 100 available puzzles from its database. This selected puzzle is then vocalized by the system, providing the user with a unique Halloween-themed challenge.

**User Input:** After hearing the puzzle, the user is prompted to input their solution through the keyboard interface provided by the device. The keyboard allows the user to type in their answer.

**Answer Validation:** Once the user submits their answer, the system performs an immediate validation check to determine its correctness. If the user's answer aligns with the correct solution, the system triggers a rewarding response.

**Reward or Haunting:** In the event that the user's answer is correct, the system dispenses candy to the user as a Halloween treat, enhancing the interactive experience. However, if the answer is incorrect, the system engages a spooky or haunting response to add an element of surprise and excitement to the Halloween encounter.

*Include videos or screencaptures of both the system and the controller.*

*Click to watch the video: Introduction of the device*
[![Act Out](https://hackmd.io/_uploads/H1tFAlFga.png)](https://www.youtube.com/watch?v=yqGF0PsgBKE)

*Click to watch the video: Acting out*
[![Act Out](https://hackmd.io/_uploads/rk0Ozbtlp.png)](https://youtu.be/3kqRtDJEGQg)


## Test the system
Try to get at least two people to interact with your system. (Ideally, you would inform them that there is a wizard _after_ the interaction, but we recognize that can be hard.)

Answer the following:

### What worked well about the system and what didn't?


The distance detection feature effectively prevented speech recognition misinterpretation. This feature allows us to restrict false triggers from other voices, ensuring that only individuals in close proximity to the device can activate the entire system.

However, our current method for answering questions has limitations. We are restricted to using a keypad for input, which means that our system can only handle numerical questions.

### What worked well about the controller and what didn't?

The controller's integration of multiple sensors was impressive, especially its 500mm range which felt just right for detecting someone's proximity without being intrusive. This allowed for a fluid transition from sensing someone nearby to awaiting a voice command. However, a noticeable challenge was the voice recognition with individuals. Given the variety in pronunciations, there were instances where the controller struggled to accurately recognize the "trick or treat" phrase. Improvements in its ability to discern and adapt to diverse voice inputs would greatly enhance its reliability and user experience. 

### What lessons can you take away from the WoZ interactions for designing a more autonomous version of the system?

Through WoZ interactions, we gain valuable insights into a wide range of potential user behaviors when interacting with the system. For instance, before actually implemented our system, we started with a WoZ interactions. We discovered that user responses to our questions can be highly unpredictable. Consequently, we implemented restrictions on user input with hardware resource, keypad.

Furthermore, designing a more autonomous system is an ongoing, iterative journey. We continually uncover opportunities for enhancement, ensuring that our system evolves to meet user needs and expectations effectively.

### How could you use your system to create a dataset of interaction? What other sensing modalities would make sense to capture?

Recording the distances at which participants initiate interactions might reveal nuances in their approach behavior. Additionally, the voices of each individual will be recorded and consolidated into a dataset. By implementing machine learning algorithms, this dataset will aid the system in detecting the myriad ways people might pronounce "trick or treat," ensuring more accurate and inclusive activation. To deepen this interaction dataset, introducing additional sensors would be insightful. A camera, for instance, could observe facial expressions and body language during interactions, while an ambient light sensor might indicate if the device's visibility or attraction changes under different lighting conditions.
