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

**\*\*\*Try each of the following four examples in the `openCV-examples`, include screenshots of your use and write about one design for each example that might work based on the individual benefits to each algorithm.\*\*\***


![alt text](https://github.com/rohangreddy/Interactive-Lab-Hub/blob/Fall2021/Lab%205/contours.png)

Contours was a cool example that allows for detection of edges. This could be useful in an walking assitant. It is quite common for people to be on their phones while walking, and so having an extra pair of eyes to detect edges of potential obstacles could be useful by alerting users when they get too close to an edge. 

![alt text](https://github.com/rohangreddy/Interactive-Lab-Hub/blob/Fall2021/Lab%205/face_detection.png)

The face detection example was able to detect the overall face as well as features such as the eyes, nose, and mouth. An example design that would work well with face detection could be a mask detector that reminds people to keep their masks on when indoors. If the algorithm detects facial features such as the nose or mouth, it could prompt the user to adjust their face covering. 

![alt text](https://github.com/rohangreddy/Interactive-Lab-Hub/blob/Fall2021/Lab%205/flow.png)

Flow was really interesting in its ability to detect the change in position and velocity of certain keypoints over time. This could be very useful in an application that monitors the velocity with which vehicles travel across the Queensboro bridge. By placing a camera level with the bridge and running this algorithm, the velocities of cars over time could be detected an analyzed. 

![alt text](https://github.com/rohangreddy/Interactive-Lab-Hub/blob/Fall2021/Lab%205/object.png)

Object detection was interesting as well, with detected objects having a bounding box around them. This could be useful in an application that attempts to find an object in a cluttered room. The algorithm can first be shown an object and be instructed to "remember" the object based on the dimensions of the bounding box that the algorithm uses when identifying the object. Then, when placed somewhere that offers a view of the entire room, the algorithm can identify the object quickly and alert the user to where it is. 

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

**\*\*\*Consider how you might use this position based approach to create an interaction, and write how you might use it on either face, hand or body pose tracking.\*\*\***

This is a really interesting example. One application that uses the position based approach of hand tracking could be a sign language detector. The algorithm can detect positions of the hands and fingers used in sign language to translate the sign into words.

(You might also consider how this notion of percentage control with hand tracking might be used in some of the physical UI you may have experimented with in the last lab, for instance in controlling a servo or rotary encoder.)



#### Teachable Machines
Google's [TeachableMachines](https://teachablemachine.withgoogle.com/train) might look very simple. However, its simplicity is very useful for experimenting with the capabilities of this technology.

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


![Alt Text](https://github.com/rohangreddy/Interactive-Lab-Hub/blob/Fall2021/Lab%205/ppe.png)

Teachable Machines is really cool. It offers a degree of flexibility over the OpenCV or MediaPipe options in the ability to train the classifier on whatever objects that you would like to detect. Although I did not make my own model, I would like to try out teachable machines as a sign language detector to see if it could translate sign language into words.


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

**\*\*\*Describe and detail the interaction, as well as your experimentation here.\*\*\***

I would like to use Teachable Machines and train it on the American Sign Language hand sign for each letter of the alphabet. I would like to explore how well the model is able to detect each letter, as well as if it would be able to piece together different letters made by hand signs into words and even sentences. 

### Part C
### Test the interaction prototype

Now flight test your interactive prototype and **note down your observations**:
For example:
1. When does it what it is supposed to do?

The system seems to do what it is supposed to do when the hand making the sign is close to the webcam.

2. When does it fail?

It seems to fail when other objects are in the same frame as the hand making the sign. It also is unable to recognize multiple hand signs that are executed in succesion.

4. When it fails, why does it fail?

It might be failing because the model was trained on images that only contain the hand making signs. Other objects present in the frame are interfering with the ability to detect the hand sign. 

It also seems to fail with multiple hand signs that are done very quickly. This might be a limitation with processing the frames of the webcam. Slowing the hand signs down seems to help with detection.

6. Based on the behavior you have seen, what other scenarios could cause problems?

The scenario that could be most problematic is when an actual user who is fluent in ASL (american sign language) uses the system. Fluent users usually are comfortable with the signs and will have a certain speed that they make their signs with. I am certain that the speed will be too much for the camera to pick up all the signs effectively.

Additionally, there are signs that ASL users use that do not directly translate to letters. For example, there are specific signs that correspond to emotions ie "I am hungry" would be a specific sign. The system would definitely not be able to pick these up because it was only trained on the signs that correspond to letters of the alphabet. 

**\*\*\*Think about someone using the system. Describe how you think this will work.\*\*\***
1. Are they aware of the uncertainties in the system?

Users fluent in ASL will definitely not be aware of the uncertainties in the system. They may expect the system to completely understand any and all signs that they present. The users will have to be instructed to slow their signs down, and to limit their signs to english alphabets and use those to spell out words and sentences they would like to convey.

2. How bad would they be impacted by a miss classification?

Mis-classification would result in a complete breakdown of the communication between the user and the machine. This may have additional consequences, such as user frustration at being misunderstood as well as a breakdown in trust between the user and the machine.

5. How could change your interactive system to address this?

It would be good to be upfront about the capabilities of the system. Users can be explicitly told that the system only accepts certain signs at a certain speed. This can allow users to change their behavior in order to best be understood by the system. 

7. Are there optimizations you can try to do on your sense-making algorithm.

In order to improve classification accuracy, it may be useful to train the classifier on larger sample sizes for each class, which in this case would be the ASL version of each letter of the alphabet. Luckily, there is a Kaggle Dataset: https://www.kaggle.com/grassknoted/asl-alphabet 

This dataset contains 3000 images of each class (hand signs of each letter). The sample size and diversity of images in the dataset (hands of different sizes, ethnicities, positions, lighting conditions, etc.) should improve classification accuracy greatly.

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

Video demo: https://youtu.be/LmsVb3n0-D4

This is intended to be an autotranslator of American Sign Language hand signs to English. The idea is that a person can make a hand sign, which would translate into its English counterpart based on the label that the ML model assigns to the hand sign.

A good environment for the model is one which exactly matches the conditions of the training images that were given to the model. Unfortunately, if the position of the webcam or the lighting conditions differ even slightly, this throws the model off completely. Additionally, hand position matters for the model. The distance at which the hand was placed in the images given to the model during training must be almost exactly the same as the hand position during real-time execution. This was something I did not consider, and varying the hand position even slightly resulted in the model completely misclassifying the letter that the hand sign was intended to represent

In this demonstration, the model was only able to get a single letter correct ('N'), and varying the position even slightly resulted in the model classifying 'N' as 'U'. 

Overall, the model is very frustrating to use due to high rate of misclassification. I will explore adding additional training examples to make the model more robust, but the reality is that a 28-class classifier may be too complex for the teachable machine to accurately classify different hand signs. I may have to simplify the model to include common hand signs that look completely different from each other in order to reduce rate of misclassification. 

### Part 2.

Following exploration and reflection from Part 1, finish building your interactive system, and demonstrate it in use with a video.

My idea was to implement an American Sign Langauge auto-translator, that would be able to to recognize ASL hand signs, translate them to English letter by letter, piece together the words in the sentence, and finally, speak the sentence outloud using text-to-speech. This would allow people who communicate primarily through hand signs to be able to communicate to individuals who are not fluent in ASL. Such a product would be very helpful for people with hearing disabilities, as it would give them the ability to "speak" outloud through the use of technology. For reference, please see the ASL chart of hand signs below.

![Alt Text](https://github.com/rohangreddy/Interactive-Lab-Hub/blob/Fall2021/Lab%205/asl-abc.png)

I ran into a lot of issues with trying to train an accurate 28-class classifier (to classify every letter of the alphabet as the corresponding ASL hand sign) using teachable machines. I tried many different ways to make the 28 class classifier work, including giving each class as much training data as I could (~200 images for each hand sign corresponding to a letter of the alphabet), varying the position and angle of my hand in the images given to train the model, etc. I even tried using a Kaggle dataset of ASL hand signs which had roughly 3000 images per hand sign, but this did not work well likely because the training images differed significantly from the images obtained from my webcam feed.

Some very helpful feedback that I received was that a 28 class classifier simply may be beyond the capabilities of the model that teachable machines uses. One suggestion was to try and cut down the number of classes to a few letters of the alphabet (rather than every single letter), and to choose those letters that contained hand signs that differed from each other the most. This was very helpful feedback because the initial 28-class model (found in the sign_lang1 folder) seemed to misclassify hand signs that differed slightly in position the most. 


**\*\*\*Include a short video demonstrating the finished result.\*\*\***
