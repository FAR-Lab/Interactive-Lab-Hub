# Final Project

Using the tools and techniques you learned in this class, design, prototype and test an interactive device.

Functional check-off - May 10
 
Final Project Presentations (video watch party) - May 12



## Objective

The goal of this final project is for you to have a fully functioning and well-designed interactive device of your own design.
 
## Description
My final project is inspired by my Lab4 design: PiT Bot. The PiT Bot will be an Intelligent Voice Agent in a tiny lightweight box. The bot should be able to display emotion through emoticons, rotate if noticing people moving towards it, and communicate with people (mainly answering questions through voice).

<p float="left">
<img src="https://github.com/iamyuchy/Interactive-Lab-Hub/blob/Spring2021/Final%20Project/1.png" height="550" />
</p>

## Deliverables

### 1. Documentation of design process

The idea and basic concept of the PiT Bot is from my Lab4 design showing below. There are few key points: (1) I want it to be able to move or turn a bit, (2) I want it to be small and light, and (3) I want it to be cute.

<p float="left">
<img src="https://github.com/iamyuchy/Interactive-Lab-Hub/blob/Spring2021/Lab%204/storyboard.png" height="550" />
</p>

At the beginning, the first thing I chose to work on is to incorperate a servo motor, so the box for the PiT Bot can turn around, like what shown in the original storyboard. I got the the ADAFRUIT INDUSTRIES 155 STANDARD SERVO - TOWERPRO SG-5TOWERPRO SG-5010, but this motor requires a seperate power source and the AAA battery case I bought isn't working. 

As a result, I changed to a smaller servo: SG90, which can directly connect to the Pi 5V output. I also got the breadboard with correponding jumper wires and GPIO caples. However, after using this smaller servo, I realized it is impossible to get the breadboard and everything onto a tiny box. Even if everything fitted into a larger box, the servo may not have enough torque to rotate it. That's why in the end, the design changed to a LEGO base with a rotating head.

<p float="left">
<img src="https://github.com/iamyuchy/Interactive-Lab-Hub/blob/Spring2021/Final%20Project/servo1.png" height="250" />
<img src="https://github.com/iamyuchy/Interactive-Lab-Hub/blob/Spring2021/Final%20Project/servo2.png" height="250" />
</p>

The next step I did is to incorperate the LCD screen with emoticons and the Joystick for general system control. Following is a picture of the intermediate stage with the servo, LCD and joystick connected.

<p float="left">
<img src="https://github.com/iamyuchy/Interactive-Lab-Hub/blob/Spring2021/Final%20Project/3.png" height="550" />
</p>

Then suggested by the instructors, I added the conductive tapes on the head with the capative sensor, so I can "pat" the bot to activate it.

Lastly, I added the temperature and humidity sensor so I can have some sort of voice interaction with the PiT Bot.

### 2. Archive of all code, design patterns, etc. used in the final design. (As with labs, the standard should be that the documentation would allow you to recreate your project if you woke up with amnesia.)

#### hardware
Following is a picture showing the general hardware setups.

<p float="left">
<img src="https://github.com/iamyuchy/Interactive-Lab-Hub/blob/Spring2021/Final%20Project/2.png" height="550" />
</p>

The power, audio output and GPIO cable are connected directly to the Pi. 

The servo is connected to 5V, GND and GPIO 18 (showing in the picture below). 

> Useful tutorial link to set it up: 
> https://www.youtube.com/watch?v=xHDT4CwjUQE&t=203s 
> https://learn.adafruit.com/adafruits-raspberry-pi-lesson-8-using-a-servo-motor/parts

The temperature and humidity sensor (DHT11) is connected to 5V, GND and GPIO 17. 

> Useful tutorial link to set it up: 
> https://www.youtube.com/watch?v=1xgY5THjwsc 

The LCD screen, Joystick and capative sensor are connected with Qwiic cables, where the end are 4 pins connected 5V, GND, SCL and SDA. The clip for the capative sensor is clipped to entry 7 of the sensor, in which the other end is clipped onto the conductive tape on the bot head.

The LCD screen, Joystick and servo are attached to the LEGO base with adhesive tacky putty.

<p float="left">
<img src="https://github.com/iamyuchy/Interactive-Lab-Hub/blob/Spring2021/Final%20Project/4.png" height="350" />
<img src="https://github.com/iamyuchy/Interactive-Lab-Hub/blob/Spring2021/Final%20Project/5.png" height="350" />
<img src="https://github.com/iamyuchy/Interactive-Lab-Hub/blob/Spring2021/Final%20Project/6.png" height="350" />
</p>

#### Software
PiT Bot can be activated by running

```
python pitbot.py
```

pitbot.py will then call display.py for LCD emoticon display, servo.py for turning the head, and speak.py for audio output.

### 3. Video of someone using your project (or as safe a version of that as can be managed given social distancing)

The video link: https://drive.google.com/file/d/11IHh6lJ0fhtfrj9t7NQdD86RodjWKTtp/view?usp=sharing

### 4. Reflections on process (What have you learned or wish you knew at the start?)

Some reflections:

1. Servos, along with other motors and sensors, definitely have a steeper learning curve. It took time to learn how to connect GPIO to the breadboard, how to set the board mode with the scripts, and which pins are we using.

2. Sometimes we need to adjust the design and limit the functionality of a product. At the beginning I was thinking adding distance sensing, cameras with face recognition, and voice interaction. At the end, I found that simple interaction may also works, especially considering the time frame and the whole concept of being lightweight and cute.

## Teams
It's an individual project. Designed and implemented by myself (jl3935).

## Examples

[Here is a list of good final projects from previous classes.](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/wiki/Previous-Final-Projects)
This version of the class is very different, but it may be useful to see these.
