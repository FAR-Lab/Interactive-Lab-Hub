# Interactive Prototyping: The Clock of Pi
**NAMES OF COLLABORATORS HERE**

Does it feel like time is moving strangely during this semester?

For our first Pi project, we will pay homage to the [timekeeping devices of old](https://en.wikipedia.org/wiki/History_of_timekeeping_devices) by making simple clocks.

It is worth spending a little time thinking about how you mark time, and what would be useful in a clock of your own design.

**Please indicate anyone you collaborated with on this Lab here.**
Be generous in acknowledging their contributions! And also recognizing any other influences (e.g. from YouTube, Github, Twitter) that informed your design. 

## Prep

Lab Prep is extra long this week. Make sure to start this early for lab on Thursday.

1. ### Set up your Lab 2 Github

Before the start of lab Thursday, [pull changes from the Interactive Lab Hub](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2021Fall/readings/Submitting%20Labs.md#to-pull-lab-updates) so that you have your own copy of Lab 2 on your own lab hub.


  If you are organizing your Lab Hub through folder in local machine, go to terminal, cd into your Interactive-Lab-Hub folder and run:

  ```
  Interactive-Lab-Hub $ git remote add upstream https://github.com/FAR-Lab/Interactive-Lab-Hub.git
  Interactive-Lab-Hub $ git pull upstream Fall2022
  ```
  
  The reason why we are adding a upstream with **course lab-hub** instead of yours is because the local Interactive-Lab-Hub folder is linked with your own git repo already. Try typing ``git remote -v`` and you should see there is the origin branch with your own git repo. We here add the upstream to get latest updates from the teaching team by pulling the **course lab-hub** to your local machine. After your local folder got the latest updates, push them to your remote git repo by running:
  
  ```
  Interactive-Lab-Hub $ git add .
  Interactive-Lab-Hub $ git commit -m "message"
  Interactive-Lab-Hub $ git push
  ```
  Your local and remote should now be up to date with the most recent files.


2. ### Get Kit and Inventory Parts
Prior to the lab session on Thursday, taken inventory of the kit parts that you have, and note anything that is missing:

***Update your [parts list inventory](partslist.md)***

3. ### Prepare your Pi for lab this week
[Follow these instructions](prep.md) to download and burn the image for your Raspberry Pi before lab Thursday.




## Overview
For this assignment, you are going to 

A) [Connect to your Pi](#part-a)  

B) [Try out cli_clock.py](#part-b) 

C) [Set up your RGB display](#part-c)

D) [Try out clock_display_demo](#part-d) 

E) [Modify the code to make the display your own](#part-e)

F) [Make a short video of your modified barebones PiClock](#part-f)

G) [Sketch and brainstorm further interactions and features you would like for your clock for Part 2.](#part-g)

## The Report
This readme.md page in your own repository should be edited to include the work you have done. You can delete everything but the headers and the sections between the \*\*\***stars**\*\*\*. Write the answers to the questions under the starred sentences. Include any material that explains what you did in this lab hub folder, and link it in the readme.

Labs are due on Mondays. Make sure this page is linked to on your main class hub page.

## Part A. 
### Connect to your Pi
Just like you did in the lab prep, ssh on to your pi. Once you get there, create a Python environment by typing the following commands.

```
ssh pi@<your Pi's IP address>
...
pi@ixe00:~ $ virtualenv circuitpython
pi@ixe00:~ $ source circuitpython/bin/activate
(circuitpython) pi@ixe00:~ $ 

```
### Setup Personal Access Tokens on GitHub
The support for password authentication of GitHub was removed on August 13, 2021. That is, in order to link and sync your own lab-hub repo with your Pi, you will have to set up a "Personal Access Tokens" to act as the password for your GitHub account on your Pi when using git command, such as `git clone` and `git push`.

Following the steps listed [here](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token) from GitHub to set up a token. Depends on your preference, you can set up and select the scopes, or permissions, you would like to grant the token. This token will act as your GitHub password later when you use the terminal on your Pi to sync files with your lab-hub repo.


## Part B. 
### Try out the Command Line Clock
Clone your own lab-hub repo for this assignment to your Pi and change the directory to Lab 2 folder (remember to replace the following command line with your own GitHub ID):

```
(circuitpython) pi@ixe00:~$ git clone https://github.com/<YOURGITID>/Interactive-Lab-Hub.git
(circuitpython) pi@ixe00:~$ cd Interactive-Lab-Hub/Lab\ 2/
```
Depends on the setting, you might be asked to provide your GitHub user name and password. Remember to use the "Personal Access Tokens" you just set up as the password instead of your account one!


Install the packages from the requirements.txt and run the example script `cli_clock.py`:

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ pip install -r requirements.txt
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ python cli_clock.py 
02/24/2021 11:20:49
```

The terminal should show the time, you can press `ctrl-c` to exit the script.
If you are unfamiliar with the Python code in `cli_clock.py`, have a look at [this Python refresher](https://hackernoon.com/intermediate-python-refresher-tutorial-project-ideas-and-tips-i28s320p). If you are still concerned, please reach out to the teaching staff!


## Part C. 
### Set up your RGB Display
<<<<<<< HEAD

### Hardware (you have done this in the prep)

=======
We have asked you to equip the [Adafruit MiniPiTFT](https://www.adafruit.com/product/4393) on your Pi in the Lab 2 prep already. Here, we will introduce you to the MiniPiTFT and Python scripts on the Pi with more details.

<img src="https://cdn-learn.adafruit.com/assets/assets/000/082/842/large1024/adafruit_products_4393_iso_ORIG_2019_10.jpg" height="200" />

The Raspberry Pi 3 has a variety of interfacing options. When you plug the pi in the red power LED turns on. Any time the SD card is accessed the green LED flashes. It has standard USB ports and HDMI ports. Less familiar it has a set of 20x2 pin headers that allow you to connect a various peripherals.

<img src="https://maker.pro/storage/g9KLAxU/g9KLAxUiJb9e4Zp1xcxrMhbCDyc3QWPdSunYAoew.png" height="400" />

To learn more about any individual pin and what it is for go to [pinout.xyz](https://pinout.xyz/pinout/3v3_power) and click on the pin. Some terms may be unfamiliar but we will go over the relevant ones as they come up.

### Hardware (you have done this in the prep)

From your kit take out the display and the [Raspberry Pi 3](https://cdn-shop.adafruit.com/970x728/3775-07.jpg)
>>>>>>> 7134d6993950a43e0c39ea3e5be268f4d1ae4a76


### Testing your Screen


#### Displaying Info with Texts
You can look in `stats.py` for how to display text on the screen!

#### Displaying an image

You can look in `image.py` for an example of how to display an image on the screen. Can you make it switch to another image when you push one of the buttons?



## Part D. 
### Set up the Display Clock Demo
Work on `screen_clock.py`, try to show the time by filling in the while loop (at the bottom of the script where we noted "TODO" for you). You can use the code in `cli_clock.py` and `stats.py` to figure this out.

### How to Edit Scripts on Pi



## Part E.
### Modify the barebones clock to make it your own

Does time have to be linear?  How do you measure a year? [In daylights? In midnights? In cups of coffee?](https://www.youtube.com/watch?v=wsj15wPpjLY)

Can you make time interactive? You can look in `screen_test.py` for examples for how to use the buttons.

Please sketch/diagram your clock idea. (Try using a [Verplank digram](http://www.billverplank.com/IxDSketchBook.pdf)!

**We strongly discourage and will reject the results of literal digital or analog clock display.**


\*\*\***A copy of your code should be in your Lab 2 Github repo.**\*\*\*


 **Idea**
  - Running clock that lets you hit the button and it will show your lap time
  
  ![Sep 12, Doc 1 2](https://user-images.githubusercontent.com/112022260/189791146-34a49da0-00a5-4dd8-8476-1e3381745855.jpg)



## Part F. 
## Make a short video of your modified barebones PiClock



\*\*\***Take a video of your PiClock.**\*\*\*

Please view the video at:

https://drive.google.com/file/d/1LBKLh8RVxWAbp8cGqDGNSfZ7c33SwGW-/view?usp=sharing

## Part G. 
## Sketch and brainstorm further interactions and features you would like for your clock for Part 2.

 For part 2, I would like to look and see how I might be able to potentially a few avenues. 1) incorporate motion sensor to automatically lap the time when someone passes 2) Add logic to show what your best lap was on  another screen 3) Increase the graphics of how it is recorded 4)Incorporate functionality for having heats within multiple laps that are a part of it 5) Add calculations and stats on how fast you have been going 6) Incorporate LEDs to give countdown of when it is starting 7) use a motion sensor to use the flipping like motion of a sand clock to make it a new lap
![IMG-0024](https://user-images.githubusercontent.com/112022260/189792438-d13e5348-83c4-4f97-a7e1-7ed827025adf.jpg)
![IMG-0025](https://user-images.githubusercontent.com/112022260/189792441-1a7f9a97-5443-41b8-82bf-2cf26c8e6834.jpg)

# Prep for Part 2

1. Pick up remaining parts for kit on Thursday lab class. Check the updated [parts list inventory](partslist.md) and let the TA know if there is any part missing.
  

2. Look at and give feedback on the Part G. for at least 2 other people in the class (and get 2 people to comment on your Part G!)

# Lab 2 Part 2

Pull Interactive Lab Hub updates to your repo.

Modify the code from last week's lab to make a new visual interface for your new clock. You may [extend the Pi](Extending%20the%20Pi.md) by adding sensors or buttons, but this is not required.

As always, make sure you document contributions and ideas from others explicitly in your writeup.

You are permitted (but not required) to work in groups and share a turn in; you are expected to make equal contribution on any group work you do, and N people's group project should look like N times the work of a single person's lab. What each person did should be explicitly documented. Make sure the page for the group turn in is linked to your Interactive Lab Hub page. 

## Summarized feedback
Feedback recieved from: Joseph Iovine, Kenneth Alvarez, William Klinenberg(outside of class)

Potential ideas surfaced in feedback
* Camera for motion sensor to lap you when you ran by (it feels unrealistic you would hit it yourself in an intense situation unless easily wearable)
* Best lap on another screen
* Add a guy walking 
* Red dot going around an ellpse based on how far you have gone


Other feedback:
   * To really be used in real life, it would require you to have a more robust case so you could hold on to it and track distance
   * It would be helpful to see the times in reverse order






## Initial updates incorporated
  - Best lap on another screen
  - Add the times in reverse order
 

## Further reflection and updates
  - Add a on start method that delays the start based on when you are ready.  This was combined with a light in order to give a visual signal to the user that the timer is about to start.

Additionally, on further reflection, I realized the need for the reset button to actually pause the application and start again in such a manner that the user would have time to prepare accordingly.  Additionally, it had surfaced in feedback that it would beneficial to have a visual cue of the start time similar those used in different racing games.

![IMG-0027](https://user-images.githubusercontent.com/112022260/191132010-c55035ba-96ee-49ef-b6c2-b40d6d1f0639.jpg)

## Additional updates
 - Added green light to extend the raspberry pi and give the user a visual aid in when the lap time is about to begin 
 - Add logic such that the first time you reset, it pauses the screen and when you hit reset it begins again given the user a countdown utilizing the green light
## Challenges
A particular challenge I encountered when developing the datasets was the mismatch between when you hit start and timer clock.  Due to the time between when I initially set the time variable vs. when it displays, there is mismatch that causes the appear the timer to start a few seconds in.  Despite multiple code refactors, I was not able to figure out the exact cause and it is an area I would like to explore in the future for more precise timing.

## Refined video

Please view the video here!
https://drive.google.com/file/d/1g4r7jNF1ItadjyQB2_xIt-xYgTiD0bS-/view?usp=sharing

