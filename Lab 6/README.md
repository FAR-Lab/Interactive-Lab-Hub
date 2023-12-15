# Little Interactions Everywhere

John Li (jl4239), Mingze Gao (mg2454), Crystal Chong (cc2795), Qianxin(Carl) Gan (qg72), Mingzhe Sun (ms3636)


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

1. **Smart Home Control:** Manage various smart home devices such as lights, thermostats, and security cameras with MQTT. Users can publish commands to a topic like "home/livingroom/light/on" to turn on the lights or "home/thermostat/temperature/set/xx" to adjust the temperature, and the corresponding devices would subscribe to these topics to receive and act on the commands.

2. **Wearable Health Monitors:** Use MQTT in wearable devices that monitor health metrics like heart rate, blood pressure, and steps taken. The device can publish this data to a secure topic, which a health app subscribes to in real-time, allowing both the user and healthcare providers to monitor the data for any health alerts.

3. **Industrial IoT Sensors:** In a manufacturing setting, MQTT can be used to connect a network of sensors on the equipment to monitor conditions such as temperature, vibration, location, and humidity. The sensors would publish their data to specific topics that maintenance systems subscribe to, enabling predictive maintenance and quick response to any anomalies.

4. **Interactive Gaming:** In multiplayer gaming environments, MQTT can be used to transmit player actions and game state updates to all connected clients in real-time. By publishing movements or commands to a common game topic, all players can have a synchronized and interactive gaming experience.

5. **Retail Digital Signage:** Retailers can employ MQTT to manage digital signage displays across multiple locations. Updates to advertisements or announcements can be published to topics corresponding to each screen or location, and the displays would subscribe to these topics to receive and show the latest content.

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
![1863bebcbdbf62c78a978a62e0ba37a](https://hackmd.io/_uploads/HkRBDZeNT.jpg)

![f66256a5975f100bfef29f59ede867f](https://hackmd.io/_uploads/Bkky_ZeET.png)




**\*\*\*Pick another part in your kit and try to implement the data streaming with it.\*\*\***

![image](https://hackmd.io/_uploads/BJOJ-MgVT.png)

![image](https://hackmd.io/_uploads/SktLefgE6.png)






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

Click to view the video:
[<img src="https://hackmd.io/_uploads/ryegfKxVa.png">](https://www.youtube.com/watch?v=GXK39LnFhd8)



### Part E
### Make it your own

Find at least one class (more are okay) partner, and design a distributed application together based on the exercise we asked you to do in this lab.

**\*\*\*1. Explain your design\*\*\*** For example, if you made a remote controlled banana piano, explain why anyone would want such a thing.
Design of the Pet Button Puzzle:
The pet button puzzle is ingeniously designed to tap into the natural instincts and intelligence of pets. By pressing different buttons, pets can trigger specific actions: dispensing food, releasing water, or even calling their owner. This design not only incorporates physical activity but also provides cognitive challenges that keep pets engaged. The buttons are made to be durable and responsive, suitable for the varied shapes and strengths of different pets. Additionally, the dispenser is constructed to provide the correct portion sizes for food and water, which is essential for maintaining a healthy pet diet.

Why People Would Want This:
People are increasingly looking for innovative ways to enhance their pets' lives. The pet button puzzle offers a dual benefit. Firstly, it provides mental stimulation for pets, which is crucial for their well-being, especially when they are left alone at home. It can help mitigate issues like separation anxiety and destructive behavior by giving pets a focus and a rewarding activity. Secondly, for pet owners, the puzzle is a convenient tool to ensure their pets are fed and hydrated on time, especially during long work hours or unexpected delays in returning home. It can also be a comforting thought that your pet can, in a way, reach out to you through the system, making it an interactive tool that strengthens the bond between the pet and the owner.

**\*\*\*2. Diagram the architecture of the system.\*\*\*** Be clear to document where input, output and computation occur, and label all parts and connections. For example, where is the banana, who is the banana player, where does the sound get played, and who is listening to the banana music?

Input Devices (Buttons for Interaction):

Food Button: When pressed by the pet, it signals the need to dispense food.
Water Button: When pressed, it signals the release of water.
Call Owner Button: Activates a communication device to alert the owner.
Computation/Processing Unit (Microcontroller/Processor):

Receives input from the buttons.
Processes the input and decides the action to take based on the button pressed.
Sends a signal to the appropriate output device.
Could also be connected to the internet for remote monitoring and notifications.
Output Devices (Mechanisms for Reward and Communication):

Food Dispenser: Activated by the processor to release a predetermined amount of food.
Water Dispenser: Triggered to provide water upon receiving the signal from the processor.
Speaker/Communication Module: Plays a pre-recorded message or sends a signal to the owner's device when the call button is pressed.
Power Supply:

Provides power to the microcontroller, sensors, and actuators.
Connectivity (for Remote Access and Notifications):

Wi-Fi/Bluetooth Module: Connects the system to the internet or a local network, allowing for remote notifications and monitoring by the owner.
User Interface (for Owners):

Mobile App/Web Interface: Allows the owner to monitor activity, change settings, and receive alerts.
Listeners (Pets and Owners):

Pets: The primary listeners to any sound output like clicks or the sound of the food dispenser, which serves as a cue for them.
Owners: Secondary listeners who may receive alerts or calls from the system based on the pet’s interaction with the puzzle.

![536e9b0df88aab70481b120f4b22cfd](https://hackmd.io/_uploads/H1x6NugNp.png)


Network: Connects all components and ensures communication with external devices or the internet.
![IMG_9631](https://hackmd.io/_uploads/ryR1qPl46.png)




**\*\*\*3. Build a working prototype of the system.\*\*\*** Do think about the user interface: if someone encountered these bananas somewhere in the wild, would they know how to interact with them? Should they know what to expect?
![3111699936479_.pic](https://hackmd.io/_uploads/By21Ydg4a.jpg)
**\*\*\*4. Document the working prototype in use.\*\*\*** It may be helpful to record a Zoom session where you should the input in one location clearly causing response in another location.


Click to view the video:
[<img src="https://hackmd.io/_uploads/SJxfWtlN6.png">](https://www.youtube.com/watch?v=-BGFuBviWq4&t=1s)

<!--**\*\*\*5. BONUS (Wendy didn't approve this so you should probably ignore it)\*\*\*** get the whole class to run your code and make your distributed system BIGGER.-->

