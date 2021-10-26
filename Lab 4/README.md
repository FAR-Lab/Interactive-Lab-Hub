# Ph-UI!!!
# Project Finite Gauntlet

**Team:**

**Xy Fang (xf48)**

**Casey Pan (yp432)**


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

To make the most out of our two member team work, we decided to each come up with different ideas that utilized capacitance sensors, and more. All ideas we presented below invloves in potentials and designs with multiple sensors, and requires at least three times of single person workload to completing prototype. In each idea, sensors should grab information from the user in a meaningful way and further transmit that information. When necessary, we fit in multiple sensors where we see fit. We then bring all of our ideas together in a discussion. This way, we would each become a fresh set of eyes examining each other’s ideas. We will see what sparks this will trigger, and bring that into our brainstorming session.

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

We have realized the need to physically prototype the devices to know how the actual display of wires and sensors might be able to fit in ergonomic designs that best suits users, also how the idea is applicable or not through real interactions. The physical prototyping can also show the sensitivity of the sensors, and the precision of its data. All of which cannot be acquired by just sketching the designs. Also, some of our device designs like the finite gauntlet requires a certain learning curve or behaviral training. We would not be able to know how this device works when human interacting with them unless a real physical prototype could be wear and tested by a human user.


**\*\*\*Pick one of these designs to prototype.\*\*\***

The design we choose to proceed with is “the Finite Gauntlet”, that is, the typing glove.

This glove embodied a new invention of how people can type, by bringing the classic 9-key (T9) English keyboard to one hand. The 9-key keyboard takes 9 binary inputs (and a 10th input as the space), which in a classic setting would be 9 buttons,  and is capable of outputting English words composed by any combination of the English 26 letters.

The Finite Gauntlet allows users to use touching fingertips using thumbs to fastly input words and sentences like keyboard utilizing a capacitive sensor, a gesture sensor to recognize input commands like backspaces and flush to speech, a OLED screen that shows the inputed words, and a output speaker that would be able to do the text to speech based on what's inputed to the device. A total of 4 sensors/units have been implemented in this device. 

![image](https://user-images.githubusercontent.com/42874337/137842948-086207d7-5e6f-4038-97b2-ae3556f10faf.png)

We take the core idea in the classic 9-key keyboard system: 9 binary inputs mapped to any combination of 26 English letters, and migrate that to a hand-wearable device. 

The Finite Gauntlet has 4 capacitive sensors, one on each fingertip of every finger except the thumb. Each capacitive sensor provides a binary input, and 4 capacitive sensors provide 24 different combination possibilities. Out of the 24 combinations, we picked 9 combinations that’s easy to compose by hand. A gesture is made when the thumb touches one, two, or three of the other fingertips (capacitive sensors). The glove recognizes 9 different hand gestures, and runs a program that maps these 9 inputs to a 9-key keyboard output.

Gestures are shown below:

![image](https://user-images.githubusercontent.com/42874337/137819115-a648012d-5683-45d1-ba05-a71ae8c9fd92.png)

![image](https://user-images.githubusercontent.com/42874337/137819138-cac0b262-49bc-4c0d-9712-9c06cc7f6c60.png)

The Finite Gauntlet we designed have multiple use in modern context:

- First of all, it can be a modern one handed input device paired with modern technologies, for example: AR googles (apple glasses).
- Another widely used scenario that we can think of is a easier way to type in for smart watches, respond to text messages and searching things, which complement the shortage of small screens of smart watches.
- We also planned to include a text-to-speech unit to our device which allows users to directly output what they type in as voices in this lab, this has some common implications to the healthcare and accessibility world:
-- Portable and accessible single hand device for speech replacement for people who lost voices
-- minimal movement required t2s device for patients of diseases like Parkinson's

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

1. Positioning of capacitive sensors
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

- In our original design, we wanted to use the UP and DOWN direction to switch between letter and number keyboards. When this question came up, we needed to re-think the encoding. We later realized that the previous UP/DOWN encoding was redundant and unnecessary, since this task could be done with one single gesture. The spared gesture can be used for output selection. 

| UP                                         | DOWN                                               | LEFT      | RIGHT          |
|--------------------------------------------|----------------------------------------------------|-----------|----------------|
| Switch between letter and number keyboards | Select the next word in the possible outputs' list | Backspace | Confirm output |


2. When actually typing with the thumb touching 2 or 3 fingers at once, it’s highly possible that one finger (capacitance sensor) will be detected first and the other second, despite the very subtle difference. In this case, how does the system tell the difference between a “finger A + finger B” and a “finger A then finger B” ?

- We need a threshold of Xms in the program to counter the subtle detection time difference between different capacitance sensors in a multi-finger input.

- This will need to be tested and refined later in the software prototyping stage.

**\*\*\*Pick one of these display designs to integrate into your prototype.\*\*\***

Our final choice of design is sketch **#5(/1)**.

**\*\*\*Explain the rationale for the design.\*\*\*** (e.g. Does it need to be a certain size or form or need to be able to be seen from a certain distance?)

The design is a glove, in terms of the 3 previously staged design choices, it has 4 capacitance sensors on four of its fingertips (all fingers except the thumb), a gesture sensor (APDS-9960) placed on the outer-side of the index finger, and a display showing typing results as a detachable module. The speaker designed previously will be placed on the waist as either a part of the whole device or an extra unit, after the input device has been tested to be reliable.

There is ambiguity between design #1 and design #5, because while we think it makes sense to have the display as a detachable module, the best physical placement choice for it is still on the inner wrist, for the following reasons:

- It is a natural place for one’s eyesight to be landing on while finger-typing;
- It does not take up the usual space of a watch

And the fact that it’s detachable gives great flexibility to the user on where to actually place it.

As we focused on designing this new way of inputing text to be as accessible and as portable as possible, we are aiming at a thin glove that attached to smart watches as the final product. The current design of the thickness and the size of our glove is aligned with our purpose. The small OLED screen to display text is at a fair distance just like smart watches that when people type, they would be able to see what they are tying in.  The form of the glove as an input device also align with ergonomic idea that hand muscles are the most delicate and sensible ones on human body.


**\*\*\*Document your rough prototype.\*\*\***

**Cardboard Prototyping**

![image](https://user-images.githubusercontent.com/42874337/137840654-7c2ecb54-3653-42b4-bbe8-3c1690898123.png)

![image](https://user-images.githubusercontent.com/42874337/137840663-4d54a117-0c64-40fe-aff3-b89c4f14e71e.png)

**Hands On Video**

[![image](https://user-images.githubusercontent.com/42874337/137840739-74681d46-8337-4f07-ac0a-729264e0d2cf.png)](https://drive.google.com/file/d/1_8C4dAzmo2JtW54vDXacyz8srLmTZD2P/view?usp=sharing)

As shown in the video, we have saved holes for plugging in the pi and actually run the device in part 2, and places for the speech to text speaker to be on waist.  

### Part 2

**I glove you, do you glove me?  ---  Ilan**

(Thank you Ilan, for gloving us.)
(and thank you for the tape as well)

### Record

#### Prototype Feedback Documentation:

1. The gauntlet you have created is very creative, but the cardboard glove is kind of hard to bend, which leads to the inconvenience of typing.
- Our Solution: We have borrowed a glove from the lab (Thank you again, Ilan) in cotton fabrics, which leads to a way better typing experience with finger gestures. It now feels softer, very light on hand, and also a better look. Very Cyberpunk now. 

2. It seems like a very hard thing to learn, not very intuitive.
- Our Solution: Yes that's true, it does requires a certain learning curve at first use, however, it's a common path of using all type of using all keyboards, and as we have tried to train ourselves over this week on doing that, we found it's not particularly harder than traditional T9 keyboard, somewhat even easier. 
- With that being said, we did change a few things about our device set up. We now associate number 1 with the last gesture for two reasons:
-- First of all, 1 in T9 typing is the least significant, as shown in the image above, and does not associate with any letters, so it’s less frequent in terms of being used, should not be occupying the easiest to reach finger
-- Secondly, it is also reasonable to place 1 in a way that resembles how people show number 1 to others, with the index finger isolated from other fingers. The new gestures are encoded to numbers as the following:

![image](https://user-images.githubusercontent.com/42874337/138805709-d49510af-6a32-4832-95db-e457afe60ffc.png)

3. How will the speaker be placed? Will it be too heavy for people to wear?
- The speaker will be placed on the arm for this prototype. However, depending on the user, it might be better placed near the neck if it’s used as a voice replacement for medical and accessible purposes. The whole device is not too heavy even for this prototype, it is easily lifted by arms and does not influence people’s daily lives. If it’s being integrated into smart watches, or being mass produced into a smaller size, it can be even more portable and easier to carry.


#### Re-Prototype:

Based on the feedback we received and attempts we made to test and redesign the prototype, we have made a new version of it with a lot of updates on setup and materials. Aside from what we talked about before about the fabric of the gloves, we have also rewired the inside of this device prototype and added the speaker to it as a new way of output. We have also made minor changes like adding more conductive tapes to fingertips and added clips to enhance the connection (also very cyberpunk, we like it a lot). Here’s our record of the process and the final design of the gauntlet:

![image](https://user-images.githubusercontent.com/42874337/138805781-b5c23176-62db-4f79-8456-d16990c3e64f.png)

![image](https://user-images.githubusercontent.com/42874337/138805796-a5ce61b2-565a-4835-b3ae-c24cf82d88b9.png)

![image](https://user-images.githubusercontent.com/42874337/138805812-ce117847-759f-4288-b092-f5318e8fa29e.png)

![image](https://user-images.githubusercontent.com/42874337/138805841-dd3a98d5-6a58-4756-b63c-1693f9400b5c.png)

[![image](https://user-images.githubusercontent.com/42874337/138805841-dd3a98d5-6a58-4756-b63c-1693f9400b5c.png)](https://drive.google.com/file/d/1432WFbeaX180M1sPeYsPxpgQvese5w3z/view?usp=sharing)

#### Works Like:

In order to make the device actually work as we designed it to be, we have conquered multiple barriers from programming to physical layout of the device. Some major issues we have conquered are: T9 typing predictive algorithm, sensor accuracy, input presentation (visual interface), and how to backspace and output using the gesture sensor. Along the way another major problem we have solved is how to create multithreaded programs (input-output concurrency) that allows as authenticate and as realistic typing experience as possible. 

Code of this device: [Code Repo](https://github.com/CaseyPYZ/Interactive-Lab-Hub/tree/Fall2021/Lab%204/finite_gauntlet)

(Including multiple versions from single thread to multithread)

##### T9 Input Imitation

We wanted the prototype to be able to provide the full experience of a well-functioning “keyboard”, so we implemented a simple version of T9 input.

***Reference: https://stackoverflow.com/questions/12074963/t9-system-to-numpad***

We built off of method #2 given in the reference shown above, which is a brute force T9 input system imitator. It had a weighting factor to determine in what order it should show the user the detected possible word inputs. The original post used Project Gutenberg's The Adventures of Sherlock Holmes as its weighting reference material. We later found out that this source was not ideal because of its artistic nature as a literature work, and the fact that it is missing some common words such as “hi”. Therefore, we replaced the weighting reference with a database that contains a massive amount of conversation text of humans with chatbots that many researchers have built before, which resembles the environment we expected our users to be in (normal daily conversations).

***Reference: http://convai.io/data/***

After these tweaks, the imitator worked great, and the predictive algorithm provided a very good typing experience just like the everyday input method we use in modern mobile devices settings. It will predict the possible words based on frequencies of the words in daily conversation, and display the words with highest frequencies just like modern input methods. 

##### Visual Presentation

The visual output of our device takes the form of three lines of text.

* **1st line:** Currently imputed characters;
* **2nd line:** List of words predicted by the T9 system;
* **3rd line:** Words being imputed already, waiting to be outputted as a sentence

At every confirmed output with a RIGHT gesture, the input buffers are cleared, so is the screen.

Here’s an example of how it works with every input:

- Input: 4

![image](https://user-images.githubusercontent.com/42874337/138806019-6edd1ebe-25a0-471d-8d3d-67922dc6521a.png)

- Input: 3

![image](https://user-images.githubusercontent.com/42874337/138806042-2b98c398-e95f-4bb9-8dd8-8274eb0d18f0.png)

- Input: 5

![image](https://user-images.githubusercontent.com/42874337/138806059-992d7d75-2854-4d89-b89c-d2571d91b954.png)

- Input: 5

![image](https://user-images.githubusercontent.com/42874337/138806074-f26cd95a-dee6-48a3-8527-a8fdfa535580.png)

- Input: 6

![image](https://user-images.githubusercontent.com/42874337/138806084-059f1ce5-1b3e-42a3-8a94-3a20dae74358.png)

##### Sensor Concurrency

One of the major problems we tackled in the development of this prototype was sensor concurrency. In our design, there are two major sensors: capacitive sensors for typing and gesture sensor for backspace/confirming output; in addition, there’s a OLED screen as our visual output method.

At first, we have our program running a main *while loop* that looped every *0.5 seconds*. This timing threshold is set in favor of the capacitive sensors, so that it recognizes an input once at every touch. However, this looping rate made our gesture sensor very insensitive to gestures. In order for the gesture sensor to work properly, it needs to be constantly watching for gestures instead of checking once every 0.5 second.

To fix this problem, we refactored our code into a multi-thread program, in which the gesture sensor runs on its only thread that runs a regular while loop with no sleeping time, while the capacitive sensors stay on the main 0.5-second-sleeping-time loop.

The OLED screen is also handled on the main thread, as it only needed to update display contents whenever the capacitive sensor inputs change.

##### Backspace and Output

As previously mentioned, backspace and output confirmation (device speaks out the sentence) is controlled by a gesture sensor that runs concurrently in its own thread.

The gesture sensor thread runs a while loop and constantly checks for gestures. It rests on an IDLE state, and has two triggering states:

**When there’s a RIGHT gesture and the input buffer is not empty:** triggers a output confirmation, the program opens up a subprocess and speaks out the sentence with GoogleTTS;
**When there’s a LEFT gesture and the input numbers (1-9, stored in the NUM buffer) for the current word is not empty:** triggers a backspace, and the last number in the current NUM buffer is popped, carrying out a backspace.

**An example of how backspace works**

![image](https://user-images.githubusercontent.com/42874337/138806175-6b9291ba-e530-4fe4-9702-550202c22fc1.png)

It’s worth noticing that we changed the placement of the gesture sensor in our final device prototype based on on-site feedback. At first we had the gesture sensor taped to the side of the glove’s index finger as originally designed, but later in testing we found out that the material of the glove is very hard for tape to stay on, and didn’t allow very stable attachments.

The attachment method that made the most sense would be sewing the sensor onto the glove, but we did not want to damage the glove (It was very generous of Ilan to lend it to us). So for the sake of user testing, we moved the sensor to the upper side of the wrist.

Despite this change, our original index-finger-side design is still solid, and worked well when we tested it on bare hands. With a more suitable glove, it can be properly implemented to carry the device’s spirit of single-hand operation.

**Final Device Test by Designer:**

[![image](https://user-images.githubusercontent.com/42874337/138806260-64475984-de9d-44d9-8b25-c73acc4f7bb7.png)](https://drive.google.com/file/d/13Tzd2pMfzkxl-mV37OJtgb4bQ9B1ijnf/view?usp=sharing)

##### User Test

We invited a participant from outside the class to experience our prototype.

[![image](https://user-images.githubusercontent.com/42874337/138806337-edf0497f-833c-4434-a4e2-8dc232f5e78e.png)](https://drive.google.com/file/d/13OhOeQ8sqMVtkOxja7GMKASgozzr4kq3/view?usp=sharing)

In general, the device worked well and functioned as intended. The participant was able to type in some words after getting familiar with the 9-key input methods and learning which gesture meant which number.

#### Future Improvements

1. We should use softer and more flexible fabric for **glove material**. User tests showed that the current material is lacking flexibility and is somewhat heavy.
2. **Conductive material for capacitive sensors** should be switched to something softer, more resilient, elastic and flexible. The conductive tape we used in this prototype worked great in transmitting capacitance, but it had no elasticity, so it broke very easily. For this device, **conductive thread** would be a great choice.
3. If the device design is connected to smaller computer units, like smart watches, and using more accurate sensors, it can be very useful and portable for many modern scenarios. For example: solving small screen problems for smartwatch text input, accessible devices that are built for people who are in need of voice replacement, pair with AR headsets like smart glasses to text without looking down. 



