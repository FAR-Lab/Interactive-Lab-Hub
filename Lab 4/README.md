# Ph-UI!!!

Now it's time to ocus on prototyping the physical look and feel of the device.

## Prototype Readings

* [What do prototypes prototype?](https://www.semanticscholar.org/paper/What-do-Prototypes-Prototype-Houde-Hill/30bc6125fab9d9b2d5854223aeea7900a218f149)

* [Paper prototyping](https://www.uxpin.com/studio/blog/paper-prototyping-the-practical-beginners-guide/) is used by UX designers to quickly develop interface ideas and run them by people before any programming occurs. 

* [Cardboard prototypes](https://www.youtube.com/watch?v=k_9Q-KDSb9o) help interactive product designers to work through additional issues, like how big something should be, how it could be carried, where it would sit. 

* [Tips to Cut, Fold, Mold and Papier-Mache Cardboard](https://makezine.com/2016/04/21/working-with-cardboard-tips-cut-fold-mold-papier-mache/) from Make Magazine.

* [Surprisingly complicated forms](https://www.pinterest.com/pin/50032245843343100/) can be built with paper, cardstock or cardboard.  The most advanced and challenging prototypes to prototype with paper are [cardboard mechanisms](https://www.pinterest.com/helgangchin/paper-mechanisms/) which move and change. 

<p align="center">
<img src="https://dysonthedesigner.weebly.com/uploads/2/6/3/9/26392736/427342_orig.jpg"  width="200" > 

Dyson Vacuum cardboard prototypes
</p>

## Acknowledgements

For this project, there are a number of individuals that I would like to give credit to for their input on the "honest mirror":
* For the weather emojis used from: [Michael Flarup](https://blog.prototypr.io/designing-weather-up-cf248e47b5d8)
* Shivani Doshi, Niki Agrawal, Hortense Gimonet, and Snigdha Singhania (and many other classmates I'm sure I'm forgetting) for their thoughts, feedback, and advice on this idea.

## Overview
Here are the parts of the assignment

A) [Capacitive Sensing](#part-a)

B) [OLED screen](#part-b) 

C) [Paper Display](#part-c)

D) [Wizard the device](#part-d-wizard-the-device) 

E) [Costume the device](#part-e-costume-the-device)

F) [Record the interaction](#part-f-record)

## Part A - Capacitive Sensing, a.k.a. Human Banana Interaction

The [capacitive sensor](https://learn.adafruit.com/adafruit-mpr121-gator) a very flexible input sensor. It measures the capacitance on each of the 12 contacts. Whenever that capacitance changes it considers it a user touch. You can attach any conductive material and it will recognize when you touch it.

<p align="center">
<img src="https://cdn-learn.adafruit.com/guides/cropped_images/000/003/226/medium640/MPR121_top_angle.jpg?1609282424" height="150" />
<img src="https://cdn-shop.adafruit.com/1200x900/4401-01.jpg" height="150">
<img src="https://post.healthline.com/wp-content/uploads/2020/08/banana-pink-background-thumb-1-732x549.jpg" height="150">
</p>

Plug in the capacitive sensor board with the qwiic connector. Connect your banana's with either the copper tape or the alligator clips (the clips work better).

![](https://media.discordapp.net/attachments/679721816318803975/823299613812719666/PXL_20210321_205742253.jpg?width=1518&height=1139)

An example with twizzlers attached to pins 6 and 10. When you run the code and touch a banana the terminal will print out the following

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python cap_test.py 
Banana 10 touched!
Banana 6 touched!
```

For my demo, I used the conductive tape rather than attaching another prop to show the versatility and usefulness of the capacitive touch sensor.

![](https://github.com/snlee159/Interactive-Lab-Hub/blob/Spring2021/Lab%204/imgs/cap_test.png)

You can see this setup in action in the demo below!

[![](https://github.com/snlee159/Interactive-Lab-Hub/blob/Spring2021/Lab%204/imgs/cap_test_demo_img.png)](https://drive.google.com/file/d/1u8lcGNRIYDVawGsenFPpNi-005Z1B-pH/view)

## Part B - OLED screen

We just received some of the small oled screens that we had coped to include in your kit. If you want one feel free to pop into the lab and get one. These don't have colors like the one on the pi but you can move it around on a cable making for more flexible interface design. The way you program this display is almost identical to the pi display. Take a look at `oled_test.py` and some more of the [Adafruit examples](https://github.com/adafruit/Adafruit_CircuitPython_SSD1306/tree/master/examples).

<p align="center">
<img src="https://cdn.sparkfun.com//assets/parts/1/6/1/3/5/17153-SparkFun_Qwiic_OLED_Display__0.91_in__128x32_-01.jpg" height="200" />
<img src="https://cdn.discordapp.com/attachments/679466987314741338/823354087105101854/PXL_20210322_003033073.jpg" height="200">
</p>

Unfortunately, I was not in New York at the time of this lab so have not received my OLED screen yet. Thus, I do not have any demos to show for this section but I did take a look at the test script and feel it is fairly straightforward. 

## Part C - Paper Display

Here is an Pi with a paper faceplate on it to turn it into a display:

<p align="center">
<img src="https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/images/paper_if.png?raw=true"  width="250"/>
</p>

This is fine, but it can be a bit difficult to lay out a great and user friendly display within the constraints of the Pi. Also, it really only works for applications where people can come and stand over the Pi, or where you can mount the Pi to the wall.

Here is another prototype for a paper display:

<p align="center">
<img src="https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/images/b_box.png?raw=true"  width="250"/>
</p>

It holds a pi and usb power supply, and provides a front stage on which to put writing, graphics, LEDs, buttons or displays.

This design can be made by scoring a long strip of corrugated cardboard of width X, with the following measurements:

| Y height of box <br> <sub><sup>- thickness of cardboard</sup></sub> | Z  depth of box <br><sub><sup>- thickness of cardboard</sup></sub> | Y height of box  | Z  depth of box | H height of faceplate <br><sub><sup>* * * * * (don't make this too short) * * * * *</sup></sub>|
| --- | --- | --- | --- | --- | 

Fold the first flap of the strip so that it sits flush against the back of the face plate, and tape, velcro or hot glue it in place. This will make a H x X interface, with a box of Z x X footprint (which you can adapt to the things you want to put in the box) and a height Y in the back. 

Here is an example:

<p align="center">
<img src="https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/images/horoscope.png?raw=true"  width="250"/>
</p>

### My Idea
For this lab, I decided to create "The Honest Mirror" as an aid for people to get feedback on how they look at they are leaving their homes. This idea came about because, while visiting family in LA, I realized I kept almost forgetting to wear my mask when I left home because there is no mirror by the entrance here like there is in my apartment in New York. This mirror not only will remind you to wear your mask but also will give you a heads up as to what weather you can expect outside and how you look. Unfortunately, this mirror is quite picky with how it looks and holds you to the same standard. Most of the time, it will disapprove of your appearance. Every now and then, though, it will give you some nice validation.

I've included an initial concept of The Honest Mirror below with what components I expect it will need for my intended functionality.

<p align="center">
  <img src="https://github.com/snlee159/Interactive-Lab-Hub/blob/Spring2021/Lab%204/imgs/concept_board.png"/>
</p>

In order to be a reasonable product, I expect the Honest Mirror will need to meet the following criteria:
* It will need to be large enough to allow a face and the miniPiTFT screen while also having enough space for the user to look at their own reflection.
* Given the mirror is intended to be placed near the entrance to the user's home, the device can be expected to be viewed from within a couple feet. Given this criteria, the text on the miniPiTFT should be large enough and simple enough as to be legible from a distance of two feet away at most.
* I wish my skills with paper prototyping were good enough to make a really elaborate mirror frame design. However, given this is my first foray into prototyping movement and with cardboard at all, I will stick to a simple rectangular frame as this is still a common mirror shape. There should be some frame shape for the device though, to make it clearer that it is a mirror.

As displayed in the concept board image above, I expect the device to require the following components:
* A "mirror" frame and reflective surface
* A "face" with movable mouth and eyes
* A servo motor for enabling facial movement
* The miniPiTFT screen for displaying weather information
* Another screen (possibly the OLED) for displaying mask alerts if the user has forgotten their mask.

### Show the paper prototypes (initial versions)
#### Look-like Prototype
For the initial look-like prototype, I decided just to do a simple sketch on paper to show my ideal level of detail and feel of the design. 

<p align="center">
  <img src="https://github.com/snlee159/Interactive-Lab-Hub/blob/Spring2021/Lab%204/imgs/look_like_proto.png"/>
</p>

A simple yet elegant frame surrounds the mirror and a detailed face appears which will speak to the user. The face is meant to be friendly and calming (despite how it often judges your appearance) to appeal to the user. Beneath the screen lies the weather information and the mask alert. The face is quite large here and takes up a good portion of the mirror. Ideally, the face would only appear after the user is able to see their own appearance and is preparing to leave so as to not get in the user's way of seeing their reflection.

The weather and mask icons are meant to be minimalist and clean. This is meant to not distract from the mirror itself and the face and to give a sense of modern style that goes well with the simpler rectangular frame.

I decided to use a drawing for the look-lide prototype rather than actually building a three dimensional model out of paper because I felt my drawing skills were far better than my cutting and folding skills. Because of this, I felt my drawing would better convey the image and feel (sleek, modern, and minimalist) I hoped to create with the honest mirror.

#### Work-like Prototype
For the work-like prototype, I took my look-like design and iterated on it by adding movable components for the face, mask alert, and weather update to better depict how the system would work. This is done with many, many layers of paper in the backing of the mirror to keep each movable component separate. The final work-like prototype is shown below.

<p align="center">
   <img src="https://github.com/snlee159/Interactive-Lab-Hub/blob/Spring2021/Lab%204/imgs/work_like_proto.png"/>
</p>

And the different movements depicting how the mirror would work are demo'd in the below video.

[![](https://github.com/snlee159/Interactive-Lab-Hub/blob/Spring2021/Lab%204/imgs/paper_work_like_proto_img.png)](https://drive.google.com/file/d/1gV5UBAz4GE8IAhO4yhOsCvPgC7pAzlf8/view)

The different parts required to make this work-like prototype are described below:
* A top layer "face" with eyes and mouth cutouts
* A bottom lip with a rectangular bottom portion for demonstrating mouth movement
* A rectangular scrap of paper with eyes drawn on it for showing eye movement
* The top layer of the mirror with cutouts for the eyes, mouth, weather (temperature and atmospheric), and mask alerts
* The mirror frame (strips of paper folded for a three dimensional feel and taped along the mirror edges)
* The second layer of the mirror backing which sits between the eye strip and the mouth to allow for independent movement of the two (has cutouts for all components except the eyes since they sit on top of this layer)
* A third layer of mirror backing which sits between the mouth cutout and the atmospheric updates and mask alert (with cutouts for the weather updates and mask alert, no cutout for the mouth since that sits on top of this layer)
* A strip of paper with different weather icons for showing atmospheric updates such as sunny, rainy, etc.
* A cut out of a cover indicating whether or not the user is wearing their mask (a cross out appears above the mask icon if they are not wearing a mask)
* A fourth layer of mirror backing which sits under the atmospheric updates and the mask alert and above the temperature updates (with more cutouts for the temperature updates
* Two strips for the temperature updates, one for each level of digits (tens and ones)
* A fifth and final layer of mirror backing to keep everything contained

The entire system is held together with generic tape.

#### Act-Like Prototype
To demonstrate how I envision a user actually interacting with the Honest Mirror, I've created a storyboard below. Ideally, the user would observe their own appearance then, once they are ready to leave, the mirror would give them last minute updates they may have missed (i.e. weather, mask, appearance).

<p align="center">
  <img src="https://github.com/snlee159/Interactive-Lab-Hub/blob/Spring2021/Lab%204/imgs/storyboard.png"/>
</p>

## Part D - Materiality
### Design of the product
For this portion, I decided to build on my paper prototype of the honest mirror and bring it to life with moving components in a sturdier form. In addition to the components mentioned in the concept board above, I've also decided to include a proximity sensor for the user to be able to trigger an interaction with a wave of their hand.

To start, I practiced cutting the cardboard into the necessary shape for the frame. I made a frame prototype which has a square "frame" and a slot to slide the bulk of the device into the frame. The device itself will be connected completely to this insert so that maintenance is easy and the device can simply be slid in and out of the frame. The frame prototype is shown below.

<p align="center">
  <img src="https://github.com/snlee159/Interactive-Lab-Hub/blob/Spring2021/Lab%204/imgs/frame_proto.png"/>
</p>

By prototyping the frame, I was able to quickly understand what structure I would need to design and what the dimensions should be for the frame.

The complete system, in frame, is shown below. Unfortunately, the gap between the frame and the backing ended up being slightly too narrow and I did not have enough cardboard to start again. Thus, you'll see in the back view, that I had to add some clasps for holding the system shut and for easier inserting and removal of the device into the frame.

<p align="center">
  <img src="https://github.com/snlee159/Interactive-Lab-Hub/blob/Spring2021/Lab%204/imgs/front_view.png" width=30%/>
  <img src="https://github.com/snlee159/Interactive-Lab-Hub/blob/Spring2021/Lab%204/imgs/back_clasped.png" width=30%/>
  <img src="https://github.com/snlee159/Interactive-Lab-Hub/blob/Spring2021/Lab%204/imgs/back_unclasped.png" width=30%/>
</p>

### Components/functionality
tbd

### demo working
tbd

## Reflection
### What went well
tbd

### What could have gone better?
tbd

### What do I wish I could have done?
mask alert -> didn't have another screen
better frame sizing -> made the mirror too big and didn't have enough cardboard
More elaborate frame -> limited cardboard experience/skills
smoother face motions -> limited cardboard experience/skills
