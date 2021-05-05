# m[Q](https://en.wikipedia.org/wiki/QAnon)tt[Anon](https://en.wikipedia.org/wiki/QAnon): Where We Go One, We Go All

## Prep

1. Pull the new changes
2. Install [MQTT Explorer](http://mqtt-explorer.com/)
3. Readings 
   * [MQTT](#MQTT)
   * [The Presence Table](https://dl.acm.org/doi/10.1145/1935701.1935800) and [video](https://vimeo.com/15932020)


## Introduction

The point of this lab is to introduce you to distributed interaction. We've included a some Natural Language Processing (NLP) and Generation (NLG) but those are not really the emphasis. Feel free to dig into the examples and play around the code which you can integrate into your projects. However we want to emphasize the grading will focus on your ability to develop interesting uses for messaging across distributed devices. 

## MQTT

MQTT is a lightweight messaging portal invented in 1999 for low bandwidth networks. It was later adopted as a defacto standard for a variety of Internet of Things (IoT) devices. 

### The Bits

* **Broker** - The central server node that receives all messages and sends them out to the interested clients. Our broker is hosted on the far lab server (Thanks David!) at `farlab.infosci.cornell.edu/8883`
* **Client** - A device that subscribes or publishes information on the network
* **Topic** - The location data gets published to. These are hierarchical with subtopics. If you were making a network of IoT smart bulbs this might look like `home/livingroom/sidelamp/light_status` and `home/livingroom/sidelamp/voltage`. Subscribing to `home/livingroom/sidelamp/#` would give you message updates to both the light_status and the voltage. Because we use this broker for a variety of projects you have access to read, write and create subtopics of `IDD`. This means `IDD/ilan/is/a/goof` is a valid topic you can send data messages to.
*  **Subscribe** - This is a way of telling the client to pay attention to messages the broker sends out on that topic. You can subscribe to a specific topic or subtopics. You can also unsubscribe
* **Publish** - This is a way of sending messages to a topic. You can publish to topics you don't subscribe to. Just remember on our broker you are limited to subtopics of `IDD`

Setting up a broker isn't much work but for the purposes of this class you should all use the broker we've set up for you. 

### Useful Tooling

Debugging and visualizing what's happening on your MQTT broker can be helpful. We like [MQTT Explorer](http://mqtt-explorer.com/). You can connect by putting in the settings from the image below.



![input settings](https://github.com/FAR-Lab/Interactive-Lab-Hub/blob/Spring2021/Lab%206/imgs/mqtt_explorer.png?raw=true)



Once connected you should be able to see all the messaged on the IDD topic. From the interface you can send and plot messages as well.



## Send and Receive 

[sender.py](./sender.py) and and [reader.py](./reader.py) show you the basics of using the mqtt in python.  Lets spend a few minutes running these and seeing how messages are transferred and show up. 

**Running Examples**

* Install the packages from `requirements.txt`, ideally in a python environment. We've been using the circuitpython environment we setup earlier this semester. To install them do `pip install -r requirements.txt`
* to run `sender.py` type `python sender.py` and fill in a topic name, then start sending messages. You should see them on MQTT Explorer
* to run `reader.py` type `python reader.py` and you should see any messages being published to `IDD/` subtopics.

## Streaming a Sensor

We've included an updated example from [lab 4](https://github.com/FAR-Lab/Interactive-Lab-Hub/tree/Spring2021/Lab%204) that streams sensor inputs over MQTT. Feel free to poke around with it!

## The One True ColorNet

It is with great fortitude and resilience that we shall worship at the altar of the *OneColor*. Through unity of the collective RGB we too can find unity in our heart, minds and souls. With the help of machines can  overthrow the bourgeoisie, get on the same wavelength (this was also a color pun) and establish [Fully Automated Luxury Communism](https://en.wikipedia.org/wiki/Fully_Automated_Luxury_Communism).

The first step on the path to *collective* enlightenment, plug the [APDS-9960 Proximity, Light, RGB, and Gesture Sensor](https://www.adafruit.com/product/3595) into the [Pi Display](https://www.adafruit.com/product/4393).

<img src="https://cdn-shop.adafruit.com/970x728/3595-03.jpg" height="300">

You are almost there!

The second step to achieving our great enlightenment is to run `python color.py`

You will find the two squares on the display. Half is showing an approximation of the output from the color sensor. The other half is up to the collective. Press the top button to share your color with the class. Your color is now our color, our color is now your color. We are one. 

I was not super careful with handling the loop so you may need to press more than once if the timing isn't quite right. Also I have't load tested it so things might just immediately break when every pushes the button at once.

You may ask "but what if I missed class?"

Am I not admitted into the collective enlightenment of the *OneColor*?

Of course not! You can got to [https://one-true-colornet.glitch.me/](https://one-true-colornet.glitch.me/) and become one with the ColorNet on the inter-webs.

Glitch is a great tool for prototyping sites, interfaces and web-apps that's worth taking some time to get familiar with if you have a chance. Its not super pertinent for the class but good to know either way. 



## Make it your own

Find at least one class (more are okay) partner, and design a distributed application together. 

**1. Explain your design** For example, if you made a remote controlled banana piano, explain why anyone would want such a thing.

The device aims to hold project partners accountable when working on a group assignment together. It will allow partners to communicate with each other by sending updates on each team member’s progress. The device will also track how much time each person has spent on the project and allow team members to send “Hurry up, don’t slack off!” messages to each other. After the project is finished, the device will announce the winner of the game as the person who slacked off the least (finished their part of the project in the shortest amount of time). 

The overall goal was to build something that could act as more casual than email but more formal than text; a messaging medium that lies somewhere between these two, like a picture frame that sits on a table and is updated from time to time with some semi-important message. Often times text is too fleeting to let the importance of a message sink in, and email seems to miss a level of freedom and play. So we created a messaging system on RPi + TFT, with MQTT and Mozilla DeepSpeech.

There are several features not fully implemented in the following storyboard, such as score keeping, but the principal idea was helpful for guiding the build of the project and conveying the purpose of the device.

Below are our brainstorming notes/storyboard: 

![](brainstorm6.1.png)
![](brainstorm6.2.png)
![](storyboard6.1.png)
![](storyboard6.2.png)

This overall interaction is shown in the first half of the video. 

**2. Diagram the architecture of the system.** Be clear to document where input, output and computation occur, and label all parts and connections. For example, where is the banana, who is the banana player, where does the sound get played, and who is listening to the banana music?

In the storyboard, Player 1 presses the start button to begin the game/start the timer in the system. After they complete the first part of the project, Player 1 will record their updates by pressing the red button. When the message has been recorded, Player 2, using their own device, will receive the message delivered to their pi and play the message using the green button. Player 2 will then complete the second part of the project and record their updates using the red button, which will prompt Player 1 to begin the third part after listening to Player 2’s updates by pressing the green button. This interaction will go on until one of the player presses the finish button, stopping the timer. The total amount of time each player spends working (time between pressing initial button (start button in first iteration or green play button in future iteration) to recording their update, added up) will be compared to each other, and the person who spends the least amount of time on the project will be deemed the winner “who slacked the least.” 

The architecture starts with Mozilla DeepSpeech for SST, this is then linked to a button on the RPi TFT so that a button triggers the stream and the stream ends after some set amount of time. The text is then stored in a text file, and the content of that text file are sent to Topic 1 in MQTT by Client 1. Client 2 running a duplicate system is subscribed to Topic 1, and receives the message that Cleint 1 sent. Client 2 plays this message using button 2 on the TFT. Inversely, Client 1 is subscribed to Topic 2, and they can read messages sent with button 2. The TFT displays these messages in descending order of time received, with the time received followed by the message. These text messages are shown as a preview on the TFT and when selected to be played, are run through pyttsx3.

**3. Build a working prototype of the system.** Do think about the user interface: if someone encountered these bananas, would they know how to interact with them? Should they know what to expect?

Below is the device apparatus. The top button is pressed to record a message that will be transcribed into text and delivered to the second raspberry pi. The bottom button is pressed to listen to the message sent by the other user: 
![](deviceapparatus6.png)

**4. Document the working prototype in use.** It may be helpful to record a Zoom session where you should the input in one location clearly causing response in another location.

Vince using the device and recording a message:
![](vinceusingsystem.png)

Capturing the speech to text stream through Deep Speech required an understanding of how the stream worked, where microphone stream data is treated in time frames. An example script provided by Mozilla was modified and imported in the script that handles mqtt and tft control, and set to run for ~10 seconds.
There is an un-implemented feature for clearing the DeepSpeech cache -- as it is, the memory cache only allows for 5 speech to text iterations before it cannot write to memory. This limitation is an example of some of the unweildy features of connecting DeepSpeech with MQTT, where we are essentially funneling a large SST task into a MQTT logs that are optimized for quick data tranfer.

There was also a lot of messing with the display text so that it would show as a clean log on the TFT. Adding EB Garamond as a font really helped with legibility and spacing between messages. Also, because showing timestamps for messages seemed like an important feature for the multiple users, and because mqtt does not inherently provide log data, there was the need to manually log time at the mqtt publish stage. This manually logged time then needs to be regex'ed out so that the message is speakable by pyttsx3.

There is an additional incomplete feature of not hardcoding client 1 and 2 and topic 1 and 2, but allowing a user to set these as arguments at command line via parser. e.g. python3.7 tester.py -client Vince -topic Rui; meaning I publish to the topic Vince and subscribe to the topic Rui. This would make it so many people could for example subscribe to a single topic, creating a network of mqtt messaging clients. This was partially implemented but is left incomplete for the purposes of this lab.

One of the most interesting results of this prototype system was finding how much microphone quality impacts transcription. The included mic was almost entirely noise to dspeech, a little bit of tuning may have improved results, but this tuning is not realistic for scaling to many devices and clients, unless the devices are uniform. So for this lab no parameter tuning was done. An earbud microphone worked better than the default rpi mic, picking up longer messages, and a stage microphone worked far better than the rest. The suggests that native audio isolation found in a high quality mic might be key to off-line speech to text.

[Video Link](https://drive.google.com/file/d/1LrZzyW5d5auMs_47vhyaIRIryTkDqJ-P/view?usp=sharing)

**5. BONUS (Wendy didn't approve this so you should probably ignore it)** get the whole class to run your code and make your distributed system BIGGER.
