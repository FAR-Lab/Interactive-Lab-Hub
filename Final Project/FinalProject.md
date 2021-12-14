# Final Project

Using the tools and techniques you learned in this class, design, prototype and test an interactive device.

Project plan - November 22

Peer feedback on Project plans: November 24

Functional check-off - November 30 & December 2

Final Project Presentations - December 7

Write-up and documentation due - December 13

## Objective

The goal of this final project is for you to have a fully functioning and well-designed interactive device of your own design.
 
## Description

The Covid-19 pandemic has exacerbated the concerns around elderly homecare. As older adults are confined to home alone, they are more vulnerable to falling. According to CDC, there are about 36 million older adults fall each year, which results in more than 32,000 deaths. Inspired by this shocking fact, we decide to build a device to potentially address this issue.

Introducing FallSafe, a wearable device to detect falls and share the information with emergency contact. Using accelerometer, the device would be able to determine whether a person is falling by sensing motion and measuring the rate of change of the velocity. The device is also integrated with a communication system via MQTT which we explored in Lab 6. Transmitting the information immediately with emergency contact would allow people to respond promptly to prevent severe consequences.

## Deliverables

1. Project plan: Big idea, timeline, parts needed, fall-back plan. <br />
https://docs.google.com/document/d/1Diftxmh99L5KeCyj5gd5Jx9XdbtfqpxcKQgLYkQG350/edit?usp=sharing <br />
Feedback on the project plan -
```
Really useful idea that could really help people. How would the device be worn? 
Consider working this out as well: is it watertight to also be used in the shower? 
Does it need charging? Does it show what its state is? Seems like a good amount of work for two people.
```
```
From a feasibility perspective, it may be hard to differentiate a fall 
from a fast movement using just the accelerator, unless there is a clear pattern present. 
Your backup plan seems very doable with CV though, and interesting.
```

2. Functioning project: The finished project should be a device, system, interface, etc. that people can interact with. <br />
![P2:Functioning](https://github.com/kchen1009/Interactive-Lab-Hub/blob/Fall2021/Final%20Project/Project1.jpeg)
![P3:Functioning](https://github.com/kchen1009/Interactive-Lab-Hub/blob/Fall2021/Final%20Project/Project2-1.jpg)
![P4:Functioning](https://github.com/kchen1009/Interactive-Lab-Hub/blob/Fall2021/Final%20Project/Project3.png)
The finished product is a wearable device to detect one's falling. By wearing the device, elderly people could ensure their safety if some unfortunate events happen. Besides having a sensor to detect a user's motion, the device is also equipped with a camera and speaker. These components allow the device to amplify the alert and further send the alert along with a recording of the incident to emergency contact. We are also aware that there might be false alarm since the sensor is sensitive and likely to be triggered unintentionally. If that's the case, there is a button next to the display, allowing users to cancel the alert.



3. Documentation of design process <br />
The idea and interaction is illustrated in the storyboard below.
![P1:Storyboard](https://github.com/kchen1009/Interactive-Lab-Hub/blob/Fall2021/Final%20Project/Storyboard.JPG)
We sought to use the story board as a foundation to design the entire system. After a few rounds of discussion and iteration, we decided that the system need to fulfill the following essential requirements - <br />
A. Sensor to detect falling <br />
B. Allow user to cancel an alert (as we consider the risk of false trigger might produce unnecessary confusion and burden) <br />
C. Send the alert and communicate with an emergency contact <br />
The following is the color scheme employed to communicate clearly about different states of the system. We are aware that color could be a fantastic facillitator in communication especially in our case when the display is not in a readable size; therefore, we want to use colors to convey and emphasize different meanings.
![P5:Alert](https://github.com/kchen1009/Interactive-Lab-Hub/blob/Fall2021/Final%20Project/Alert.png)
4. Archive of all code, design patterns, etc. used in the final design. (As with labs, the standard should be that the documentation would allow you to recreate your project if you woke up with amnesia.) <br />



5. Video of someone using your project <br />
Video - https://drive.google.com/file/d/1mxeScjrWFT1AI0EFFzXBPnWg3Pgqlleq/view?usp=sharing
6. Reflections on process (What have you learned or wish you knew at the start?) <br />

 One thing we wish we could spend more time doing research on is the user behavior. If we have more time, we'd like to learn more about where/when and all kinds falling situations for elderly people so we could adjust our design accordingly. For instance, if we find out that most falls occur in the bathroom, we would have made the exterior of the device waterproof. For now, since it's still a rough prototype, we decided to go with cardboards because they are affordable and effective. We did tons of experiments and found out that cardboards are pretty durable - we dropped the device to imitate falling, and surprisingly the cardboard itself did not rip at all while holding the pi together.

7. Group work distribution questionnaire

## Change of Design

It is fine to change your project goals, but please resubmit the project plan for the new design when you do that.


## Teams
We are a team of two - Kristy Chen (sc3248) and Ling Zhong (lz555). We designed the interaction together, with Ling further working on the remote communication and the integration of camera and email. Kristy worked on the assembly of the system, scenario testing, and the production of the demo video.

## Examples

[Here is a list of good final projects from previous classes.](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/wiki/Previous-Final-Projects)
This version of the class is very different, but it may be useful to see these.
