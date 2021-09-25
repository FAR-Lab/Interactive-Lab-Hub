Last login: Thu Sep 23 12:57:58 on console
(base) kristychen@Kristys-MBP ~ % ssh pi@192.168.1.76
pi@192.168.1.76's password: 
Linux ixe00 5.10.11-v7l+ #1399 SMP Thu Jan 28 12:09:48 GMT 2021 armv7l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Sun Sep 19 15:25:57 2021 from 192.168.1.134
pi@ixe00:~ $ vitualenv circuitpython
-bash: vitualenv: command not found
pi@ixe00:~ $ virtualenv circuitpython
created virtual environment CPython3.7.3.final.0-32 in 1597ms
  creator CPython3Posix(dest=/home/pi/circuitpython, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/home/pi/.local/share/virtualenv)
    added seed packages: Adafruit_Blinka==6.2.2, Adafruit_PlatformDetect==3.1.1, Adafruit_PureIO==1.1.8, Pillow==8.1.1, RPi.GPIO==0.7.0, adafruit_circuitpython_apds9960==2.2.5, adafruit_circuitpython_busdevice==5.0.5, adafruit_circuitpython_register==1.9.4, adafruit_circuitpython_rgb_display==3.10.5, circuitpython_i2c_button==2.2.1, pip==21.0.1, pip==21.2.4, pyftdi==0.52.9, pyserial==3.5, pyusb==1.1.1, rpi_ws281x==4.2.5, setuptools==53.0.0, setuptools==57.4.0, spidev==3.5, sysv_ipc==1.1.0, webcolors==1.11.1, wheel==0.36.2, wheel==0.37.0
  activators BashActivator,CShellActivator,FishActivator,PowerShellActivator,PythonActivator,XonshActivator
pi@ixe00:~ $ source circuitpython/bin/activate
(circuitpython) pi@ixe00:~ $ cd Interactive-Lab-Hub/Lab\ 2/
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ python cli_clock.py
^CTraceback (most recent call last):
  File "cli_clock.py", line 5, in <module>
    sleep(1)
KeyboardInterrupt
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ python screen_clock.py
^CTraceback (most recent call last):
  File "screen_clock.py", line 82, in <module>
    disp.image(image, rotation)
  File "/home/pi/circuitpython/lib/python3.7/site-packages/adafruit_rgb_display/rgb.py", line 197, in image
    pix = color565(img.getpixel((i, j)))
  File "/home/pi/circuitpython/lib/python3.7/site-packages/PIL/Image.py", line 1366, in getpixel
    self.load()
  File "/home/pi/circuitpython/lib/python3.7/site-packages/PIL/Image.py", line 819, in load
    if self.im and self.palette and self.palette.dirty:
KeyboardInterrupt
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ 
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ nano screen_clock.py
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ python screen_clock.py
^[[A^[[A^CTraceback (most recent call last):
  File "screen_clock.py", line 86, in <module>
    disp.image(image, rotation)
  File "/home/pi/circuitpython/lib/python3.7/site-packages/adafruit_rgb_display/rgb.py", line 197, in image
    pix = color565(img.getpixel((i, j)))
KeyboardInterrupt
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ nano screen_clock.py
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ python screen_clock.py
^[[A^CTraceback (most recent call last):
  File "screen_clock.py", line 86, in <module>
    disp.image(image, rotation)
  File "/home/pi/circuitpython/lib/python3.7/site-packages/adafruit_rgb_display/rgb.py", line 199, in image
    pixels[2 * (j * imwidth + i) + 1] = pix & 0xFF
KeyboardInterrupt
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ nano screen_clock.py
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ python screen_clock.py
^CTraceback (most recent call last):
  File "screen_clock.py", line 86, in <module>
    disp.image(image, rotation)
  File "/home/pi/circuitpython/lib/python3.7/site-packages/adafruit_rgb_display/rgb.py", line 200, in image
    self._block(x, y, x + imwidth - 1, y + imheight - 1, pixels)
  File "/home/pi/circuitpython/lib/python3.7/site-packages/adafruit_rgb_display/rgb.py", line 137, in _block
    self._COLUMN_SET, self._encode_pos(x0 + self._X_START, x1 + self._X_START)
  File "/home/pi/circuitpython/lib/python3.7/site-packages/adafruit_rgb_display/rgb.py", line 297, in write
    spi.write(data)
  File "/home/pi/circuitpython/lib/python3.7/site-packages/busio.py", line 317, in write
    return self._spi.write(buf, start, end)
  File "/home/pi/circuitpython/lib/python3.7/site-packages/adafruit_blinka/microcontroller/generic_linux/spi.py", line 83, in write
    self._spi.writebytes(buf[start:end])
  File "/home/pi/circuitpython/lib/python3.7/site-packages/Adafruit_PureIO/spi.py", line 360, in writebytes
    data = array.array("B", data).tobytes()
KeyboardInterrupt
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ nano screen_clock.py
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ python screen_clock.py
  File "screen_clock.py", line 85
    draw.text((x, y), "It's" + strftime(%H:%M), font=font1, fill="#FFFFFF")
                                        ^
SyntaxError: invalid syntax
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ nano screen_clock.py
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ python screen_clock.py
  File "screen_clock.py", line 86
    draw.text((x, y), "It's" + strftime(%H:%M), font=font1, fill="#FFFFFF")
                                        ^
SyntaxError: invalid syntax
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ nano screen_clock.py
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ python screen_clock.py
Traceback (most recent call last):
  File "screen_clock.py", line 87, in <module>
    draw.text((x, y), "It's" + hour + ":" + min, font=font1, fill="#FFFFFF")
TypeError: can only concatenate str (not "int") to str
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ nano screen_clock.py
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ python screen_clock.py
^CTraceback (most recent call last):
  File "screen_clock.py", line 88, in <module>
    disp.image(image, rotation)
  File "/home/pi/circuitpython/lib/python3.7/site-packages/adafruit_rgb_display/rgb.py", line 197, in image
    pix = color565(img.getpixel((i, j)))
  File "/home/pi/circuitpython/lib/python3.7/site-packages/PIL/Image.py", line 1369, in getpixel
    return self.im.getpixel(xy)
KeyboardInterrupt
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ nano screen_clock.py
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ python screen_clock.py
^CTraceback (most recent call last):
  File "screen_clock.py", line 90, in <module>
    disp.image(image, rotation)
  File "/home/pi/circuitpython/lib/python3.7/site-packages/adafruit_rgb_display/rgb.py", line 197, in image
    pix = color565(img.getpixel((i, j)))
  File "/home/pi/circuitpython/lib/python3.7/site-packages/adafruit_rgb_display/rgb.py", line 42, in color565
    def color565(r, g=0, b=0):
KeyboardInterrupt
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ nano screen_clock.py
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ python screen_clock.py
^[[^CTraceback (most recent call last):
  File "screen_clock.py", line 90, in <module>
    disp.image(image, rotation)
  File "/home/pi/circuitpython/lib/python3.7/site-packages/adafruit_rgb_display/rgb.py", line 200, in image
    self._block(x, y, x + imwidth - 1, y + imheight - 1, pixels)
  File "/home/pi/circuitpython/lib/python3.7/site-packages/adafruit_rgb_display/rgb.py", line 137, in _block
    self._COLUMN_SET, self._encode_pos(x0 + self._X_START, x1 + self._X_START)
  File "/home/pi/circuitpython/lib/python3.7/site-packages/adafruit_rgb_display/rgb.py", line 292, in write
    with self.spi_device as spi:
  File "/home/pi/circuitpython/lib/python3.7/site-packages/adafruit_bus_device/spi_device.py", line 76, in __enter__
    baudrate=self.baudrate, polarity=self.polarity, phase=self.phase
  File "/home/pi/circuitpython/lib/python3.7/site-packages/busio.py", line 198, in configure
    if detector.board.any_raspberry_pi or detector.board.any_raspberry_pi_40_pin:
  File "/home/pi/circuitpython/lib/python3.7/site-packages/adafruit_platformdetect/board.py", line 420, in any_raspberry_pi
    return self._pi_rev_code() is not None
  File "/home/pi/circuitpython/lib/python3.7/site-packages/adafruit_platformdetect/board.py", line 196, in _pi_rev_code
    rev = self.detector.get_cpuinfo_field("Revision")
  File "/home/pi/circuitpython/lib/python3.7/site-packages/adafruit_platformdetect/__init__.py", line 53, in get_cpuinfo_field
    match = re.search(pattern, line, flags=re.IGNORECASE)
  File "/usr/lib/python3.7/re.py", line 183, in search
    return _compile(pattern, flags).search(string)
  File "/usr/lib/python3.7/re.py", line 274, in _compile
    flags = flags.value
  File "/usr/lib/python3.7/types.py", line 164, in __get__
    def __get__(self, instance, ownerclass=None):
KeyboardInterrupt
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ nano screen_clock.py
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ python screen_clock.py
^CTraceback (most recent call last):
  File "screen_clock.py", line 95, in <module>
    disp.image(image, rotation)
  File "/home/pi/circuitpython/lib/python3.7/site-packages/adafruit_rgb_display/rgb.py", line 197, in image
    pix = color565(img.getpixel((i, j)))
  File "/home/pi/circuitpython/lib/python3.7/site-packages/PIL/Image.py", line 1369, in getpixel
    return self.im.getpixel(xy)
KeyboardInterrupt
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ nano screen_clock.py
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ python screen_clock.py
  File "screen_clock.py", line 96
    y += size1
             ^
TabError: inconsistent use of tabs and spaces in indentation
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ nano screen_clock.py
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ nano screen_clock.py
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ python screen_clock.py
^CTraceback (most recent call last):
  File "screen_clock.py", line 96, in <module>
    disp.image(image, rotation)
  File "/home/pi/circuitpython/lib/python3.7/site-packages/adafruit_rgb_display/rgb.py", line 197, in image
    pix = color565(img.getpixel((i, j)))
  File "/home/pi/circuitpython/lib/python3.7/site-packages/PIL/Image.py", line 1366, in getpixel
    self.load()
  File "/home/pi/circuitpython/lib/python3.7/site-packages/PIL/Image.py", line 841, in load
    if cffi and USE_CFFI_ACCESS:
KeyboardInterrupt
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ nano screen_clock.py
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ python screen_clock.py
  File "screen_clock.py", line 96
    y += size1
             ^
TabError: inconsistent use of tabs and spaces in indentation
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ nano screen_clock.py
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ python screen_clock.py
^[[A^[[A^CTraceback (most recent call last):
  File "screen_clock.py", line 97, in <module>
    disp.image(image, rotation)
  File "/home/pi/circuitpython/lib/python3.7/site-packages/adafruit_rgb_display/rgb.py", line 197, in image
    pix = color565(img.getpixel((i, j)))
  File "/home/pi/circuitpython/lib/python3.7/site-packages/PIL/Image.py", line 1366, in getpixel
    self.load()
  File "/home/pi/circuitpython/lib/python3.7/site-packages/PIL/Image.py", line 849, in load
    return self.im.pixel_access(self.readonly)
KeyboardInterrupt
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ nano screen_clock.py
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ python screen_clock.py
^[[A^CTraceback (most recent call last):
  File "screen_clock.py", line 98, in <module>
    disp.image(image, rotation)
  File "/home/pi/circuitpython/lib/python3.7/site-packages/adafruit_rgb_display/rgb.py", line 197, in image
    pix = color565(img.getpixel((i, j)))
  File "/home/pi/circuitpython/lib/python3.7/site-packages/PIL/Image.py", line 1367, in getpixel
    if self.pyaccess:
KeyboardInterrupt
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ nano screen_clock.py
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ dir /ad
dir: cannot access '/ad': No such file or directory
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ dir
button_device.py       I2C_scan.py					     partslist.md	       README.md	 screen_test.py
button_registers.py    image.py						     PlacingMiniPiTFTonPi.jpg  red.jpg		 stats.py
cli_clock.py	       library_example.py				     prep.md		       requirements.txt
Extending\ the\ Pi.md  Other\ ways\ to\ connect\ IxE\ to\ your\ computer.md  proximity.py	       screen_clock.py
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ cp /kristychen/Downloads/water.jpg /Interactive-Lab-Hub/Lab 2
cp: target '2' is not a directory
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ cp /kristychen/Downloads/water.jpg /Interactive-Lab-Hub/Lab\ 2/
cp: cannot stat '/kristychen/Downloads/water.jpg': No such file or directory
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ cd kristychen
-bash: cd: kristychen: No such file or directory
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ cd /kristychen
-bash: cd: /kristychen: No such file or directory
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ git add .
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ git commit -m 'Lab 2
> ^C
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ git commit -m 'Lab 2'

*** Please tell me who you are.

Run

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

to set your account's default identity.
Omit --global to set the identity only in this repository.

fatal: unable to auto-detect email address (got 'pi@ixe00.(none)')
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ git config --global user.email "kristy.sh.chen@gmail.com"
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ git config --global user.name "Kristy Chen"
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ git add .
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ git commit -m 'Lab 2'
[Fall2021 451eabf] Lab 2
 1 file changed, 33 insertions(+), 6 deletions(-)
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ git push
Username for 'https://github.com': kchen1009
Password for 'https://kchen1009@github.com': 
To https://github.com/kchen1009/Interactive-Lab-Hub.git
 ! [rejected]        Fall2021 -> Fall2021 (fetch first)
error: failed to push some refs to 'https://github.com/kchen1009/Interactive-Lab-Hub.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ git add .
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ git commit -m 'Lab 2'
On branch Fall2021
Your branch is ahead of 'origin/Fall2021' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ git push
Username for 'https://github.com': kchen1009
Password for 'https://kchen1009@github.com': 
To https://github.com/kchen1009/Interactive-Lab-Hub.git
 ! [rejected]        Fall2021 -> Fall2021 (fetch first)
error: failed to push some refs to 'https://github.com/kchen1009/Interactive-Lab-Hub.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ nano screen_clock.pyclient_loop: send disconnect: Broken pipe
(base) kristychen@Kristys-MBP ~ % ssh pi@192.168.1.76
pi@192.168.1.76's password: 
Linux ixe00 5.10.11-v7l+ #1399 SMP Thu Jan 28 12:09:48 GMT 2021 armv7l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Sat Sep 25 12:42:55 2021 from 192.168.1.134
pi@ixe00:~ $ virtualenv circuitpython
created virtual environment CPython3.7.3.final.0-32 in 1786ms
  creator CPython3Posix(dest=/home/pi/circuitpython, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/home/pi/.local/share/virtualenv)
    added seed packages: Adafruit_Blinka==6.2.2, Adafruit_PlatformDetect==3.1.1, Adafruit_PureIO==1.1.8, Pillow==8.1.1, RPi.GPIO==0.7.0, adafruit_circuitpython_apds9960==2.2.5, adafruit_circuitpython_busdevice==5.0.5, adafruit_circuitpython_register==1.9.4, adafruit_circuitpython_rgb_display==3.10.5, circuitpython_i2c_button==2.2.1, pip==21.0.1, pip==21.2.4, pyftdi==0.52.9, pyserial==3.5, pyusb==1.1.1, rpi_ws281x==4.2.5, setuptools==53.0.0, setuptools==57.4.0, spidev==3.5, sysv_ipc==1.1.0, webcolors==1.11.1, wheel==0.36.2, wheel==0.37.0
  activators BashActivator,CShellActivator,FishActivator,PowerShellActivator,PythonActivator,XonshActivator
pi@ixe00:~ $ source circuitpython/bin/activate
(circuitpython) pi@ixe00:~ $ cd Interactive-Lab-Hub/Lab\ 2/
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ nano screen_clock.py

  GNU nano 3.2                                                        screen_clock.py                                                                  

while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    #TODO: Lab 2 part D work should be filled in here. You should be able to look in cli_clock.py and stats.py 
    y = top
    draw.text((x, y), "You need to consume", font=font1, fill="#FFFFFF")
    y += size1
    draw.text((x, y), "2L", font=font3, fill="#0000FF")
    y += size3
    draw.text((x, y), "of water daily", font=font1, fill="#FFFFFF")
    time = datetime.datetime.now()
    hour = time.hour
    min = time.minute
    now = int(2000/24*hour)
    if not buttonA.value:
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        y = top
        draw.text((x, y), "Current time:  ", font=font1, fill="#FFFFFF")
        y += size1
        draw.text((x, y), str(hour) + ":" + str(min), font=font2, fill="#FFC0CB")
        y += size2
        draw.text((x, y), "You should consume", font=font1, fill="#FFFFFF")
        y += size1
        draw.text((x, y), str(now) + "mL", font=font3, fill="#0000FF")
    disp.image(image, rotation)
