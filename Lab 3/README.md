Teammate for this lab: Hongyu Shen (hs692)

# Chatterboxes

In this lab, we want you to design interaction with a speech-enabled device--something that listens and talks to you. This device can do anything *but* control lights (since we already did that in Lab 1).  First, we want you first to storyboard what you imagine the conversational interaction to be like. Then, you will use wizarding techniques to elicit examples of what people might say, ask, or respond.  We then want you to use the examples collected from at least two other people to inform the redesign of the device.

We will focus on **audio** as the main modality for interaction to start; these general techniques can be extended to **video**, **haptics** or other interactive mechanisms in the second part of the Lab.

## Prep for Part 1: Get the Latest Content and Pick up Additional Parts 

### Pick up Additional Parts

### Get the Latest Content

## Part 1.
### Text to Speech 

\*\***Write your own shell file to use your favorite of these TTS engines to have your Pi greet you by name.**\*\*

[link to name shell](https://github.com/xuanyufang/Interactive-Lab-Hub/blob/Fall2021/Lab%203/name.sh)


### Speech to Text

\*\***Write your own shell file that verbally asks for a numerical based input (such as a phone number, zipcode, number of pets, etc) and records the answer the respondent provides.**\*\*

[link to speech2text shell](https://github.com/xuanyufang/Interactive-Lab-Hub/blob/Fall2021/Lab%203/SpeechToText.sh)

### Serving Pages

### Storyboard

Our device is a voice interaction game. The player plays the role of a 911 operator who receives an emergency call asking for help. The other end of the phone call is a man who claims that he is trapped in a locked apartment and has lost all his memories. He asks for the player’s help to escape from the apartment. The man describes what he sees and lists out possible actions; the player instructs the man to conduct these actions by speech to move forward with the game. This game is suitable to be designed as a voice interaction game because it simulates a phone call in which the player does not have vision.

\*\***Post your storyboard and diagram here.**\*\*

![image](https://user-images.githubusercontent.com/42874337/135953990-cac7ddab-a51b-4716-b446-30f18f9c01f3.png)

![image](https://user-images.githubusercontent.com/42874337/135954019-b6289976-4be1-47ed-8cf3-c4a5bcdd0c40.png)

\*\***Please describe and document your process.**\*\*

Script:

**Narrator:** *Welcome to Hotline, a voice interaction game. You are now a 9-1-1 hotline operator, you will help a person in need over the phone,  and the only way you can do so is to talk to him and tell him what to do. Here comes your call...*

*beep beep beep*

**Male voice:** “Is this 911, hi, I need help, please! Can you help me?”

**Player response:** “yes”/“Hi”/“what happened” / “where are you” / “who are you” …

**Male voice:** ”I lost my memory and I’m now trapped in a room! There’s no one with me, and I don’t remember anything!”

**Player response:** “What is the room like” / “What’s in the room”/”What can you see” …

**Male voice:** “Ok, ok, I’m in a study I guess, there’s a door, let me see … it’s locked, there are many books on a bookshelf, there's a painting on the wall… and it’s just like a regular study...”

**Player response:**

door - still locked

Painting - nothing special (0) triggered (1)

book/bookshelf - Voice: ”Ok, I’ll check the book …… oh! There’s a book that looks strange, let me check… Oh my god, the book is carved hollow inside and there’s a key in it!” ->

**Player response:**

Door - “Oh it’s the key for the door, I’m out, let me see...” ->

Others - “what do you want me to do with the key?”

Male voice: “Ok, now I’m out, I’m in a … hallway I think, quite a simple house, there’s no window though, let me see … (walking around) … are you still there? I see three rooms, other than the study, one to my left, it says, bathroom, one to my right,I think is the kitchen, and one ahead, should be the bedroom?”

**Player response:**

Bathroom / left- “The door is open, god bless, it seems to be… a normal bathroom, quite small.” ->

Kitchen / Right - “I can smell something, it smells so good in it, the door is locked, I can’t go in, my god, I’m so hungry, how long has it been! Maybe I should try somewhere else?”

Bedroom / Ahead - “it’s weird, there’s not even a grip on the door, wait a minute, there’s something written on the door … *What's in the soup today?* what? What does that mean? Maybe I should try somewhere else?”

**Male voice:** “Now I’m in the bathroom, there’s the bathtub, nothing unusual, the toilet, and a mirror ...”

**Player response:**

Bathtub - “It’s … just a regular bathtub I think...”

mirror - “ok, you are right, I should probably see what I look like, maybe I could remember something? Let me see … Oh My God!! Who am I, what’s wrong with this terrible face! I’m not looking at it anymore!”

Toilet - “Ok, It’s really dirty, but got to do whatever gets me out of this shithole .... Wait, it’s not flushing, maybe something is clogged, let me check... who would have thought that! Are you like a detective or something? It’s a key! Probably opens the door to the kitchen!” ->

**Male voice:** “Now that I have the key, where should I go? Bedroom, Kitchen, or study?”

**Player response:**

Bedroom - “Ok, let me see, there’s no key hole on the door, really weird, just something written on the door … *What’s in the soup today?* what does that mean?”

Study - “Just like before, I don’t see anything useful, maybe I should do something with the key?”

Kitchen - “ahh, there’s a keyhole, let me try… Ok, the door's open, let me see what’s inside, man, it smells so good!” ->

**Male Voice:** “So… Here's the kitchen, some bowls … some bread, the stove is still on, and something is boiling in the pot, dang, that smells so good, Wonder what’s in it… should I go check the pot?”

**Player Responses:**

Yes / pot/ check/ why not / what/ inside - “it’s soup! I need to have some…(tasting soup) Ok, it tastes like heaven, my lord, I think there’s tomatoes, chicken, onions, and chilies, I wish you could be here to taste it.” ->

Others - “Oh I’m too hungry, I need to know what smells that good” - then go to yes

**Male Voice:** “Ok, enough soup, what should I do now? Should I go Bathroom, study, or bedroom?”

**Player Responses:**

Study - “still the same old study, maybe I should check out other rooms?”

Bathroom - “eww, it’s dirty, not going back again”

Bedroom - “Yes! The soup! Maybe that will solve the puzzle!” ->

**Male Voice:** “Ok, now I’m at the bedroom door, it’s hardly a door, no grip or anything, a question on it though, *What’s in the soup today?* , oh man, I shouldn’t have finished it all, do you still remember what’s in it?”

**Player Responses:**

Tomato / chicken / onion / chilli / s  - “Yes, yes, I still remember that taste! You are right!” ->

**Male Voice:** “So… should I just say the word? *INPUT* *INPUT* holy shit, it’s opening! The door opened automatically, is someone listening to me? …. OK, this is the bedroom, still no exit in it, how can this house have no exit! Ok, there’s the bed, of course, queen size I guess, looking cozy, a computer on the desk, and a book on the nightstand… What should I do?”

**Player Responses:**

Bed - “I’m not going to sleep at this time, maybe something else?”

Desk / computer - “you are right, maybe I can connect to the internet … ok it’s totally dead, just a decoration I guess…, maybe something else?”

Book / nightstand - “Sure, it’s never late to read, here’s a bookmarked page *reading* Painting is always a good place for many private people to hide their secrets in their home, many indoor designs leave a secret space on the wall that is covered by paintings and decorations … wait, that sounds real familiar... ”  ->

**Male Voice:** “I think that’s it for the bedroom, where should I go next, I don’t see another new door… should I go back to the kitchen, or bathroom, or study?”

**Player Responses:**

Study - “Wait, you are right, there’s a painting there! Maybe something hidden!” ->

Bathroom - “eww, it’s dirty, not going back again!”

Kitchen - “No soup there anymore, maybe somewhere else?”


**Male Voice:** “Ok, study, the painting, let’s see what’s behind it… My god, there is actually something! Can you imagine that? There’s a half-full vile of some greenish fluid … and a note … *drink it and you will be free*, what does that mean? Should I drink it? Shoot… the phone is going to die … hey, hey can you still hear me... should I drink … ”

The connection has been lost. After an hour or so, you received another call suddenly, “Is this 911, hi, I need help, please! Can you help me?” ”I lost my memory and I’m now trapped in a room! There’s no one with me, and I don’t remember anything!”

***// If no keyword is recognized: What, what are you saying? I don’t understand.***

***// If “repeat” - repeat male voice***


### Acting out the dialogue

Find a partner, and *without sharing the script with your partner* try out the dialogue you've designed, where you (as the device designer) act as the device you are designing.  Please record this interaction (for example, using Zoom's record feature).

\*\***Describe if the dialogue seemed different than what you imagined when it was acted out, and how.**\*\*

1. The dialogue sometimes does not predict what the player would be talking about, which causes confusions, sometimes players will just don't know how to act and then lost track of the game.
2. Sometimes if the player is not paying attention, might lost track of the game flow and forgot about the context, added repeat/say it again function for the player to hear it again.
3. When responding, bathroom and bedroom sounds too familiar, which might causes trouble in real interaction with the device
4. Although it's tried to be human like in terms of conversation, text to speech might not have a emotional tone to describe such a situation.
5. When player is not familiar with the game at first, they might try to say irrelavant words, which brings trouble to continue the game, should have a easier start that smoothly goes into the storyline.

**Recording of Acting**

[![image](https://user-images.githubusercontent.com/42874337/137243870-bdbb2226-e76a-4e6c-b25e-cf8096b71880.png)](https://drive.google.com/file/d/13G31O49YIGqYho0mpnuVIs2emSeCyw7Z/view?usp=sharing)

### Wizarding with the Pi (optional)

**Recording of Wizarding**

[![image](https://user-images.githubusercontent.com/42874337/137244045-4ff1e1da-1112-4642-83da-26f242a1c7e9.png)](https://drive.google.com/file/d/13DMY7OZAOmPFqzAin08qX3pPGObybJPk/view?usp=sharing)

\*\***Describe if the dialogue seemed different than what you imagined, or when acted out, when it was wizarded, and how.**\*\*

We have found that the wizarding dialogue is somewhat slow and not responsive, and not seem like an ideal gaming experience. The dialogue is not continuous, and the player is not fully aware of what they should be doing. The script is not clear in terms of instructing the players ways to continue playing. Thus, we decide to not use the Wizard of Oz controller, nor build a interface, but making it a fully autonomous audio game without visual interfaces so it would feel exactly like answering a call. 
**Since we decide not to include any visual interface through controller, but to make the interaction fully autonomous with audio, we will include more modality, ways of interaction, and put in extra amount of time to build our device. We hope that we won't receive any points deducted due to the lack of visual interface, since we have managed to make the whole device working autonomously and completely without visual, and that's even the theme of this game. We hope you like it. We have firstly tested by ourselves when we finished designing whole system. This is the beta version before we ask real participants to interact with the device.**

**Designer Beta Test of Full Script**

[![image](https://user-images.githubusercontent.com/42874337/137243103-6beb508e-7e84-49a7-9567-558ae039c69b.png)](https://drive.google.com/file/d/1HTalyqZ_k71L_fTSfw79f9N0Rv87wib7/view?usp=sharing)


# Lab 3 Part 2

For Part 2, you will redesign the interaction with the speech-enabled device using the data collected, as well as feedback from part 1.

**Feedback Collection:**

1. It reminds me of Jake Gyllenhall's new film, *The Guilty*, where he plays an 911 operator who assist someone over the phone. One thing you might want to try out is to add some other objects as "clues" in the game. For example, the male voice enters a kitchen and the player can ask "what do you see in the kitchen?" or "try open the oven, what do you see in there?" I feel like that's gonna add up the flexibility for players to explore and imagine the scene like they're actually there.
2. This is a really interesting idea, 1) does the player get to see the map of the house or any video of where the person is in the house (no, the point of this game is to use only limited voice interaction way to give out instructions to machine, and receive feedback to complete a task). 2) Is there a time limit on the game - for example if you don't make it out in 20 minutes does the game automatically end? (No, the game design is rather simple, and very much linear, player won't be able to stuck)
3. The idea of creating a game is super interesting and movel! It definitely makes for a much more complex dialogue, more similar to real conversation,perhaps to help with player's input, the device could give specific options that player could respond with insteaed to help facilitate the interaction.(Useful opinion, in order to keep our design of audio interaction, we provided specific options not through a visual way, but through audio suggestion.)
4. Since only certain words are accepted during the game by the player, it would be a better idea to print acceptable words on the screen to avoid confusion (Nice point, designed already key word detection in phrases, so that participants can just talk as normal conversation.)


## Prep for Part 2

**1. What are concrete things that could use improvement in the design of your device? For example: wording, timing, anticipation of misunderstandings...**

The wording itself can definitely help us in terms of improving the design and the interaction experience of player of this game. Our original script, after piloting and testing with different players, have been proven to be too strict to rely on our player's knowledge about this game. They can be easily lost when loosing context of the storyline. Wording also create certain problems during the process of coding the device. For example, we have found that the word "bedroom" and "bathroom"  are too similar to each other, which means a higher chance of the machine to misunderstand the player's voice input. Thus, we decided to change "bathroom" to "restroom" to create differences in sound. However, when piloting with people compare to pilot with machine, we have found a strong media equation phenomenon among players. This means that they behave significantly different when they interact with human compare to interacting with machine. Players tend to assume the machine is not as smart as human, which leads to slower pronounciation and shorter phrase. However, this will drastically distract players from the immersive gaming experience, and create a non-real feeling for the player to be in the game settings. Our plan to improve it is through changing the wording and timing of the whole game to make the machine respond more like human in emergency, and added different tones of the computer to promote the immersive feelings.

**2. What are other modes of interaction _beyond speech_ that you might also use to clarify how to interact?**

Other than speech to text and text to speech, we also implemented many other features to make our project more game like and more fun for our players. First of all, we included actual phone ringing sound and busy sound effect to indicate which phase the players are at and claraify the interaction of phone calls. Another implementation is the rotery sensor freshly distributed this week. We have included it as part of the gaming experience -- like using a transponder in old time. Occationally during the game, our players will face a situation that their connections are going to be unstable and they will have to rotate the rotery sensor to find the right place to connect back, as similar to transponder in old times in emergency assistance. Players also need to click on the rotery button to answer the call, which is simimlar to the interaction experience of an actual 911 agent when answering a phone call on the telephone. The new modes of interactions are all aiming for bringing our players a more immersive phone call experience, and more align with our initial design.

**3. Make a new storyboard, diagram and/or script based on these reflections.**

**New Script：**

"Wait... the connection is kinda unstable..."

"Oh! thank god I have got you back"

"So… should I just say the word?" + result + result

"Wait... the connection is lost again... hold on"

"Wow you are a genius! How did you fix that?"

**Description:**

The new scripts are implemented with the button rotery tasks of tuning the signal to reconnect, we have also edited the scripts to give more human like responses, more emotional rhetorics, and much clearer choices display through audio feedbacks.

**Story Board:**

![image](https://user-images.githubusercontent.com/42874337/137239070-8f76887f-c5d4-48b4-90f4-fe182d28570b.png)


## Prototype your system

The system should:
* use the Raspberry Pi 
* use one or more sensors
* require participants to speak to it. 

*Document how the system works*

[Part 2 Code Link](https://github.com/xuanyufang/Interactive-Lab-Hub/blob/Fall2021/Lab%203/app.py)

Instead of just wizarding the device through a controller, we started with that in part 1 and then actually make the whole device fully autonomous, with text to speech and speech to text and make actual interaction with players in part 2. We believe that would be able to show that this is enough work for a team of 2, even beyond. Our device included S2T, T2S, a new modality of rotery sensor, and interactive dialogues that would be able to respond based on what the player is saying. It has been a fully autonomous device instead of just a system prototype in the end, and we hope you like it. Please let us know if you are interested in playing! 

*Include videos or screencaptures of both the system and the controller.*

Since our System ends up as a fully autonomous device, here's a screen capture of our code to show our system hidden behind the autonomous interaction.

![image](https://user-images.githubusercontent.com/42874337/137247557-52413add-5a20-4b0d-80fb-7d2f017b7885.png)


## Test the system

Try to get at least two people to interact with your system. (Ideally, you would inform them that there is a wizard _after_ the interaction, but we recognize that can be hard.)

Our device is not just a wizard, but a fully autonomous device that allows players to interact in their own ways. Thus, our participants are totally unaware what they going to see or experience, and we expect our device to be able to cope with most of the situations by its own designs. We make minor changes to our game everytime we tested with a participant.

**Version 1.0**

*Fixed: Included more responsive wording, provided more organized choices for the participants*

[![image](https://user-images.githubusercontent.com/42874337/137230354-15de47bf-be8a-4a92-ae75-9f67c0b69fed.png)](https://drive.google.com/file/d/12rMf6i4VK2de9EC8s3IVHLHOWCheCnh_/view?usp=sharing)

**Version 1.5**

*Removed logical error in storylines*

[![image](https://user-images.githubusercontent.com/42874337/137246490-63c8d22b-875e-4749-8175-a761f2b3b25e.png)](https://drive.google.com/file/d/12qXtF3bYcFKQqV81BgVRbvT9BM4kFTIe/view?usp=sharing)

**Version 2.0**

*Now will repeat what player said at the door to the bedroom, and other minor fixs.*

[![image](https://user-images.githubusercontent.com/42874337/137246641-cf7e19d7-4270-4249-8a9a-36a4c26e8146.png)](https://drive.google.com/file/d/12wwaELIaDZgxDmtOMZ4ZYTjvGABInEZq/view?usp=sharing)

Answer the following:

### What worked well about the system and what didn't?

***What worked well:***

- The speech recognition was more sensitive than we imagined, so the interaction was pretty smooth. We were afraid that the speech-2-text model wouldn't recognize complex sentences, so we only set up the model to recognize keywords such as "bedroom", "study", and "kitchen". It ended up working pretty well. The device could recognize the keyword in a sentence.
- The flow of the game was designed well. The players said that the script was interesting and fun, and the ending was thought-provoking. They had fun playing the game.
- The game gave pretty clear instructions on what options players had, so the process usually went smoothly. There wasn't any case where the player didn't know what to do or how to continue.

***What didn't work well:***

- The interactions with rotery sensor could be confusing due to delayed feedback. There are two ways users interact with the rotery sensor: 1) to "pick up" the call, player needs to keep pressing the button until the "ring" ends; 2) to stay connected on the line, player needs to rotate the sensor to a specific value. In both cases, player needs to do it slowly because feedback can only be provided after the audio ends. 
- A player commented that she felt like she was guided by the caller for help rather than guiding him. The interaction should be designed to give players more freedom in giving directions and suggestions to the caller. However, due to technical obstacles, this is quite hard to achieve. 


### What worked well about the controller and what didn't?

Instead of using a controller to wizard the device, we decided to build a fully autonomous one. This is due to the size of our script and the challenge of continuous conversation without delay. It would be too slow for a human to keep track of user response and find the correct next instrution to give to the user. This was clearly shown in our "Wizarding the device" video we did for Part 1.


### What lessons can you take away from the WoZ interactions for designing a more autonomous version of the system?

We have already implemented an autonomous system due to the reasons described above. We found human responce towards human compare to machine is completely different. Thus, we designed a more intuitive interaction experience for our autonomous version.


### How could you use your system to create a dataset of interaction? What other sensing modalities would make sense to capture?

We could add a controller to allow players to move around with the left, right, up, down options. In the meantime, we could display a real-time updating map on the website to give the player a more intuitive view of his/her location.

Also We have already implemented a rotery sensor as a novel modality in this game. This actually can be data that collected from users to see how much time they would take to complete a spatial task, and how patient they are in terms of solving a puzzle.



Special Thanks to people who helped us on testing the device: Ruby Pan, Katherine Lv, Sylvia Ding, Wenhe Li, Zixiong Feng, Zhenghe Wang.
Thank you all!
![5f6aa9df04e26c41757ae3a5cdb01c0](https://user-images.githubusercontent.com/42874337/137217223-8418415a-6fcd-497b-a37c-0b120c7f48f9.jpg)

