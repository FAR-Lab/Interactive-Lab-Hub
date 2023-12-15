# IDD Final Project - Music Player 
Amber Tsao (ct649), Aris Huang (th625), Julia Lin (jtl236), Sherri Lin (yl3658), Wayne Cheng (cc2796), Ifeng Wu (iw84)

**Project Plan**

**Big Idea**

Similar to what we have previously done for the observant system lab, our final project will be primarily focusing on utilizing computer vision to detect hand gestures as a new form of interaction to tell the music player to change to previous or next songs. We will use the "1" gesture to signify pausing or unpausing a song, the "2" gesture to signify next song, and the "3" gesture to signify the previous song. In addition, we will use the rotary encoder to adjust the volume up and down. We will also use capacitive sensor along with conductive copper tape to change the categories of the songs. On the MiniPiTFT display, we will show user’s current song and the playing time of the song. There will be button for the user to change the background of the display.


Song Categories:
1) R&B 
2) Pop 
3) K-Pop 
4) Dance 


Timeline:
Nov 14:  Settle the plan of the initial proposal
Nov 21: Finish creating all the main functionalities of the music player
Dec 4: Test the practical effect and troubleshoot the problem
Dec 11: Optimize the design and improve the effectivity
Dec 14: Finalize and submit the final result


**Parts Needed**

| Name | Image | Quantity |
| -------- | -------- | -------- |
| Raspberry Pi 4 Model B      | ![introduction 01](https://hackmd.io/_uploads/SJm6kAGrp.jpg)| 1     |
| 2K Webcam with Microphon  | ![Screenshot 2023-12-13 at 1.41.10 PM](https://hackmd.io/_uploads/Hyz1i_vU6.png) | 1     |
| Adafruit Mini PiTFT Display     | ![4393-05](https://hackmd.io/_uploads/rJKZZRzB6.jpg)| 1     |
| Capacitive Sensor     |![68747470733a2f2f63646e2d6c6561726e2e61646166727569742e636f6d2f6775696465732f63726f707065645f696d616765732f3030302f3030332f3232362f6d656469756d3634302f4d50523132315f746f705f616e676c652e6a70673f31363039323832343234](https://hackmd.io/_uploads/Bk-exSfLp.jpg)| 1     |
| Adafruit I2C QT Rotary Encoder     |![REI2C_top_angle_with_RC](https://hackmd.io/_uploads/BkItWCMS6.jpg) | 1     |
| Conductive Foil Tape     |![3483-00](https://hackmd.io/_uploads/HyHT-0Grp.jpg)| 1     |
| Qwiic Button - Green LED    |   ![16842-SparkFun_Qwiic_Button_-_Green_LED-02](https://hackmd.io/_uploads/Bys0GAGS6.jpg)| 1     |
| Alligator Clip    |  ![1592-00](https://hackmd.io/_uploads/S1c77Rfr6.jpg) | 4     |
| Cardboard    | ![81i4Y0eXwaL._AC_UF894,1000_QL80_](https://hackmd.io/_uploads/rJZwmRzr6.jpg) | 1     |



**Fall Back Plan**

The biggest challenge that we may encounter is using the hand gesture to signal the changing state of the music being played. We may run into problems with hand gesture detection or experiencing lagging between when the user signals. The latency may caused some lag in response; for instance, may lead to skipping multiple songs. Our fall-back plan use the capacitive sensor to map the music controller action rather than using hand gesture detection.


**Functioning Project**
The functioning project is a music player which users are able to interact with using hand gestures and buttons. The user is able to make the "1" gesture to signify pausing and pausing the song, the "2" gesture to signify the next song, the "3" gesture to signify the previous song. The user is also able to press on a button to change the background of the display, and press the button for the genre of music they would like to listen to.

## Project Setup Guideline

#### Step1: Setup the hardware environment

#### Step2: Create a virtual environment
```
python -m venv idd_final_env
source idd_final_env/bin/activate
```

#### Step3: Install required packages
```
pip3 install -r requirement.txt
```

#### Step4: Stop running the mini-screen service
```
sudo systemctl stop mini-screen.service
```

#### Step5: Run application
```
python musicPlayer.py 
```

**Documentation of Design Process**

Design Roadmap:
![IDD-8](https://hackmd.io/_uploads/S1cUxU8Lp.jpg)

Initial Design of the Final Deliverable:
![IMG_76A3FC5EEC68-1](https://hackmd.io/_uploads/BJBPmnQSp.jpg)


Building process:

- Assembling required materials
- Wiring up the required components
- Writing the code and testing
- Building the frame to house the components
- Assembling the components into the frame
- Painting the outer layer of the frame to make it more aesthetically pleasing
- Dimensions of the frame: height: 8.66 inches, width: 6.29 inches, length: 1.96 inches

**Setting up the required components and writing/testing the code:**
![S__16506934](https://hackmd.io/_uploads/SyS9UuDIT.jpg)
![S__16506935](https://hackmd.io/_uploads/SJS9LdDIT.jpg)
![S__16515111](https://hackmd.io/_uploads/B1r5U_vLa.jpg)

**Painting the outer frame:**
![S__16506932](https://hackmd.io/_uploads/BkScLdvLa.jpg)
![S__16506936](https://hackmd.io/_uploads/SJBqIOwUp.jpg)


Final Design:
![IMG_6FFA3D22DBAF-1](https://hackmd.io/_uploads/HkAHf8I8p.jpg)


*revised from initial design due to spatial constraint, we had to move some components around so they can all fit within the box 


**Physical Design of Device**

FRONT VIEW 
![S__26320906](https://hackmd.io/_uploads/rygUar88T.jpg)

The user is able to try on several functions of our music player with hand gestures. 

In the middle of the device, the user could aim the camera and make the "1", "2", "3" gestures to alter the corresponding functions.

On the left side of the device, the user could see the MiniPiTFT displaying the song name being played, the singer name, and the music playing time. In addition, the user is able to change the background of the display screen by pressing the Green LED Qwiic Button above the MiniPiTFT. 

On the right side of the device, the user could rotate the Rotary Encoder to control the volume of playing music. Once user rotates toward the right side can volume up and vice versa.


TOP VIEW

![S__26320908](https://hackmd.io/_uploads/BJqOaHI86.jpg)
The user is able to select which genre of music they would like to listen to, from Dance, K-pop, R&B, and Pop. Once the user makes a selection, the music player will automatically start playing a song from the selected genre.

COMPUTER VIEW

![IMG_3C658F6338FD-1](https://hackmd.io/_uploads/B1fLPDUUT.jpg)

On the computer screen, the user is able to see what the camera is capturing of their gesture. In addition, the user can see the text output of their actions. For example, if they use the "1" gesture, the display will show whether the song is paused or unpaused. The user is able to know the state of the program. 
 
**Final Video**

[Interaction Video](https://drive.google.com/file/d/12u2BBvKE4nnI54TFaM40LYKrBi_T9HjB/view?usp=sharing)


In the video shows a user interacting with the music player with hand gesture. The user first holds up "1" gesture to unpause or pause the song. When the music start playing, the MiniPiTFT will show the name of the song name, artist name, and playing time. After that he user holds up "2" gesture to play the next song. Then the user holds up "3" gesture to play the previous song.

For changing 4 available genres (from left to right: Dance, Kpop, R&B, Pop) of the playing song, the user clicks the 4 sensors on top.

Next, the user rotates the rotate encoder clockwised to increase volume

At the end of the video, the user pressed the green LED bottom to switch the display background
