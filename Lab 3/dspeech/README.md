# DeepSpeech

This uses [Mozilla DeepSpeech](https://github.com/mozilla/DeepSpeech) and works shockingly well even on the Pi. You may want to change the VAD (Voice Activity Detection) parameter down to 2 given the quality of our microphones. 

## Setup
Undering the virtual environment you created for this exercise, `cd` to the `dspeech` folder under Lab 3 and run the following command lines:

```
(dspeechexercise) pi@ixe00:~/Interactive-Lab-Hub/Lab 3/dspeech $ sudo apt-get install libatlas3-base
(dspeechexercise) pi@ixe00:~/Interactive-Lab-Hub/Lab 3/dspeech $ pip install -r requirements.txt
(dspeechexercise) pi@ixe00:~/Interactive-Lab-Hub/Lab 3/dspeech $ sh downloader.sh
```

## Running

```
(dspeechexercise) pi@ixe00:~/Interactive-Lab-Hub/Lab 3/dspeech $ python deepspeech_demo.py -m deepspeech-0.9.3-models.tflite -s deepspeech-0.9.3-models.scorer
```
