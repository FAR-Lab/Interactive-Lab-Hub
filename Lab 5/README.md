# Observant Systems: Overnight Sensation

**NAMES OF COLLABORATORS HERE**
Partner: Shifeng Hong (Sh2769) https://github.com/mado0512/Interactive-Lab-Hub 

**Please indicate anyone you collaborated with on this Lab here.**
Be generous in acknowledging their contributions! And also recognizing any other influences (e.g. from YouTube, Github, Twitter) that informed your design. 

# Part 1

## Part A. 
### Set up your Pi for on-device AI

***Include a screenshot of ollama list showing your models.***

Ollama list:
<img width="548" height="79" alt="Screenshot 2026-10-21 at 10 40 26 AM" src="https://github.com/user-attachments/assets/e987d627-b7b4-45aa-b767-cf0f3f769425" />


## Part B. 
### See: recognize people in real time with YOLO

***Include a short video or screenshots of your experiments with the person detection. Write down three situations where it did not see you, or saw a person who was not there, and what you think the cause was.***

I actually had more trouble getting it to not see me or recognize a person. I was surprised to find YOLO quite sensitive. It was actually able to spot a person who sat pretty far behind me/was tiny on the camera. It seems that it's able to detect body parts and just labels it as "person" rather than needing to see the whole face or enough details to objectively tell this is a being, rather than one element. This was shown by my hand still being marked when I was holding up my phone case. 

What surprised me most was it recognizing when my torso was in the frame. I assumed that because I was wearing a solid-colored large sweater, it wouldn't recognize me. There were moment it flickered, but it somehow still picked up that I was a person. 

<img width="648" height="561" alt="Screenshot 2026-10-22 at 10 29 54 AM" src="https://github.com/user-attachments/assets/91e31627-a7af-4842-b147-ccb64c432f57" />
<img width="645" height="566" alt="Screenshot 2026-10-22 at 10 31 53 AM" src="https://github.com/user-attachments/assets/c0ecebfd-efe9-4805-92f4-ed19d4f48732" />
<img width="643" height="534" alt="Screenshot 2026-10-22 at 10 34 15 AM" src="https://github.com/user-attachments/assets/c8bc0e77-3244-43bb-a3c3-38f0dab38679" />
<img width="616" height="484" alt="Screenshot 2026-10-22 at 10 36 18 AM" src="https://github.com/user-attachments/assets/1b52f6f3-de3f-4371-b0aa-c07b1da7fe74" />

## Part C. 
### See more: hands and pose with MediaPipe

\*\*\***Include a screenshot or short video of the hand pose demo, and write how you might use face, hand or body pose tracking in your observant system.**\*\*\*

<img width="701" height="612" alt="Screenshot 2026-10-21 at 6 40 45 PM" src="https://github.com/user-attachments/assets/894dff6d-c25c-4223-8c6e-26f66d19d331" />

My partner and I were thinking of using facial movements for our project. More specifically, using the system to detect when a users eyes and mouth are open or closed.

## Part D. 
### Reason: run Qwen on the Pi with Ollama

***Ask Qwen three questions to answer. Paste the questions, the answers and how long each took. Try one of them with qwen3:0.6b and compare.***

1.  python ask_qwen.py --image snap.jpg "What is in this photo?"
A close-up selfie of a young woman with dark hair, wearing a gold ring on her index finger and making a peace sign.

2. python ask_qwen.py --model qwen3:0.6b "Tell me briefly about TikTok."
TikTok is a social media platform where users share short, creativevideos, often called "tiktoks." It's popular for people who want toexpress themselves or connect with others. The platform has a largeuser base and a wide range of content, from music and dance to foodand lifestyle. It's known for being a hub for trends and trends.
	
[qwen3:0.6b, 12.2 s]

3. python ask_qwen.py "Tell me briefly about TikTok."
TikTok is a social media platform that allows users to create and share videos, primarily focusing on music, trends, and entertainment.nIt has grown into one of the largest digital ecosystems by enablingcreators to reach millions of people instantly through short-form content. The service connects users with each other via comments, likes, shares, and stories to foster community engagement and discovery.
	
[qwen3.5:0.8b, 14.3 s]

I found that using qwen3:0.6b resulted in a shorter load time, but probably because the response was briefer and less detailed than when I didn't use the model. 

---

# Lab 5 Part 2: Overnight Sensation

## Part F. 
### Read Part 2 and storyboard your night-time interaction

Storyboard a night-time interaction built on your observant system, in three panels:

1. **Before bed.** How does the person hand the night over, and how does the device acknowledge it?
2. **While asleep.** What does the device watch or work through?
3. **When awake.** What is the one thing the person learns, and in what medium?

\*\*\***Insert ideas, sketches, Verplank diagrams and storyboards for your night-time interaction here.**\*\*\*
For our project, Shifeng and I are planning on making a sleep apnea/snoring detection device that logs how often these instances occur so that users can improve their sleep hygiene. 

We currently plan to have the camera set-up on a bed headboard, angled so that its able to see a users face. Users turn the device on by pressing a button. When users go to bed, the system detects when the users eyes are closed. If the eyes are closed for 5 consecutive minutes, then the system processes that the user is asleep, moving onto the second phase that detects for instances of snoring/sleep apnea. We plan to achieve this by detecting when the users mouth is open and, if time permits, when the system detects noise/snoring. If the system detects both of these stimuli, then the computer writes a log which includes times naps and a brief clip of when the instances occurs. In the morning, the user will be able to review the log that the system has written down and see how frequent their snoring or apnea was. 

Storyboard: 

<img width="1385" height="771" alt="Screenshot 2026-10-22 at 11 12 04 AM" src="https://github.com/user-attachments/assets/8549331c-9eab-461f-b441-c802a357e9b7" />

## Prep for Part 2

1. Look at and give feedback on the Part F storyboards.
   **Put the feedback for your ideas here.**
2. [Update your Lab Hub](prep.md#get-the-latest-content) to get the latest content for Part 2.
3. Decide where the device will spend the night and who else lives there. Get their OK before the first run.
4. Revise your storyboard with the feedback and with what you learned in Part E about where the pipeline breaks.

\*\*\***Post your revised storyboard here.**\*\*\*

## Part G. 
### Design the interaction before bed

The hand-off: the person tells the device what to watch tonight, and the device acknowledges it. Keep it to a thirty-second ritual. A button or a touch (Lab 4), a spoken sentence (Lab 3), a wave or a Quiet Coyote at the camera (Part C). The acknowledgement can be a line on the display, a tone, or an LED that dims rather than lights up. At its simplest, the hand-off just sets the question that the morning will answer.

\*\*\***Describe the bedtime interaction and include a short video of someone handing the night over to the device.**\*\*\*

## Part H. 
### Incorporate the observant system during sleep

The Part E pipeline becomes the night shift. `overnight.py` runs your `interpret()` from `yolo_to_qwen.py` every few seconds, people only unless you pass `--all`, and writes the readings to `night_log.jsonl`; the reasoning waits for the morning. Start it inside `tmux` so it keeps running after you close your laptop, and stop it with Ctrl-C in the morning:

```
(.venv) pi@raspberrypi:~/Interactive-Lab-Hub/Lab 5 $ tmux new -s night
(.venv) pi@raspberrypi:~/Interactive-Lab-Hub/Lab 5 $ python overnight.py
```

Fake a night first: run it for thirty seconds while you walk around, stop it, and run `morning.py` from Part I. When that looks right, run a real night. If your storyboard needs a sensor rather than the camera, swap in the Lab 4 example code and log its reading the same way.

\*\*\***Run the system for at least one real night. Include the log (or an excerpt) and a few sentences on what broke or surprised you.**\*\*\*

## Part I. 
### Design the interaction when awake

The reveal. The night produced a log; the morning turns it into something a half-awake person can take in. `morning.py` is the smallest version: it asks Qwen for a three-sentence report.

```
(.venv) pi@raspberrypi:~/Interactive-Lab-Hub/Lab 5 $ python morning.py
```

Make it yours: show the report on the Mini PiTFT, read it aloud with Piper from Lab 3, plot the night as a timeline, or ask for JSON (`--json`, Part D) and move a servo. Whatever you pick, make sure it is honest about a night in which nothing happened.

## Final documentation

Document all the prototypes and iterations you have designed and worked on. The deliverables for this lab are writings, sketches, photos, and videos that show what your system:

* "Looks like": how the device sits in the room at night, and what it looks like at bedtime and in the morning.
* "Works like": the pipeline from detector to interpreter to log to reasoner, with a real night's data.
* "Acts like": how a person hands the night over and what they get back.

\*\*\***Include a short video of the whole system: the bedtime hand-off, a log excerpt or timelapse of the night, and the morning reveal from a real overnight run.**\*\*\*

As always, make sure you document contributions and ideas from others (and AI) explicitly in your writeup.

You are permitted (but not required) to work in groups and share a turn in; you are expected to make equal contribution on any group work you do, and N people's group project should look like N times the work of a single person's lab. Make sure the page for the group turn in is linked to your personal Interactive Lab Hub page.

## Deliverables & Submission for Lab 5

For submission, the readme.md page for this lab should be edited to include the work you have done:
* Upload any materials that explain what you did, including your code and night log, into your Lab 5 repository, and link them in your Lab 5 readme.md.
* Link your Lab 5 readme.md in your main Interactive-Lab-Hub readme.md.
* Labs are due on Mondays, make sure to submit your Lab 5 readme.md to Canvas.

<details>
  <summary><strong>Submission Cleanup Reminder (Click to Expand)</strong></summary>
