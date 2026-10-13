# Ph-UI!!!


---

## Lab Overview
Jessica Chon (jc3932)
Asian Auntie Machine

## Part 1 Lab Preparation

I decided to create an “Asian Auntie Machine,” for this lab. I was inspired by the common trope of aunties who try to feed you more food, scold you for eating more, but then continue to offer you more anyway. Using a cardboard figure, servos, a proximity sensor, and a small OLED display, I want to recreate this contradictory behavior through beckoning and swatting motions, along with changing facial expressions and/or or sentences on the screen. The goal is to capture the humor and absurdity of this interaction in a playful, physical way.

**\*\*\*Draw 5 sketches that explore different physical arrangements for your sensing and actuation.\*\*\***

Below are my five sketches exploring different physical arrangements for my sensing and actuation components. I tried to consider how the components could be housed without getting in the way of the interaction. For example, many of the sensors and actuators are hidden inside or underneath boxes, with wires concealed within structures such as arms.

<img width="1010" height="763" alt="Screenshot 2026-10-11 at 4 21 48 PM" src="https://github.com/user-attachments/assets/df91ce91-389f-4c89-a6b7-5da19f59b107" />

As I continued sketching, I also started thinking more about how the physical form could contribute to the interaction itself. My designs gradually progressed from a literal, human-like figures to more abstract arrangements. This change came from the useless box inspiration, which I believe is able to convey playfulness and even frustration  without using any literal representations or people.

<img width="1102" height="678" alt="image" src="https://github.com/user-attachments/assets/6caa51b5-d536-4ad3-891d-6e64540a503d" />

**\*\*\*What questions do these sketches raise? What do you need to physically prototype to answer them?\*\*\***

I found the sketching process useful because it made me think more deeply about how I would disguise and house the components, as well as the physical limitations of the items I plan to use. I started considering how much space the servos would need to move the arms, where the sensor should be placed, and how I could hide the wiring without restricting where I could position the components.

The rough cardboard prototype will be helpful in figuring out the auntie's overall form and how the different components could fit together. In particular, I want to test how the arms could hold the snack jar while still allowing enough room for the beckoning and swatting motions. I'll also need to consider where the OLED screen could fit into the face and where the sensor could be positioned to detect the user's gestures without being obstructed by the cardboard. 

I also started thinking more about how to make the machine feel immersive. I hadn't initially thought about adding a screen, but I realized that using a small OLED display as the mouth could help communicate the auntie's reactions and reinforce whether the user should continue taking snacks or stop.

**\*\*\*Pick one design to prototype and explain why.\*\*\***

I decided to go with Sketch 1. Initially, I liked Sketch 4 because I wanted to explore more indirect ways of signaling the interaction to the user. However, I worried that if I made the design too abstract, it could be misconstrued as diet-related commentary rather than poking fun at the absurdity and contradictory nature of this type of Asian auntie interaction. I liked Sketch 1 because I think the cardboard human figure is literal enough to establish that this is an auntie who behaves in a recognizable way, and we generally dismiss more controversial behavior to older figures. I did consider Sketch 2, but as I was acting our the interactions, I believed having the figure hold the jar would add too much intimidation, making users not think they could grab the snacks. 

For the prototype, I'm planning to have the auntie beckon the user to take snacks, then switch to a swatting motion after the user has taken snacks a certain number of times. The OLED mouth will display expressions that reinforce these actions. If the user leaves the machine alone for a while, it will start beckoning them to take snacks again.

**\*\*\*Document your rough prototype with photos and/or video.\*\*\***

As I started working on the physical prototype, I began thinking more seriously about balancing, sizing, and weight. I realized that the auntie couldn't be too small or too big, since that would affect how realistic and comfortable the interaction felt. I wanted her to be large enough to feel like a character the user is interacting with, but not so large that the interaction becomes overwhelming or difficult to approach.

<img width="421" height="539" alt="Screenshot 2026-10-11 at 4 21 27 PM" src="https://github.com/user-attachments/assets/322b405d-7dbe-4baf-8a8a-00062505df4b" />

I also started considering the weight of the arms more carefully. The servos are small and weaker, so I realized I needed to keep the arms as lightweight as possible. Originally, I was thinking of having the hand or wrist rotate to create the beckoning motion more realistically. However, I realized that placing a servo at the end of the arm would add too much weight and make it harder for the main servo to lift the arm. Because of this, I decided to simplify the movements instead. Rather than rotating the wrist, I'm exploring smaller tapping movements against the plate to encourage the user to take more snacks, followed by a larger up-and-down arm movement to imitate a swatting motion or placing a hand over the snacks to tell the user to stop.

<img width="581" height="742" alt="Screenshot 2026-10-11 at 4 21 42 PM" src="https://github.com/user-attachments/assets/b6536d00-4b18-49a5-a3c5-d36baf1cf912" /><img width="585" height="659" alt="Screenshot 2026-10-11 at 4 21 35 PM" src="https://github.com/user-attachments/assets/3cfc805f-cb1d-48be-8605-ecd67059479e" />

I still need to test how fast the servo can move and how that affects the interaction. I want the swatting motion to feel distinct enough to communicate that the auntie is telling the user to stop, but I also don't want it to look too aggressive. Depending on the speed and range of movement, it could come across more as a playful swat or a gentle gesture of disapproval.

**USER TESTING**: I went back home for the weekend, so I was thankfully able to find a friend to user test. My main concern was whether the arm-swinging motion could convey enough emotion and cues to signal when to take or stop taking food. To test this, I asked my friend to go through the interaction with little explanation of the project background so I could see how they would respond naturally.

During testing, I noticed that the arm movements alone weren’t clear enough to communicate when to take more or when to stop, which was what I was concerned with. I also  that the arm didn’t have enough time to react before my friend grabbed the food, making it difficult to use the swinging motion to signal them to stop. More importantly, my friend seemed ready to stop after taking the first piece, rather than continue taking more. She only took more when  I intervened with verbal cues like “take some more!” while mimicing how an Auntie would speak. This made me realize that the interaction was becoming more confusing and burdensome than fun or playful, partly because I was trying to communicate two opposing actions: encouraging the user to take food while also telling them when to stop.

Based on this, I think it would be better to pivot toward encouraging the user to keep taking food rather than adding an element that tells them to stop. I actually feel more confident about this direction because it connects to a real-life experience: my Asian mom wouldn’t stop offering my friend food, even when she protested, haha. I think leaning into this familiar dynamic could make the interaction feel more natural, playful, and relatable. Thsi is further supported by my friend laughing when I kept encouraging her to take food.

For my next iteration, I don’t think I need to change much about the physical prototype, since my friend was amused by its appearance. Instead, I plan to focus on improving the interaction by incorporating the speech element from the last lab and using a sensor to trigger the interaction when the user approaches. When the user tries to leave, the figure will tell them they should take more, while the arm will reinforce this through gentle tapping on the food. All the wiring, raspberry pi, and servos will remain positioned behind the figure, and the arm will be made of paper so it can move quickly and easily without putting too much weight on the servos.

---

## Part 2

Following exploration and reflection from Part 1, complete the "looks like," "works like" and "acts like" prototypes for your design, reiterated below.

---

### Part E

#### Build & Integrate: Sensing + Actuation

For Part 2, build the Feast Automata interaction you developed in Part D by connecting sensing/input to physical actuation.

**Your prototype should:**
- Use at least one sensing or input device.
- Use servo-based physical actuation.
- Connect sensing and actuation into a meaningful interaction around eating, drinking, cooking, serving, or sharing food.
- Additional inputs, displays, LEDs, buttons, or other outputs are optional extensions.

**Document your system with:**
- Code for your sensing + actuation prototype
- Photos and/or video of the working prototype in action
- A simple interaction diagram or sketch showing how sensing and actuation are connected
- Written reflection: What did you learn about connecting sensing, movement, and physical form? What was fun, surprising, or challenging?

**Questions to consider:**
- How does your chosen sensor or input shape the physical response?
- How does the physical arrangement of the sensor and actuator change the interaction?
- What thresholds, timing, or movement patterns make the interaction feel clear or playful?
- What changes when you adjust the sensor placement or servo motion?

Iterate on the sensing, movement, and physical form, and document what you discover.

See encoder_accel_servo_dashboard.py in the Lab 4 folder for an optional example of chaining together three devices.

**`Lab 4/encoder_accel_servo_dashboard.py`**

#### Example Application: Windmill Coaster

Now that you have explored both sensing and actuation, here is a simple example that combines the two.

The **Windmill Coaster** uses a Qwiic distance/proximity sensor to detect when a cup is placed on a coaster. When the cup is detected, a servo motor animates a small windmill by sweeping it back and forth, turning an ordinary action during drinking into a playful physical interaction.

<p align="center">
    <img src="windmill_coaster11.gif" alt="Windmill Coaster Demo" width="400"/>
</p>


This example demonstrates a simple interaction pipeline:

**cup placed → distance sensor detects cup → servo actuates windmill**

Connect the Qwiic distance sensor to the Pi and connect the servo to Channel 0 of the Servo pHAT. Make sure the Servo pHAT is powered through its USB-C connection.

Run the example script:

```bash
python windmill_coaster.py
```

The script continuously reads the proximity value from the distance sensor. When the value passes a threshold, the servo begins animating the windmill. When the cup is removed, the servo stops and returns to its resting position.

You may need to adjust `CUP_THRESHOLD` in [`windmill_coaster.py`](windmill_coaster.py) depending on the size of your cup and the physical placement of the sensor. You can run `qwiic_distance.py` first to compare readings with and without a cup.

Use this example as a starting point. Change the sensor, movement, physical form, or dining interaction to create your own Feast Automata variation.

#### Optional Extensions

The following examples are optional resources if you want to add more inputs or outputs to your prototype.

##### Using Multiple Qwiic Buttons: Changing I2C Address (Physically & Digitally)

If you want to use more than one Qwiic Button in your project, you must give each button a unique I2C address. There are two ways to do this:

##### 1. Physically: Soldering Address Jumpers

On the back of the Qwiic Button, you'll find four solder jumpers labeled A0, A1, A2, and A3. By bridging these with solder, you change the I2C address. Only one button on the chain can use the default address (0x6F).

**Address Table:**

| A3 | A2 | A1 | A0 | Address (hex) |
|----|----|----|----|---------------|
|  0 |  0 |  0 |  0 |    0x6F       |
|  0 |  0 |  0 |  1 |    0x6E       |
|  0 |  0 |  1 |  0 |    0x6D       |
|  0 |  0 |  1 |  1 |    0x6C       |
|  0 |  1 |  0 |  0 |    0x6B       |
|  0 |  1 |  0 |  1 |    0x6A       |
|  0 |  1 |  1 |  0 |    0x69       |
|  0 |  1 |  1 |  1 |    0x68       |
|  1 |  0 |  0 |  0 |    0x67       |
| ...| ...| ...| ... |     ...      |

For example, if you solder A0 closed (leave A1, A2, A3 open), the address becomes 0x6E.

**Soldering Tips:**
- Use a small amount of solder to bridge the pads for the jumper you want to close.
- Only one jumper needs to be closed for each address change (see table above).
- Power cycle the button after changing the jumper.

##### 2. Digitally: Using Software to Change Address

You can also change the address in software (temporarily or permanently) using the example script `qwiic_button_ex6_changeI2CAddress.py` in the Lab 4 folder. This is useful if you want to reassign addresses without soldering.

Run the script and follow the prompts:
```bash
python qwiic_button_ex6_changeI2CAddress.py
```
Enter the new address (e.g., 5B for 0x5B) when prompted. Power cycle the button after changing the address.

**Note:** The software method is less foolproof and you need to make sure to keep track of which button has which address!


##### Using Multiple Buttons in Code

After setting unique addresses, you can use multiple buttons in your script. See these example scripts in the Lab 4 folder:

- **`qwiic_1_button.py`**: Basic example for reading a single Qwiic Button (default address 0x6F). Run with:
	```bash
	python qwiic_1_button.py
	```

- **`qwiic_button_led_demo.py`**: Demonstrates using two Qwiic Buttons at different addresses (e.g., 0x6F and 0x6E) and controlling their LEDs. Button 1 toggles its own LED; Button 2 toggles both LEDs. Run with:
	```bash
	python qwiic_button_led_demo.py
	```

Here is a minimal code example for two buttons:
```python
import qwiic_button

# Default button (0x6F)
button1 = qwiic_button.QwiicButton()
# Button with A0 soldered (0x6E)
button2 = qwiic_button.QwiicButton(0x6E)

button1.begin()
button2.begin()

while True:
		if button1.is_button_pressed():
				print("Button 1 pressed!")
		if button2.is_button_pressed():
				print("Button 2 pressed!")
```

For more details, see the [Qwiic Button Hookup Guide](https://learn.sparkfun.com/tutorials/qwiic-button-hookup-guide/all#i2c-address).

---

##### PCF8574 GPIO Expander: Add More Pins Over I²C

Sometimes your Pi’s header GPIO pins are already full (e.g., with a display or HAT). That’s where an I²C GPIO expander comes in handy.

We use the Adafruit PCF8574 I²C GPIO Expander, which gives you 8 extra digital pins over I²C. It’s a great way to prototype with LEDs, buttons, or other components on the breadboard without worrying about pin conflicts—similar to how Arduino users often expand their pinouts when prototyping physical interactions.

**Why is this useful?**
- You only need two wires (I²C: SDA + SCL) to unlock 8 extra GPIOs.
- It integrates smoothly with CircuitPython and Blinka.
- It allows a clean prototyping workflow when the Pi’s 40-pin header is already occupied by displays, HATs, or sensors.
- Makes breadboard setups feel more like an Arduino-style prototyping environment where it’s easy to wire up interaction elements.

**Demo Script:** `Lab 4/gpio_expander.py`

<p align="center">
    <img src="gpio_leds.gif" alt="GPIO Expander LED Demo" width="400"/>
</p>

We connected 8 LEDs (through 220 Ω resistors) to the expander and ran a little light show. The script cycles through three patterns:
- Chase (one LED at a time, left to right)
- Knight Rider (back-and-forth sweep)
- Disco (random blink chaos)

Every few runs, the script swaps to the next pattern automatically:
```bash
python gpio_expander.py
```

This is a playful way to visualize how the expander works, but the same technique applies if you wanted to prototype buttons, switches, or other interaction elements. It’s a lightweight, flexible addition to your prototyping toolkit.

---


---

---

### Part F

### Final Documentation

Document all the prototypes and iterations you have designed and worked on! Again, deliverables for this lab are writings, sketches, photos, and videos that show what your prototype:
* "Looks like": shows how the device should look, feel, sit, weigh, etc.
* "Works like": shows what the device can do
* "Acts like": shows how a person would interact with the device

---

## Deliverables \& Submission for Lab 4

The deliverables for this lab are, writings, sketches, photos, and videos that show what your prototype:
* "Looks like": shows how the device should look, feel, sit, weigh, etc.
* "Works like": shows what the device can do.
* "Acts like": shows how a person would interact with the device.

For submission, the readme.md page for this lab should be edited to include the work you have done:
* Upload any materials that explain what you did, into your lab 4 repository, and link them in your lab 4 readme.md.
* Link your Lab 4 readme.md in your main Interactive-Lab-Hub readme.md. 
* Labs are due on Mondays, make sure to submit your Lab 4 readme.md to Canvas.
