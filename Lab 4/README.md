# Ph-UI!!!

For lab this week, we focus on both on sensing, to bring in new modes of input into your devices, as well as prototyping the physical look and feel of the device. You will think about the physical form the device needs to perform the sensing as well as present the display or feedback about what was sensed. 

## Part 1 Lab Preparation

### Get the latest content:
As always, pull updates from the class Interactive-Lab-Hub to both your Pi and your own GitHub repo. As we discussed in the class, there are 2 ways you can do so:

**\[recommended\]**Option 1: On the Pi, `cd` to your `Interactive-Lab-Hub`, pull the updates from upstream (class lab-hub) and push the updates back to your own GitHub repo. You will need the personal access token for this.

```
pi@ixe00:~$ cd Interactive-Lab-Hub
pi@ixe00:~/Interactive-Lab-Hub $ git pull upstream Fall2021
pi@ixe00:~/Interactive-Lab-Hub $ git add .
pi@ixe00:~/Interactive-Lab-Hub $ git commit -m "get lab4 content"
pi@ixe00:~/Interactive-Lab-Hub $ git push
```

Option 2: On your your own GitHub repo, [create pull request](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2021Fall/readings/Submitting%20Labs.md) to get updates from the class Interactive-Lab-Hub. After you have latest updates online, go on your Pi, `cd` to your `Interactive-Lab-Hub` and use `git pull` to get updates from your own GitHub repo.

### Start brasinstorming ideas by reading: 
* [What do prototypes prototype?](https://www.semanticscholar.org/paper/What-do-Prototypes-Prototype-Houde-Hill/30bc6125fab9d9b2d5854223aeea7900a218f149)
* [Paper prototyping](https://www.uxpin.com/studio/blog/paper-prototyping-the-practical-beginners-guide/) is used by UX designers to quickly develop interface ideas and run them by people before any programming occurs. 
* [Cardboard prototypes](https://www.youtube.com/watch?v=k_9Q-KDSb9o) help interactive product designers to work through additional issues, like how big something should be, how it could be carried, where it would sit. 
* [Tips to Cut, Fold, Mold and Papier-Mache Cardboard](https://makezine.com/2016/04/21/working-with-cardboard-tips-cut-fold-mold-papier-mache/) from Make Magazine.
* [Surprisingly complicated forms](https://www.pinterest.com/pin/50032245843343100/) can be built with paper, cardstock or cardboard.  The most advanced and challenging prototypes to prototype with paper are [cardboard mechanisms](https://www.pinterest.com/helgangchin/paper-mechanisms/) which move and change. 
* [Dyson Vacuum Cardboard Prototypes](http://media.dyson.com/downloads/JDF/JDF_Prim_poster05.pdf)
<p align="center"><img src="https://dysonthedesigner.weebly.com/uploads/2/6/3/9/26392736/427342_orig.jpg"  width="200" > </p>

### Gathering materials for this lab:

* Cardboard (start collecting those shipping boxes!)
* Found objects and materials--like bananas and twigs.
* Cutting board
* Cutting tools
* Markers

(We do offer shared cutting board, cutting tools, and markers on the class cart during the lab, so do not worry if you don't have them!)

## Deliverables \& Submission for Lab 4

The deliverables for this lab are, writings, sketches, photos, and videos that show what your prototype:
* "Looks like": shows how the device should look, feel, sit, weigh, etc.
* "Works like": shows what the device can do.
* "Acts like": shows how a person would interact with the device.

For submission, the readme.md page for this lab should be edited to include the work you have done:
* Upload any materials that explain what you did, into your lab 4 repository, and link them in your lab 4 readme.md.
* Link your Lab 4 readme.md in your main Interactive-Lab-Hub readme.md. 
* Group members can turn in one repository, but make sure your Hub readme.md links to the shared repository.
* Labs are due on Mondays, make sure to submit your Lab 4 readme.md to Canvas.


## Lab Overview

A) [Capacitive Sensing](#part-a)

B) [OLED screen](#part-b) 

C) [Paper Display](#part-c)

D) [Materiality](#part-d)

E) [Servo Control](#part-e)

F) [Record the interaction](#part-f)

## The Report (Part 1: A-D, Part 2: E-F)

### Part A
### Capacitive Sensing, a.k.a. Human-Twizzler Interaction 

We want to introduce you to the [capacitive sensor](https://learn.adafruit.com/adafruit-mpr121-gator) in your kit. It's one of the most flexible input devices we are able to provide. At boot, it measures the capacitance on each of the 12 contacts. Whenever that capacitance changes, it considers it a user touch. You can attach any conductive material. In your kit, you have copper tape that will work well, but don't limit yourself! In the example below, we use Twizzlers--you should pick your own objects.


<p float="left">
<img src="https://cdn-learn.adafruit.com/guides/cropped_images/000/003/226/medium640/MPR121_top_angle.jpg?1609282424" height="150" />
<img src="https://cdn-shop.adafruit.com/1200x900/4401-01.jpg" height="150">
</p>

Plug in the capacitive sensor board with the QWIIC connector. Connect your Twizzlers with either the copper tape or the alligator clips (the clips work better). In this lab, we will continue to use the `circuitpython` virtual environment we created before. Activate `circuitpython` and `cd` to your Lab 4 folder to install the requirements by:

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ pip3 install -r requirements.txt
```

<img src="https://media.discordapp.net/attachments/679721816318803975/823299613812719666/PXL_20210321_205742253.jpg" width=400>
These Twizzlers are connected to pads 6 and 10. When you run the code and touch a Twizzler, the terminal will print out the following

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python cap_test.py 
Twizzler 10 touched!
Twizzler 6 touched!
```

### Part B
### More sensors

#### Light/Proximity/Gesture sensor (APDS-9960)

We here want you to get to know this awesome sensor [Adafruit APDS-9960](https://www.adafruit.com/product/3595). It is capable of sensing proximity, light (also RGB), and gesture! 

<img src="https://cdn-shop.adafruit.com/970x728/3595-03.jpg" width=200>

Connect it to your pi with Qwiic connector and try running the 3 example scripts individually to see what the sensor is capable of doing!

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python light_test.py
...
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python proximity_test.py
...
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python gesture_test.py
...
```

You can go the the [Adafruit GitHub Page](https://github.com/adafruit/Adafruit_CircuitPython_APDS9960) to see more examples for this sensor!

#### Rotary Encoder

A rotary encoder is an electro-mechanical device that converts the angular position to analog or digital output signals. The [Adafruit rotary encoder](https://www.adafruit.com/product/4991#technical-details) we ordered for you came with separated breakout board and encoder itself, that is, they will need to be soldered if you have not yet done so! We will be bringing the soldering station to the lab class for you to use, also, you can go to the MakerLAB to do the soldering off-class. Here is some [guidance on soldering](https://learn.adafruit.com/adafruit-guide-excellent-soldering/preparation) from Adafruit. When you first solder, get someone who has done it before (ideally in the MakerLAB environment). It is a good idea to review this material beforehand so you know what to look at.

<p float="left">
<img src="https://cdn-shop.adafruit.com/970x728/4991-01.jpg" height="200" />
<img src="https://cdn-shop.adafruit.com/970x728/377-02.jpg" height="200" />
<img src="https://cdn-shop.adafruit.com/970x728/4991-09.jpg" height="200">
</p>

Connect it to your pi with Qwiic connector and try running the example script, it comes with an additional button which might be useful for your design!

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python encoder_test.py
```

You can go to the [Adafruit Learn Page](https://learn.adafruit.com/adafruit-i2c-qt-rotary-encoder/python-circuitpython) to learn more about the sensor! The sensor actually comes with an LED (neo pixel): Can you try lighting it up? 

#### Joystick

A [joystick](https://www.sparkfun.com/products/15168) can be used to sense and report the input of the stick for it pivoting angle or direction. It also comes with a button input!

<p float="left">
<img src="https://cdn.sparkfun.com//assets/parts/1/3/5/5/8/15168-SparkFun_Qwiic_Joystick-01.jpg" height="200" />
</p>

Connect it to your pi with Qwiic connector and try running the example script to see what it can do!

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python joystick_test.py
```

You can go to the [SparkFun GitHub Page](https://github.com/sparkfun/Qwiic_Joystick_Py) to learn more about the sensor!

#### (Optional) Distance Sensor

Note: We did not distribute this sensor to you, so if you are interested in playing with it, please come pick it up from the TA!

Earlier we have asked you to play with the proximity sensor, which is able to sense object within a short distance. Here, we offer [Qwiic Multi Distance Sensor](https://www.sparkfun.com/products/17072), which has a field of view of about 25° and is able to detect objects up to 3 meters away! 

<p float="left">
<img src="https://cdn.sparkfun.com//assets/parts/1/6/0/3/4/17072-Qwiic_Multi_Distance_Sensor_-_VL53L3CX-01.jpg" height="200" />
</p>

Connect it to your pi with Qwiic connector and try running the example script to see how it works!

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python distance_test.py
```

You can go to the [SparkFun GitHub Page](https://github.com/sparkfun/Qwiic_VL53L1X_Py) to learn more about the sensor and see other examples!

### Part C
### Physical considerations for sensing

Usually, sensors need to positioned in specific locations or orientations to make them useful for their application. Now that you've tried a bunch of the sensors, pick one that you would like to use, and an application where you use the output of that sensor for an interaction. For example, you can use a distance sensor to measure someone's height if you position it overhead and get them to stand under it.

For the purposes of this lab, I will be using the proximity sensor in a prototype "Interactive Maze Game", where the objective is to hold and turn the maze in such a way as to move a ball from the start position to the end position while avoiding obstacles. 

**\*\*\*Draw 5 sketches of different ways you might use your sensor, and how the larger device needs to be shaped in order to make the sensor useful.\*\*\***

![alt text](https://github.com/rohangreddy/Interactive-Lab-Hub/blob/Fall2021/Lab%204/1A.JPG)

The idea behind Figure 1A is to put the proximity sensor on the bottom floor inside of the prototype. Then, when the ball falls through the hole in the endzone, it will land on the proximity sensor which can increment a score or stop a timer indicating to the player that they have won. 

![alt text](https://github.com/rohangreddy/Interactive-Lab-Hub/blob/Fall2021/Lab%204/1B.JPG)

The idea behind Figure 1B is to put the proximity sensor on a panel of a ledge that catches the ball when it falls through the endzone.

![alt text](https://github.com/rohangreddy/Interactive-Lab-Hub/blob/Fall2021/Lab%204/1C.JPG)

Figure 1C involves placing the proximity sensor along the inner boundary (wall) of the endzone. When the ball rolls into the endzone, it will hit the proximity sensor based on momentum and prompt an action.

![alt text](https://github.com/rohangreddy/Interactive-Lab-Hub/blob/Fall2021/Lab%204/1D.JPG)

Figure 1D involves placing the proximity sensor on the floor of the panel. When the ball rolls into the endzone, it will roll over the proximity sensor, prompting an action.

![alt text](https://github.com/rohangreddy/Interactive-Lab-Hub/blob/Fall2021/Lab%204/1E.JPG)

Figure 1E involves placing the proximity sensor on a flap that covers the endzone. When the ball rolls under the proximity sensor, an action will be prompted

**\*\*\*What are some things these sketches raise as questions? What do you need to physically prototype to understand how to anwer those questions?\*\*\***

These sketches raise several important questions regarding the ideal placement of the proximity sensor. This placement depends on the proximity sensor's sensitivity (how close or far and object needs to be for it to register). For example, in Figure 1C where the proximity sensor is placed along the inner wall of the endzone, the proximity sensor may register the opposing wall as within its proximity range. Other questions raised involve the functionality and design of the game. One possible consideration is to have holes in the endzone and the deadzones (marked as X in the sketches above) so that the ball falls through when it reaches these spots. Figure 1A involves placing the proximity sensor inside of the prototype under the endzone on the floor. However, the ball may not fall exactly on the proximity sensor since the distance between the top of the maze and the floor may be quite far. Additionally, if the ball falls through any of the deadzone holes and lands on the proximity sensor by chance, it would register as a win. 

I need to physically prototype a three dimensional hollow box to experiment with the various proximity sensor locations to determine which is the most ideal based on sensing capability and least amount of interference with gameplay.

**\*\*\*Pick one of these designs to prototype.\*\*\***

Of all of the designs, Figure 1D or 1E seemed the most feasible. Placing the proximity sensor on the inner wall or floor of the endzone seems the most feasible. Placement will ideally depend on the range of the proximity sensor; if the proximity sensor can safely be placed on the inner wall without picking up the opposing wall, this would be the ideal design to go with. 

### Part D
### Physical considerations for displaying information and housing parts


Here is an Pi with a paper faceplate on it to turn it into a display interface:

<img src="https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/images/paper_if.png?raw=true"  width="250"/>


This is fine, but the mounting of the display constrains the display location and orientation a lot. Also, it really only works for applications where people can come and stand over the Pi, or where you can mount the Pi to the wall.

Here is another prototype for a paper display:

<img src="https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/images/b_box.png?raw=true"  width="250"/>

Your kit includes these [SparkFun Qwiic OLED screens](https://www.sparkfun.com/products/17153). These use less power than the MiniTFTs you have mounted on the GPIO pins of the Pi, but, more importantly, they can be more flexibily be mounted elsewhere on your physical interface. The way you program this display is almost identical to the way you program a  Pi display. Take a look at `oled_test.py` and some more of the [Adafruit examples](https://github.com/adafruit/Adafruit_CircuitPython_SSD1306/tree/master/examples).

<p float="left">
<img src="https://cdn.sparkfun.com//assets/parts/1/6/1/3/5/17153-SparkFun_Qwiic_OLED_Display__0.91_in__128x32_-01.jpg" height="200" />
<img src="https://cdn.discordapp.com/attachments/679466987314741338/823354087105101854/PXL_20210322_003033073.jpg" height="200">
</p>


It holds a Pi and usb power supply, and provides a front stage on which to put writing, graphics, LEDs, buttons or displays.

This design can be made by scoring a long strip of corrugated cardboard of width X, with the following measurements:

| Y height of box <br> <sub><sup>- thickness of cardboard</sup></sub> | Z  depth of box <br><sub><sup>- thickness of cardboard</sup></sub> | Y height of box  | Z  depth of box | H height of faceplate <br><sub><sup>* * * * * (don't make this too short) * * * * *</sup></sub>|
| --- | --- | --- | --- | --- | 

Fold the first flap of the strip so that it sits flush against the back of the face plate, and tape, velcro or hot glue it in place. This will make a H x X interface, with a box of Z x X footprint (which you can adapt to the things you want to put in the box) and a height Y in the back. 

Here is an example:

<img src="https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/images/horoscope.png?raw=true"  width="250"/>

Think about how you want to present the information about what your sensor is sensing! Design a paper display for your project that communicates the state of the Pi and a sensor. Ideally you should design it so that you can slide the Pi out to work on the circuit or programming, and then slide it back in and reattach a few wires to be back in operation.
 
**\*\*\*Sketch 5 designs for how you would physically position your display and any buttons or knobs needed to interact with it.\*\*\***

![alt text](https://github.com/rohangreddy/Interactive-Lab-Hub/blob/Fall2021/Lab%204/2A.JPG)

Figure 2A involves placing the OLED screen on the lower panel of the prototype right in front of the user.

![alt text](https://github.com/rohangreddy/Interactive-Lab-Hub/blob/Fall2021/Lab%204/2B.JPG)

Figure 2B involves placing both the OLED screen and an LED start button on the lower panel of the prototype, which is right in front of the user.

![alt text](https://github.com/rohangreddy/Interactive-Lab-Hub/blob/Fall2021/Lab%204/2C.JPG)

Figure 2C involves keeping the LED start button on the lower panel in front of the user, but placing the OLED screen on a back panel flap that rises up vertically.

![alt text](https://github.com/rohangreddy/Interactive-Lab-Hub/blob/Fall2021/Lab%204/2D.JPG)

Figure 2D involves placing both the LED start button and the OLED screen on a back panel flap that rises up vertically.

![alt text](https://github.com/rohangreddy/Interactive-Lab-Hub/blob/Fall2021/Lab%204/2E.JPG)

Figure 2E involves placing the OLED screen on the back panel vertical flap, but places the LED button on the side of the prototype where the user holds the prototype while playing the game. 

**\*\*\*What are some things these sketches raise as questions? What do you need to physically prototype to understand how to anwer those questions?\*\*\***

I never realized the effect placement of the screen and LED button could have on players playing the game. In figures 2A and 2B, the screen and LED button are placed on the lower panel closest to the user. I initally thought this would be a good place to put these, but realized that based on the way the game is played with the user holding the prototype, the screen had minimal visibility. Additionally, since the game is meant to be played with the user holding the prototype by the two sides of the box, having a button on the lower panel in front of the user would require the user to put down the box in order to press the start button, which interrupts game flow. 

In order to determine ideal placement of the screen and the LED button to maximize user engagement, I will need to physically prototype a three dimensional box and experiment with the various positinos for the screen and the button while simulating gameplay. 

**\*\*\*Pick one of these display designs to integrate into your prototype.\*\*\***

Of all of the designs, Figure 2E is the most promising. The OLED screen on the back panel is perfect for visibility for the user to keep track of their score or time as they are playing the game. Additionally, the side panel is perfect for the LED button because it is right where the user holds the prototype while playing. Therefore they would be able to press the start button without actually putting the prototype down.

**\*\*\*Explain the rationale for the design.\*\*\*** (e.g. Does it need to be a certain size or form or need to be able to be seen from a certain distance?)

The idea for this application is an "Interactive Maze Game", where the objective is to hold and rotate the prototype in such a way as to move a ball from the start position to the end position while avoiding obstacles. The prototype design involves a three dimensional box, where the maze sits on a panel towards the top of the box. Keeping the maze on a panel in this way allows for the borders of the box to act as outer walls of the maze. Additionally, obstacles include holes in the floor of the maze that the ball can fall through. Keeping the maze panel towards the top of the box allows for the ball to fall through the holes and allows for the user to easily retrieve the ball when this happens. 

As the game is designed to be played with the user holding the box and rotating it to direct the ball through the maze, the prototype needs to be light enough to comfortably hold and rotate. The OLED screen would be on a vertical back flap of the prototype such that the user can easily visualize their progress (in the form of score or time taken to navigate through the maze) and the LED start button would be on the side of the prototype where the user holds the box. 

A hollow three dimensional cardboard box has the perfect form factor and will be useful to prototype with.  

Build a cardbord prototype of your design.

**\*\*\*Document your rough prototype.\*\*\***

![alt text](https://github.com/rohangreddy/Interactive-Lab-Hub/blob/Fall2021/Lab%204/IMG-0302.jpg)

![alt text](https://github.com/rohangreddy/Interactive-Lab-Hub/blob/Fall2021/Lab%204/IMG-0303.jpg)


LAB PART 2

### Part 2

Following exploration and reflection from Part 1, complete the "looks like," "works like" and "acts like" prototypes for your design, reiterated below.

### Part E (Optional)
### Servo Control with Joystick

In the class kit, you should be able to find the [Qwiic Servo Controller](https://www.sparkfun.com/products/16773) and [Micro Servo Motor SG51](https://www.adafruit.com/product/2201). The Qwiic Servo Controller will need external power supply to drive, which we will be distributing the battery packs in the class. Connect the servo controller to the miniPiTFT through qwiic connector and connect the external battery to the 2-Pin JST port (ower port) on the servo controller. Connect your servo to channel 2 on the controller, make sure the brown is connected to GND and orange is connected to PWM.

<img src="https://scontent-lga3-1.xx.fbcdn.net/v/t1.15752-9/245605956_303690921194525_3309212261588023460_n.jpg?_nc_cat=110&ccb=1-5&_nc_sid=ae9488&_nc_ohc=FvFLlClTKuUAX9nJ3LR&_nc_ht=scontent-lga3-1.xx&oh=b7ec1abc8d458b6c1b7a00a6f11398ac&oe=618D7D96" width="400"/>

In this exercise, we will be using the nice [ServoKit library](https://learn.adafruit.com/16-channel-pwm-servo-driver/python-circuitpython) developed by Adafruit! We will continue to use the `circuitpython` virtual environment we created. Activate the virtual environment and make sure to install the latest required libraries by running:

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ pip3 install -r requirements.txt
```

A servo motor is a rotary actuator or linear actuator that allows for precise control of angular or linear position. The position of a servo motor is set by the width of an electrical pulse, that is, we can use PWM (pulse-width modulation) to set and control the servo motor position. You can read [this](https://learn.adafruit.com/adafruit-arduino-lesson-14-servo-motors/servo-motors) to learn a bit more about how exactly a servo motor works.

Now that you have a basic idea of what a servo motor is, look into the script `qwiic_servo_example.py` we provide. In line 14, you should see that we have set up the min_pulse and max_pulse corresponding to the servo turning 0 - 180 degree. Try running the servo example code now and see what happens:

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python servo_test.py
```

It is also possible to control the servo using the sensors mentioned in as in part A and part B, and/or from some of the buttons or parts included in your kit, the simplest way might be to chain Qwiic buttons to the other end of the Qwiic OLED. Like this:

<p align="center"> <img src="chaining.png"  width="200" ></p>

You can then call whichever control you like rather than setting a fixed value for the servo. For more information on controlling Qwiic devices, Sparkfun has several python examples, such as [this](https://learn.sparkfun.com/tutorials/qwiic-joystick-hookup-guide/all#python-examples).

We encourage you to try using these controls, **while** paying particular attention to how the interaction changes depending on the position of the controls. For example, if you have your servo rotating a screen (or a piece of cardboard) from one position to another, what changes about the interaction if the control is on the same side of the screen, or the opposite side of the screen? Trying and retrying different configurations generally helps reveal what a design choice changes about the interaction -- _make sure to document what you tried_!

### Part F
### Record

Document all the prototypes and iterations you have designed and worked on! Again, deliverables for this lab are writings, sketches, photos, and videos that show what your prototype:
* "Looks like": shows how the device should look, feel, sit, weigh, etc.
* "Works like": shows what the device can do
* "Acts like": shows how a person would interact with the device

Maze Runner is intended to be an interactive version of the traditional maze game. The game is designed to be held by the user, who has an objective to turn/rotate the prototype in such a way as to move the ball through the maze to the endpoint in the center all while navigating obstacles and avoiding pitfalls.

Pictures of the finalized prototype are included below. Changes from the previous iteration include the addition of holes through which the ball can fall through, and cutouts for the OLED screen as well as the LED button. 

![alt text](https://github.com/rohangreddy/Interactive-Lab-Hub/blob/Fall2021/Lab%204/IMG-0255.jpg)

The 3-D nature of the box allows for the raspberry pi to be discreetly housed within the unit. An important piece of feedback that I received was that I would have to be conscious of where the computing components are located within the unit. Since the game involves a ball falling through some of the holes, computing components and wires would have to be placed in such a way as to allow the ball to freely fall through without interference, as well as to allow the user to safely retrieve the ball with minimal hassle. In order for to achieve this design goal, I decided to open up the bottom of the prototype and place the raspberry pi on the inner back panel of the box. This allows for the ball to safely fall through the open bottom and for the user to be able to easily retrieve it. Additionally, placing the Pi on the center of the inner back panel was the optimal position that resulted in a relatively even weight distribution. This was an important design consideration, since the game is meant to be held by users - placement of the pi on the other inner panels of the prototype did not have the right feel.

![alt text](https://github.com/rohangreddy/Interactive-Lab-Hub/blob/Fall2021/Lab%204/IMG-0256.jpg)

Another change that I incorporated based on user feedback was to actually put the LED button on the front lower panel of the prototype in order to increase its visibility. A tendency for users during user testing was to immediately pick up the game and start playing without pressing the start button. Therefore, I also decided to add a pre-initialization state to the game where the game awaits user input. Please see the short video below.

https://youtu.be/2uPztmmkKnI

In the pre-initialization state, the OLED screen clearly shows a "Press Start!" prompt that indicates to the user that they should press the start button. Additionally, I added blinking green light functionality to the button so as to catch the user's attention and make them aware of the location of the start button.

When the button is pressed, the LED light on the button turns on and stays green (ie it stops blinking), giving users visual feedback that the game has started. Additionally, a stopwatch is displayed on the OLED screen that counts upwards in seconds, giving users an indication of the time it is taking for them to navigate through the maze. As users navigate obstacles and avoid the holes in the maze that the ball can fall through, they can easily gauge their time on the OLED screen that is placed on an adjustable flap which can be repositioned for optimal visibility. 

When the user finally navigates the maze and reaches the endpoint, the ball will roll over a proximity sensor. When the sensor senses the presence of the ball, the timer stops and the user can check to see how their time was. Afterwards, the prototype once again enters the pre-initialization state, and the user can press start in order to try again and beat their previous time. Please also see the video explanation below of how the prototype is designed to be used. 

https://youtu.be/HHl5aDZcoD4

Lastly, please see the video below on how a person would interact with the device. Note that the perspective is flipped (the box is held backwards in the video) for better visibility of how the game works live. This perspective has the added advantage of allowing viewers of the video to feel as if they are holding the game and playing themselves. The video quality is a little blurry due to limitations with the webcam, but please note the the change in the OLED screen to the display of the stopwatch when the start button is pressed, as well as the pausing of the time when the ball reaches the proximity sensor. 

https://youtu.be/2INAGaeZQfo

As the user navigates the maze, they successfully take the first turn and traverse the obstacle "walls". However, they overshoot the next turn after passing the final obstacle wall and the ball ends up falling through the hole. The user was easily able to retrieve the ball and place it back on the starting position with minimal hassle. When the user is finally able to reach the endpoint in the middle of the maze, the ball triggers the proximity sensor to stop the time and the user is able to see the time that it took for them to navigate the maze on this attempt. The game then enters the pre-initialization state, indicating to the user that they can press start in order to try to navigate the maze again. 

Code for this lab can be found in the 'maze.py' file. Special thanks to the creators of the sparkfun-qwiic button for making an easy-to-use software package as well as for including examples of how to use the buttons on their Github repository: https://github.com/sparkfun/Qwiic_Button_Py
