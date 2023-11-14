# Little Interactions Everywhere

+ Tingrui（Freya) Zhang - tz428
+ Khiem Pham - dpk45
+ Sissel Sun - rs923

## Prep

1. Pull the new changes from the class interactive-lab-hub. (You should be familiar with this already!)
2. Install [MQTT Explorer](http://mqtt-explorer.com/) on your laptop. If you are using Mac, MQTT Explorer only works when installed from the [App Store](https://apps.apple.com/app/apple-store/id1455214828).
3. Readings before class:
   * [MQTT](#MQTT)
   * [The Presence Table](https://dl.acm.org/doi/10.1145/1935701.1935800) and [video](https://vimeo.com/15932020)


## Overview

The point of this lab is to introduce you to distributed interaction. We have included some Natural Language Processing (NLP) and Generation (NLG) but those are not really the emphasis. Feel free to dig into the examples and play around the code which you can integrate into your projects if wanted. However, we want to emphasize that the grading will focus on your ability to develop interesting uses for messaging across distributed devices. Here are the four sections of the lab activity:

A) [MQTT](#part-a)

B) [Send and Receive on your Pi](#part-b)

C) [Streaming a Sensor](#part-c)

D) [The One True ColorNet](#part-d)

E) [Make It Your Own](#part-)

## Part 1.

### Part A
### MQTT

MQTT is a lightweight messaging portal invented in 1999 for low bandwidth networks. It was later adopted as a defacto standard for a variety of [Internet of Things (IoT)](https://en.wikipedia.org/wiki/Internet_of_things) devices. 

#### The Bits

* **Broker** - The central server node that receives all messages and sends them out to the interested clients. Our broker is hosted on the far lab server (Thanks David!) at `farlab.infosci.cornell.edu/8883`. Imagine that the Broker is the messaging center!
* **Client** - A device that subscribes or publishes information to/on the network.
* **Topic** - The location data gets published to. These are *hierarchical with subtopics*. For example, If you were making a network of IoT smart bulbs this might look like `home/livingroom/sidelamp/light_status` and `home/livingroom/sidelamp/voltage`. With this setup, the info/updates of the sidelamp's `light_status` and `voltage` will be store in the subtopics. Because we use this broker for a variety of projects you have access to read, write and create subtopics of `IDD`. This means `IDD/ilan/is/a/goof` is a valid topic you can send data messages to.
*  **Subscribe** - This is a way of telling the client to pay attention to messages the broker sends out on the topic. You can subscribe to a specific topic or subtopics. You can also unsubscribe. Following the previouse example of home IoT smart bulbs, subscribing to `home/livingroom/sidelamp/#` would give you message updates to both the light_status and the voltage.
* **Publish** - This is a way of sending messages to a topic. Again, with the previouse example, you can set up your IoT smart bulbs to publish info/updates to the topic or subtopic. Also, note that you can publish to topics you do not subscribe to. 


**Important note:** With the broker we set up for the class, you are limited to subtopics of `IDD`. That is, to publish or subcribe, the topics will start with `IDD/`. Also, setting up a broker is not much work, but for the purposes of this class, you should all use the broker we have set up for you!


#### Useful Tooling

Debugging and visualizing what's happening on your MQTT broker can be helpful. We like [MQTT Explorer](http://mqtt-explorer.com/). You can connect by putting in the settings from the image below.


![input settings](imgs/mqtt_explorer.png?raw=true)


Once connected, you should be able to see all the messages under the IDD topic. , go to the **Publish** tab and try publish something! From the interface you can send and plot messages as well. Remember, you are limited to subtopics of `IDD`. That is, to publish or subcribe, the topics will start with `IDD/`.


<img width="1026" alt="Screen Shot 2022-10-30 at 10 40 32 AM" src="https://user-images.githubusercontent.com/24699361/198885090-356f4af0-4706-4fb1-870f-41c15e030aba.png">



### Part B
### Send and Receive on your Pi

[sender.py](./sender.py) and and [reader.py](./reader.py) show you the basics of using the mqtt in python. Let's spend a few minutes running these and seeing how messages are transferred and shown up. Before working on your Pi, keep the connection of `farlab.infosci.cornell.edu/8883` with MQTT Explorer running on your laptop.

**Running Examples on Pi**

* Install the packages from `requirements.txt` under a virtual environment:

  ```
  pi@raspberrypi:~/Interactive-Lab-Hub $ source circuitpython/bin/activate
  (circuitpython) pi@raspberrypi:~/Interactive-Lab-Hub $ cd Lab\ 6
  (circuitpython) pi@raspberrypi:~/Interactive-Lab-Hub/Lab 6 $ pip install -r requirements.txt
  ...
  ```
* Run `sender.py`, fill in a topic name (should start with `IDD/`), then start sending messages. You should be able to see them on MQTT Explorer.

  ```
  (circuitpython) pi@raspberrypi:~/Interactive-Lab-Hub/Lab 6 $ python sender.py
  >> topic: IDD/AlexandraTesting
  now writing to topic IDD/AlexandraTesting
  type new-topic to swich topics
  >> message: testtesttest
  ...
  ```
* Run `reader.py`, and you should see any messages being published to `IDD/` subtopics. Type a message inside MQTT explorer and see if you can receive it with `reader.py`.

  ```
  (circuitpython) pi@raspberrypi:~ Interactive-Lab-Hub/Lab 6 $ python reader.py
  ...
  ```

<img width="890" alt="Screen Shot 2022-10-30 at 10 47 52 AM" src="https://user-images.githubusercontent.com/24699361/198885135-a1d38d17-a78f-4bb2-91c7-17d014c3a0bd.png">


**\*\*\*Consider how you might use this messaging system on interactive devices, and draw/write down 5 ideas here.\*\*\***
1. Apple "Ready to Eat" Sensor
  We can use sensors to determine if an apple, or potentially any fruit, is ripe and ready to eat. Multiple sensors can be integrated into our system, such as firmness, color, and perhaps ethylene emission (a gas emitted by ripening fruit). The sensor data would be transmitted using MQTT to a smartphone app or a central monitoring system. When the apple reaches its optimal ripeness, a notification is sent to the user. 
2. Interactive Scavenger Hunt
  In this interactive game, participants are engaged in a scavenger or treasure hunt where they must find hidden objects in certain locations. Players can send inquiries about their current location. In response, the game host (an automated system based on pi) will use MQTT to send back hints, such as the distance to the nearest clue or the direction they should head. The game can be integrated with GPS or RFID technologies. 
3. Vault Protector with Proximity Detection
  This idea is a security system designed to protect valuables in a safe or vault. It would use motion sensors to detect if someone is approaching or tampering with the vault. Upon detecting unauthorized presence or tampering, the system would immediately send an alert via MQTT to the owner's smartphone or security center. This can be paired with other security measures like cameras or alarms.
4. Improvisation and Recording Music Notation
  This system is designed to capture and record music as it is being improvised. While a musician plays, the system would accurately record each note, its timing, duration, and dynamics. For instance, sensors on a piano could detect which keys are pressed and for how long. The data from these sensors would be transmitted in real-time using MQTT to a software application that converts this data into standard music notation. This notation could then be displayed or saved for future reference.
5. Time-Lapse Photography
  Time-lapse photography involves taking sequences of photos at set intervals to capture changes that occur slowly over time. When played back at normal speed, time appears to be moving faster. Cameras equipped with sensors can be programmed to take photos at specific intervals. Additional sensors might measure environmental conditions like light or temperature, triggering the camera to capture images under certain conditions. The camera or sensor system could use MQTT to send status updates or images to a central system for processing and storage. This allows for remote monitoring and control of the time-lapse process.
6. Telegram Sender/Receiver Morse Code
  This idea revolves around a system that can send and receive messages in Morse code using the Telegram messaging platform. Morse code involves sending messages through a series of dots and dashes. The system would involve a button for inputting Morse code and a mechanism to convert Morse code into text, and vice versa. To send messages, a user could input Morse code manually, which would then be translated into text and sent via MQTT. 

### Part C
### Streaming a Sensor

We have included an updated example from [lab 4](https://github.com/FAR-Lab/Interactive-Lab-Hub/tree/Fall2021/Lab%204) that streams the [capacitor sensor](https://learn.adafruit.com/adafruit-mpr121-gator) inputs over MQTT. 

Plug in the capacitive sensor board with the Qwiic connector. Use the alligator clips to connect a Twizzler (or any other things you used back in Lab 4) and run the example script:

<p float="left">
<img src="https://cdn-learn.adafruit.com/assets/assets/000/082/842/large1024/adafruit_products_4393_iso_ORIG_2019_10.jpg" height="150" />
<img src="https://cdn-shop.adafruit.com/970x728/4210-02.jpg" height="150">
<img src="https://cdn-learn.adafruit.com/guides/cropped_images/000/003/226/medium640/MPR121_top_angle.jpg?1609282424" height="150"/>
<img src="https://media.discordapp.net/attachments/679721816318803975/823299613812719666/PXL_20210321_205742253.jpg" height="150">
</p>

 ```
 (circuitpython) pi@raspberrypi:~ Interactive-Lab-Hub/Lab 6 $ python distributed_twizzlers_sender.py
 ...
 ```

**\*\*\*Include a picture of your setup here: what did you see on MQTT Explorer?\*\*\***

![twizzler](twizzler.png)
On MQTT Explorer, there's a message "Twizzler 5 touched!"

**\*\*\*Pick another part in your kit and try to implement the data streaming with it.\*\*\***

![keypad](keypad.png)
We picked the numpad. Once a button is pressed, the message of corresponding button would appear on the MQTT Explorer. The picture shows an example where '5' is pressed. 


### Part D
### The One True ColorNet

It is with great fortitude and resilience that we shall worship at the altar of the *OneColor*. Through unity of the collective RGB, we too can find unity in our heart, minds and souls. With the help of machines, we can overthrow the bourgeoisie, get on the same wavelength (this was also a color pun) and establish [Fully Automated Luxury Communism](https://en.wikipedia.org/wiki/Fully_Automated_Luxury_Communism).

The first step on the path to *collective* enlightenment, plug the [APDS-9960 Proximity, Light, RGB, and Gesture Sensor](https://www.adafruit.com/product/3595) into the [MiniPiTFT Display](https://www.adafruit.com/product/4393). You are almost there!

<p float="left">
  <img src="https://cdn-learn.adafruit.com/assets/assets/000/082/842/large1024/adafruit_products_4393_iso_ORIG_2019_10.jpg" height="150" />
  <img src="https://cdn-shop.adafruit.com/970x728/4210-02.jpg" height="150">
  <img src="https://cdn-shop.adafruit.com/970x728/3595-03.jpg" height="150">
</p>


The second step to achieving our great enlightenment is to run `color.py`. We have talked about this sensor back in Lab 2 and Lab 4, this script is similar to what you have done before! Remember to activate the `circuitpython` virtual environment you have been using during this semester before running the script:

 ```
 (circuitpython) pi@raspberrypi:~ Interactive-Lab-Hub/Lab 6 $ systemctl stop mini-screen.service
 (circuitpython) pi@raspberrypi:~ Interactive-Lab-Hub/Lab 6 $ python color.py
 ...
 ```

By running the script, wou will find the two squares on the display. Half is showing an approximation of the output from the color sensor. The other half is up to the collective. Press the top button to share your color with the class. Your color is now our color, our color is now your color. We are one.

(A message from the previous TA, Ilan: I was not super careful with handling the loop so you may need to press more than once if the timing isn't quite right. Also, I haven't load-tested it so things might just immediately break when everyone pushes the button at once.)

**\*\*\*Can you set up the script that can read the color anyone else publish and display it on your screen?\*\*\***
![Color](color.png)

### Part E
### Make it your own

Find at least one class (more are okay) partner, and design a distributed application together based on the exercise we asked you to do in this lab.

**\*\*\*1. Explain your design\*\*\*** For example, if you made a remote controlled banana piano, explain why anyone would want such a thing.

We create a remote controlled camera system. Everyone who subscribes to our MQTT topic can control the camera i.e. take a picture, the camera being in a remote location. This has uses in home monitoring systems, where a homeowner wants to see who is currently in his house or what is happening in his house at the moment he is at work. However, our main goal is to allow everyone to control the camera: this is similar to an audience controlling what a livestreamer does.

**\*\*\*2. Diagram the architecture of the system.\*\*\*** Be clear to document where input, output and computation occur, and label all parts and connections. For example, where is the banana, who is the banana player, where does the sound get played, and who is listening to the banana music?

The pi with the camera is at a fixed location e.g. at a house, looking at Queens Bridge, at a busy NYC corner… The controller can be in any remote location and with access to the topic. The controller sends a message to the MQTT server, and the pi takes the picture.

![Diagram](diagram.png)

**\*\*\*3. Build a working prototype of the system.\*\*\*** Do think about the user interface: if someone encountered these bananas somewhere in the wild, would they know how to interact with them? Should they know what to expect?

Our cameras are meant to be left alone 🙂. Practically, we hide them from view, so that no stranger will mess with them.

Our working prototype is a first step towards EarthCam, where users can view the streaming of the camera and record or take a picture of their own choice. However, images and videos are too large to send over MQTT, which is a setback we plan to solve in the future.

**\*\*\*4. Document the working prototype in use.\*\*\*** It may be helpful to record a Zoom session where you should the input in one location clearly causing response in another location.

[Demo Video](https://drive.google.com/file/d/12y5nXuxuGaV1omgSj9smJseexG77miK2/view?usp=sharing)

<!--**\*\*\*5. BONUS (Wendy didn't approve this so you should probably ignore it)\*\*\*** get the whole class to run your code and make your distributed system BIGGER.-->

