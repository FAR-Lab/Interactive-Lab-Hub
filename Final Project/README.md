# Interactive-Devices-Final-Project

Sam Willenson: https://github.com/swillenson/Interactive-Lab-Hub

Rahul Sahetiya: https://github.com/RSAHETIYA/Interactive-Lab-Hub

## 1. Project plan: Big idea, timeline, parts needed, fall-back plan.

### Big Idea:

We will be creating two pianos that will be linked together to facilitate a teaching experience. Keys played on one piano will translate into LEDs turning on above the keys of the other piano, and vice versa. The theory and motivation behind this is that learning music can be difficult. By seeing explicit LEDs light up above each key on a keyboard, it will make it much easier for a musician to learn songs, whether they are a beginner or an advanced player. Beginners will be able to use this device by having an instructor show them where to place their fingers, while the students are still looking down at their own hands. Currently, students have to take their eyes off of their own instrument to learn which notes to play which can hinder the ability of a student to learn quickly and effectively. Advanced musicians can use this device to more easily communicate what notes they are playing to each other, or help a musician if they are lost during a song. In the future, we intend to add a secondary mode to these pianos, where users can play a game of musical Simon using the keyboards. This adds another way to interact with the devices, as well as a gamification twist on standard education methods. Simon can be used as a way to test students’ ability to add onto a group of notes and stay within key.

### Timeline:

1. Week 1 (11/15 - 11/22): Make sure all parts needed are available/ order parts that are not readily available Look into music libraries and communication protocols to use Design both keyboards and possibly start prototyping

2. Week 2 (11/22 - 11/29) - “Demonstrate that your project is functioning well enough for somebody to use and interact with it. This presentation will just be to the teaching team.” Finish writing code for music functionality of piano Finish writing code for LED representations Complete building two rough prototypes of pianos Demonstrate functionality with one “teaching” piano and one “learning” piano

3. Week 3 (11/29 - 12/6): Polish both prototypes Expand functionality to allow for teaching to work both ways Develop Simon game if time permits

4. Week 4 (12/6 - 12/13): Complete documentation and other written parts as needed

### Parts Needed:

The parts we are envisioning to use are:

- Hardware:
    - Cardboard
    - Laser cutter or normal cutting tools
    - Copper tape as electrolytic contacts
    - Capacitive touch sensor, Wire to route between sensor and contacts
    - LED lights (ideally x24 for full octave on both pianos)
    - 2x LCD screen, Speakers
- Software:
    - UDP or MQTT networking protocol
    - GPIO Pins
    - MusicalBeeps Library
    - MPR121 library

### Risks/Contingencies:

Multi-key press if user is not precise with playing motions (user accidentally touches note they do not intend to play i.e. pinky grazes a black key when going for a C note. This can trigger an unintended note to be played) Simon game proves too difficult to develop Can’t acquire all parts in time Program to control music functionality is inefficient causing a delayed sound Messaging protocol in use is very delayed/high latency

### Fall-back plan:

The biggest stretch for this project is making and implementing the Simon game functionality. If unable to, given our current plans, we should still be able to complete and polish two keyboards that have teaching/learning functionality. It also might not be feasible to implement the teaching/learning both ways, so we will need to fall back to one piano being dedicated for learning and the other piano being dedicated to teaching. If we encounter some errors with the capacitive touch sensing, it should still be possible to simulate a good key press system using normal buttons or maybe limit switches.


## 2. Functioning project: The finished project should be a device, system, interface, etc. that people can interact with.

The device was finished and works; we show several successful interactions in the sections below.

## 3. Documentation of design process

First we had to design our Piano Box, laser cut it, and glue it together. We went through multiple prototyping phases before settling in on a final design. 
![designs](/imgs/prototype_designs.jpeg)
We designed our box to have a base of 7 inches by 11 inches, with a height of 4 inches. We used finger edge joints so that each face of the box would fit together well. We cut the roof of the device in half so that we could give our device more of a piano look. This also let the front face of the device sit halfway into the depth of the box giving it the correct cosmetic look of a piano. The front face of the box has 12 holes for the LEDs to sit in. Each of these holes has to fit a 3mm diameter LED, so we made the holes 3.5 mm to account for error. Below is both an image of the vector file in addition to the intial assembly of the enclosure.

![boxVecotr](/imgs/enclosure_vector.png)

![emptyBox](https://user-images.githubusercontent.com/112603386/207697881-3df0dcbc-65dd-4b0e-9f24-cb697f526d99.jpeg)

The keys of our device extends from the back of the box to the front, hanging over the front of the base by around 2.5 inches. Again, this is to give our box the look and feel of a real piano. We had an idea for how to make the keys 3 dimensional, but after hitting a few roadblocks and time constraints, we chose to pivot to a 2-dimensional key implementation. Our keyboard was a piece of cardboard, cut to the dimensions of the box, that we hand-drew piano keys onto. Because we only used 12 keys we made the keys as big as they could be for the size of the housing. We then taped copper tape to the top side of our cardboard so we could attach a capacitive touch sensor to this keyboard. By then attaching alligator clips from the mpr121 capacitive touch sensor to each individual key, we are able to decipher the inputs from our users.

Next we had to add all of our LEDs to the product. The goal was to have a dedicated LED for each of the 12 keys in a musical octave, however due to the lack of available GPIO pins on each of our Raspberry Pis we ran into an issue. Our TFT screens (which are used to connect the raspberry pi to the mp121 capacitive touch sensor) were taking up some of these GPIO pins so we were left with only 9 per Raspberry Pi. To fix this issue we planned on implementing a decoder to split the logic from some of these GPIO pins to make the voltage levels control multiple LEDs.

Here are images of us soldering the decoder into the design:
![rahulSolder](https://user-images.githubusercontent.com/112603386/207697928-e46965c9-dac7-4272-afa0-d3eaf6409a40.jpeg)
![rahulSolder2](https://user-images.githubusercontent.com/112603386/207697944-68baeb96-61be-4764-ab2a-2d3b2b9b1086.jpeg)
![solderCloseup](https://user-images.githubusercontent.com/112603386/207697970-42d0a780-90ec-462d-a4c4-4adda17cc601.jpeg)

We are both eperienced at soldering, but we made one mistake - assuming the Maker Lab had Leaded solder. Because of the lack of Lead solder, this whole process proved to be more time consuming and difficult than originally expected. When our first board was finished, we tested the device to see if each LED can be powered on individually. Unfortunately, something unexpected was happening and we were getting unexpected LEDs turning on: for example LED 5 powering on when we want LED 2 on, and multiple LEDs powering on at the same time. 

To fix this issue we brainstormed how we might be able to pivot to not using the decoder. How could we best represent each of the 12 keys with only 9 available GPIO pins. We came up with an idea that would be symmetrical and evenly distributed across the board. Instead of having each note be represented by it's own individual LED, we will have only the white keys with LEDs housed above them. This way when a user hits a black key, this can be represented by the surrounding white keys to the left and right of this black key light up. Now single LEDs represent white keys, and double LEDs represent black keys (in the middle of the 2 LEDs).

![wiring](imgs/wiring.jpeg)

After we figured this out we cut a hole in the back of our piano boxes to be able to snake out the power cord and webcam (which is used as a speaker for this device) cables out of the back.

Now we attached the LEDs on the protoboards to the inside of the front face of our board, taped them down to be secure, and fit in the Raspberry Pi with all the alligator clips attached to a MFR capacitive touch sensor board. 

![front](/imgs/front_view.jpg)
![side](/imgs/side_view.jpg)
![internal](/imgs/internal_view.jpg)
![bothNoTop](https://user-images.githubusercontent.com/112603386/207701128-3e72a2a3-2f06-410e-983f-fbf2c40d9311.jpeg)

Next we use an mpr121 capacitive touch sensor. With all the alligator clips attached to our copper 2D piano keys, we are ready to test. During the testing process we tweaked our code mutiple times to account for different issues. While the pianos worked perfectly fine by themselves, there did seem to be an issue with sending data between both. Originally during our previous testing phase, we had used UDP with a deidcated reciever and transmitter. However, one we had both pianos transmitting and recieving, there turned out to be some issues as it is difficult under the UDP protocol to send and recieve at the same time. This is due to the fact that both pianos are essentially clients and servers. To remedy this, we switched to using the MQTT protocol as Cornell has a dedicated broker which can handle all intermediary communication.

https://user-images.githubusercontent.com/112603386/207701316-f26428f6-9e98-4399-bb6e-1b2f7bd7c155.mp4

We can see above that the design is working properly. The LEDs all work and when a black key is pressed the 2 surrounding LEDs light up at the same time.

## 4. Archive of all code, design patterns, etc. used in the final design. (As with labs, the standard should be that the documentation would allow you to recreate your project if you woke up with amnesia.)

With respect to the components used in the final design, there are two: the enclosure and code powering the project. The .svg (vector file) of the enclosure is located [here](/enclosure/box2.0.svg) and the final version of the code is located [here](/src/final_project.py). There were other parts to the project, and they are covered extensively in the previous documentation section.

## 5. Video of someone using your project

Here is a storybaord of how an intended interaction would look like:

![pianoStoryboard](https://user-images.githubusercontent.com/112603386/208217610-31778336-420b-4e92-ad8a-a2959d0a41bd.png)

We have had many people test our product, and should have filmed more of them! We did capture two encounters however.
  
Here is a demo video of how an interaction can work to teach someone the C Blues scale on a piano without looking at each other hands, only using the device as intended:


https://user-images.githubusercontent.com/112603386/208215125-62527cbc-b175-450a-87de-98e385223295.mov

Below is a test with one user where the video unfortunately starts after I tought our user the C Blues scale using the LEDs and him not looking at my fingers. While this part of the interaction was not captured, the second half of our interaction was captured where we are still both interacting with each piano and I am showing him more functionality of how the piano can arpeggiate notes in a fun way.

https://user-images.githubusercontent.com/112603386/207703890-32ca8f64-c52b-4e9d-b117-49368c32c527.mov


Here is another user test where the user was unfortunately filming with a very low quality camera. However the interaction can still be seen:



https://user-images.githubusercontent.com/112603386/207704002-e08ac922-6cd1-4f9e-933d-ad9c8a11f371.mp4



## 6. Reflections on process (What have you learned or wish you knew at the start?)
We learned that sometimes people get excited about unintended outcomes of a project. Because the musical library we used to form the synth sounds did not play multiple notes at once, we used a loop to continuosly loop through sounds when a user plays a chord. This made an arpeggiated chord instead of a continuous one. This was a workaround for us to be able to play all the notes someone presses as long as they hold the chord out long enough for the code to loop through each held note. However, we learned when user testing that this was often a favorite feature of our users. It made them feel more talented at piano because of how fast the notes were playing. One lesson learned here is how important user testing is; what was a side feature to us the designers was a showcase feature to the users themselves.

We also learned that detailed planning before the start of an experiment is extremely important. While we did prototype before we started laser cutting, there were a few things we overlooked. We forgot to add a slot to snake out the power cords and webcam cords. This was fine in the end but we had to make a cut by hand, it could have been much more precise if we designed this into our laser cutting file.

We also learned to to efficiently have 2 raspberry pis communicate wirelessly with one another. While we did experiment with UDP and other network protocols, we did eventually end up going back to MQTT as it was lightweight and easy to use based on past experience. Further than this project that functionality can have many implications with very neat use cases. 

One thing we wish we knew at the start of the project was that our implementation of the decoder would not end up working. We spent a long time trying to get the decoder working and in the end had to pivot and think of a creative way to signify each key individually using a maximum of 9 GPIO outputs which corresponds to 9 LEDs that we can toggle on/off. If we knew that time spent on the decoder would be for nothing, we would have used that time to make our keys 3 dimensional rather than 2 dimensional with copper tape. We believe the 3 dimensional keys would have made the user experience with our device more interactive and fun.

Another thing we wish we knew was how important having the higher octave C note would be. We only had 12 keys meaning we had one key for every note in a chromatic scale, however many songs use 2 of the same note. We wish we would have added more keys but this was difficult due to the mpr121 sensor only having 12 inputs as well as our bottleneck on GPIO pins.

Overall, we believe that while we did fail to implement some aspects of our project plan that would have enhanced the overall user experience, we did come up with some creative workarounds that eventually led to a final project we are proud of.

## 7. Group work distribution questionnaire
Both of us, Sam and Rahul, shared the work on all aspects of the project. We both talked about the idea behind the product, we both talked about what parts to order, we both worked on the code, we both worked on the housing, we both worked on the soldering, we both worked on the spacing of the LEDs, we both worked on the actual taping of the copper tape to the piano keys, and we both tested with users seperately. While distribution of each task was not entirely equal, we did play to our respective strengths to be more efficient. We communicated early and often, and overall, the team was a success.
