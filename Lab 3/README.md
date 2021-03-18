# You're a wizard, Sam

<img src="https://pbs.twimg.com/media/Cen7qkHWIAAdKsB.jpg" height="400">

In this lab, we want you to practice wizarding an interactive device as discussed in class. We will focus on audio as the main modality for interaction but there is no reason these general techniques can't extend to video, haptics or other interactive mechanisms. In fact, you are welcome to add those to your project if they enhance your design.

## Acknowledgements
I would like to thank Shivani Doshi, Ritika Poddar, and Ilan Mandel for brainstorming with me and giving feedback on my project idea. The exact feedback is listed in Part 2 below.

## Text to Speech and Speech to Text

The demo `text2speech` files:

```
pi@ixe00:~/text2speech $ ls
Download        festival_demo.sh  GoogleTTS_demo.sh  pico2text_demo.sh
espeak_demo.sh  flite_demo.sh     lookdave.wav

```

were run and resulted in the following:

[![](https://github.com/snlee159/Interactive-Lab-Hub/blob/Spring2021/Lab%203/text2speechdemosimage.png)](https://drive.google.com/file/d/1V3xPS5feFjIEdYPoxQkmjCmJgabt5b9p/view?usp=sharing)

Similarly, running `./vosk_demo_mic.sh` and saying `One Two Three` resulted in the following printout from `speech2text`:
```
{
  "result" : [{
      "conf" : 1.000000,
      "end" : 2.340000,
      "start" : 1.980000,
      "word" : "one"
    }, {
      "conf" : 1.000000,
      "end" : 3.030000,
      "start" : 2.520000,
      "word" : "two"
    }, {
      "conf" : 1.000000,
      "end" : 3.600000,
      "start" : 3.090000,
      "word" : "three"
    }],
  "text" : "one two three"
}
```

Showing that Vosk was accurately hearing my words and interpreting them properly.

## Serving Pages

The simple webserver was called with the following command:

```
(idd_env) pi@ixe00:~/Documents/Interactive-Lab-Hub/Lab 3$ python server.py
```

Navigating to http://ixe00.local:5000]() resulted in a simple "Hello World" webpage:

[![Screen Shot 2021-03-17 at 6 18 59 PM](https://user-images.githubusercontent.com/33201141/111559156-408ac580-874d-11eb-850c-9bde1a75360e.png)

## Demo

In the [demo directory](./demo), an example wizard of oz project template with the following command:

```
(idd_env) pi@ixe00:~/Documents/Interactive-Lab-Hub/Lab 3/demo $ python app.py
```

In that project, audio and sensor data is streamed from the Pi to a wizard controller that runs in the browser. You can control what system says from the controller as well. You can see the demo running below:

![Screen Shot 2021-03-17 at 6 28 36 PM](https://user-images.githubusercontent.com/33201141/111559886-99a72900-874e-11eb-8d6a-1a155abd40f6.png)

Where the top graph is showing an accelerometer's reading, the `Eavesdrop` button allows you to hear what a person is saying via the microphone, and the `Speak` box allows you to type in the box and have the pi say whatever you type.

## Optional

There is an included [dspeech](.dspeech) demo that uses [Mozilla DeepSpeech](https://github.com/mozilla/DeepSpeech) for speech to text. This is run with the following command:

```
(dspeech_env) pi@ixe00:~/Documents/Interactive-Lab-Hub/Lab 3/dspeech $ python deepspeech_demo.py -m deepspeech-0.9.3-models.tflite -s deepspeech-0.9.3-models.scorer
```

While the system consistently misses the first word that I say as it is just recognizing that I'm speaking then, it interprets my words fairly well. Here's the output from a test I ran:

```
Recognized: testing testing testing
Recognized: hello can you hear me i'm talking to you
Recognized: i am talking to you right now and you are interpreting everything that i say
```

# Lab 3 Part 2

Create a system that runs on the Raspberry Pi that takes in one or more sensors and requires participants to speak to it. Document how the system works and include videos of both the system and the controller

## Prep for Part 2
I've decided to make a "bomb" game. The user has to perform various tasks, including solving riddles, in order to "diffuse" the bomb and win the game. The process I've decided on is sketched below:

![lab_schematic](https://user-images.githubusercontent.com/33201141/111568294-b5fe9200-875d-11eb-9470-a03c4f517822.png)

## Share your idea sketches with Zoom Room mates and get feedback
I pitched this idea to four people: Shivani Doshi, Ritika Poddar, Dhanya Lakshmi, and Ilan Mandel. Their thoughts are mentioned below:

From Shivani:
```
Shivani thought it was a cool idea. She suggested some fun questions the bomb could ask the player and how animations could be shown on the miniPiTFT.
```

From Ritika:
```
She liked the idea and we spent some time talking about applications of the proximity sensor in both of our projects.
```

From Dhanya:
```
Lean into the Monty Python theme and have the system say "Ni!" everytime the user gets too close.
```

From Ilan:
```
Ilan thought it was a cool idea. He suggested also using the proximity sensor as a color sensor and sending the player on tasks to bring the bomb things of a specific color. I like this idea a lot and it will be incorporated into the task list.
```

## Prototype your system
List components, tasks, interaction expectations, what is Wizarded and what isn't, and show my built wizarding portal.

[Add images of all of the above]

[Add demo video]

## Test the system
I'm currently quarantining in Los Angeles which means I don't have access to many friends to interact with the system. I did however recruit my significant other to interact with it. (Note, I did not explain to him how it works beforehand but he did see me building it so it wasn't a perfectly novel system for him.)

A video of his interaction with the game is shown below:

[Add interaction video]

## Reflection
### What worked well about the system and what didn't?
*your answer here*

### What worked well about the controller and what didn't?
*your answer here*

### What lessons can you take away from the WoZ interactions for designing a more autonomous version of the system?
*your answer here*

### How could you use your system to create a dataset of interaction? What other sensing modalities would make sense to capture?
*your answer here*
