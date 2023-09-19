# Interactive Prototyping: The Clock of Pi
**Kenneth Lee (kml343), Gloria Hu (rh692), Yifan Yu (yy2253)**

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
  Interactive-Lab-Hub $ git pull upstream Fall2023
  ```
  
  The reason why we are adding a upstream with **course lab-hub** instead of yours is because the local Interactive-Lab-Hub folder is linked with your own git repo already. Try typing ``git remote -v`` and you should see there is the origin branch with your own git repo. We here add the upstream to get latest updates from the teaching team by pulling the **course lab-hub** to your local machine. After your local folder got the latest updates, push them to your remote git repo by running:
  
  ```
  Interactive-Lab-Hub $ git add .
  Interactive-Lab-Hub $ git commit -m "message"
  Interactive-Lab-Hub $ git push
  ```
  Your local and remote should now be up to date with the most recent files.

The new GitHub.com UI makes this step easy from the webbrowser:
![image](https://github.com/FAR-Lab/Interactive-Lab-Hub/assets/90477986/91d0fbc8-2eba-401f-a5a7-66640910cb62)


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
Just like you did in the lab prep, ssh on to your pi. Once you get there, create a Python environment (named venv) by typing the following commands.

```
ssh pi@<your Pi's IP address>
...
pi@raspberrypi:~ $ python -m venv venv
pi@raspberrypi:~ $ source venv/bin/activate
(venv) pi@raspberrypi:~ $ 

```
### Setup Personal Access Tokens on GitHub
Set your git name and email so that commits appear under your name.
```
git config --global user.name "Your Name"
git config --global user.email "yourNetID@cornell.edu"
```

The support for password authentication of GitHub was removed on August 13, 2021. That is, in order to link and sync your own lab-hub repo with your Pi, you will have to set up a "Personal Access Tokens" to act as the password for your GitHub account on your Pi when using git command, such as `git clone` and `git push`.

Following the steps listed [here](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token) from GitHub to set up a token. Depends on your preference, you can set up and select the scopes, or permissions, you would like to grant the token. This token will act as your GitHub password later when you use the terminal on your Pi to sync files with your lab-hub repo.


## Part B. 
### Try out the Command Line Clock
Clone your own lab-hub repo for this assignment to your Pi and change the directory to Lab 2 folder (remember to replace the following command line with your own GitHub ID):

```
(venv) pi@raspberrypi:~$ git clone https://github.com/<YOURGITID>/Interactive-Lab-Hub.git
(venv) pi@raspberrypi:~$ cd Interactive-Lab-Hub/Lab\ 2/
```
Depends on the setting, you might be asked to provide your GitHub user name and password. Remember to use the "Personal Access Tokens" you just set up as the password instead of your account one!


Install the packages from the requirements.txt and run the example script `cli_clock.py`:

```
(venv) pi@raspberrypi:~/Interactive-Lab-Hub/Lab 2 $ pip install -r requirements.txt
(venv) pi@raspberrypi:~/Interactive-Lab-Hub/Lab 2 $ python cli_clock.py 
02/24/2021 11:20:49
```

The terminal should show the time, you can press `ctrl-c` to exit the script.
If you are unfamiliar with the Python code in `cli_clock.py`, have a look at [this Python refresher](https://hackernoon.com/intermediate-python-refresher-tutorial-project-ideas-and-tips-i28s320p). If you are still concerned, please reach out to the teaching staff!


## Part C. 
### Set up your RGB Display
We have asked you to equip the [Adafruit MiniPiTFT](https://www.adafruit.com/product/4393) on your Pi in the Lab 2 prep already. Here, we will introduce you to the MiniPiTFT and Python scripts on the Pi with more details.

<img src="https://cdn-learn.adafruit.com/assets/assets/000/082/842/large1024/adafruit_products_4393_iso_ORIG_2019_10.jpg" height="200" />

The Raspberry Pi 4 has a variety of interfacing options. When you plug the pi in the red power LED turns on. Any time the SD card is accessed the green LED flashes. It has standard USB ports and HDMI ports. Less familiar it has a set of 20x2 pin headers that allow you to connect a various peripherals.

<img src="https://maker.pro/storage/g9KLAxU/g9KLAxUiJb9e4Zp1xcxrMhbCDyc3QWPdSunYAoew.png" height="400" />

To learn more about any individual pin and what it is for go to [pinout.xyz](https://pinout.xyz/pinout/3v3_power) and click on the pin. Some terms may be unfamiliar but we will go over the relevant ones as they come up.

### Hardware (you have already done this in the prep)

From your kit take out the display and the [Raspberry Pi 4](https://cdn-shop.adafruit.com/970x728/3775-07.jpg)

Line up the screen and press it on the headers. The hole in the screen should match up with the hole on the raspberry pi.

<p float="left">
<img src="https://cdn-learn.adafruit.com/assets/assets/000/087/539/medium640/adafruit_products_4393_quarter_ORIG_2019_10.jpg?1579991932" height="200" />
<img src="https://cdn-learn.adafruit.com/assets/assets/000/082/861/original/adafruit_products_image.png" height="200">
</p>

### Testing your Screen

The display uses a communication protocol called [SPI](https://www.circuitbasics.com/basics-of-the-spi-communication-protocol/) to speak with the raspberry pi. We won't go in depth in this course over how SPI works. The port on the bottom of the display connects to the SDA and SCL pins used for the I2C communication protocol which we will cover later. GPIO (General Purpose Input/Output) pins 23 and 24 are connected to the two buttons on the left. GPIO 22 controls the display backlight.

To show you the IP and Mac address of the Pi to allow connecting remotely we created a service that launches a python script that runs on boot. For the following steps stop the service by typing ``` sudo systemctl stop mini-screen.service```. Othwerise two scripts will try to use the screen at once. 

We can test it by typing 
```
(venv) pi@raspberrypi:~/Interactive-Lab-Hub/Lab 2 $ python screen_test.py
```

You can type the name of a color then press either of the buttons on the MiniPiTFT to see what happens on the display! You can press `ctrl-c` to exit the script. Take a look at the code with
```
(venv) pi@raspberrypi:~/Interactive-Lab-Hub/Lab 2 $ cat screen_test.py
```

#### Displaying Info with Texts
You can look in `screen_boot_script.py` and `stats.py` for how to display text on the screen!

#### Displaying an image

You can look in `image.py` for an example of how to display an image on the screen. Can you make it switch to another image when you push one of the buttons?



## Part D. 
### Set up the Display Clock Demo
Work on `screen_clock.py`, try to show the time by filling in the while loop (at the bottom of the script where we noted "TODO" for you). You can use the code in `cli_clock.py` and `stats.py` to figure this out.

![alt text](https://github.com/KennethLeeCornell/Interactive-Lab-Hub/blob/Fall2023/Lab%202/images/lab2aPartD.jpg)

### How to Edit Scripts on Pi
Option 1. One of the ways for you to edit scripts on Pi through terminal is using [`nano`](https://linuxize.com/post/how-to-use-nano-text-editor/) command. You can go into the `screen_clock.py` by typing the follow command line:
```
(venv) pi@raspberrypi:~/Interactive-Lab-Hub/Lab 2 $ nano screen_clock.py
```
You can make changes to the script this way, remember to save the changes by pressing `ctrl-o` and press enter again. You can press `ctrl-x` to exit the nano mode. There are more options listed down in the terminal you can use in nano.

Option 2. Another way for you to edit scripts is to use VNC on your laptop to remotely connect your Pi. Try to open the files directly like what you will do with your laptop and edit them. Since the default OS we have for you does not come up a python programmer, you will have to install one yourself otherwise you will have to edit the codes with text editor. [Thonny IDE](https://thonny.org/) is a good option for you to install, try run the following command lines in your Pi's ternimal:

  ```
  pi@raspberrypi:~ $ sudo apt install thonny
  pi@raspberrypi:~ $ sudo apt update && sudo apt upgrade -y
  ```

Now you should be able to edit python scripts with Thonny on your Pi.

Option 3. A nowadays often preferred method is to use Microsoft [VS code to remote connect to the Pi](https://www.raspberrypi.com/news/coding-on-raspberry-pi-remotely-with-visual-studio-code/). This gives you access to a fullly equipped and responsive code editor with terminal and file browser.  

Pro Tip: Using tools like [code-server](https://coder.com/docs/code-server/latest) you can even setup a VS Code coding environment hosted on your raspberry pi and code through a web browser on your tablet or smartphone! 

## Part E.
### Modify the barebones clock to make it your own

Does time have to be linear?  How do you measure a year? [In daylights? In midnights? In cups of coffee?](https://www.youtube.com/watch?v=wsj15wPpjLY)

Can you make time interactive? You can look in `screen_test.py` for examples for how to use the buttons.

Please sketch/diagram your clock idea. (Try using a [Verplank digram](http://www.billverplank.com/IxDSketchBook.pdf)!

![alt text](https://github.com/KennethLeeCornell/Interactive-Lab-Hub/blob/Fall2023/Lab%202/images/lab2aPartE.jpg)

**We strongly discourage and will reject the results of literal digital or analog clock display.**


\*\*\***A copy of your code should be in your Lab 2 Github repo.**\*\*\*

After you edit and work on the scripts for Lab 2, the files should be upload back to your own GitHub repo! You can push to your personal github repo by adding the files here, commiting and pushing.

```
(venv) pi@raspberrypi:~/Interactive-Lab-Hub/Lab 2 $ git add .
(venv) pi@raspberrypi:~/Interactive-Lab-Hub/Lab 2 $ git commit -m 'your commit message here'
(venv) pi@raspberrypi:~/Interactive-Lab-Hub/Lab 2 $ git push
```

After that, Git will ask you to login to your GitHub account to push the updates online, you will be asked to provide your GitHub user name and password. Remember to use the "Personal Access Tokens" you set up in Part A as the password instead of your account one! Go on your GitHub repo with your laptop, you should be able to see the updated files from your Pi!


## Part F. 
## Make a short video of your modified barebones PiClock

\*\*\***Take a video of your PiClock.**\*\*\*
[YouTube Video of our PiClock](https://www.youtube.com/watch?v=xxyKwtn9TNY)

## Part G. 
## Sketch and brainstorm further interactions and features you would like for your clock for Part 2.
![alt text](https://github.com/KennethLeeCornell/Interactive-Lab-Hub/blob/Fall2023/Lab%202/images/lab2aPartG.jpg)


# Prep for Part 2

1. Pick up remaining parts for kit on Thursday lab class. Check the updated [parts list inventory](partslist.md) and let the TA know if there is any part missing.
  

2. Look at and give feedback on the Part G. for at least 2 other people in the class (and get 2 people to comment on your Part G!)

Michael: I thought the interaction was really well done, and the amount of toggling between different units of time really impressed me. Maybe for a future feature, marking future dates could be useful in a “calendar” type of function.

Kevin: The clock is really innovative, and I love how the bottom bar counts the seconds. The choice of colors helped a lot to distinguish the hour, minute, and second.  

John: very interesting demo, I would recomand adding button interaction to the clock, for example if you click a button the color changes? or the background changes?

# Lab 2 Part 2

Pull Interactive Lab Hub updates to your repo.

Modify the code from last week's lab to make a new visual interface for your new clock. You may [extend the Pi](Extending%20the%20Pi.md) by adding sensors or buttons, but this is not required.

As always, make sure you document contributions and ideas from others explicitly in your writeup.

You are permitted (but not required) to work in groups and share a turn in; you are expected to make equal contribution on any group work you do, and N people's group project should look like N times the work of a single person's lab. What each person did should be explicitly documented. Make sure the page for the group turn in is linked to your Interactive Lab Hub page. 

# Interactive Prototyping: The Game of Pi

Gilberto Ruiz (ger83), Michael Hanlon (mph99), Kenneth Lee (kml343), Gloria Hu (rh692), Yifan Yu (yy2253)

# Part 1.
# Sketch and brainstorm further interactions and features you would like for your clock
# Ideation and Diagrams

![first image](https://github.com/Ruiznogueras05CT/Interactive-Lab-Hub/assets/142849822/7c300d80-4855-44c0-b40d-d2528adf6520)

The player must dodge asteroids for a duration of two minutes. By pressing two buttons, they can move up or down to evade them.

![second image](https://github.com/Ruiznogueras05CT/Interactive-Lab-Hub/assets/142849822/e5534783-c00c-4da3-aae7-44b2e4a27f0b)


This image depicts the player having successfully avoided the asteroids and continuing their movement.

![third image](https://github.com/Ruiznogueras05CT/Interactive-Lab-Hub/assets/142849822/242c7058-a0ac-43c9-9527-7d0f821808e1)

![fourth image](https://github.com/Ruiznogueras05CT/Interactive-Lab-Hub/assets/142849822/6c90dd25-07fd-447d-879f-55c6a01629d5)

In Scenario 1, if the player collides with any asteroid, an explosion occurs, it's a game over.

![fifth image](https://github.com/Ruiznogueras05CT/Interactive-Lab-Hub/assets/142849822/c36faf6f-092f-469c-bd20-215d456fcb9f)

![sixth image](https://github.com/Ruiznogueras05CT/Interactive-Lab-Hub/assets/142849822/1eb34749-a6ef-4b5e-8312-a228ea3382d3)

In Scenario 2, the player adeptly dodges the asteroids, swiftly toggling up and down

![seventh image](https://github.com/Ruiznogueras05CT/Interactive-Lab-Hub/assets/142849822/7427630a-1345-4265-9677-44a8d4de0fae)

After successfully evading all asteroids for the entire two minutes, the player wins!

# A Video for the Ideation
  
[https://github.com/Ruiznogueras05CT/Interactive-Lab-Hub/assets/142849822/20c5cb45-cfc0-463c-832a-8ceb9f3833a0]  
https://github-production-user-asset-6210df.s3.amazonaws.com/142931503/268519127-381b6d51-2dc6-4e0b-9ce4-f6261b349e4e.mp4    

   
https://github.com/gloriahu28/Interactive-Lab-Hub/assets/142931503/381b6d51-2dc6-4e0b-9ce4-f6261b349e4e

# Part G.
# Make a short video of your modified barebones PiClock

# Losing Example
In this situation, you're playing the game and crashed on one of the projectiles


[https://github.com/Ruiznogueras05CT/Interactive-Lab-Hub/assets/142849822/01a62e0d-2fb0-4a32-ab82-22375ef270aa]


# Win Example
In this situation, if you've survived for a minute, then you will score a point and the projectiles will move faster and change color

[https://github.com/Ruiznogueras05CT/Interactive-Lab-Hub/assets/142849822/ef73f220-5a90-4f48-8a5d-2b64557ce2cb]

# Code for game implementation in `game_test.py`
To run the game code, box2d-py must be set up with Conda: 
1) Download conda: wget https://github.com/conda-forge/miniforge/releases/download/23.3.1-1/Mambaforge-23.3.1-1-Linux-aarch64.sh
2) Make executable: chmod -v +x Mambaforge*.sh
3) Install conda: ./Mambaforge-23.3.1-1-Linux-aarch64.sh
4) Make conda environment with Box2D: conda create -n pybox2d -c conda-forge python=3.9 box2d-py
5) Activate conda environment: conda activate pybox2d
6) Install lab 2 requirements in conda environment: pip install -r requirements.txt
