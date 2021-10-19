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

![image](https://user-images.githubusercontent.com/42874337/137847010-4a04a417-266e-4c13-8b7a-5ae1a2f812a0.png)

**Design 3**

![image](https://user-images.githubusercontent.com/42874337/137847042-dd96c3b7-ce52-4fb4-9fe2-7d8efedaa925.png)

**Design 4**

![image](https://user-images.githubusercontent.com/42874337/137838962-6ef27de4-a2b3-4681-b7c9-f5acdcece9ba.png)

**Design 5**

![image](https://user-images.githubusercontent.com/42874337/137839129-efeb0660-bb07-4a72-973c-f251f1f1ebc0.png)


**\*\*\*What are some things these sketches raise as questions? What do you need to physically prototype to understand how to anwer those questions?\*\*\***

1. For small, condensed devices like “The ‘’Bite Me’ Alarm”, where sensors are placed rather closely to each other on the surface, and delicate order-specific interactions are needed, will it be too much of a burden for the user to get it right?

2. For the Typing Glove (Finite Gauntlet) - How natural/well-functioning/effective will it be? We’re trying to invent a new way of typing input. Can this be learned and become an actual way of typing?

3. A common question that raises from these sketches is that how to actually matches the size of our pi and sensors to the purpose that we are designing the device for. Sometimes the larger the devices gets means the longer the wires are and the more accurate the sensors are, it might not able to achieve through our current kit.


**\*\*\*Pick one of these designs to prototype.\*\*\***

The design we choose to proceed with is “the Finite Gauntlet”, that is, the typing glove, with a name inspired by the Infinity Gauntlet.

This glove embodied a new invention of how people can type, by bringing the classic 9-key English keyboard to one hand. The 9-key keyboard takes 9 binary inputs (and a 10th input as the space), which in a classic setting would be 9 buttons,  and is capable of outputting English words composed by any combination of the English 26 letters.

![image](https://user-images.githubusercontent.com/42874337/137842948-086207d7-5e6f-4038-97b2-ae3556f10faf.png)

We take the core idea in the classic 9-key keyboard system: 9 binary inputs mapped to any combination of 26 English letters, and migrate that to a hand-wearable device. 

The Finite Gauntlet has 4 capacitive sensors, one on each fingertip of every finger except the thumb. Each capacitive sensor provides a binary input, and 4 capacitive sensors provide 24 different combination possibilities. Out of the 24 combinations, we picked 9 combinations that’s easy to compose by hand. A gesture is made when the thumb touches one, two, or three of the other fingertips (capacitive sensors). The glove recognizes 9 different hand gestures, and runs a program that maps these 9 inputs to a 9-key keyboard output.

Gestures are shown below:

![image](https://user-images.githubusercontent.com/42874337/137819115-a648012d-5683-45d1-ba05-a71ae8c9fd92.png)

![image](https://user-images.githubusercontent.com/42874337/137819138-cac0b262-49bc-4c0d-9712-9c06cc7f6c60.png)

The Finite Gauntlet as a typing tool introduces a typing method that’s not only new and fun, but could also be helpful for people facing special conditions:

- For people in medical conditions where delicate gestures could help improve brain functions, using the Finite Gauntlet would be a way to conduct daily exercises;
- In emergency situations where phones aren’t a good idea, for example, when it’s too shaky, or when a person needs to remain unseen in the dark, the Finite Glove could be used to type & send emergency messages;



#### Prototype Process


**Cardboard Prototyping**

![image](https://user-images.githubusercontent.com/42874337/137840439-c492609e-6728-4fbb-843e-b3162efbc4e0.png)

![image](https://user-images.githubusercontent.com/42874337/137840447-39d17c90-ccf0-44f9-af8f-ec8acc631bfd.png)

![image](https://user-images.githubusercontent.com/42874337/137840462-ca956d76-ab56-4351-89a9-ee434db3b6ab.png)

![image](https://user-images.githubusercontent.com/42874337/137840473-39e89e38-288e-4259-9280-3162d2ae98b1.png)

![image](https://user-images.githubusercontent.com/42874337/137840500-3d4b3969-9de9-451a-b70d-f29dce17fd7a.png)

![image](https://user-images.githubusercontent.com/42874337/137840545-1ff46f57-1bfd-4af4-bddf-d848b1d49599.png)

![image](https://user-images.githubusercontent.com/42874337/137840580-3b925c33-a1da-48f4-96e1-2cd15eaaa7b5.png)

![image](https://user-images.githubusercontent.com/42874337/137840613-a600bf72-25f1-4359-9317-41da4ef594bf.png)


### Part D
### Physical considerations for displaying information and housing parts
 
**\*\*\*Sketch 5 designs for how you would physically position your display and any buttons or knobs needed to interact with it.\*\*\***


As shown in the sketch notes above, there were three main decisions we needed to make while considering the physical layout of our design:

1. Positioning of capacitance sensors
2. Positioning of gesture sensors
3. Positioning of display

We discussed the pros and cons of different positioning choices, and came up with the 5 different designs, embodying different combinations of choices we saw as reasonable.

**NOTE:** “Knuckles” in this context refers to the space between two fingle knuckles on the palm-side of fingers.

1.

![image](https://user-images.githubusercontent.com/42874337/137841612-b7a83af6-5dc3-4598-af9e-f4f5ddb4571b.png)

2.

![image](https://user-images.githubusercontent.com/42874337/137841623-ff21e7aa-e8a5-4d1d-a497-57f51fee53a5.png)

3.

![image](https://user-images.githubusercontent.com/42874337/137841635-e7f5a8c1-4b99-41f3-b420-0936d13e6f3a.png)

4.

![image](https://user-images.githubusercontent.com/42874337/137841647-9e42ccb9-5bd4-466f-8c91-d453a3e674fa.png)

5.

![image](https://user-images.githubusercontent.com/42874337/137841656-86b4bf90-c290-4d65-9bf1-48681465bd65.png)

**Pros & Cons of the original 9-knuckles design**

**PROS:** keys can be quite graphically and straight-forwardly placed the same as how a standard 9-key keyboard would appear on screen. Keys can be printed on the glove in their respective positions, and users do not need to memorize touch-combinations for keys.

**CONS:** 9 capacitance sensors needed instead of 4, higher cost and more risk of technical glitches, reduces robustness of the product. Glove with sensors placed on knuckles won’t be as comfortable as one with sensors only on fingertips.

**\*\*\*What are some things these sketches raise as questions? What do you need to physically prototype to understand how to anwer those questions?\*\*\***

1. Do we need to consider output selection for our glove？What kind of interaction would function the best as a output selection? 

- After sketching out our designs, we re-examined them as typing tools, and realized that in order for this product to be a well-functioning 9-key typing tool, it needs to have a output selection function, just as a standard 9-key keyboard would have.

- In our original design, we wanted to use the UP and DOWN direction to switch between letter and number keyboards. When this question came up, we needed to re-think the encoding, with experience and insights from the prototype.

| UP                                         | DOWN                                               | LEFT      | RIGHT          |
|--------------------------------------------|----------------------------------------------------|-----------|----------------|
| Switch between letter and number keyboards | Select the next word in the possible outputs' list | Backspace | Confirm output |


2. When actually typing with the thumb touching 2 or 3 fingers at once, it’s highly possible that one finger (capacitance sensor) will be detected first and the other second, despite the very subtle difference. In this case, how does the system tell the difference between a “finger A + finger B” and a “finger A then finger B” ?

- We need a threshold of Xms in the program to counter the subtle detection time difference between different capacitance sensors in a multi-finger input.

- This will need to be tested and refined later in the software prototyping stage.

**\*\*\*Pick one of these display designs to integrate into your prototype.\*\*\***

Our final choice of design is sketch **#5(/1)**.

**\*\*\*Explain the rationale for the design.\*\*\*** (e.g. Does it need to be a certain size or form or need to be able to be seen from a certain distance?)

The design is a glove, in terms of the 3 previously staged design choices, it has 4 capacitance sensors on four of its fingertips (all fingers except the thumb), a gesture sensor (APDS-9960) placed on the outer-side of the index finger, and a display showing typing results as a detachable module.

There is ambiguity between design #1 and design #5, because while we think it makes sense to have the display as a detachable module, the best physical placement choice for it is still on the inner wrist, for the following reasons:

- It is a natural place for one’s eyesight to be landing on while finger-typing;
- It does not take up the usual space of a watch

And the fact that it’s detachable gives great flexibility to the user on where to actually place it.


**\*\*\*Document your rough prototype.\*\*\***

**Cardboard Prototyping**

![image](https://user-images.githubusercontent.com/42874337/137840654-7c2ecb54-3653-42b4-bbe8-3c1690898123.png)

![image](https://user-images.githubusercontent.com/42874337/137840663-4d54a117-0c64-40fe-aff3-b89c4f14e71e.png)

**Hands On Video**

[![image](https://user-images.githubusercontent.com/42874337/137840739-74681d46-8337-4f07-ac0a-729264e0d2cf.png)](https://drive.google.com/file/d/1_8C4dAzmo2JtW54vDXacyz8srLmTZD2P/view?usp=sharing)



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

