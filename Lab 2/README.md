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
We have asked you to equip the [Adafruit MiniPiTFT](https://www.adafruit.com/product/4393) on your Pi in the Lab 2 prep already. Here, we will introduce you to the MiniPiTFT and Python scripts on the Pi with more details.

<img src="https://cdn-learn.adafruit.com/assets/assets/000/082/842/large1024/adafruit_products_4393_iso_ORIG_2019_10.jpg" height="200" />

The Raspberry Pi 3 has a variety of interfacing options. When you plug the pi in the red power LED turns on. Any time the SD card is accessed the green LED flashes. It has standard USB ports and HDMI ports. Less familiar it has a set of 20x2 pin headers that allow you to connect a various peripherals.

<img src="https://maker.pro/storage/g9KLAxU/g9KLAxUiJb9e4Zp1xcxrMhbCDyc3QWPdSunYAoew.png" height="400" />

To learn more about any individual pin and what it is for go to [pinout.xyz](https://pinout.xyz/pinout/3v3_power) and click on the pin. Some terms may be unfamiliar but we will go over the relevant ones as they come up.

### Hardware (you have done this in the prep)

From your kit take out the display and the [Raspberry Pi 3](https://cdn-shop.adafruit.com/970x728/3775-07.jpg)

Line up the screen and press it on the headers. The hole in the screen should match up with the hole on the raspberry pi.

<p float="left">
<img src="https://cdn-learn.adafruit.com/assets/assets/000/087/539/medium640/adafruit_products_4393_quarter_ORIG_2019_10.jpg?1579991932" height="200" />
<img src="https://cdn-learn.adafruit.com/assets/assets/000/082/861/original/adafruit_products_image.png" height="200">
</p>

### Testing your Screen

The display uses a communication protocol called [SPI](https://www.circuitbasics.com/basics-of-the-spi-communication-protocol/) to speak with the raspberry pi. We won't go in depth in this course over how SPI works. The port on the bottom of the display connects to the SDA and SCL pins used for the I2C communication protocol which we will cover later. GPIO (General Purpose Input/Output) pins 23 and 24 are connected to the two buttons on the left. GPIO 22 controls the display backlight.

We can test it by typing 
```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ python screen_test.py
```

You can type the name of a color then press either of the buttons on the MiniPiTFT to see what happens on the display! You can press `ctrl-c` to exit the script. Take a look at the code with
```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ cat screen_test.py
```
![screentest](https://user-images.githubusercontent.com/112603386/189815913-fe28687b-1708-44b0-80fa-dbd141da1e03.jpg)



#### Displaying Info with Texts
You can look in `stats.py` for how to display text on the screen!

#### Displaying an image

You can look in `image.py` for an example of how to display an image on the screen. Can you make it switch to another image when you push one of the buttons?



## Part D. 
### Set up the Display Clock Demo
Work on `screen_clock.py`, try to show the time by filling in the while loop (at the bottom of the script where we noted "TODO" for you). You can use the code in `cli_clock.py` and `stats.py` to figure this out.

### How to Edit Scripts on Pi
Option 1. One of the ways for you to edit scripts on Pi through terminal is using [`nano`](https://linuxize.com/post/how-to-use-nano-text-editor/) command. You can go into the `screen_clock.py` by typing the follow command line:
```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ nano screen_clock.py
```
You can make changes to the script this way, remember to save the changes by pressing `ctrl-o` and press enter again. You can press `ctrl-x` to exit the nano mode. There are more options listed down in the terminal you can use in nano.

Option 2. Another way for you to edit scripts is to use VNC on your laptop to remotely connect your Pi. Try to open the files directly like what you will do with your laptop and edit them. Since the default OS we have for you does not come up a python programmer, you will have to install one yourself otherwise you will have to edit the codes with text editor. [Thonny IDE](https://thonny.org/) is a good option for you to install, try run the following command lines in your Pi's ternimal:

  ```
  pi@ixe00:~ $ sudo apt install thonny
  pi@ixe00:~ $ sudo apt update && sudo apt upgrade -y
  ```

Now you should be able to edit python scripts with Thonny on your Pi.



## Part E.
### Modify the barebones clock to make it your own

Does time have to be linear?  How do you measure a year? [In daylights? In midnights? In cups of coffee?](https://www.youtube.com/watch?v=wsj15wPpjLY)

Can you make time interactive? You can look in `screen_test.py` for examples for how to use the buttons.

Please sketch/diagram your clock idea. (Try using a [Verplank digram](http://www.billverplank.com/IxDSketchBook.pdf)!

**We strongly discourage and will reject the results of literal digital or analog clock display.**

![verplanck](https://user-images.githubusercontent.com/112603386/189816015-a5ccf8d0-06f1-45ce-b49d-5de828bf393d.jpg)

The idea behind this design is a clock that keeps track of blood alcohol content for someone drinking alcohol. Often times people get carried away during a night out on the town, and this can lead to dangerous drivers. With this device, users will click the bottom button each time they drink 1 drink. The device will show the message "drink logged" to show user that the drink has been successfully logged into the device. This BAC equation is based on a 5% 12 oz beer, so if it is a "double" mixed drink log 2 drinks. At any point even before the users first drink, they can click the lower button on the device to check their current BAC. If it is below 0.08 (the legal driving limit), the device will read you must wait 0min to drive - meaning they are legally safe to drive. If the users BAC is over 0.08 it will display the amount of time they must wait befeore their BAC is below 0.08. Once the required time has been waited, and without adding any more drinks to their system, the user can check the BAC/time until drive variables to ensure they are legally safe to drive!


\*\*\***A copy of your code should be in your Lab 2 Github repo.**\*\*\*

After you edit and work on the scripts for Lab 2, the files should be upload back to your own GitHub repo! You can push to your personal github repo by adding the files here, commiting and pushing.

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ git add .
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ git commit -m 'your commit message here'
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ git push
```

After that, Git will ask you to login to your GitHub account to push the updates online, you will be asked to provide your GitHub user name and password. Remember to use the "Personal Access Tokens" you set up in Part A as the password instead of your account one! Go on your GitHub repo with your laptop, you should be able to see the updated files from your Pi!


## Part F. 
## Make a short video of your modified barebones PiClock

\*\*\***Take a video of your PiClock.**\*\*\*


https://user-images.githubusercontent.com/112603386/189817296-048ba211-72c2-4471-9c19-7f4fd51481be.mov



## Part G. 
## Sketch and brainstorm further interactions and features you would like for your clock for Part 2.
![further](https://user-images.githubusercontent.com/112603386/189817325-3aa5165f-c26c-4aa0-b9ae-14dd2647d4c7.jpg)


# Prep for Part 2

1. Pick up remaining parts for kit on Thursday lab class. Check the updated [parts list inventory](partslist.md) and let the TA know if there is any part missing.
  

2. Look at and give feedback on the Part G. for at least 2 other people in the class (and get 2 people to comment on your Part G!)
  Vikram, James, Jackson Feedback: Vik: make the text more readable - possibly display the text on different pages. Make it bigger and separated. James: truncate the values so it is more easily readable. JAckson create a limit of youve drinken too much.

# Lab 2 Part 2

Pull Interactive Lab Hub updates to your repo.

Modify the code from last week's lab to make a new visual interface for your new clock. You may [extend the Pi](Extending%20the%20Pi.md) by adding sensors or buttons, but this is not required.

As always, make sure you document contributions and ideas from others explicitly in your writeup.

You are permitted (but not required) to work in groups and share a turn in; you are expected to make equal contribution on any group work you do, and N people's group project should look like N times the work of a single person's lab. What each person did should be explicitly documented. Make sure the page for the group turn in is linked to your Interactive Lab Hub page. 

Idea:

The idea behind this design is a clock that keeps track of blood alcohol content for someone drinking alcohol. Often times people get carried away during a night out on the town, and this can lead to dangerous drivers. The device will first prompt the user to input their weight starting from 100 lbs. The user can use the right button to raise the weight input, and left button to lower the weight. Once the user weight is accurately depicted, they click both buttons to save the weight. Users will then click the left button each time they drink 1 drink. The device will show the message "drink logged" to show user that the drink has been successfully logged into the device. The user will click the right button to display the current BAC, time, amount of drinks consumed, and wait time until it is safe to drive. This BAC equation is based on a 5% 12 oz beer, so if it is a "double" mixed drink the user will log 2 drinks.  At any point even before the users first drink, they can click the left button on the device to check their current BAC. If it is below 0.08 (the legal driving limit), the device will read you must wait 0min to drive - meaning they are legally safe to drive. If the users BAC is over 0.08 it will display the amount of time they must wait befeore their BAC is below 0.08. If their BAC gets above a certain threshold, the user is prompted to call a cab instead of waiting out the time to sober up. The user is given a number to call for taxi service. If the user has not reached this threshold, once the required time has been waited, and without adding any more drinks to their system, the user can check the BAC/time until drive variables to ensure they are legally safe to drive! My final iteration of the device design has a hole in the housing so the user can either wear this device as a necklace, or attach it to their keychain.


Story Board:

![storyboard](https://user-images.githubusercontent.com/112603386/191174122-bea4457e-2a53-4f1c-b588-845414eec552.jpg)



Device Design Iterations:

Iteration 1
![iteration1](https://user-images.githubusercontent.com/112603386/191172221-267a6da3-1486-4353-b714-0e2e8435df4a.jpg)
This is my first iteration of my device. It displays the BAC and can log drinks, but it uses a simple BAC formula that is based on the average male weight of 150 lbs.


Iteration 2
![iteration2](https://user-images.githubusercontent.com/112603386/191173153-6a3b2f3a-73fc-4b52-8084-d7ecc7add542.jpg)
This is the second iteration of my device. It has now incorporated a first screen to prompt the user to input their correct weight. Once the user has set this input correctly, they press both buttons simultaneously to go to the next screen. The weight is set with knobs that can be turned. The knobs also function as buttons to interact with the second screen phase of the device, which operates the same as the first.


Iteration 3
![iteration3](https://user-images.githubusercontent.com/112603386/191173352-2f6a581d-d75c-4da6-86f7-a86510a52717.jpg)
This is the final and best iteration of my device. I have gotten rid of the knobs for pure buttons, because that overcomplicates this device. The simplicity of the buttons for weight input is just as effective as the knobs, and makes the device slimmer. The housing now has a hole in the top so the user can put a necklace chain through the hole, or put the device on their keychain for convenience. Because the device is now vertically oriented, the buttons have been moved to the bottom. The screens operate the same as the second iteration.

User Test:
https://user-images.githubusercontent.com/112603386/191173769-be988722-af38-4294-bb1e-4905e2809a9c.mov

This is a user test for my device. The user can be seen in a simulated scenario of drinking alcohol. After each drink they consume, they log the drink in the device. After each drink they can check their current BAC and wait time until it is safe to drive. The BAC and time can be seen ticking down based on data pulled from the clock. This test was filmed before I added the weight screen so I will show that below. I have included the feedback of spacing out the wait time text to make it easier to read. I have also included a threshold response, where the device prompts the user to call a cab if they have had too much to drink and it will take too long to sober up.

Dev User Test:

https://user-images.githubusercontent.com/112603386/191174167-4541d7a5-c84b-4372-9bfa-de079394f9ef.mov

This is another user test for my device. You can see the device initially prompts the user for a weight input, and once set I press both buttons at the same time to advance to the next screen. Here I use the device in teh same way as the initial user test, except now the BAC calculation is more accurate.


Feedback:
My user tester, Jackson Reimer, gave me some good feedback. The feedback was that I should use pictures because users that are inibriated above the threshold will likely not be able to read as clearly as completely sober people. If I added a taxi image instead of pure text it would be easier to use for the intended user.

I ran into trouble trying to implement this feedback - I was able to display a picture of a taxi but when I tried to add text to this it would not display. For future iterations of this device I would debug the display so I could put a full screen picture of a taxi and display text over this image to give the user a phone number of the taxi service. 






