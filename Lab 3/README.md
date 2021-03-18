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
From a remote browser on the same network, check to make sure your webserver is working by going to [http://ixe00.local:5000]()


## Demo

In the [demo directory](./demo), you will find an example wizard of oz project you may use as a template. **You do not have to** feel free to get creative. In that project, you can see how audio and sensor data is streamed from the Pi to a wizard controller that runs in the browser. You can control what system says from the controller as well.

## Optional

There is an included [dspeech](.dspeech) demo that uses [Mozilla DeepSpeech](https://github.com/mozilla/DeepSpeech) for speech to text. If you're interested in trying it out we suggest you create a seperarate virutalenv. 

# Lab 3 Part 2

Create a system that runs on the Raspberry Pi that takes in one or more sensors and requires participants to speak to it. Document how the system works and include videos of both the system and the controller

## Prep for Part 2
1. Sketch ideas for what you'll work on in lab on Wednesday.

## Share your idea sketches with Zoom Room mates and get feedback
what was the feedback? Who did it come from?

## Prototype your system
The system should:
* use the Raspberry Pi
* use one or more sensors
* require participants to speak to it

Document how the system works

Include videos or screencaptures of both the system and the controller.

## Test the system

Try to get at least two people to interact with your system. (Ideally, you would inform them that there is a wizard after the interaction, but we recognize that can be hard.)

Answer the following:

### What worked well about the system and what didn't?
*your answer here*

### What worked well about the controller and what didn't?

*your answer here*

### What lessons can you take away from the WoZ interactions for designing a more autonomous version of the system?

*your answer here*


### How could you use your system to create a dataset of interaction? What other sensing modalities would make sense to capture?

*your answer here*
