# Punny title goes here



## Prep

1. Pull the new changes
2. Install [MQTT Explorer](http://mqtt-explorer.com/)
3. Readings 
   * [MQTT](#MQTT)
   * [The Presence Table](https://dl.acm.org/doi/10.1145/1935701.1935800) and [video](https://vimeo.com/15932020)
   * 

## Introduction

The point of this lab is to introduce you to distributed interaction. We've included a some Natural Language Processing (NLP) and Generation (NLG) but those are not really the emphasis. Feel free to dig into the examples and play around the code which you can integrate into your projects. However we want to emphasize the grading will focus on your ability to develop interesting uses for messaging across distributed devices. 



## MQTT

MQTT is a lightweight messaging portal invented in 1999 for low bandwidth networks. It was later adopted as a defacto standard for a variety of Internet of Things (IoT) devices. 

#### The Bits

* **Broker** - The central server node that receives all messages and sends them out to the interested clients. Our broker is hosted on the far lab server (Thanks David!) at `farlab.infosci.cornell.edu/8883`
* **Client** - A device that subscribes or publishes information on the network
* **Topic** - The location data gets published to. These are hierarchical with subtopics. If you were making a network of IoT smart bulbs this might look like `home/livingroom/sidelamp/light_status` and `home/livingroom/sidelamp/voltage`. Subscribing to `home/livingroom/sidelamp/#` would give you message updates to both the light_status and the voltage. Because we use this broker for a variety of projects you have access to read, write and create subtopics of `IDD`. This means `IDD/ilan/is/a/goof` is a valid topic you can send data messages to.
*  **Subscribe** - This is a way of telling the client to pay attention to messages the broker sends out on that topic. You can subscribe to a specific topic or subtopics. You can also unsubscribe
* **Publish** - This is a way of sending messages to a topic. You can publish to topics you don't subscribe to. Just remember on our broker you are limited to subtopics of `IDD`

Setting up a broker isn't much work but for the purposes of this class you should all use the broker we've set up for you. 

#### Useful Tooling

Debugging and visualizing what's happening on your MQTT broker can be helpful. We like [MQTT Explorer](http://mqtt-explorer.com/). You can connect by putting in the settings from the image below.



![input settings](/Users/ilanmandel/Documents/IDD/Interactive-Lab-Hub/Lab 6/imgs/mqtt_explorer.png)



Once connected you should be able to see all the messaged on the IDD topic. From the interface you can send and plot messages as well.

## Internet of Cornell Tech Things 

You will join a network of loosely networked Cornell Tech Things, which use the MQTT to communicate to one another. For the first step in this, we will build a simple client-server between your computer and your Interaction Engine. (Use the ``HelloThere`` and ``HelloFromHere`` code samples to do this!)

```
### Important side note
The ``HelloThere`` and ``HelloFromHere`` examples are used to use an MQTT server/broker that is no longer active. In order to test and experiment with these examples please use the ```mqtt.eclipse.org``` address.

Set up your Arduino so that it can control an RGB LED and read input from a button.
```

Now, change the code for your Interaction Engine so that you can set different buttons on a remote webpage that change the color of the RGB LED. Also, set it so that you can press a button to change the background color on the webpage. (Again, the ``HelloThere`` and ``HelloFromHere`` code samples show you how to communicate with a MQTT server. Merge the code from those samples into your interaction engine code to control the light and to send messages based on the button press.)

Now we will modify our Interaction Engine to send messages to a MQTT server/broker.  

When you start your MQTT client, you will specify “your color”. When you press your button, the client will send this color to the MQTT server, and all the other devices on the server will change their LEDs this color. 

We will use ```mqtt.eclipse.org```, channel IxE for a MQTT server/broker for the course. The TA [has set up a web camera with her devices being broadcast](http://farlab.infosci.cornell.edu:8081) so that you can see if your actions change the LED of her Thing. You should be able to press your button and see the remote LED change to your color. On the remote webpage, you should be able to press a color button and see it show up on your LED.

When everyone in the class is connected to the server, everyone will be able to push their color out to everyone else’s Things by pressing their own buttons.

Technical specification:
```
MQTT_boker: mqtt.eclipse.org 
Topic: ixe/
Acceptable messages (string): 'red' || 'green' || 'blue' (more to be added later)
```

## Make it your own

Find at least one class partner, and design a distributed application together. 

**1. Explain your design** For example, if you made a remote controlled banana piano, explain why anyone would want such a thing.

**2. Diagram the architecture of the system.** Be clear to document where input, output and computation occur, and label all parts and connections. For example, where is the banana, who is the banana player, where does the sound get played, and who is listening to the banana music?

**3. Build a working prototype of the system.** Do think about the user interface: if someone encountered these bananas, would they know how to interact with them? Should they know what to expect?

**4. Document the working prototype in use.** It may be helpful to record a Zoom session where you should the input in one location clearly causing response in another location.
