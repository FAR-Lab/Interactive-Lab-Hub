

# Staging Interaction

In the original stage production of Peter Pan, Tinker Bell was represented by a darting light created by a small handheld mirror off-stage, reflecting a little circle of light from a powerful lamp. Tinkerbell communicates her presence through this light to the other characters. See more info [here](https://en.wikipedia.org/wiki/Tinker_Bell). 

There is no actor that plays Tinkerbell--her existence in the play comes from the interactions that the other characters have with her.

For lab this week, we draw on this and other inspirations from theatre to stage interactions with a device where the main mode of display/output for the interactive device you are designing is lighting. You will plot the interaction with a storyboard, and use your computer and a smartphone to experiment with what the interactions will look and feel like. 

_Make sure you read all the instructions and understand the whole of the laboratory activity before starting!_



## Prep

### To start the semester, you will need:
1. Read about Git [here](https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F).
2. Set up your own Github "Lab Hub" repository to keep all you work in record by [following these instructions](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2021Fall/readings/Submitting%20Labs.md).
3. Set up the README.md for your Hub repository (for instance, so that it has your name and points to your own Lab 1) and [learn how to](https://guides.github.com/features/mastering-markdown/) organize and post links to your submissions on your README.md so we can find them easily.


### For this lab, you will need:
1. Paper
2. Markers/ Pens
3. Scissors
4. Smart Phone -- The main required feature is that the phone needs to have a browser and display a webpage.
5. Computer -- We will use your computer to host a webpage which also features controls.
6. Found objects and materials -- You will have to costume your phone so that it looks like some other devices. These materials can include doll clothes, a paper lantern, a bottle, human clothes, a pillow case, etc. Be creative!

### Deliverables for this lab are: 
1. 7 Storyboards
1. 3 Sketches/photos of costumed devices
1. Any reflections you have on the process
1. Video sketch of 3 prototyped interactions
1. Submit the items above in the lab1 folder of your class [Github page], either as links or uploaded files. Each group member should post their own copy of the work to their own Lab Hub, even if some of the work is the same from each person in the group.

### The Report
This README.md page in your own repository should be edited to include the work you have done (the deliverables mentioned above). Following the format below, you can delete everything but the headers and the sections between the **stars**. Write the answers to the questions under the starred sentences. Include any material that explains what you did in this lab hub folder, and link it in your README.md for the lab.

## Lab Overview
For this assignment, you are going to:

A) [Plan](#part-a-plan) 

B) [Act out the interaction](#part-b-act-out-the-interaction) 

C) [Prototype the device](#part-c-prototype-the-device)

D) [Wizard the device](#part-d-wizard-the-device) 

E) [Costume the device](#part-e-costume-the-device)

F) [Record the interaction](#part-f-record)

Labs are due on Mondays. Make sure this page is linked to on your main class hub page.

## Part A. Plan 

_Scenario_: This interactive device was designed with individuals with cognitive deficits, especially older adults with cognitive deficits such as dementia, in mind. These users are often confused about the state of the world (i.e. where they are, what time of day it is, what they were about to do or what was happening previously) and need to be constantly reoriented through the help of their caregivers. They are have other conditions, such as experiencing agitation and anixiety throughout the day, waking up and attempting to walk in the middle of the night, and not able to move from one place to another as easily to experience other settings. So this device aims to reorient users through light and sound to show what time of day it is with additional interactions to help these potential users. 

_Setting:_ A indoors room  (home/apartment, care facilities, etc.) throughout the day after the player wakes up in the morning and until they go to sleep.

_Players:_ 1) Individuals, especially older adults, with cognitive deficits, 2) caretakers (paid aids or family members), 3) possibly other patients if the setting is a larger facility, rather than a private room at home. The main player is the older adult with cognitive deficits.

_Activity:_ The older adult is most likely sitting/lying down on a chair or couch, sitting there and intermittently falling asleep and waking up, or watching television, listening to music, reading a book, etc. The caretaker is in the room occupied with other tasks but monitoring the older adult in case they need to move. 

_Goals:_ 1) Reorienting themselves in the time of day (knowing what time of day it is), 2) experiencing other places without physically moving, 3) calming anxieties that might occur.

_Device:_ The interactive device is a desk lamp with speakers. The interaction will occur through light and sound. 


**Storyboards**

_Overview_
![overview](https://github.com/hjkim63/Interactive-Lab-Hub/blob/b488bbc3e1e960b6c929db4272ad90b5136d58bb/Lab%201/storyboard_overview.jpg)

_Individual sketches_
![A](https://github.com/hjkim63/Interactive-Lab-Hub/blob/b488bbc3e1e960b6c929db4272ad90b5136d58bb/Lab%201/storyboard_A.jpg)
![B](https://github.com/hjkim63/Interactive-Lab-Hub/blob/b488bbc3e1e960b6c929db4272ad90b5136d58bb/Lab%201/storyboard_B.jpg)
![C](https://github.com/hjkim63/Interactive-Lab-Hub/blob/b488bbc3e1e960b6c929db4272ad90b5136d58bb/Lab%201/storyboard_C.jpg)


_Storyboard Feedback_
- Light and colors alone might be difficult for the user to understand what is intended
- Light might confused the user, in the case they are in later stages of dementia or simply forget such lights exist



## Part B. Act out the Interaction

**Are there things that seemed better on paper than acted out?**
- Noticing the light seemed straightforward on paper, but when acted out, the user needs more signals of where to look or the light needs to be noticeable 
- Colors of the light alone might be difficult to convey the time of day --might need the help of more indictive sounds that are associated with specific times of day (crickets at night, birds chirping in the morning, etc.) 

**Are there new ideas that occur to you or your collaborators that come up from the acting?**
- Some element of personalization to the user would be nice for the sounds and lights to have the intended effect
- 

## Part C. Prototype the device

Using the browser of a smart phone, the screen and audio speakers acted as the source of light and sound. I used my laptop computer as the service remotely control the light (change in hues, speed in changes of color to act as blinking, etc.) and sound on the device. Ideally, this device would be able to identify what time of day it is through a clock/timer function. The device should also be able to detect if the light from the device is causing more anxiety in the main player, in which case the light should subside.

I used the code for the "Tinkerbelle" tool provided from the course [here](https://github.com/FAR-Lab/tinkerbelle). I experimented with the sounds to fit the keywods (pool, waves, leaves rustling) and how to control the light to mimic different lighting effects (gradient, changing colors, blinking, etc.)

\*\***Give us feedback on Tinkerbelle.**\*\*
Tinkerbelle was extremely easy to implement and run, but I wish there were opportunities and guidance to modify the code, such as to implement the varying lighting effects. The sounds auto-suggested from the input keywords were helpful and provided creative sounds that weren't initally planned. For example, I had initially input "leaves rustling" to convey a park setting, but rather the "server" generated sounds of walking in fall leaves, which converyed more "active sounds" that the user could interact with.


## Part D. Wizard the device

I experimented with different ways to use the phone as the light sources on a lamp-like device. Tying the smart phone to inside a table lamp was not successful as the lamp was too small to amplify the light source large enough for a user to notice. Instead, I changed the initial design to a floor lamp, and staged it by putting the smart phone (at full brightness and full audio) in a lamp with a large cone. 

**Here are the first attemps of the set up video.**

_Goal:_ give the illusion that the user is at a pool. (lights of blue hues, pool sounds)
![prototype_Goal_1](https://github.com/hjkim63/Interactive-Lab-Hub/blob/4596a8ec8afb5d04c027927b3c66a5846fd63f65/Lab%201/prototype_1.MOV)

Now, change the goal within the same setting, and update the interaction with the paper prototype. 

_Goal:_ reorient user to time of day --morning/sunrise. (yellow and orange lights)
![prototype_Goal_2](https://github.com/hjkim63/Interactive-Lab-Hub/blob/4596a8ec8afb5d04c027927b3c66a5846fd63f65/Lab%201/protoype2.MOV)


## Part E. Costume the device

_Costume idea sketches:_
![costumes](https://github.com/hjkim63/Interactive-Lab-Hub/blob/8e7234508cd892af355a9a6c11a08bb02a80279f/Lab%201/costume.jpg)

_Setting of the device:_ The device would be either placed on a side table/desk or standing/propped up on the floor (possibly hanging but would be more difficult to install). There is few external factors that would make the device vulnerable to heat or water. In the case the light has an alarm functionality, there would need to be brighter lights that gets the attention of the main user and others (caretakers) within the room as well. 

_Considerations & concerns:_ While the floor lamp with a large, upward looking cone helps to distribute the light in the room to give am ambience effect, the source of light is slightly too far for the user to notice right away.


## Part F. Record

_Video of prototyped interactions:_

Walking in park: ![prototyped_interaction_park](https://github.com/hjkim63/Interactive-Lab-Hub/blob/e17004ff1dfd46776d22d19f278b9c1b01449213/Lab%201/interaction_1.mov)
Visiting the pool ![prototyped_interaction_pool](https://github.com/hjkim63/Interactive-Lab-Hub/blob/e17004ff1dfd46776d22d19f278b9c1b01449213/Lab%201/interaction_2.mov)



\*\***Please indicate anyone you collaborated with on this Lab.**\*\*
Be generous in acknowledging their contributions! And also recognizing any other influences (e.g. from YouTube, Github, Twitter) that informed your design. 



# Staging Interaction, Part 2 

This describes the second week's work for this lab activity.


## Feedback

The following feedback points are summarized from 1) Canvas peer review, 2) in-person lab activity (Sylvia Ding
Sylvia Ding, Michael Kelleher, Elizabeth Pysher, Sidarth Wadhwa), and 3) TA review :
- Promising idea as "clock for older adults with cognitive deficits"
- Focusing on other experiences and activites that are less touch-sensory based (swimming in pools) and more sound-sensory based (i.e. reading in cafe, walking in park, watching movies) might be easier to have intended effect
- Could experiment more with intensity and gradient of light to give different effects
- Try thinking about different modalities and devices while focusing on other interactions, other than lights from devices that are already intended for light, such as a lamp

## Reflections



## Make it your own

Do last week’s assignment again, but this time: 
1) It doesn’t have to (just) use light, 
2) You can use any modality (e.g., vibration, sound) to prototype the behaviors! Again, be creative! Feel free to fork and modify the tinkerbell code! 
3) We will be grading with an emphasis on creativity. 

\*\***Document everything here. (Particularly, we would like to see the storyboard and video, although photos of the prototype are also great.)**\*\*

## Part A. Plan 

_Scenario_: This interactive device is designed for individuals with cognitive deficits, especially older adults with cognitive deficits such as dementia. These users are 1)not very familiar with technology and 2) often confused about the state of the world which presents a need for these users to be constantly reoriented by more analog methods, such as to-do lists, pictures/diagrams, or even caregivers. In reattemping Part 1 of this assignment, I focused on the interaction of the device as a "clock for older adults with dementia" that could help users tell what time of day, what day of week, what month of the year, and what season without necessarily telling time through the traditional way of reading a clock. 

The design of this device was inspired by a speech therapy whiteboard of an interview participant (male in their 80's) with moderate stage dementia. Personal information and real images were ommitted for privacy reasons.

_Setting:_ A indoors room (home/apartment, care facilities, etc.).

_Players:_ 1) Individuals, especially older adults, with cognitive deficits, 2) caretakers (paid aids or family members), 3) possibly other patients if the setting is a larger facility, rather than a private room at home. The main player is a single older adult with cognitive deficits (disregard settings with multiple older adults at the moment).

_Activity:_ The older adult is most likely sitting/lying down on a chair or couch, intermittently falling asleep and waking up. The older adult might look arond the room (at the television if it is playing), reading, listening to music, etc., but mostly engaging in sedentary activities. The caretaker is in the room occupied with other tasks but monitoring the older adult in case they need to move. 

_Goals:_ 1) Reorienting themselves in the time of day (knowing what time of day it is), 2) experiencing other places without physically moving, 3) calming anxieties that might occur.

_Device:_ The interactive device is a desk lamp with speakers. The interaction will occur through light and sound. 


**Storyboards**

_Overview_
![overview](https://github.com/hjkim63/Interactive-Lab-Hub/blob/b488bbc3e1e960b6c929db4272ad90b5136d58bb/Lab%201/storyboard_overview.jpg)

_Individual sketches_
![A](https://github.com/hjkim63/Interactive-Lab-Hub/blob/b488bbc3e1e960b6c929db4272ad90b5136d58bb/Lab%201/storyboard_A.jpg)
![B](https://github.com/hjkim63/Interactive-Lab-Hub/blob/b488bbc3e1e960b6c929db4272ad90b5136d58bb/Lab%201/storyboard_B.jpg)
![C](https://github.com/hjkim63/Interactive-Lab-Hub/blob/b488bbc3e1e960b6c929db4272ad90b5136d58bb/Lab%201/storyboard_C.jpg)


_Storyboard Feedback_
- Light and colors alone might be difficult for the user to understand what is intended
- Light might confused the user, in the case they are in later stages of dementia or simply forget such lights exist



## Part B. Act out the Interaction

**Are there things that seemed better on paper than acted out?**
- Noticing the light seemed straightforward on paper, but when acted out, the user needs more signals of where to look or the light needs to be noticeable 
- Colors of the light alone might be difficult to convey the time of day --might need the help of more indictive sounds that are associated with specific times of day (crickets at night, birds chirping in the morning, etc.) 

**Are there new ideas that occur to you or your collaborators that come up from the acting?**
- Some element of personalization to the user would be nice for the sounds and lights to have the intended effect
- 

## Part C. Prototype the device

Using the browser of a smart phone, the screen and audio speakers acted as the source of light and sound. I used my laptop computer as the service remotely control the light (change in hues, speed in changes of color to act as blinking, etc.) and sound on the device. Ideally, this device would be able to identify what time of day it is through a clock/timer function. The device should also be able to detect if the light from the device is causing more anxiety in the main player, in which case the light should subside.

I used the code for the "Tinkerbelle" tool provided from the course [here](https://github.com/FAR-Lab/tinkerbelle). I experimented with the sounds to fit the keywods (pool, waves, leaves rustling) and how to control the light to mimic different lighting effects (gradient, changing colors, blinking, etc.)

\*\***Give us feedback on Tinkerbelle.**\*\*
Tinkerbelle was extremely easy to implement and run, but I wish there were opportunities and guidance to modify the code, such as to implement the varying lighting effects. The sounds auto-suggested from the input keywords were helpful and provided creative sounds that weren't initally planned. For example, I had initially input "leaves rustling" to convey a park setting, but rather the "server" generated sounds of walking in fall leaves, which converyed more "active sounds" that the user could interact with.


## Part D. Wizard the device

I experimented with different ways to use the phone as the light sources on a lamp-like device. Tying the smart phone to inside a table lamp was not successful as the lamp was too small to amplify the light source large enough for a user to notice. Instead, I changed the initial design to a floor lamp, and staged it by putting the smart phone (at full brightness and full audio) in a lamp with a large cone. 

**Here are the first attemps of the set up video.**

_Goal:_ give the illusion that the user is at a pool. (lights of blue hues, pool sounds)
![prototype_Goal_1](https://github.com/hjkim63/Interactive-Lab-Hub/blob/4596a8ec8afb5d04c027927b3c66a5846fd63f65/Lab%201/prototype_1.MOV)

Now, change the goal within the same setting, and update the interaction with the paper prototype. 

_Goal:_ reorient user to time of day --morning/sunrise. (yellow and orange lights)
![prototype_Goal_2](https://github.com/hjkim63/Interactive-Lab-Hub/blob/4596a8ec8afb5d04c027927b3c66a5846fd63f65/Lab%201/protoype2.MOV)


## Part E. Costume the device

_Costume idea sketches:_
![costumes](https://github.com/hjkim63/Interactive-Lab-Hub/blob/8e7234508cd892af355a9a6c11a08bb02a80279f/Lab%201/costume.jpg)

_Setting of the device:_ The device would be either placed on a side table/desk or standing/propped up on the floor (possibly hanging but would be more difficult to install). There is few external factors that would make the device vulnerable to heat or water. In the case the light has an alarm functionality, there would need to be brighter lights that gets the attention of the main user and others (caretakers) within the room as well. 

_Considerations & concerns:_ While the floor lamp with a large, upward looking cone helps to distribute the light in the room to give am ambience effect, the source of light is slightly too far for the user to notice right away.


## Part F. Record

_Video of prototyped interactions:_

Walking in park: ![--](https:)
