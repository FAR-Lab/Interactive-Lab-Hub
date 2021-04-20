# Observant Systems


For lab this week, we focus on creating interactive systems that can detect and respond to events or stimuli in the environment of the Pi, like the Boat Detector we mentioned in lecture. 
Your **observant device** could, for example, count items, find objects, recognize an event or continuously monitor a room.

This lab will help you think through the design of observant systems, particularly corner cases that the algorithms need to be aware of.

In Lab 5 part 1, we focus on detecting and sense-making.

In Lab 5 part 2, we'll incorporate interactive responses.


## Prep

1.  Pull the new Github Repo.
2.  Read about [OpenCV](https://opencv.org/about/).
3.  Read Belloti, et al's [Making Sense of Sensing Systems: Five Questions for Designers and Researchers](https://www.cc.gatech.edu/~keith/pubs/chi2002-sensing.pdf)

### For the lab, you will need:

1. Raspberry Pi
1. Raspberry Pi Camera (2.1)
1. Microphone (if you want speech or sound input)
1. Webcam (if you want to be able to locate the camera more flexibly than the Pi Camera)

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

Befor you get started connect the RaspberryPi Camera V2. [The Pi hut has a great explanation on how to do that](https://thepihut.com/blogs/raspberry-pi-tutorials/16021420-how-to-install-use-the-raspberry-pi-camera).  

#### OpenCV
A more traditional to extract information out of images is provided with OpenCV. The RPI image provided to you comes with an optimized installation that can be accessed through python.

Additionally, we also included 4 standard OpenCV examples. These examples include contour(blob) detection, face detection with the ``Haarcascade``, flow detection(a type of keypoint tracking), and standard object detection with the [Yolo](https://pjreddie.com/darknet/yolo/) darknet.

Most examples can be run with a screen (I.e. VNC or ssh -X or with an HDMI monitor), or with just the terminal. The examples are separated out into different folders. Each folder contains a ```HowToUse.md``` file, which explains how to run the python example.

```shell
pi@ixe00:~/openCV-examples $ tree -l
.
├── contours-detection
│   ├── contours.py
│   └── HowToUse.md
├── data
│   ├── slow_traffic_small.mp4
│   └── test.jpg
├── face-detection
│   ├── face-detection.py
│   ├── faces_detected.jpg
│   ├── haarcascade_eye_tree_eyeglasses.xml
│   ├── haarcascade_eye.xml
│   ├── haarcascade_frontalface_alt.xml
│   ├── haarcascade_frontalface_default.xml
│   └── HowToUse.md
├── flow-detection
│   ├── flow.png
│   ├── HowToUse.md
│   └── optical_flow.py
└── object-detection
    ├── detected_out.jpg
    ├── detect.py
    ├── frozen_inference_graph.pb
    ├── HowToUse.md
    └── ssd_mobilenet_v2_coco_2018_03_29.pbtxt
```
#### Filtering, FFTs, and Time Series data.
Additional filtering and analysis can be done on the sensors that were provided in the kit. For example, running a Fast Fourier Transform over the IMU data stream could create a simple activity classifier between walking, running, and standing.

Using the set up from the [Lab 3 demo](https://github.com/FAR-Lab/Interactive-Lab-Hub/tree/Spring2021/Lab%203/demo) and the accelerometer, try the following:

**1. Set up threshold detection** Can you identify when a signal goes above certain fixed values?

threshold-passed is printed when the threshold set is passed.

![alt text](https://github.com/williamzhang012998/Interactive-Lab-Hub/blob/Spring2021/Lab%205/thresholddetect.png)

**2. Set up averaging** Can you average your signal in N-sample blocks? N-sample running average?

Signal is averaged over the previous 10 points.

![alt text](https://github.com/williamzhang012998/Interactive-Lab-Hub/blob/Spring2021/Lab%205/averaging.png)

**3. Set up peak detection** Can you identify when your signal reaches a peak and then goes down?

peak-detected is printed when a peak is detected. 
![alt text](https://github.com/williamzhang012998/Interactive-Lab-Hub/blob/Spring2021/Lab%205/peakdetect.png)

Include links to your code here, and put the code for these in your repo--they will come in handy later.

Code is given in the "demo" folder.

#### Teachable Machines (beta, optional)
Google's [TeachableMachines](https://teachablemachine.withgoogle.com/train) might look very simple.  However, its simplicity is very useful for experimenting with the capabilities of this technology.

You can train a Model on your browser, experiment with its performance, and then port it to the Raspberry Pi to do even its task on the device.

Here is Adafruit's directions on using Raspberry Pi and the Pi camera with Teachable Machines:

1. [Setup](https://learn.adafruit.com/teachable-machine-raspberry-pi-tensorflow-camera/raspberry-pi-setup)
2. Install Tensorflow: Like [this](https://learn.adafruit.com/running-tensorflow-lite-on-the-raspberry-pi-4/tensorflow-lite-2-setup), but use this [pre-built binary](https://github.com/bitsy-ai/tensorflow-arm-bin/) [the file](https://github.com/bitsy-ai/tensorflow-arm-bin/releases/download/v2.4.0/tensorflow-2.4.0-cp37-none-linux_armv7l.whl) for Tensorflow, it will speed things up a lot.
3. [Collect data and train models using the PiCam](https://learn.adafruit.com/teachable-machine-raspberry-pi-tensorflow-camera/training)
4. [Export and run trained models on the Pi](https://learn.adafruit.com/teachable-machine-raspberry-pi-tensorflow-camera/transferring-to-the-pi)

Alternative less steps option is [here](https://github.com/FAR-Lab/TensorflowonThePi).

#### PyTorch  
As a note, the global Python install contains also a PyTorch installation. That can be experimented with as well if you are so inclined.

### Part B
### Construct a simple interaction.

Pick one of the models you have tried, pick a class of objects, and experiment with prototyping an interaction.
This can be as simple as the boat detector earlier.
Try out different interactions outputs and inputs.
**Describe and detail the interaction, as well as your experimentation.**

I decided to use the object-detection model for detecting cars. In designing bridges, many times you have to know how many cars cross the bridge everyday. Because I don't live next to a busy bridge, I have decided to create an interaction where I can count the number of cars that are on a bridge at a certain time from a recorded video.

The interaction should detect and tell the user the number of cars there are on the screen, what is the confidence of prediction and maybe even detect some other things like traffic lights.

### Part C
### Test the interaction prototype

Now flight test your interactive prototype and **note your observations**:
For example:
1. When does it what it is supposed to do?
   The intercation does what it is supposed to do under normal conditions where the video is clear and the visibility is good.
3. When does it fail?
   The interaction fails when the visibility is not good or when something that the system is not designed to count comes into the frame (for example a large number of birds).
5. When it fails, why does it fail?
   It fails because the models fail to account for certain objects and organisms.
7. Based on the behavior you have seen, what other scenarios could cause problems?
   There could potentially be a problem if there is a car crash. This is because a lot of times, in car crashes, the cars overlap and it could be hard for the system to differentiate the different cars.

**Think about someone using the system. Describe how you think this will work.**
1. Are they aware of the uncertainties in the system?
   Yes, they should be away of the uncertainties as the confidence of prediction is displayed next to each prediction on screen. 
3. How bad would they be impacted by a miss classification?
   I would not say that the user will be impacted greatly by a miss classification as counting cars on a bridge to determine bridge use rate is normally not a life or death matter.
5. How could change your interactive system to address this?
   I could include other things that the system don't currently account for. For example, the system can maybe detect common species of bird, detect a car crash and detect ships.
7. Are there optimizations you can try to do on your sense-making algorithm.
   I am sure that improvements on the algorithm can be made and the program can be made to run faster. But at this moment I am not sure it can be done.

### Part D
### Characterize your own Observant system

Now that you have experimented with one or more of these sense-making systems **characterize their behavior**.
During the lecture, we mentioned questions to help characterize a material:
* What can you use X for?
  The system can be used for calculating the use rate of a bridge or tracking the use rate of a parking lot.
* What is a good environment for X?
  Bridges, parking lots, environments where the visibility is good and there are not a lot of other object other than cars.
* What is a bad environment for X?
  Any environment where there are many other objects other than cars.
* When will X break?
  When objects or cars are too close to each other. The system then won't be able to differentiate different cars from each other.
* When it breaks how will X break?
  When it breaks, the number of cars that the system counts will be incorrect.
* What are other properties/behaviors of X?
  There are not a lot of other properties of the system.
* How does X feel?
  The system feels pretty efficient to use.

**Include a short video demonstrating the answers to these questions.**

You Only Look Once (YOLO) is a CNN architecture for performing real-time object detection. The algorithm applies a single neural network to the full image, and then divides the image into regions and predicts bounding boxes and probabilities for each region. This lab aims to count every vehicle, which includes, motorcycle, bus, car, cycle, truck, train) detected in the input video using YOLOv3 object-detection algorithm.

https://drive.google.com/file/d/1kp1nEAqXW8izBuanlSBdvXsNP_dz7OiM/view?usp=sharing
