# Pre Lab

If you don't have all your parts you will be doing Alt Lab 5. That is a combination of labs 4 + 5.

## Surface Mounting
Before lab:
- Take index of your parts. If things are missing order them ASAP
- Read about the methods of surface mount soldering. [This](https://www.sparkfun.com/tutorials/59) and [this](https://learn.adafruit.com/smt-manufacturing/overview) are good overviews of the ways we can get SMD components to stick to a board.
### For those of you in NYC
- determine if you have access to the Makerlab. If you do not take whatever steps are necessary to get there (e.g. covid test, speaking to Makerlab director Niti Parikh, etc)
- I am hoping there is enough room in the Makerlab for us to be there socially distanced. We will primarily be talking about hot air re-work stations and reflow ovens. _You should still read about the methods for DIY at home Surface Mount soldering_. You will not have access to Cornell Tech and the Makerlab forever, learning techniques for doing this at home make for a more valuable skill than only being able to do it with specialized equipment.
### For those of you not in NYC
- get your hands on [Lead free low heat solder paste](https://www.digikey.com/short/z22b2r). There are tons of these with various attributes. Just make sure you can put a relatively fine tip on it. When it comes, refrigerate it. Tweezers are more or less a necessity, you can use what you have at home but precision tweezers make a difference and don't cost much. I like  [these](https://www.adafruit.com/product/422). I also would highly recommend getting a [flux pen](https://www.adafruit.com/product/3468), these are good for surface mount, but also regular soldering and desoldering.
- What method you eventually decide to go with will depend on your particular set up. In general the method described in the [first](https://www.sparkfun.com/tutorials/59) reading with a hot plate or skillet. A stove will also work but either a.) **USE A PAN YOU DON"T COOK WITH** and/or b.) coat the bottom in tin foil. A layer of sand in the pan will distribute heat for more even heating.
- There is no reason you can't combine methods. Hand soldering a pin or two of the dense IC's will keep them from shifting around.

## Burning a bootloader
- Be able to answer "What is a [bootloader](https://www.baldengineer.com/arduino-bootloader.html)?" There will be a pop quiz.
- On the board you designed determine which pins map to MOSI, MISO, SCK, RST, VCC and GND.
- Take a look at how to burn an [arduino with another arduino](https://www.arduino.cc/en/tutorial/arduinoISP). Is there anything you will have to do differently
- Which boot loader is on the [metro mini](https://www.adafruit.com/product/2590) in your kit?
- The arduinoIDE stores board file in `/Users/(username)/Library/Arduino15/packages`, You can see where this is by looking at the bottom of the preferences menu.
- In `/Users/(username)/Library/Arduino15/packages/adafruit/hardware/avr/(version #)/` what is the `boards.txt` file doing?


