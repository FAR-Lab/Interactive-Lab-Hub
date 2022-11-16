Final Project Team Members: Sam Willenson (shw58), Rahul Sahetiya (rs2248)

Final Project Presentation Slide:
![IDD Final Project Slide](https://user-images.githubusercontent.com/112603386/201853861-d8a84505-fe94-40c7-b983-9b27b2513f48.png)

Project Plan:

Big Idea:

We will be creating two pianos that will be linked together to facilitate a teaching experience. Keys played on one piano will translate into LEDs turning on above the keys of the other piano, and vice versa. Eventually, we intend to add a secondary mode to these pianos, where users can play a game of musical Simon using the keyboards. This adds another way to interact with the devices, as well as a gamification twist on standard education methods. Simon can be used as a way to test students’ ability to add onto a group of notes and stay within key. 

Timeline:

Week 1 (11/15 - 11/22): 
Make sure all parts needed are available/ order parts that are not readily available
Look into music libraries and communication protocols to use
Design both keyboards and possibly start prototyping

Week 2 (11/22 - 11/29) - “Demonstrate that your project is functioning well enough for somebody to use and interact with it. This presentation will just be to the teaching team.”
Finish writing code for music functionality of piano
Finish writing code for LED representations
Complete building two rough prototypes of pianos
Demonstrate functionality with one “teaching” piano and one “learning” piano

Week 3 (11/29 - 12/6):
Polish both prototypes
Expand functionality to allow for teaching to work both ways
Develop Simon game if time permits

Week 4 (12/6 - 12/13):
Complete documentation and other written parts as needed

Parts Needed:

The part we are envisioning to use are:
Cardboard
Laser cutter or normal cutting tools
Copper tape as electrolytic contacts
Capacitive touch sensor
Wire to route between sensor and contacts
LED lights (ideally x24 for full octave on both pianos)
2x LCD screen
Speakers

Risks/Contingencies:

Multi-key press if user is not precise with playing motions (user accidentally touches note they do not intend to play i.e. pinky grazes a black key when going for a C note. This can trigger an unintended note to be played)
Simon game proves too difficult to develop
Can’t acquire all parts in time
Program to control music functionality is inefficient causing a delayed sound
Messaging protocol in use is very delayed/high latency

Fall-back plan:

The biggest stretch for this project is making and implementing the Simon game functionality. If unable to, given our current plans, we should still be able to complete and polish two keyboards that have teaching/learning functionality. It also might not be feasible to implement the teaching/learning both ways, so we will need to fall back to one piano being dedicated for learning and the other piano being dedicated to teaching. If we encounter some errors with the capacitive touch sensing, it should still be possible to simulate a good key press system using normal buttons or maybe limit switches. 

