# Observant Systems


For lab this week, we focus on creating interactive systems that can detect and respond to events or stimuli in the environment of the Pi, like the Boat Detector we mentioned in lecture. 
Your **observant device** could, for example, count items, find objects, recognize an event or continuously monitor a room.

This lab will help you think through the design of observant systems, particularly corner cases that the algorithms needs to be aware of.

## Prep

1.  Pull the new Github Repo.
2.  Install VNC on your laptop if you have not yet done so. This lab will actually require you to run script on your Pi through VNC so that you can see the video stream. Please refer to the [prep for Lab 2](https://github.com/FAR-Lab/Interactive-Lab-Hub/blob/Fall2021/Lab%202/prep.md), we offered the instruction at the bottom.
3.  Read about [OpenCV](https://opencv.org/about/), [MediaPipe](https://mediapipe.dev/), and [TeachableMachines](https://teachablemachine.withgoogle.com/).
4.  Read Belloti, et al.'s [Making Sense of Sensing Systems: Five Questions for Designers and Researchers](https://www.cc.gatech.edu/~keith/pubs/chi2002-sensing.pdf).

### For the lab, you will need:

1. Raspberry Pi
1. Webcam 
1. Microphone (if you want to have speech or sound input for your design)

### Deliverables for this lab are:
1. Show pictures, videos of the "sense-making" algorithms you tried.
1. Show a video of how you embed one of these algorithms into your observant system.
1. Test, characterize your interactive device. Show faults in the detection and how the system handled it.

## Overview
Building upon the paper-airplane metaphor (we're understanding the material of machine learning for design), here are the four sections of the lab activity:

A) [Play](#part-a)

B) [Fold](#part-b)

C) [Flight test](#part-c)

D) [Reflect](#part-d)

---

### Part A
### Play with different sense-making algorithms.

#### OpenCV
A more traditional method to extract information out of images is provided with OpenCV. The RPI image provided to you comes with an optimized installation that can be accessed through python. We included 4 standard OpenCV examples: contour(blob) detection, face detection with the ``Haarcascade``, flow detection (a type of keypoint tracking), and standard object detection with the [Yolo](https://pjreddie.com/darknet/yolo/) darknet.

Most examples can be run with a screen (e.g. VNC or ssh -X or with an HDMI monitor), or with just the terminal. The examples are separated out into different folders. Each folder contains a ```HowToUse.md``` file, which explains how to run the python example. 

Following is a nicer way you can run and see the flow of the `openCV-examples` we have included in your Pi. Instead of `ls`, the command we will be using here is `tree`. [Tree](http://mama.indstate.edu/users/ice/tree/) is a recursive directory colored listing command that produces a depth indented listing of files. Install `tree` first and `cd` to the `openCV-examples` folder and run the command:

```shell
pi@ixe00:~ $ sudo apt install tree
...
pi@ixe00:~ $ cd openCV-examples
pi@ixe00:~/openCV-examples $ tree -l
.
├── contours-detection
│   ├── contours.py
│   └── HowToUse.md
├── data
│   ├── slow_traffic_small.mp4
│   └── test.jpg
├── face-detection
│   ├── face-detection.py
│   ├── faces_detected.jpg
│   ├── haarcascade_eye_tree_eyeglasses.xml
│   ├── haarcascade_eye.xml
│   ├── haarcascade_frontalface_alt.xml
│   ├── haarcascade_frontalface_default.xml
│   └── HowToUse.md
├── flow-detection
│   ├── flow.png
│   ├── HowToUse.md
│   └── optical_flow.py
└── object-detection
    ├── detected_out.jpg
    ├── detect.py
    ├── frozen_inference_graph.pb
    ├── HowToUse.md
    └── ssd_mobilenet_v2_coco_2018_03_29.pbtxt
```

The flow detection might seem random, but consider [this recent research](https://cseweb.ucsd.edu/~lriek/papers/taylor-icra-2021.pdf) that uses optical flow to determine busy-ness in hospital settings to facilitate robot navigation. Note the velocity parameter on page 3 and the mentions of optical flow.

Now, connect your webcam to your Pi and use **VNC to access to your Pi** and open the terminal. Use the following command lines to try each of the examples we provided:
(***it will not work if you use ssh from your laptop***)

```
pi@ixe00:~$ cd ~/openCV-examples/contours-detection
pi@ixe00:~/openCV-examples/contours-detection $ python contours.py
...
pi@ixe00:~$ cd ~/openCV-examples/face-detection
pi@ixe00:~/openCV-examples/face-detection $ python face-detection.py
...
pi@ixe00:~$ cd ~/openCV-examples/flow-detection
pi@ixe00:~/openCV-examples/flow-detection $ python optical_flow.py 0 window
...
pi@ixe00:~$ cd ~/openCV-examples/object-detection
pi@ixe00:~/openCV-examples/object-detection $ python detect.py
```

**\*\*\*Try each of the following four examples in the `openCV-examples`, include screenshots of your use and write about one design for each example that might work based on the individual benefits to each algorithm.\*\*\*** <br />
![P1:example](https://github.com/kchen1009/Interactive-Lab-Hub/blob/Fall2021/Lab%205/images/Example1.png)
Contour Deetection can be used integrated within license plate reader to capture license plate number. This kind of plate reader design would be particularly useful at parking lots as it could prevent manual input of plate number at a kiosk. The integrated system could simply detect whether there is a license plate on a car and what the number is.
![P2:example](https://github.com/kchen1009/Interactive-Lab-Hub/blob/Fall2021/Lab%205/images/Example2.png)
Facial Detection can be implemented to identify if there is a human face present. A design I think of is to integrate facial detection algorithm into a smart mirror, so when a human face is identified, the mirror could start displaying weather or calendar information.
![P3:example](https://github.com/kchen1009/Interactive-Lab-Hub/blob/Fall2021/Lab%205/images/Example3.png)
Flow Detection can be used to determine how heavy the traffic is by detecting flow points and tracking motion of cars on a freeway.
![P4:example](https://github.com/kchen1009/Interactive-Lab-Hub/blob/Fall2021/Lab%205/images/Example4.png)
Object Detection can be applied widely. I think it'd be cool to integrate object detection within a pet camera. The purpose of the design is to notify users when their pets are at the front of the camera, so users wouldn't need to constantly check whether their pets have come nearby or not.

#### MediaPipe

A more recent open source and efficient method of extracting information from video streams comes out of Google's [MediaPipe](https://mediapipe.dev/), which offers state of the art face, face mesh, hand pose, and body pose detection.

![Alt Text](mp.gif)

To get started, create a new virtual environment with special indication this time:

```
pi@ixe00:~ $ virtualenv mpipe --system-site-packages
pi@ixe00:~ $ source mpipe/bin/activate
(mpipe) pi@ixe00:~ $ 
```

and install the following.

```
...
(mpipe) pi@ixe00:~ $ sudo apt install ffmpeg python3-opencv
(mpipe) pi@ixe00:~ $ sudo apt install libxcb-shm0 libcdio-paranoia-dev libsdl2-2.0-0 libxv1  libtheora0 libva-drm2 libva-x11-2 libvdpau1 libharfbuzz0b libbluray2 libatlas-base-dev libhdf5-103 libgtk-3-0 libdc1394-22 libopenexr23
(mpipe) pi@ixe00:~ $ pip3 install mediapipe-rpi4 pyalsaaudio
```

Each of the installs will take a while, please be patient. After successfully installing mediapipe, connect your webcam to your Pi and use **VNC to access to your Pi**, open the terminal, and go to Lab 5 folder and run the hand pose detection script we provide:
(***it will not work if you use ssh from your laptop***)


```
(mpipe) pi@ixe00:~ $ cd Interactive-Lab-Hub/Lab\ 5
(mpipe) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ python hand_pose.py
```

Try the two main features of this script: 1) pinching for percentage control, and 2) "[Quiet Coyote](https://www.youtube.com/watch?v=qsKlNVpY7zg)" for instant percentage setting. Notice how this example uses hardcoded positions and relates those positions with a desired set of events, in `hand_pose.py` lines 48-53. 

**\*\*\*Consider how you might use this position based approach to create an interaction, and write how you might use it on either face, hand or body pose tracking.\*\*\*** <br />
An interaction I have in mind is to allow users to control music player with hand pose. Instead of pressing a "previous button", users could request for the previous track by point their index finger to the left. If they'd like to play the next track, they could also point their index finger to the right. When they want to stop playing, users could hold palm against camera. On the other hand, if they'd like the player to start playing, they could thumb up to signal the device.

(You might also consider how this notion of percentage control with hand tracking might be used in some of the physical UI you may have experimented with in the last lab, for instance in controlling a servo or rotary encoder.)



#### Teachable Machines
Google's [TeachableMachines](https://teachablemachine.withgoogle.com/train) might look very simple. However, its simplicity is very useful for experimenting with the capabilities of this technology.

![Alt Text](tm.gif)

To get started, create and activate a new virtual environment for this exercise with special indication:

```
pi@ixe00:~ $ virtualenv tmachine --system-site-packages
pi@ixe00:~ $ source tmachine/bin/activate
(tmachine) pi@ixe00:~ $ 
```

After activating the virtual environment, install the requisite TensorFlow libraries by running the following lines:
```
(tmachine) pi@ixe00:~ $ cd Interactive-Lab-Hub/Lab\ 5
(tmachine) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ sudo chmod +x ./teachable_machines.sh
(tmachine) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ ./teachable_machines.sh
``` 

This might take a while to get fully installed. After installation, connect your webcam to your Pi and use **VNC to access to your Pi**, open the terminal, and go to Lab 5 folder and run the example script:
(***it will not work if you use ssh from your laptop***)

```
(tmachine) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ python tm_ppe_detection.py
```


(**Optionally**: You can train your own model, too. First, visit [TeachableMachines](https://teachablemachine.withgoogle.com/train), select Image Project and Standard model. Second, use the webcam on your computer to train a model. For each class try to have over 50 samples, and consider adding a background class where you have nothing in view so the model is trained to know that this is the background. Then create classes based on what you want the model to classify. Lastly, preview and iterate, or export your model as a 'Tensorflow' model, and select 'Keras'. You will find an '.h5' file and a 'labels.txt' file. These are included in this labs 'teachable_machines' folder, to make the PPE model you used earlier. You can make your own folder or replace these to make your own classifier.)

**\*\*\*Whether you make your own model or not, include screenshots of your use of Teachable Machines, and write how you might use this to create your own classifier. Include what different affordances this method brings, compared to the OpenCV or MediaPipe options.\*\*\***
![P5:teachable-machine](https://github.com/kchen1009/Interactive-Lab-Hub/blob/Fall2021/Lab%205/images/Teachable1.png)
![P6:teachable-machine](https://github.com/kchen1009/Interactive-Lab-Hub/blob/Fall2021/Lab%205/images/Teachable2.png)
First I have to say I was amazed by how smart the tool is for identifying detected items. It directly informs users if there is an object detected and what the object is. The tool is rahter more straightforward compared to the OpenCV or MediaPipe options. As a user, I understand that I could place anything in front of the camera, and the technology of Teachable Machines (if model properly trained) would return a message with explicit information. On the contrary, openCV detection methods isn't as simple to figure out what a particular algorithm is for. For instance, I knew it's face detection only because I read the description. There was no visible affordance or obvious sign to inform me what objects exactly can be attended to, whether it's a hand pose, a motion, or simply a face. If I didn't read the text description itself, I have to go through rounds of trial and error to distinguish what object would be detected/ignored, especially since there was no feedback when it detected objects that is not consistent with what the algorithm is designed for. I'd like to use Teachable Machines to detect people's energy level. That being said, I will have to make my own model and create a classfier for facial expression and posture.

*Don't forget to run ```deactivate``` to end the Teachable Machines demo, and to reactivate with ```source tmachine/bin/activate``` when you want to use it again.*


#### Filtering, FFTs, and Time Series data. (optional)
Additional filtering and analysis can be done on the sensors that were provided in the kit. For example, running a Fast Fourier Transform over the IMU data stream could create a simple activity classifier between walking, running, and standing.

Using the accelerometer, try the following:

**1. Set up threshold detection** Can you identify when a signal goes above certain fixed values?

**2. Set up averaging** Can you average your signal in N-sample blocks? N-sample running average?

**3. Set up peak detection** Can you identify when your signal reaches a peak and then goes down?

**\*\*\*Include links to your code here, and put the code for these in your repo--they will come in handy later.\*\*\***


### Part B
### Construct a simple interaction.

Pick one of the models you have tried, pick a class of objects, and experiment with prototyping an interaction.
This can be as simple as the boat detector earlier.
Try out different interaction outputs and inputs.

**\*\*\*Describe and detail the interaction, as well as your experimentation here.\*\*\*** <br />
![P7:interaction](https://github.com/kchen1009/Interactive-Lab-Hub/blob/Fall2021/Lab%205/images/Interaction1.png)
Initially I sought to extend the idea of outputting weather information when users stand in front of the mirror, and therefore, I tried to prototype the interaction using the facial detection method provided by OpenCV to experiment with the idea. 
<br /><br />
However, I later decided to try out the Teachable Machines and create my own model to make the interaction more interesting. As mentioned earlier, I am interested in designing a system to detect users' energy level. A use case of this piece of data could be something as follows - a customer walks to the self-order kiosk in a coffee shop; while the customer is looking at the menu, the kiosk integrated with an energy detector would determine the customer's energy level and make suggestions on what items/how many shots of espresso to order. In my design, a user's body energy is characterized into 3 levels: energetic, half-charged, and drained. Feedack provided to users would be based on these 3 energy levels.
![P8:training](https://github.com/kchen1009/Interactive-Lab-Hub/blob/Fall2021/Lab%205/images/Training.png)
The screenshot above shows the training process based of the image samples collected. The following screenshots are 3 different energy levels detected. <br />
Energetic
![P9:energetic](https://github.com/kchen1009/Interactive-Lab-Hub/blob/Fall2021/Lab%205/images/Energetic.png)
Half-charged <br />
![P10:half-charged](https://github.com/kchen1009/Interactive-Lab-Hub/blob/Fall2021/Lab%205/images/Half-charged.png)
Drained <br />
![P11:drained](https://github.com/kchen1009/Interactive-Lab-Hub/blob/Fall2021/Lab%205/images/Drained.png)
### Part C
### Test the interaction prototype

Now flight test your interactive prototype and **note down your observations**:
For example:
1. When does it what it is supposed to do?
2. When does it fail?
3. When it fails, why does it fail?
4. Based on the behavior you have seen, what other scenarios could cause problems?

The model works well when the testing participants have obvious facial expressions and body poses; for instance, sitting with a round-shouldered slouch and almost closed eyes when users are drained. I also tested the protoype myself, and it worked perfectly well for me. This is mainly due to the fact that the model was trained with the image samples of my face and poses. The system failed when the testing participants remained neutral and didn't reveal too much emotion. The model were having hard time understanding how the users felt and distinguishing energy levels. Some other scenarios that I believe could also cause problems are when users have glasses or hats on. These accessiories might hinder the system's ability to detect users' energy levels.

**\*\*\*Think about someone using the system. Describe how you think this will work.\*\*\***
1. Are they aware of the uncertainties in the system?
2. How bad would they be impacted by a miss classification?
3. How could change your interactive system to address this?
4. Are there optimizations you can try to do on your sense-making algorithm. <br />
I believe most people are aware that there could be uncertainties when it comes to detecing facial expressions, especially when the system is about determining energy level. It would not be 100% accurate, and the accuracy would even decreases in some cases such as people faking a smile when they are actually drained. Even though people might be aware of the existence of uncertainties, they could be unfamiliar with fluctuating factors like lighting, hair styles, and accessories wore (as mentioned above). A miss classification might be a serious issue since people are already aware of the uncertainties. If the system is applied to a self-order kiosk like my design, users might even just use the detection system for fun. However, even if it is applied for casual use, something I could change to address a miss classification is to add a disclaimer to inform users that there might be some edge cases and that they should take the suggestions with a grain of salt. I could even add additional sensors to the system to have more thorough and complete detection of facial expressions and body poses. A possible optimization I can try to do on the algorithm would be training the model with more diverse set of data including different races or ethnicities to further eliminate uncertainties based on these concerns.

### Part D
### Characterize your own Observant system

Now that you have experimented with one or more of these sense-making systems **characterize their behavior**.
During the lecture, we mentioned questions to help characterize a material:
* What can you use X for?
* What is a good environment for X?
* What is a bad environment for X?
* When will X break?
* When it breaks how will X break?
* What are other properties/behaviors of X?
* How does X feel?

**\*\*\*Include a short video demonstrating the answers to these questions.\*\*\***

### Part 2.

Following exploration and reflection from Part 1, finish building your interactive system, and demonstrate it in use with a video.

**\*\*\*Include a short video demonstrating the finished result.\*\*\***
