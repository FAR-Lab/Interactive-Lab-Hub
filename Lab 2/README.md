# Interactive Prototyping: The Clock of Pi

Does it feel like time is moving strangely during this semester?

For our first Pi project, we will pay homage to the [timekeeping devices of old](https://en.wikipedia.org/wiki/History_of_timekeeping_devices) by making simple clocks.

It is worth spending a little time thinking about how you mark time, and what would be useful in a clock of your own design.

Reference:
[Adafruit Official Tutorial to MPU6050 Sensor](https://github.com/adafruit/Adafruit_CircuitPython_MPU6050)

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
### Setup Personal Access Tokens on GitHub
## Part B. 
### Try out the Command Line Clock
### Hardware (you have done this in the prep)
### Testing your Screen
#### Displaying Info with Texts
#### Displaying an image
## Part D. 
### Set up the Display Clock Demo
### How to Edit Scripts on Pi
## Part E.
### Modify the barebones clock to make it your own

Does time have to be linear?  How do you measure a year? [In daylights? In midnights? In cups of coffee?](https://www.youtube.com/watch?v=wsj15wPpjLY)

Can you make time interactive? You can look in `screen_test.py` for examples for how to use the buttons.

**We strongly discourage and will reject the results of literal digital or analog clock display.**

\*\*\***A copy of your code should be in your Lab 2 Github repo.**\*\*\*

[lab2 code update](https://github.com/xuanyufang/Interactive-Lab-Hub/blob/Fall2021/Lab%202/lab2.py)


## Part F. 
## Make a short video of your modified barebones PiClock

During my time at undergraduate in the south, my friend and I always drove out for dinner. We always played the same album, Sgt. Pepper's lonely heart club's Band, which is also our favorite album of all time, when we were driving. The full length of the album is 40 mins, and it became our way of measuring time -- McDonald is about half album away, Five Guys is three songs away, and Krispy Kreme is one album and five songs away. During driving, we hardly actual notice time, we just play the song and consider it to be a special time measurement to us, and I believe many people had the same experience. In this lab, I draw my idea from that experience and designed this clock that describe time in a non-linear way. It tells people how many repeat of the album since today's beginning, and precice to which song it should be at right now. I include a progress bar that would be able to be concise on exact progress of this song. This is exactly like a clock, but with a different way of measuring time non-linearly. I used my favorite album here, but it can be personalized for each user with different albums in terms of length of time. 

The interaction I designed is related to button's position. The upside button will lead to what was the last song (to help the clock user better remember what position the current song is at in the whole album), while the downside button will lead to what will be the next song, and how many more repeats of the album and song till the end of the day.



\*\*\***Take a video of your PiClock.**\*\*\*

[![image](https://user-images.githubusercontent.com/42874337/134100917-6621c56c-6453-4576-81cf-6ab83e42ed06.png)](https://drive.google.com/file/d/12Af0Er_XnjjHDnK-HLhMqPCxmMhwnGjN/view?usp=sharing)


## Part G. 
## Sketch and brainstorm further interactions and features you would like for your clock for Part 2.

I have thought of a couple of ways this can be improved, not only the interface, but also its interaction ways. For example, I can implement a new button combination to signal the device to change its album selection to measure time, or maybe even a pool that can let user to select from.

![image](https://user-images.githubusercontent.com/42874337/134107567-c0f7d10b-ac6b-48c2-9212-5c4d6b844daf.png)

Another idea is that I can attach a sound unit to it and when the user want to hear the song that currently suggesting the time, they can press both buttons to play the music. Or even include an alarm system that would allow user to set up alarm to wake up, not according to time, but according to songs or albums length, then when the time arrives, the device automatically plays the current song's current clip associated with the exact time.

![image](https://user-images.githubusercontent.com/42874337/134107584-4814d79b-1aae-4273-9e67-4d6704007c68.png)


# Prep for Part 2

**Feedback from classmates and TAs:**




# Lab 2 Part 2

**Sensor Added:
**

Adafruit CircuitPython MPU 6050 - Gyro, Acceleration, and Temperature Sensor

**Description:
**

[![image](https://user-images.githubusercontent.com/42874337/135004460-2b4c486b-dc89-4630-981b-acc550671419.png)](https://drive.google.com/file/d/12edV-qaVkllJe7w_ayZOtPTRJnxt7PWb/view?usp=sharing)


