# Lab 2 Prep

### Get Kit and Inventory Parts
Prior to lab Wednesday, taken inventory of the kit parts that you have, and note anything that is missing:

***Update your [parts list inventory](partslist.md)***

### For Lab 2, part 1, you will need:

- [Raspberry Pi 4](https://www.adafruit.com/product/4296)
- [Power Supply](https://www.adafruit.com/product/4298)
- [SD card](https://www.bhphotovideo.com/c/product/1536561-REG/silicon_power_sp032gbsthbv1v20sp_32gb_elite_a1_uhs_1.html/reviews)
- [SD card reader](https://www.bhphotovideo.com/c/product/751120-REG/Iogear_GFR204SD_10_in_1_USB_2_0_SD_MicroSD_MMC.html)
- [Adafruit MiniPiTFT](https://www.adafruit.com/product/4393)

### Burn your Pi image to your SD card

#### On your computer download
- [Raspberry Pi Imager](https://www.raspberrypi.org/software/)
- Our Copy of Raspbian at [this dropbox link](https://www.dropbox.com/sh/2jt06jka7lg5z70/AAB6XnRWWais0wP5bOZ93upSa?dl=0), or use our ftp server here: ftp://farlab.infosci.cornell.edu/IXE_20210224.img.xz .
Download and use the ``.xz`` file in the Raspberry Pi Imager.

- If using windows: [Windows 10 SSH Client](https://docs.microsoft.com/en-us/windows/terminal/tutorials/ssh) or [PuTTY](https://www.putty.org/)

#### Setting up your OS
1. Plug the SD card into your computer using the card reader
2. Choose the downloaded file for "Choose OS" and the SD card for "Choose SD card" then hit write.
<img src="https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/wiki/images/pi_imager_os_select.png" alt="choose os" height="200" />
3. Configure the Pi for <a href=https://www.raspberrypi.org/documentation/configuration/wireless/headless.md>headless mode</a> . Create a file called "wpa_supplicant.conf" in the Boot image of the new disk. The file contents should have the following:

	```
	ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
	update_config=1
	country=<Insert 2 letter ISO 3166-1 country code here, for the United states it is US>
	
	network={
	 ssid="<Name of your wireless LAN>"
	 psk="<Password for your wireless LAN>"
	}
	```
	Make sure to update the above contents with your own network information.
	
	This information gets copied over to your Raspberry Pi when it boots up, so that the Pi gets a DHCP address from your network router and can show up on your network

4. Eject or unmount the microSD card drive, and then remove it and reinsert it into the RPi in the slot on the bottom (silver rectangle on the right)

<img src="https://cdn-shop.adafruit.com/1200x900/4296-12.jpg" alt="Pi bottom side" height="200" />


5. Boot the RPi by connecting it to a power source

### Try to set up your Pi to run in headless mode

#### Connecting to your Pi

Unlike your laptop, the Pi doesn't come with its own keyboard or mouse. While you could plug in a monitor, keyboard, and mouse we will be connecting to your Pi over SSH. You can do this in [Mac Terminal](https://blog.teamtreehouse.com/introduction-to-the-mac-os-x-command-line) or [Windows 10 SSH Client](https://docs.microsoft.com/en-us/windows/terminal/tutorials/ssh). Make sure you connect your laptop to the same network as you entered in your `wpa_supplicant.conf` above.

1. In Terminal type `$ arp -a` and you should see output that looks like this:
    ```
	rt-ac5300-c020 (192.168.2.1) at b0:6e:bf:86:c0:20 on en0 ifscope [ethernet]
	ixe00 (192.168.1.131) at (incomplete) on en0 ifscope [ethernet]
	? (224.0.0.251) at 1:0:5e:0:0:fb on en0 ifscope permanent [ethernet]
	? (239.255.255.250) at 1:0:5e:7f:ff:fa on en0 ifscope permanent [ethernet]
   ```
Take note the ip address in the line that starts with `ixe00`. For me that is `192.168.2.131` but you should use whatever number you see there.

2. Verify your pi is online. In terminal type `ping 192.168.2.131` replacing that number with your own.
    ```
	 ping 192.168.1.131
	PING 192.168.1.131 (192.168.1.131): 56 data bytes
	64 bytes from 192.168.1.131: icmp_seq=0 ttl=64 time=252.118 ms
	64 bytes from 192.168.1.131: icmp_seq=1 ttl=64 time=10.331 ms
	64 bytes from 192.168.1.131: icmp_seq=2 ttl=64 time=10.209 ms
	64 bytes from 192.168.1.131: icmp_seq=3 ttl=64 time=14.816 ms
	^C
	--- 192.168.1.131 ping statistics ---
	4 packets transmitted, 4 packets received, 0.0% packet loss
	round-trip min/avg/max/stddev = 10.209/71.868/252.118/104.084 ms
	```
You can use `control-C` to interrupt and exit the ping (press the `control` key, and while holding it down, also press the `C` key, then let go of both together--this looks like `^C` in the terminal).

2.  SSH into the Pi.

When you first log in it will show you a "fingerprint" and ask you whether you want to continue connecting. Say `yes`.



```shell
ssh pi@192.168.1.131
The authenticity of host '192.168.1.131' can't be established.
ECDSA key fingerprint is SHA256:Y9S4oMH2H70fz3K/L42Kw39k+zkpyfr0DmGdzBx7SKk.
Are you sure you want to continue connecting (yes/no)? yes
```
From your terminal, log in to your Pi using the command `ssh pi@192.168.1.131` with the password: `raspberry` 

After you say yes, type the password `raspberry` and hit Enter. You should see this:

```shell
pi@192.168.1.131's password:
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


*** Note here if you run into issues*** (and Slack message the teaching team), so that we can use Lab time on Wednesday to try to fix them.


### Refresh your knowledge of command line interfaces: 

The command line/Terminal is a powerful way to interact with your computer without using a Graphical User Interface (GUI). When you ssh on to your pi you have a prompt you can enter commands. In your terminal there is a shell, there are many shells but for this class we will use one of the most common **bash**

```
pi@ixe00:~ $ echo $SHELL
/bin/bash
```
In the code above we've typed `echo $SHELL`. The `echo` tells it to print something to the screen. You could try typing `echo 'hello'` to see how that works for strings. The `$` at the front of `$SHELL` tells bash we are referring to a variable. In this case it is a variable the OS is using to store the shell program. In a folder `/bin` is a program called bash that we are currently using. 

The up arrow with show the most recent command.

#### Navigation in the command line

There are many commands in the command line. They can take a variety of options that change how they are used. You can look these up online to learn more. Many commands have a manual page with documentation that you can see directly in the terminal by typing `man [command]`. For example:

```
pi@ixe00:~ $ man echo
ECHO(1)                           User Commands                          ECHO(1)

NAME
       echo - display a line of text
SYNOPSIS
       echo [SHORT-OPTION]... [STRING]...
       echo LONG-OPTION
DESCRIPTION
       Echo the STRING(s) to standard output.
       -n     do not output the trailing newline
       -e     enable interpretation of backslash escapes
       -E     disable interpretation of backslash escapes (default)
       --help display this help and exit
       --version
Manual page echo(1) line 1 (press h for help or q to quit)
```
These are some useful commands. Read the manual pages for advanced usage.

* `pwd` - print working directory, tells us where on the computer we are
* `ls` - list the things in the current directory. 
* `cd` - change directory. This lets you move to another folder on your machine.
* `mkdir` - make directory. You can create directories with this command
*  `cp` - copy a file. You can copy from one place to any other place
*  `mv` - move a file, also used to rename a file
*  `rm` -  delete a file. To delete a folder you need the recursive flag `rm -r [folder]`
*  `cat` - view a file
*  `nano` - this is a text editor (there are many) that will let you edit files in terminal.
 
There is plenty more to learn about using the terminal to navigate a computer but this should give a good start for getting around the raspberry pi.

<!--I am considering that we should remove this section entirely and make them get used to using the terminal at the outset -->
### Enable X Windows

For times we want to use a GUI like a normal computer we will want to enable X windows usage on the Raspberry Pi. (Should this not work see below for instructions on how to use VNC)

On the Mac, please install [XQuartz](https://www.xquartz.org).

On the PC, please install [XMing](https://sourceforge.net/projects/xming/).

To enable XWindows to open with the Pi, we need to log into the Pi with the -X flag to enable xwindows forwarding:
```
shell
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

``Banana.jpg``
``Wormy.py``

### Using VNC
Another way to connect to your IxE is using VNC (Virtual Network Computing). It essentially is remote login. The easiest client to use is [VNC Connect](https://www.realvnc.com/en/connect/download/viewer/). Download and install it. Once that's done type the IP address of the IxE in the text-box at the top. 
![](images/VNC1.png)

After that a login window should appear, use your normal logins (originally: Account=pi, Password=raspberry).
![](images/VNC2.png)

At that point the normal RPI desktop should appear and you can start and stop programs from here. 


