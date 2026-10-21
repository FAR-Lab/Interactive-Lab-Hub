# Prep for Lab 5: Get the Latest Content and Set Up

Complete these before lab on Wednesday.

## Get the Latest Content

As always, pull updates from the class Interactive-Lab-Hub to both your Pi and your own GitHub repo.

**\[recommended\]** Option 1: On the Pi, `cd` to your `Interactive-Lab-Hub`, pull the updates from upstream (class lab-hub) and push the updates back to your own GitHub repo. You will need the *personal access token* for this.

```
pi@raspberrypi:~$ cd Interactive-Lab-Hub
pi@raspberrypi:~/Interactive-Lab-Hub $ git pull upstream Fall2026
pi@raspberrypi:~/Interactive-Lab-Hub $ git add .
pi@raspberrypi:~/Interactive-Lab-Hub $ git commit -m "get lab5 content"
pi@raspberrypi:~/Interactive-Lab-Hub $ git push
```

Option 2: On your own GitHub repo, create a pull request to get updates from the class Interactive-Lab-Hub. After you have the latest updates online, go to your Pi, `cd` to your `Interactive-Lab-Hub` and use `git pull`.

## Read

1. Read about [OpenCV](https://opencv.org/about/), [MediaPipe](https://mediapipe.dev/), the [Ultralytics YOLO Raspberry Pi guide](https://docs.ultralytics.com/guides/raspberry-pi/), and the [Ollama API](https://github.com/ollama/ollama/blob/main/docs/api.md).
2. Read Belloti, et al.'s [Making Sense of Sensing Systems: Five Questions for Designers and Researchers](https://www.cc.gatech.edu/~keith/pubs/chi2002-sensing.pdf). You will use the five questions (address, attention, action, alignment, accident) in Part 2.

## VNC

The live demos in Parts B, C and E open a video window, so you will run them on your Pi through VNC. If you have not set it up yet, follow [Using VNC to see your Pi desktop](https://github.com/IRL-CT/Interactive-Lab-Hub/blob/Fall2026/Lab%202/prep.md#using-vnc-to-see-your-pi-desktop) from the Lab 2 prep. Everything else in this lab, including the overnight scripts, runs over plain ssh (and so does Part E with `--headless`).

## For the lab, you will need

1. Raspberry Pi 5 (the 4 GB model is enough; 8 GB is comfortable) and the webcam
1. A place where the Pi can sit undisturbed for a whole night, with power and ideally wifi (Part 2)
1. Optional: the Qwiic sensors, buttons and OLED from Lab 4, the speaker and microphone from Lab 3, and the Mini PiTFT from Lab 2. They are good ways to talk to a device before bed and to hear from it in the morning.

## Get a head start on the installs (optional)

Part A of the [README](README.md#part-a) creates the Python environment, exports the YOLO model and installs Ollama with two Qwen models. Together that is a couple of gigabytes of downloads and a long `pip install`, so if you have good wifi before lab, do Part A now and bring the screenshots.
