INFO 4325: Interactive Device Design 
# RIOC Bus Tracker Project
Group Members: Sarang Pramode (sp872) & Olena Bogdanov (ob234) 

### Problem Statement 
Roosevelt Island residents(specifically Cornell Tech Students) are not aware of the RedBus schedule in realtime. The schedule is posted on a static page which can be found here, which varies based on rush hour and driver availability. From experience this has not been consistent and can lead to wait time from anywhere between 2min to 20min.

### Problem Description
We hope to create a device people can interact with to be aware of bus schedules. We also hope to study user interactions with the red bus, specifically, learn the number of students using the bus and the pain points as to when they don't want to use it.

### User Research 
To begin our project, we reached out to a few friends who live in the house to ask them about their experiences taking the RIOC bus. Most of them prefer to walk to Main Street because it’s faster, and generally avoid taking the red bus. In general, people seemed to be averse to taking the RIOC bus for the sake of efficiency - they were unsure of where the bus is, when it would arrive, and preferred to avoid relying on the 15-minute estimate offered by RIOC. However, two students mentioned that they would be more likely to travel via bus if the bus schedule offered more detailed information on this mode of transportation. Overall, it seems that a lack of awareness about the bus, avoidance of relying on estimated bus schedules, and a preference for walking are some of the pain points that residents of Roosevelt Island experienced when it comes to engaging with the RIOC bus system. In conclusion, there are a few main things we wanted to keep in mind going forward: [1] There exists a lack of information on bus times, which leads to erratic wait times for students, [2] Students are not aware that an online bus schedule exists, and [3] students reported that they would take the bus if they anticipated its arrival, however it was the lack of available information which caused the greatest amount of inconvenience and uncertainty.

### Storyboard & Verplank Diagram 
For our [storyboard](https://github.com/sp872-Sarang/Interactive-Lab-Hub/blob/fe5d31931dcc0aeeabb3734472247a36b69404b5/Final%20Project/assets/storyboard.png) and [verplank](
https://github.com/sp872-Sarang/Interactive-Lab-Hub/blob/fe5d31931dcc0aeeabb3734472247a36b69404b5/Final%20Project/assets/verplank.png) diagram our goal was to convey the inefficiencies that emerge when interacting with the bus network. We re-create an experience many Roosevelt Island residents can relate to; traveling to the bus stop, only to experience odd departure and arrival times, ultimately reducing the users ability to interact with the system. The breakthrough occurs when our subject, Jack, notices a new, innovative product that resolves this issue - the bus tracker system, which ensures that users have the best understanding of when and where to catch the bus. 

![storyboard](https://github.com/sp872-Sarang/Interactive-Lab-Hub/blob/fe5d31931dcc0aeeabb3734472247a36b69404b5/Final%20Project/assets/storyboard.png)
![verplank](https://github.com/sp872-Sarang/Interactive-Lab-Hub/blob/fe5d31931dcc0aeeabb3734472247a36b69404b5/Final%20Project/assets/verplank.png)

&nbsp; &nbsp;

## Ideation Part 1: Prototypes 
The idea is to create a local mesh network which is placed on a single strip in line of sight on west loop road which can notify users standing on the bus stop at the entrance of Cornell Tech campus. The outcome of this section correspond to the [Functional Check-Off Slide Set](https://docs.google.com/presentation/d/1ggy2iLC1x2BC1jz5pk0lwDpPvXzG58ecRH5AkmBrPm4/edit?usp=sharing). 

### Detection Node 
We considered a few factors when designing the prototype for the detection node. First, we wanted to make sure that the detection node worked for different environments - our first course of action would be to pilot-test the product, meaning that the design specifications for the detection node housing, and the included components would be different from the final product. 

The first prototype diagram, we focused on designing a product that would be possible to implement on a short-term basis, and as a result, we required a battery pack to be installed within the detection node. It is segmented into three major components: the battery pack, central pi unit, and the webcam. As the permanent installation would not require a battery pack, the final component would be much smaller. 

### Communication Node 
We emulated a bus arrival using a flag which was changed manually. We used this prototype to develop the state diagram and data packets and test any bugs when designing the system. Ultimately, we decided not to incorporate it into the final prototype as the screen wasn't the correct size - users found it difficult to see and interact with. Our nex steps were to implement a dashboard which can accessed by scan via the users mobile device. 

[Video | Prototype Testing | Bus Arrival Emulation](https://drive.google.com/file/d/1RdR2YJqAdSTYUIs21w_4qgJ3VvrxD971/view?usp=sharing)

[Video | Functional Check-In](https://drive.google.com/file/d/1C4MjyItW-Z7OiaSUTtsryfwuJhHPJi3L/view?usp=sharing)

### Object Recognition: Initial model tests & results
This project is focused on real-time object tracking of the RIOC bus, using computer vision and machine learning for image processing. We explored multiple methods for facilitating real-time, accurate object detection. 

The first system used the YOLO object detection model, which is capable of frame-by-frame object recognition across 80 classes. This model is simple, lightweight, and easy to implement, and it performed well during the initial functional check-in. In order to facilitate the interaction between YOLO and the Raspberry Pi, we focused on using BerryNet, an open-source library that creates a gateway between edge devices and deep learning models. However, after encountering a Berry-side technical incompatibility, we moved to implementing a different deep-learning / pi architecture for this project. 

In order to complete image detection, our starting point was the YOLO model, which is pre-trained to detect a bus, among other objects. We tested our starting model on RIOC bus images, which worked well and offered a great starting point that would allow us to integrate the model into the final project. 


## Ideation: Part 2: Results 
In this section, we describe the outcome of the first stage and provide a final overview of the bus detection system. 

### Node State Diagrams 
After developing an initial prototype and implementing node-to-node communication, we implemented the following state diagrams for the [interface](https://github.com/sp872-Sarang/Interactive-Lab-Hub/blob/e62b6822117f246068863c833ccb4a9993b33964/Final%20Project/assets/interface_node.png) and [detection](https://github.com/sp872-Sarang/Interactive-Lab-Hub/blob/034888a7a6f3bcd51b3cb09fa7d195bbcbbbfa99/Final%20Project/assets/detection_node.png) nodes.

![interface](https://github.com/sp872-Sarang/Interactive-Lab-Hub/blob/e62b6822117f246068863c833ccb4a9993b33964/Final%20Project/assets/interface_node.png)

![detection](https://github.com/sp872-Sarang/Interactive-Lab-Hub/blob/034888a7a6f3bcd51b3cb09fa7d195bbcbbbfa99/Final%20Project/assets/detection_node.png)

### ML Model 
The final prototype used the tensorflow object-detection pipeline on the pi. Tensorflow lite is a lightweight version of tensorflow designed for low powered devices such as the raspberry pi. This format is usually used for IoT applications, for its small size and faster performance than bigger models. In this case, this format is perfect for the Raspberry Pi. 

#### Using a model trained on a generic dataset 
We used efficientnet-Lite0 object detection model, which was pretrained on a COCO 2017 dataset and optimized for TFLite. EfficientNet-Lite brings the power of EfficientNet to edge devices and comes in five variants, allowing users to choose from the low latency/model size option (EfficientNet-Lite0) to the high accuracy option (EfficientNet-Lite4). We were able to extract the class that represents a bus, which can be used to update other sensors, as well as the dashboard, of bus arrival and departures. 

#### Training a model on a custom dataset 
Since the previous model was trained on a generic dataset, we tried another approach to see if we could get results better suited to the scope of our project. We selected the [MobileNet SSD v2](https://roboflow.com/model/mobilenet-ssd-v2), as this architecture provides good realtime results on limited compute. It's designed ot run in realtime at 30 frames per second, even on mobile devices. 

The [custom dataset](https://github.com/sp872-Sarang/Interactive-Lab-Hub/blob/018593d8a53b3f162953bc7cc58d3c17dc75c91e/Final%20Project/ML_model/bus.v1i.tfrecord.zip) is a compliation of hand-labelled images of the RIOC bus, which was then procesed on [Roboflow](https://github.com/sp872-Sarang/Interactive-Lab-Hub/blob/cb5dc5be27b8684cff2ac81879d74dc14d92678a/Final%20Project/assets/roboflow_example.png) and converted into a tf-compatible doc. We found that the efficient-net-Lite0 option works better, and hope to use our dataset with this model in the future. 

<img src="https://github.com/sp872-Sarang/Interactive-Lab-Hub/blob/cb5dc5be27b8684cff2ac81879d74dc14d92678a/Final%20Project/assets/roboflow_example.png" height="500">

The following is a video of the model in action, however, the display showing bus-detection results is shown in the image. 

[Bus Detection Test](https://youtube.com/shorts/_5twojFx45Q?feature=share)

<img src="https://github.com/sp872-Sarang/Interactive-Lab-Hub/blob/4bafcd50ecc672135bdde3c47ca5bda962f00404/Final%20Project/assets/bus%20detection%20res.jpg" height="500">

One important thing to keep in mind is that the model detects numerous frames each second and labels them - as a result, additional logic is required to ensure stable tracking of the bus. For instance, tracking the time first seen and time last seen may be more helpful rather than getting a frame-by-frame output of each result. 

### System Architecture 
Our system is dependent on two nodes: an interface and detection node, which work in unison to transmit information on bus operation times. We use the NRF tranciever modules to communicate between the two systems. In the final iteration of our project, our system architecture changed to replace existing planned BerryNet + Yolo structure with the TFlite + OpenCV pipeline. 

![System Architecture](https://github.com/sp872-Sarang/Interactive-Lab-Hub/blob/fa5ff72fb99f6b55bd14c44b263edc6dd49b7858/Final%20Project/assets/system_architecture.png)

### Process Diagram 
We developed this process diagram to illustrate the relationships between major components of the bus monitoring system. In order to increase the scope of the project, we implement a communication node that facilitates the interaction between the detection and interface nodes. The goal is to transmit data as steadily and quickly as possible throughout the system, after the detection node has tracked the RIOC bus. 

![process diagram](https://github.com/sp872-Sarang/Interactive-Lab-Hub/blob/530bb67bf0378f3367b456e08bc423b07537cbc5/Final%20Project/assets/process%20diagram.png)

### Final Dashboard & test
The dashboard was built from the ground up using HTML, CSS and Javascript and run on a local apache web server on bootup at the interface node.With the current device users can view the dashboard by connecting to a local hotspot at the bus stop. When connected , they will be directed to the bus tracker dashboard. If the device were to be deployed at bus stops we expect to connect to the eduroam/Cornell’s/ public networks so that users may scan a QR code and get access to bus status information at various bus stops. With public access networks there is a necessity for security but that is not explored as part of this project.

![dash](https://github.com/sp872-Sarang/Interactive-Lab-Hub/blob/e6f7e75ddedf1ff55a413023c7806b0e421da064/Final%20Project/assets/dash.png)

<img src="https://github.com/sp872-Sarang/Interactive-Lab-Hub/blob/bb83e434f62f158cb916c3ed696cd2f37c358780/Final%20Project/assets/test1.jpeg" height="250">

<img src="https://github.com/sp872-Sarang/Interactive-Lab-Hub/blob/bb83e434f62f158cb916c3ed696cd2f37c358780/Final%20Project/assets/test2.jpeg" height="250">

<img src="https://github.com/sp872-Sarang/Interactive-Lab-Hub/blob/bb83e434f62f158cb916c3ed696cd2f37c358780/Final%20Project/assets/test3.jpeg" height="250">


## Conclusion & Future Work
During the initial phase of the project ideation we wanted to create a device which was universal to interact with and solved 2 key problems - 1) Access to bus time information and 2) Reduce wait times at the bus stops. After internally testing various versions we realized that the key decision users would make is either wait for the bus or decide to walk and save time, which relied on knowing if the bus were to arrive soon or not. Hence a local server which users could connect to would provide access to bus times solved a key pain point. We did try getting in touch with RIOC to see if we could deploy our prototype on the west loop road, but they weren't as responsive as we hoped. 

In future iterations, we hope to add a larger LED screen/tablet which users can interact with and use a touch panel to allow users to use the system. We also hope to scale the system to multiple stops.
















