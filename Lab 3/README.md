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

# Lab 3 Part 2

For Part 2, you will redesign the interaction with the speech-enabled device using the data collected, as well as feedback from part 1.

**Feedback Collection:**
1. It reminds me of Jake Gyllenhall's new film, *The Guilty*, where he plays an 911 operator who assist someone over the phone

## Prep for Part 2

1. What are concrete things that could use improvement in the design of your device? For example: wording, timing, anticipation of misunderstandings...
2. What are other modes of interaction _beyond speech_ that you might also use to clarify how to interact?
3. Make a new storyboard, diagram and/or script based on these reflections.

## Prototype your system

The system should:
* use the Raspberry Pi 
* use one or more sensors
* require participants to speak to it. 

*Document how the system works*

*Include videos or screencaptures of both the system and the controller.*

## Test the system
Try to get at least two people to interact with your system. (Ideally, you would inform them that there is a wizard _after_ the interaction, but we recognize that can be hard.)

Answer the following:

### What worked well about the system and what didn't?
\*\**your answer here*\*\*

### What worked well about the controller and what didn't?

\*\**your answer here*\*\*

### What lessons can you take away from the WoZ interactions for designing a more autonomous version of the system?

\*\**your answer here*\*\*


### How could you use your system to create a dataset of interaction? What other sensing modalities would make sense to capture?

\*\**your answer here*\*\*

