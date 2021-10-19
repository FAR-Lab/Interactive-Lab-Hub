# Ph-UI!!!
# Project Finite Gauntlet

**Team:**

**Xy Fang (xf48)**

**Casey Pan (yp432)**

**Anpu Li (al2487)**


For lab this week, we focus on both on sensing, to bring in new modes of input into your devices, as well as prototyping the physical look and feel of the device. You will think about the physical form the device needs to perform the sensing as well as present the display or feedback about what was sensed. 

## Part 1 Lab Preparation

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

C) [Paper Display](#part-c)

D) [Materiality](#part-d)

E) [Servo Control](#part-e)

F) [Record the interaction](#part-f)

## The Report (Part 1: A-D, Part 2: E-F)

### Part C
### Physical considerations for sensing

For this section, we focused on capacitive sensors as our main sensor. We think touch is an interaction form holding a wide range of potentials, and the 12 contacts on the sensor, when selected and combined in different ways, are capable of encoding a great number of different inputs.

To make the most out of our 3-member team work, we decided to each come up with different ideas that utilized capacitance sensors, and more. In each idea, sensors should grab information from the user in a meaningful way and further transmit that information. When necessary, we fit in multiple sensors where we see fit. We then bring all of our ideas together in a discussion. This way, we would each become a fresh set of eyes examining each other’s ideas. We will see what sparks this will trigger, and bring that into our brainstorming session.

**\*\*\*Draw 5 sketches of different ways you might use your sensor, and how the larger device needs to be shaped in order to make the sensor useful.\*\*\***

**Design 1**

![image](https://user-images.githubusercontent.com/42874337/137838941-c8b0a71c-e760-44b7-b1aa-9e7c0fbcb779.png)

**Design 2**

![image](https://user-images.githubusercontent.com/42874337/137838962-6ef27de4-a2b3-4681-b7c9-f5acdcece9ba.png)

**Design 3**

![image](https://user-images.githubusercontent.com/42874337/137839129-efeb0660-bb07-4a72-973c-f251f1f1ebc0.png)


**\*\*\*What are some things these sketches raise as questions? What do you need to physically prototype to understand how to anwer those questions?\*\*\***

1. For small, condensed devices like “The ‘’Bite Me’ Alarm”, where sensors are placed rather closely to each other on the surface, and delicate order-specific interactions are needed, will it be too much of a burden for the user to get it right?

2. For the Typing Glove (Finite Gauntlet) - How natural/well-functioning/effective will it be? We’re trying to invent a new way of typing input. Can this be learned and become an actual way of typing?

3. A common question that raises from these sketches is that

**\*\*\*Pick one of these designs to prototype.\*\*\***



![image](https://user-images.githubusercontent.com/42874337/137819115-a648012d-5683-45d1-ba05-a71ae8c9fd92.png)

![image](https://user-images.githubusercontent.com/42874337/137819138-cac0b262-49bc-4c0d-9712-9c06cc7f6c60.png)

### Part D
### Physical considerations for displaying information and housing parts
 
**\*\*\*Sketch 5 designs for how you would physically position your display and any buttons or knobs needed to interact with it.\*\*\***



**\*\*\*What are some things these sketches raise as questions? What do you need to physically prototype to understand how to anwer those questions?\*\*\***



**\*\*\*Pick one of these display designs to integrate into your prototype.\*\*\***



**\*\*\*Explain the rationale for the design.\*\*\*** (e.g. Does it need to be a certain size or form or need to be able to be seen from a certain distance?)



Build a cardbord prototype of your design.

**\*\*\*Document your rough prototype.\*\*\***


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

