
# Pre-Lab6

1) Review Basic Unix commands. You can use this to review, [Basic Linux Commands](https://www.hostinger.com/tutorials/linux-commands) 

2) Download and burn the IxE disk image to your microSD card. ( The instructions are mentioned below under "Preparing your Raspberry pi" )


# GreetingBot

In this lab, we will use a Raspberry Pi to create a GreetingBot! 

## Introducing the **Raspberry Pi**

### Preparing your Raspberry Pi

* Download the Interactive-Device-Design-2020 disk image to your laptop hard drive. This is 3 GB, so it might take a while.
                here:https://www.dropbox.com/sh/2jt06jka7lg5z70/AAB6XnRWWais0wP5bOZ93upSa?dl=0


* Use [Etcher](https://www.balena.io/etcher/) to flash this image to your microSD card.

* In the Boot image of the new disk, create a file called [wpa_supplicant.conf](https://www.raspberrypi.org/documentation/configuration/wireless/headless.md) with the following information:

```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=<Insert 2 letter ISO 3166-1 country code here, US or CN>

network={
 ssid="<Name of your wireless LAN>"
 psk="<Password for your wireless LAN>"
}
```

This information gets copied over to your Raspberry Pi when it boots up, so that it shows up on your network

* Eject or unmount the microSD card drive, and then remove it and reinsert it into the RPi.

* Boot the RPi by connecting it to a power source


## Connect to your Interaction Engine

The Pi is a single-board computer, but it doesn't have its own keyboard or mouse, so we will be connecting to the Pi remotely from your laptop over wifi. 

We will [ssh](https://en.wikipedia.org/wiki/Secure_Shell) into the system so that we can control the computer via [Terminal on Mac](http://blog.teamtreehouse.com/introduction-to-the-mac-os-x-command-line) or [PuTTy on Windows](https://www.ssh.com/ssh/putty/download).

* Make sure your computer/laptop is on the same network as the RPi is on.

* Using [Fing](https://www.fing.com) or equivalent program to scan the local wireless network for the Pi. (Sometimes it takes a few minutes for the device to show up on the network.) 

**Record the IP address and the MAC address for the RPi.** 


In the following section, we will refer to your IP address with the name `$Address`. Whenever you see this, replace the text (`$Address`) with the IP address you found on Fing.


### 1. Verify the Pi is online

First, in your terminal program, `ping` your Pi to make sure it is online. Open your terminal (or `cmd` on Windows) and type `ping $Address` where your replace `$Address` with the IP address. 

```shell
you@your-machine:~$ ping 192.168.2.2
PING 192.168.2.2: 56 data bytes
64 bytes from 192.168.2.2: icmp_seq=0 ttl=64 time=0.467 ms
64 bytes from 192.168.2.2: icmp_seq=1 ttl=64 time=0.471 ms
64 bytes from 192.168.2.2: icmp_seq=2 ttl=64 time=0.550 ms
64 bytes from 192.168.2.2: icmp_seq=3 ttl=64 time=0.670 ms
64 bytes from 192.168.2.2: icmp_seq=4 ttl=64 time=0.720 ms
^C
--- 192.168.2.2 ping statistics ---
5 packets transmitted, 5 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 0.467/0.576/0.720/0.103 ms
```

You can use `control-C` to interrupt and exit the ping (press the `control` key, and while holding it down, also press the `C` key, then let go of both together--this looks like `^C` in the terminal).

If you do not see the response from the `ping` command, [troubleshoot](Getting-an-IxE-based-Pi-on-your-Wi-Fi#troubleshooting) to get your Pi online.  

### 2.  SSH into the Pi.

When you first log in it will show you a "fingerprint" and ask you whether you want to continue connecting. Say `yes`.



```shell
ssh pi@192.168.2.2
The authenticity of host '192.168.2.2' can't be established.
ECDSA key fingerprint is SHA256:Y9S4oMH2H70fz3K/L42Kw39k+zkpyfr0DmGdzBx7SKk.
Are you sure you want to continue connecting (yes/no)? yes
```
From your terminal, log in to your Pi using the command `ssh pi@$Address` with the password: `raspberry` 

After you say yes, type the password `raspberry` and hit Enter. You should see this:

```shell
pi@192.168.2.2's password:
Linux ixe00 4.9.59-v7+ #1047 SMP Sun Oct 29 12:19:23 GMT 2017 armv7l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Wed Jan 17 10:42:03 2018

SSH is enabled and the default password for the 'pi' user has not been changed.
This is a security risk - please log


in as the 'pi' user and type 'passwd' to set a new password.

pi@ixe00:~ $ 
```

Once you are signed in, your terminal will now connected directly to the 'terminal' on your Pi, via `ssh`. You can tell this by looking at the user and hostname at the beginning of each line, which should now look like:

```shell
pi@ixe00 ~ $
```

### Change the password

Because the Pi asked you to! Also to keep your RPi from getting hacked.

Write it down somewhere, because we don't know how to recover lost passwords on the RPi.

## Explore the RPi

### Enable X Windows
We will want to enable X windows usage on the Raspberry Pi. (Should this not work see below for instructions on how to use VNC)

On the Mac, please install XQuartz.

On the PC, please install XMing.

To enable XWindows to open with the Pi, we need to log into the Pi with the -X flag to enable xwindows forwarding:
```shell
$ ssh -X pi@ixe00.local
pi@ixe00.local's password: 
Linux ixe00 4.19.66-v7+ #1253 SMP Thu Aug 15 11:49:46 BST 2019 armv7l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Thu Jul 30 17:50:45 2020 from fe80::480:f9c8:6452:925e%wlan0
pi@ixe00:~ $ xeyes
```
Here, we test out the Xwindows using the Xeyes program. Use Ctrl-C afterwards to end the program.

Look in the RPi image and see where things are at. In specific, see if you can find:

``The Arduino sketchbook``
``Banana.jpg``
``Wormy.py``

### Using VNC
Another way to connect to your IxE is using VNC (Virtual Network Computing). It essentially is remote login. The easiest client to use is [VNC Connect](https://www.realvnc.com/en/connect/download/viewer/). Download and install it. Once that's done type the IP address of the IxE in the text-box at the top. 
![](images/VNC1.png)

After that a login window should appear, use your normal logins (originally: Account=pi, Password=raspberry).
![](images/VNC2.png)

At that point the normal RPI desktop should appear and you can start and stop programs from here. 


![](images/VNC3.png)
Including Arduino, and terminals to run python programs.
The image below shows where to find the terminal and how to run one of the object recognition examples. 

**Make sure to plug your camera if you try this.***

![](images/VNC4.png)

For easy copy and paste:
```shell
cd pi-object-detection/
./test_object_detection.sh 
```

### Try some Python code on the Pi

We will be using Python in future modules, so try running some of the sample python code in ``python_games``:

``wormy.py``
``catanimation.py``
``tetromino.py``

Take a look at the code in the python file, using ``cat``, or ``nano``.

Also try the shellscripts in the ``textToSpeech`` directory.

** How do you know what the shell script is doing? **

Adapt the scripts so that they say what you want them to say.

Now try the shellscripts in the ``speechToText`` directory. 

These scripts use a program called [``vosk``](https://alphacephei.com/vosk/) to recognize numbers. 

**How do we use ``vosk`` to recognize words and phrases?**

**Include the output of vosk recognizing phrases you taught it to look for.**

**Include the listing for a shell script and model files that you use to get vosk to recognize these phrases.**


### Experimenting with Linux processes


Try running multiple programs at the same time using the ‘&’ to make each process a background process:
```shell
pi@ixe00:~ $ cd python_games/
pi@ixe00:~/python_games $ python2 wormy.py &
[1] 2851
pi@ixe00:~/python_games $ python2 drawing.py &
[2] 2856
pi@ixe00:~/python_games $ 
```
Make the last background process a foreground process with ‘fg’”
```shell
pi@ixe00:~/python_games $ python2 drawing.py &
[1] 2879
pi@ixe00:~/python_games $ fg
python drawing.py
```

One a process is in the foreground, it is possible to end it by typing Ctrl-c.

Sometimes, we want to push a process to the background after we’ve started it. Here is how to do that:

```shell
pi@ixe00:~/python_games $ python2 drawing.py
^Z
[1]+  Stopped                 python2 drawing.py
pi@ixe00:~/python_games $ bg
[1]+ python drawing.py &
pi@ixe00:~/python_games $ 
```

Also, it is possible to kill background processes through their process ids. We highlight where you can look for that process id:

```shell
pi@ixe00:~/python_games $ python2 drawing.py &
[1] 2894
pi@ixe00:~/python_games $ ps -x
  PID TTY      STAT   TIME COMMAND
  497 ?        Ss     0:00 /lib/systemd/systemd --user
  500 ?        S      0:00 (sd-pam)
  505 ?        Ssl    0:00 /usr/bin/lxsession -s LXDE-pi -e LXDE
 <various processes left out>
 2474 ?        S      0:42 sshd: pi@pts/0
 2477 pts/0    Ss     0:00 -bash
 2894 pts/0    Sl     0:01 python drawing.py
 2907 pts/0    R+     0:00 ps -x
pi@ixe00:~/python_games $ kill -9 2894
pi@ixe00:~/python_games $ 
[1]+  Killed                  python2 drawing.py
pi@ixe00:~/python_games $ 
```

## Connect the Arduino and the RPi

Connect your Arduino board to your RPi using a short USB cable.
Now, on the RPi, run the Arduino program:

```shell
pi@ixe00:~ $ arduino
```

Use the Arduino IDE to flash Blink onto the Arduino. Don’t forget to set the port!

Now, try adding a sensor and checking that you can read the value on the RPi using the Serial Monitor.

### Hello Pi, Hello Arduino

With your Pi and Arduino, try out the ``helloPi`` and ``helloArduino`` sketches. Tweak them to make them do something new.

``HelloPi.ino`` sets up the Arduino to say hello to the Pi repeatedly. 
``HelloPi.py`` echos the Arduino’s message to the console in text form.
``sayHelloPi.py`` plays the helloPi.wav file whenever the Pi gets any message from the Arduino on the serialPort.

Flash the Arduino with ``HelloPi.ino``.
With ``HelloPi.ino`` running on the Arduino, run ``HelloPi.py`` on the Pi using ``$python HelloPi.py``.

**What would you change to make sayHelloPi say something else?**

**How could you make it so that the Pi would only say something if the lights came on in the room?**

**How could you make it so that the Pi would say different things based on different sensor values read by the Arduino?**

Next, try out ``HelloArduino``. First have ``HelloArduino.ino`` listen for messages from ``HelloArduino.py``. Next, use ``morse_code_translator.ino``. What happens differently? 

Change the ``HelloArduino.py`` program to take in inputs from the user to have them translated to morse code on the Arduino.

## Your own voice agent 

Program a simple application that understands different basic greetings (for example, Yo!, Good morning! And Good afternoon!) and responds either visibly, physically or auditorially in kind!

You are free to adapt this assignment to have the agent respond to any other set of vocabulary for any other purpose.

**Record someone trying out your design**

Using a phone or other video device, record someone trying out your GreetingBot. (This does not need to be an advertisement for your ChatBot; it is okay if the person is confused or asks questions or doesn't like it. We like the drama. Do not record someone using the default ChatBot.) Post the video to your README.md page!

**Submit your code to Github**

This project is going to be the submission of this week. You will need to upload the changes you made on the Pi to the GitHub page. To do that you need to follow three simple steps: Stage => Commit => Push! 

[Uploading on github via terminal](https://docs.github.com/en/free-pro-team@latest/github/managing-files-in-a-repository/adding-a-file-to-a-repository-using-the-command-line)

```
$ git add .
# Adds the file to your local repository and stages it for commit. To unstage a file, use 'git reset HEAD YOUR-FILE'.

$ git commit -m "Add existing file"
# Commits the tracked changes and prepares them to be pushed to a remote repository. To remove this commit and modify the file, use 'git reset --soft HEAD~1' and commit and add the file again.

$ git push origin your-branch
# Pushes the changes in your local repository up to the remote repository you specified as the origin
```

You might be required to login in the terminal to your GitHub account. For more details on how the Git commands work or what other commands are available checkout this [cheatsheet](https://education.github.com/git-cheat-sheet-education.pdf).  


#### Pro-tips and other commands
`nano` is a general purpose text editor, so you can use it for any type of text file like the `.js`, `.html`, and `.css` files in this project.

Notice on the bottom of the terminal window that there is some text showing things like `^G Get Help` and `^O Write Out`. These are the commands that you can use in `nano`. The `^` character stands for `Ctrl`. So to `Write Out` (which means to save the file), you would type `Ctrl` and `O` (that's the letter `O`, not the number `0`). When you've typed these, you will see a bar appear at the bottom of the terminal that says `File Name to Write: chatServer.js`. This is the file name you are saving to. In this case, we want the same name, so we can just hit the `Enter` key. You will then see a message on the bottom that tells you how many lines were written, something like `[ Wrote 116 lines ]`.



