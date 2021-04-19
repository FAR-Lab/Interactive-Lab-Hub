# Observant Systems




## Prep


### For the lab, you will need:



### Deliverables for this lab are:
1. Show pictures, videos of the "sense-making" algorithms you tried.
1. Show a video of how you embed one of these algorithms into your observant system.
1. Test, characterize your interactive device. Show faults in the detection and how the system handled it.


## Overview


### Part A
### Play with different sense-making algorithms.

#### OpenCV

#### Filtering, FFTs, and Time Series data.

#### Teachable Machines (beta, optional)


#### PyTorch  


### Part B
### Construct a simple interaction.

**Describe and detail the interaction, as well as your experimentation.**

I am creating a system to monitor when the best spot on the couch is open. This way, if you're at a house party and having a good time talking to people, but are waiting to sit down, you dont need to constantly walk to the other part of the room to check the couch. You just look at the screen closest to you, and it will tell you whether or not the spot is available. The camera will be focused on the primary spot. If it detects a person, it will say that the spot is taken, however if it does not, it will say that the spot is available.

While experimenting, I noticed that the camera was displaying all sorts of objects at first. I kept playing around with the focus/resolution to make the window it was looking at smaller. Eventually, I made it so narrow that it wouldn't name any objects at all and wouldn't draw a box around them, but the text output for the system would change to recognize whether or not a person was on the couch. This was a cleaner way of doing it, although a bit of a hack. I also moved the camera closer to the spot, so that the window of the camera lens was smaller.

### Part C
### Test the interaction prototype

Now flight test your interactive prototype and **note your observations**:
For example:
1. The system does what it's supposed to do when there is no one on screen, or when a person is sitting in the spot. However, it breaks when someone is on screen but not in the spot.
2. It fails when there is a person on the screen, but not in the spot. So if there is no person on the screen it will say that the spot is open, but if there's       a person anywhere on the screen it will say the spot is taken, even though they're not necessarily in spot and the spot may still be available.
3. It fails because the focus/resolution or frame is not narrow enough. It's picking up everything in the lens, not just the specific spot on the couch. It also fails because it is recognizing parts of a human as a person, even though the whole person may not be pictured. therefore it's pickup up a hand or part of a head, when in reality the person's whole body would be captured if they were in the spot.
4. Although I did not have multiple people to try this with, I think if there were a lot of people at a party, too many people could end up in the frame at once, or someone may block the camera, cause it to think the spot is available when it is not, because it's not seeing a human being. Additionally, if there are other random objects in the background it may recognize them as people and fail.

**Think about someone using the system. Describe how you think this will work.**
1. I think if someone was actually using the system they would instantly be aware of the uncertainties, since you can see both the alert and the camera feed on the same screen. This way, if the camera says the spot is unavailable, they'll still be able to see that no one is sitting in it. Additionally, if they see that someone is walking around and in motion it will catch their eye, so they'll realize it's open before the notification tells them.
2. I don't think they would be impacted too negatively by a miss classification. At the end of the day, the purpose of the device is to keep you informed as to whether or not the good spot on the couch is open without you having to constantly walkover and check. This way with a quick glance at the screen you can see whether or not the spot is open. The written and colored text alert is nice because it grabs your attention when something changes and makes it easier to notice when you're mid-conversation. However, you'd probably notice the person getting up from the spot and walking away anyway, and would know if the spot is open. That being said, if I build it later on to not have the camera feed, and just be an alert, or a light somewhere in your apartment, then it would need to be more exact.
3. I need to narrow down the window that the camera is searching in. I could do this through coding, or alternatively I could move the camera closer to the spot so that it is the only thing it is capturing.
4. Yes, I could make it so that the camera only recongizes a person when the person's full body is picture, and not just a part of the body, this way you know they're fully in the seat.

### Part D
### Characterize your own Observant system

As shown, the device can be used for determining whether or not someone is in the good spot on the couch. The screen can be displayed anywhere else in the home or the apartment, and will tell someone in a different area or room if the spot is open. A good environment for this is big spaces where the couch is far away or hidden from other parts of the party. A bad environment is one where there are tons of people and the spot may get filled before the person who sees the alert is able to get there. It will break if someone is in the camera frame (even partially) but not in the spot. The system in its current form allows you to also see who the person is that's sitting there, if they're about to get up, or if they're actually on screen and not in the spot (indicating that the system is wrong). It feels like a very neat and simple solution to a common problem at house parties. However, it could probably be done more simply with a colored light, a text alert on your phone, or just the alert on the screen and no camera feed. For this to happen, the model would need to be trained more accurately and the window of the camera would need to be more narrow.

**Include a short video demonstrating the answers to these questions.**

https://drive.google.com/file/d/1wjtAtYutlEK6VfAyCYm68JLUFCgCeeLA/view?usp=sharing


