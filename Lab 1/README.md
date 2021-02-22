

# Staging Interaction

In the original stage production of Peter Pan, Tinker Bell was represented by a darting light created by a small handheld mirror off-stage, reflecting a little circle of light from a powerful lamp. Tinkerbell communicates her presence through this light to the other characters. See more info [here](https://en.wikipedia.org/wiki/Tinker_Bell). 

There is no actor that plays Tinkerbell--her existence in the play comes from the interactions that the other characters have with her.



For lab this week, we draw on this and other inspirations from theatre to stage interactions with a device where the main mode of display/output for the interactive device you are designing is lighting. You will plot the interaction with a storyboard, and use your computer and a smartphone to experiment with what the interactions will look and feel like. _Make sure you read all the instructions and understand the whole of the laboratory activity before starting!_



## Prep

1. Set up [your Github "Lab Hub" repository](../../../) by [following these instructions](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2021Spring/readings/Submitting%20Labs.md).
2. Set up the README.md for your Hub repository (for instance, so that it has your name and points to your own Lab 1) and [learn how](https://guides.github.com/features/mastering-markdown/) to post links to your submissions on your readme.md so we can find them easily.

### For lab, you will need:

1. Paper
1. Markers/ Pen
1. Smart Phone--Main required feature is that the phone needs to have a browser and display a webpage.
1. Computer--we will use your computer to host a webpage which also features controls
1. Found objects and materials--you’ll have to costume your phone so that it looks like some other device. These materials can include doll clothes, a paper lantern, a bottle, human clothes, a pillow case. Be creative!
1. Scissors

### Deliverables for this lab are: 
1. Storyboard
1. Sketches/photos of costumed device
1. Any reflections you have on the process.
1. Video sketch of the prototyped interaction.
1. Submit these in the lab1 folder of your class [Github page], either as links or uploaded files. Each group member should post their own copy of the work to their own Lab Hub, even if some of the work is the same for each person in the group.


## Overview
For this assignment, you are going to 

A) [Plan](#part-a-plan) 

B) [Act out the interaction](#part-b-act-out-the-interaction) 

C) [Prototype the device](#part-c-prototype-the-device)

D) [Wizard the device](#part-d-wizard-the-device) 

E) [Costume the device](#part-e-costume-the-device)

F) [Record the interaction](#part-f-record)

## The Report
This readme.md page in your own repository should be edited to include the work you have done. You can delete everything but the headers and the sections between the **stars**. Write the answers to the questions under the starred sentences. Include any material that explains what you did in this lab hub folder, and link it in the readme.

Labs are due on Mondays. Make sure this page is linked to on your main class hub page.

## Part A. Plan 

To stage the interaction with your interactive device, think about:

_Setting:_ Where is this interaction happening? (e.g., a jungle, the kitchen) When is it happening?

_Players:_ Who is involved in the interaction? Who else is there? If you reflect on the design of current day interactive devices like the Amazon Alexa, it’s clear they didn’t take into account people who had roommates, or the presence of children. Think through all the people who are in the setting.

_Activity:_ What is happening between the actors?

_Goals:_ What are the goals of each player? (e.g., jumping to a tree, opening the fridge). 

The interactive device can be anything *except* a computer, a tablet computer or a smart phone, but the main way it interacts needs to be using light.
**Describe your setting, players, activity and goals here.**

* **Setting:** In the bedroom of an apartment, during the COVID time. 
* **Players:** David is a graduate student who is a TA for 2 different classes. He is alone in this bedroom with his interactive calendar. 
* **Activity:** David does not check his schedule very often, and when he is concetarted on something, he will forget some important events, such as holding his office hour or being late to the class he teaches. The interactive calender using lights to tell David if there is any events coming up, and different color of lights can signal different kind of events. 
One day afternoon when David finished his assignment, he starts watching his faviorite TV series. The interactive calender starts flashing red light when David is concentrated on the TV series. David notices the red light and he knows he has office hour in 15 mins. He turns off the TV and prepares his office hour. 
* **Goals:** The goal for David is to keep up with his schedule and not miss any impotant event. 



Sketch a storyboard of the interactions you are planning. It does not need to be perfect, but must get across the behavior of the interactive device and the other characters in the scene. 
**Include a picture of your storyboard here**

![alt text](https://github.com/YuanhaoZhu/Interactive-Lab-Hub/blob/Spring2021/Lab%201/storyboard_lab1.png
 "Storyboard")
 
Present your idea to the other people in your breakout room. You can just get feedback from one another or you can work together on the other parts of the lab.
**Summarize feedback you got here.**

**Feedback:**
* This idea sounds like the google calender, while google calendar notify people with sounds, this interactive calender notify people with colored light. One advantage of this interactive calendar is that you will know the type of event by different color while google calender only have the same notificiation sound. 

* The colored light might cause some trouble with color blind people. While the most color blind type are red-green color blind, twitch the color palette a little bit can still adapt their needs. For full colorblind people, you might need to adjust the color option to blickiing light, breathing light, etc. 



## Part B. Act out the Interaction

Try physically acting out the interaction you planned. For now, you can just pretend the device is doing the things you’ve scripted for it. 

**Are there things that seemed better on paper than acted out?**

What player is thinking, what he wants to do after see the device light up etc. is easy to see when I script it out on paper. While the player is acting it, he needs to exaggerate his gesture, facial expression to let audience know his emotion and thoughts. 

**Are there new ideas that occur to you or your collaborators that come up from the acting?**

I think instead of this one-direction signal: you see the light and execute your task, it would be better that we can have some feedback on this device. Maybe I want to turn off the lights because I’m already on this task and don’t want to see this light blicking. In another scenario, I may want to cancel or postpone this event. If the device can take input like voice, hand clapping, or button press, we can make calendar even more interactive.

## Part C. Prototype the device

You will be using your smartphone as a stand-in for the device you are prototyping. You will use the browser of your smart phone to act as a “light” and use a remote control interface to remotely change the light on that device. 

Code for the "Tinkerbelle" tool, and instructions for setting up the server and your phone are [here](https://github.com/FAR-Lab/tinkerbelle).

We invented this tool for this lab! 
**Give us feedback on Tinkerbelle.**

My python version is 3.8 and the Tinkerbelle does not work for me. I was unable to try out Tinkerbelle but I can talk about it from the UI aspect. You can choose from a color palette and also choose from the color wheel, it’s nice because people have a good set of choice but also great flexibility. I think it will be better to incorporate any blicking or flashing feature to the Tinkerbelle so it can express more information. Also it will be more intuitive to have a slide bar to control the brightness. 

## Part D. Wizard the device
Take a little time to set up the wizarding set-up that allows for someone to remotely control the device while someone acts with it. Hint: You can use Zoom to record videos, and you can pin someone’s video feed if that is the scene which you want to record. 

**Include your first attempts at recording the set-up video here.**

* [My first-attemp set-up video](https://youtu.be/D3BDoxz0s5c "My first-attemp set-up video").

Now, hange the goal within the same setting, and update the interaction with the paper prototype. 

**Show the follow-up work here.**

* [My follow-up video](https://youtu.be/FMMO76oEVK0 "My follow-up video").

## Part E. Costume the device

Only now should you start worrying about what the device should look like. Develop a costume so that you can use your phone as this device.

Think about the setting of the device: is the environment a place where the device could overheat? Is water a danger? Does it need to have bright colors in an emergency setting?

**Include sketches of what your device might look like here.**

![alt text](https://github.com/YuanhaoZhu/Interactive-Lab-Hub/blob/Spring2021/Lab%201/costume_the_device_sketch_lab1.png
 "Storyboard")
 
**What concerns or opportunitities are influencing the way you've designed the device to look?**

The device should be able to be mounted on the wall or hung up so that the light can catch users attention. The prop and the device should not be too heavy, otherwise they might fall off. The device should be place in the area that users spend their most time on. Also the prop should not cover up the light of the device to make the light as bright as possible. 


This is the final look of my device. Since I cannot put nails on the apartment wall (because the landlord does not allow), I put the device on the windowsill. The position of the device is good because it can be easily detected during daily activities in the apartment. I finally choose this candle lantern to mount my phone because it does not cover up the screen and can keep my phone steady on the windowsill.

![alt text](https://github.com/YuanhaoZhu/Interactive-Lab-Hub/blob/Spring2021/Lab%201/final_look_lab1.png
 "finallook")


## Part F. Record

**Take a video of your prototyped interaction.**

* [My final video](https://youtu.be/h-lSWV1q1yg "My final video").

**Please indicate anyone you collaborated with on this Lab.**
Be generous in acknowledging their contributions! And also recognizing any other influences (e.g. from YouTube, Github, Twitter) that informed your design. 
Thanks to Chang Han, who is the actor in the final video.

# Staging Interaction, Part 2 

This describes the second week's work for this lab activity.


## Prep (to be done before Lab on Wednesday)

You will be assigned three partners from another group. Go to their github pages, view their videos, and provide them with reactions, suggestions & feedback: explain to them what you saw happening in their video. Guess the scene and the goals of the character. Ask them about anything that wasn’t clear. 

**Summarize feedback from your partners here.**
* Include audio, because users might miss out the visual signal.
* Users need to memorize the color code, need to fix this problem.
* could make the alarm sound different for different scenarios.



**Original feedback for reference:**
* Feedback from Chelsea Luo: I like the idea of using light as a visual indicator for immediate information feedback. It might be good to include audio as part of the alert, since it might be easy to miss the visual signal while working on something else.
* Feedback from Jiayun Liu: The video is very clear and the interaction design is quite intuitive. The lantern fits well for the purpose. However, I wonder how the user could remember which color represents which events, if there is no cheat sheet provided. Also what if the user is not in the same room with the device when an event alarm is on?
* Feedback from Ruijun Li: The idea is very smart and practical, especially as is described in the "Plan" part, the device could be deployed under the circumstances of the Covid when people are in social distancing, indulging in tittytainment or any other activities. I super love how you draw the storyboard and make the film -- They are so creative and attractive! And they present comparative scenarios to highlight the functionality of the device. Also, how you costume the device enable it to be a cute portable household device, like a small furniture. The only suggestion I have would be, maybe you could make the alarm sound more diverse and adaptive for different scenarios, e.g. the Valentine alarm could be different from the office hour alarm, with different volumes.




## Make it your own

Do last week’s assignment again, but this time: 
1) It doesn’t have to (just) use light, 
2) You can use any modality (e.g., vibration, sound) to prototype the behaviors, 
3) We will be grading with an emphasis on creativity. 

**Document everything here.**
# Storyboard
![alt text](https://github.com/YuanhaoZhu/Interactive-Lab-Hub/blob/Spring2021/Lab%201/storyboard%202.jpg
 "storyboard v2")
# Final Video
* [My final video v2](https://youtu.be/gYh6wp_twFI "My final video v2").
