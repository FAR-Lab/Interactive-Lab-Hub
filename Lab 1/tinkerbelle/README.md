# Tinkerbelle

Tinkerbelle is a simple tool for prototyping interaction, using a phone as a web-controlled smart light. 

You can control it via the web interface or using any software that can connect to a websocket. In the Python folder you will find a simple example that demonstrates a color gradient.

## Installation

This uses a python webserver called Flask. 
You should have [Python3 installed](https://realpython.com/installing-python/).

<!--To install flask in a virtual environment:
```
$ sudo pip3 install virtualenv
$ virtualenv tinkerbelle
$ cd tinkerbelle
$ source bin/activate
```-->

Now clone this repo to download the python code that serves up the flask page.

```
$ git clone https://github.com/FAR-Lab/tinkerbelle.git
$ cd tinkerbelle
$ pip3 install -r requirements.txt
```

## Getting started
Run the tinker.py code, which serves up a webpage

```
$ python3 tinker.py
 * Restarting with stat
access at http://localhost:5000
 * Debugger is active!
 * Debugger PIN: 192-305-172
connected
```

Open the browser with [http://localhost:5000](http://localhost:5000)

#### On a mobile device
Make sure you are connected to the same network as the computer you are running the web-server. Turn your brightness and volume to full. In your phone settings, set the screen to never shut off or lock. On the phone browser navigate to whatever ip address is printed out in the console. In this case that would be `http://[yourIPaddress]:5000`

There should be two buttons. Selecting tinkerbell should full screen the webpage and fade out the buttons.

![mobile screen](/imgs/phone1.png)

#### On a computer
Navigate to the ip address shown in terminal `http://[yourIPaddress]:5000` or if using the same computer as the web-server `http://localhost:5000`.

Select [Jane Wren](https://en.wikipedia.org/wiki/Tinker_Bell#On_stage) for the controller. 

![control interface](/imgs/controller.png)

Here changing the color on the color selector will change the background for both the control interface and the tinker-belle device.

You can change the swatches shown at the bottom of the color selector by editing lines 39 to 54 in `public/index.js` and restarting the web-server.

```
swatches: [
        'rgba(255, 255, 255, 1)',
        'rgba(244, 67, 54, 1)',
        'rgba(233, 30, 99, 1)',
        'rgba(156, 39, 176, 1)',
        'rgba(103, 58, 183, 1)',
        'rgba(63, 81, 181, 1)',
        'rgba(33, 150, 243, 1)',
        'rgba(3, 169, 244, 1)',
        'rgba(0, 188, 212, 1)',
        'rgba(0, 150, 136, 1)',
        'rgba(76, 175, 80, 1)',
        'rgba(139, 195, 74, 1)',
        'rgba(205, 220, 57, 1)',
        'rgba(255, 235, 59, 1)',
        'rgba(255, 193, 7, 1)',
        'rgba(0, 0, 0, 1)',
      ],
```

Typing a description in the Audio input box will play the first result from [https://freesound.org/](https://freesound.org/). The stop button stops playback. Try typing `gong` or `barking`.
