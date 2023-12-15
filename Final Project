# Magic Cube

Group Members: John Li (jl4239), Mingze Gao (mg2454), Crystal Chong (cc2795), Mingzhe Sun (ms3636)

Special thanks to Qianxin(Carl) Gan (qg72)

## Description
The "Magic Cube" project is an innovative controller that responds to the user's gestures. It is a dynamic system that consists of a main cube with an array of 16 smaller cubes, each programmed to create captivating patterns through choreographed movements. This cutting-edge controller elevates user experience by transforming simple gestures into interactive art.

The system is designed with a cube controller that connects via WIFI. It includes an ESP32, a gyroscope sensor, an accelerometer, haptic feedback, and is powered by a LiPo battery. The structural components consist of a 3D-printed cube, a structure sender using MQTT via WIFI, and a cube feedback touch utilizing capacitive touch.

The block diagram outlines the various components of the system, which includes a wireless charging pad, a LiPo battery, a haptic driver with a haptic motor, and an accelerometer all connected to an ESP32 Feather. It connects to a server via WiFi, and the signals are then sent to a servo driver controlling a 4x4 servo array.

This innovative system is not just a piece of technology but an artistic tool that reimagines control and interaction in a digitally enhanced physical space.
## Project Plan
### Big Idea
### Timeline
Project plan - November 14
Peer feedback on Project plans: November 21
Functional check-off - November 30
Cube controller hardware integration - December 3
Servo array software function validation - December 9
Cube embedded system function validation - December 9
Servo array  system assemble - December 11
Final Project Presentations - December 12
Write-up and documentation - December 15 

### Parts Needed
#### Servo Array
SG90 9g Micro Servo Motor S51 * 16
Zio 16 Servo Controller * 1
3D Printed Array * 1
3D Printed Piston * 16
#### Cube Controller
Adafruit ESP32-S2 Feather with BME280 Sensor - STEMMAQT -4MB Flash + 2 MB PSRAM
Universal Qi Wireless Receiver Module
Adafruit Micro-Lipo Charger for LiPo/Lilon Batt w/MicroUSB
Jack - v1
Lithium lon Polymer Battery - 3.7v 1200mAh
Adafruit DRV2605L Haptic Motor Controller - STEMMA QT/Qwiic
Vibrating Mini Motor Disc
3D Printed Cube
### Fall-back 
The main challenge of the project is the  mechanic structure of the 3D printed servo array. The servo should be structed in a way to push up the piston smoothly and create a strong visual effect.  The fall-back plan for this is to use cardboard to create similar visual effect which is esaier and time-saving.  


## Functioning Project
The "Magic Cube" project has been successfully implemented, resulting in a fully functioning interactive device. Here are the key components and functionalities of the completed project:

### Cube Controller Features:

- **ESP32 Connectivity:** The cube controller seamlessly connects to the server via WiFi using the ESP32 module.
- **Gesture Recognition:** Utilizing the gyroscope sensor, the cube responds to user gestures, translating them into dynamic patterns.
- **Haptic Feedback:** Integrated with the Adafruit DRV2605L Haptic Motor Controller, the cube provides tactile feedback for enhanced user interaction.
- **Wireless Charging:** The inclusion of a Universal Qi Wireless Receiver Module enables convenient wireless charging of the LiPo battery.

### Servo Array Features:

- **16-Servo Array:** The servo array, controlled by a Zio 16 Servo Controller, creates visually captivating patterns through choreographed movements.
- **3D Printed Structure:** The 3D-printed servo array, along with pistons, contributes to the mechanical structure, ensuring smooth movements for a strong visual effect.

### Overall System Integration:

- **MQTT Communication:** The system employs MQTT communication for seamless interaction between the cube controller, servo array, and the server.
- **Capacitive Touch:** Cube feedback touch, utilizing capacitive touch, enhances the user experience with additional interactive elements.

### Testing and Validation:

- **Functional Check-Off:** The project successfully passed the functional check-off on November 30, ensuring that all individual components work cohesively.
- **Pattern Validation:** The servo array software functions were validated on December 9, confirming the creation of captivating patterns.
- **Embedded System Validation:** On the same date, the cube embedded system functions were validated, ensuring smooth operation.

## Code documentation
### Required Tools and Software:
**Arduino IDE:** To upload the cube_control.ino sketch to the microcontroller.
**Python Environment:** Python 3.x with paho-mqtt library installed (install via pip install paho-mqtt).
**MQTT Broker:** Access to an MQTT broker (could be a local or cloud-based broker like Mosquitto or HiveMQ).

### Setting Up the Arduino Environment:
Open the cube_control.ino File:
Launch the Arduino IDE.
Open the cube_control.ino file in the IDE.
#### Configure Network: 
line21:
`const char* ssid = "WhiteSky-Cornell";`
`const char* password = "4xjf6grn";`

#### and MQTT Settings:
User open ssl to get the ssl  certificate for access MQTT server.
`openssl s_client -connect farlab.infosci.cornell.edu:8883 -showcerts`
Include the last certificate from the resulting command
`const char* ROOT_CERT = "-----BEGIN CERTIFICATE-----\n"
"MIID0zCCArugAwIBAgIQVmcdBOpPmUxvEIFHWdJ1lDANBgkqhkiG9w0BA
......
-----END CERTIFICATE-----\n'`

line 34:
`const char* mqtt_broker = "farlab.infosci.cornell.edu";`
`const int mqtt_port = 8883;`
`const char* mqtt_username = "idd";`
`const char* mqtt_password = "device@theFarm";`
`const char* topic = "IDD/Cube";`

update the WiFi credentials (ssid and password) to connect to the available network.
Set the MQTT broker address to the one you are using (mqtt_server variable).

#### Upload to the Microcontroller:

Connect the microcontroller (e.g., ESP8266, ESP32) to your computer via USB.
Select the correct board and port in the Arduino IDE.
![image](https://hackmd.io/_uploads/B1SkkZdU6.png)

### Setting Up the Python Listener:
#### Open the cube_listener.py File:
Ensure Python 3 or higher is installed on your computer.
Open the cube_listener.py file in a Python IDE or text editor.

#### Configure MQTT Settings:
In the Python script, set the broker_address to the same MQTT broker address used in the Arduino sketch.

`line 74: topic = 'IDD/a/fun/topic'`

Ensure the topic variable matches the topic used in the Arduino sketch.

#### Run the Python Script:

Run the cube_listener.py script in your Python environment.

`python cube_listenor.py`

The script will connect to the MQTT broker and listen to the specified topic.


### Testing the Setup:

#### Verify Connection:
Ensure both the microcontroller and the Python listener are connected to the MQTT broker.
Check the serial monitor in the Arduino IDE and the console in your Python environment for connection status.
cube_controllor.ino line 147:
`testing hello`

#### Send and Receive Messages:
The cube_control.ino sketch should be sending data(0-16, 99) to the MQTT broker.
The cube_listener.py script should receive and display these messages.

![image](https://hackmd.io/_uploads/SkLXkZOUT.png)


#### Troubleshooting:
If messages are not being received, verify network connectivity, broker settings, and topic names.
Ensure that the MQTT broker is running and accessible to both the microcontroller and the Python listener.

### Additional Notes:
These instructions assume a basic setup. Adjustments might be required based on the specifics of your MQTT broker and network environment.
For any issues or further clarification, please refer to the project documentation or contact the project team.

## Video Demostration
Demo for water wave pattern (Click to view the demo)
[![Demo for water wave pattern](https://hackmd.io/_uploads/BJpRjQKL6.png)](https://youtu.be/geulUWIEBAU?si=RRKsR7cBHxGSDyE2)

Demo for emojis pattern (Click to view the demo)
[![Demo for emojis pattern](https://hackmd.io/_uploads/BJmNnXt8T.png)](https://youtube.com/shorts/qyMroalDsIY?si=0ZJFcywn6DtwDChw)

Demo for snake pattern and alphabetics (Click to view the demo)
[![Demo for snake pattern and alphabetics](https://hackmd.io/_uploads/Bke837KUT.png)](https://youtube.com/shorts/A0PCnrdS-2E?si=upPTQTMMarFyF1BD)


## Reflection
In the process of creating the "Magic Cube," we have gained a wealth of knowledge and insights. The project reinforced the necessity of having a broad skill set that spans multiple disciplines, including electronics, coding, and design, which are crucial when building interactive tools. One major takeaway was the complexity involved in establishing stable wireless connections using MQTT, which was a cornerstone for the cube's communication. Managing the energy consumption for such an interactive device proved to be a delicate balancing act, one that is as crucial as any other aspect of design.

The physical design's influence on user interaction was another significant lesson; understanding this from the beginning would have shaped early design choices. Learning the value of iterative design through repeated prototyping phases, each refinement brought the project closer to its final form. Early user testing would have provided insights that could have fine-tuned the project more effectively. Time management, detailed record-keeping, and adaptability in problem-solving are skills that have been sharpened and will be invaluable for future projects. We learned this experience is not just a recount of the past but a set of practical lessons for future technological endeavors.

## Work Distribution
We capitalized on our individual strengths to distribute the workload efficiently for the "Magic Cube" project. One person took the lead on electronics, meticulously wiring, and soldering components to ensure the cube's responsiveness. Two group members were in charge of coding the system, implementing MQTT for communication, and ensuring seamless integration of the software with the main cube. The other two members were in charge of coding the raspberry Pi that receives the message from the main cube to control the set of 16 small blocks. We also had one person manage the physical construction and aesthetics of the cube, utilizing 3D printing technology to bring the structural concept to life. Lastly, all members focused on user experience and testing, gathering feedback to refine the interaction process, and documenting our progress for future reference. This collaborative effort allowed us to utilize each member's expertise effectively resulting in a well-rounded and innovative project outcome. We also want to thank Carl Gan who supported us in modeling 3D printings. 














## Objective

The goal of this final project is for you to have a fully functioning and well-designed interactive device of your own design.
 
## Description
Your project is to design and build an interactive device to suit a specific application of your choosing, and *test the interaction with people*. 

## Deliverables

1. Project plan: Big idea, timeline, parts needed, fall-back plan.

2. Functioning project: The finished project should be a device, system, interface, etc. that people can interact with.

3. Documentation of design process
4. Archive of all code, design patterns, etc. used in the final design. (As with labs, the standard should be that the documentation would allow you to recreate your project if you woke up with amnesia.)
5. Video of someone using your project
6. Reflections on process (What have you learned or wish you knew at the start?)

7. Group work distribution questionnaire

## Change of Design

It is fine to change your project goals, but please resubmit the project plan for the new design when you do that.

## Grading rubric

20% Project planning: Allocation of needed resources (time, people, materials, facilities) anticipated well.
20% Design of project: Interaction, hardware and software aspects of projects planned well.
20% Testing of project: Functional or wizarded system tested with people
20% Prototype functionality: System capable of interaction, either through autonomous or wizarded mechanisms
20% Project documentation: Text, video, and photo of project illustratign capability and documenting plans and process

## Teams

You can and are not required to work in teams. Be clear in documentation who contributed what. The total project contributions should reflect the number of people on the project.

## Examples

[Here is a list of good final projects from previous classes.](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/wiki/Previous-Final-Projects)

