# Pre Lab 5
For next week's lab, we'll be making useless boxes. For the lab, we'll have readymade files for you to customize and laser cut. However, we'd like you to take a moment to think about how to make a box with a hinged lid. 
1. Take a look at this [useless box example](https://makezine.com/projects/the-most-useless-machine/) and try to create one out of paper in less than 30 minutes. 
1. Where will the switch, Arduino, and servo go? 
1. Submit a picture of your paper prototype! Bonus points if you submit a timelapse of the process. 


[[paper-prototype.jpg]]



# Integrated Interactive Device

***

For this week’s lab, you will design and build an autonomous device that incorporates:

* Physical Fabrication
* Actuation
* Sensing/Input
* Timing
* Sound

As a guide, we have included instructions to get you most of the way through designing a Jack-in-a-Box. Feel free to explore alternatives to the basic design. For example, if you turn the box on its side, you could have a mouse trap, or a cat door. 


## In the report
Show photos and a video of your final design in action.

Include your sketches and designs for your device, including for ideas you didn't pursue this time.


## Basic Cardboard Box construction

Building off of the strip box from [Lab 3](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/wiki/Lab-03), this box design is built from two cardboard strips that are the same width X.

This design can be made by scoring two long strips of corrugated cardboard of width X, with the following measurements:

| <---- X ----> <br> <sub><sup>+ thickness of cardboard</sup></sub> | <---- X ----> |
| --- | --- | --- | 

| <---- X ----> | <---- X ----> | <---- X ----> | <---- X ----> |
| --- | --- | --- | --- |


Use an Olfa knife with a cutting mat to cut out your pattern, using 2 cuts to score the cardboard strip at the bends and 3 cuts to cut. (A second mat can be used as a straight edge, and you can use one strip to measure out X on the other.)

![](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/Lab5/images/IMG_0550.jpeg?raw=true)

Fold the flaps up, and cut the as necessary to level the sides. 

Hot glue the two pieces in a 't', with the 3-segment strip on the bottom. You have a few seconds, while the glue is hot, to make sure the pieces are lined up correctly before the glue cools and sets.  The weight of the double cardboard bottom helps to make the box stable.

![](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/Lab5/images/IMG_0552.jpeg?raw=true)
![](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/Lab5/images/IMG_0553.jpeg?raw=true)

On the side flap where you plan to mount the servo motor, use a bead of hot glue along the edge to join the flaps together. Hold the flaps for a few seconds until the hot glue sets. 

![](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/Lab5/images/IMG_0554.jpeg?raw=true)

DO NOT GLUE THE OTHER SIDE FLAP. 

## Make a cardboard servo motor mount

The cardboard mount holds the servo motor against the side of the box. 

![](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/Lab5/images/IMG_0555.jpeg?raw=true)

This can be made with strip of cardboard scrap of width X, where X > the height of the servo motor

| F length of flap | D <br><sub><sup>= depth of servo to the flange</sup></sub> | W width of the servo <br><sub><sup>+ two cardboard thicknesses</sup></sub> | D <br><sub><sup>= depth of servo to the flange</sup></sub> | F length of flap|
| --- | --- | --- | --- | --- | 

Cut a square hole in the middle of the strip for the rectangular face of the servo to fit through.

Hot glue the flaps and the back of the servo and stick this in the back corner of the box, with the pivot of the servo near the lid. As before, you will need to hold things in place for a bit while the hot glue sets.

![](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/Lab5/images/IMG_0556.jpeg?raw=true)![](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/Lab5/images/IMG_0557.jpeg?raw=true)

** include a photo of your box and servo mount **

## Make the service panel for your box. 

Check to make sure your breadboard and battery fit in. To make programming easier, orient things so the USB cable faces the open side of the box. 

![](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/Lab5/images/IMG_0558.jpeg?raw=true)

Use shipping tape to make slick patches on the sides of the box, and use removable blue tape (with the ends folded under to make grab tabs) to make a reclosable service panel for your box.

![](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/Lab5/images/IMG_0559.jpeg?raw=true)
![](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/Lab5/images/IMG_0560.jpeg?raw=true)![](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/Lab5/images/IMG_0561.jpeg?raw=true)

** include a photo of your box closed  **


## Electronics

![electronics circuit](https://user-images.githubusercontent.com/54110697/64988326-35758180-d899-11e9-9473-b1610101d91b.jpg)

Tip: If you don't have the 9V connector, you just need to make sure that the micro controller is plugged into your computer, for power. 

### Program your device

Load the [example](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2019Fall/Lab5/JackInABox.ino) previously downloaded.

You can also make your own program but make sure you put HIGH digital value to pin 5 if you connected the circuit as the one in the electronics part.

Pay attention that you can change the position of close and open box in the following lines:

#define closePos  10

#define openPos   110


## Make your box open using the servo motor

You'll have to hot glue an arm to the servo motor arm to push back the lid. How should that arm be designed?

** include a photo of your arm design  **

## Putting it all together
***
Think about where each component should go, and assemble your box so that the servo motor opens the box.

** include a video of the box opening  **

## Create Jack

Using cardboard, paper, or found objects, make a jack that pops out when the top opens. 

Here are useful links:

[How to make a paper spring](https://bookzoompa.wordpress.com/2010/03/14/how-to-make-a-paper-spring/)
[How to Use Slicer to make 3D shapes using stacked slices of laser (or Olfa) -cut cardboard](https://core-electronics.com.au/tutorials/using-slicer-for-fusion360-for-laser-cutting-tutorial.html)

** include drawings, sketches or links to any part files used for creating Jack   **

** include a video of the finished design   **

## Lab Submission
***
For your write up, include:
1.	Your Arduino code.
2.	.stl or .svg files for your Jack — if you use some other technique, include the respective supporting material.
3.	At least one photo-studio-quality photo of your box closed, and another photo of your box open. 

4.	A video of your box in action.
