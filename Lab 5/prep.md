### Mediapipe
For the media pipe example create a new virtualenvironment
``````
python -m venv venv-mp 
source venv-mp/bin/activate
``````

Install dependencies in it
``````
(venv-mp) pip install mediapipe pyalsaaudio opencv-python
``````
Make the loop_audio shell script executable 

```
sudo chmod +x ./loop_audio.sh
```
### Teachable Machines
Create another virtual machine for the teachable machines example
``````
python -m venv venv-tml
source venv-tml/bin/activate
``````
Install dependencies in it
``````
(venv-tm) pip install teachable-machine-lite opencv-python
``````