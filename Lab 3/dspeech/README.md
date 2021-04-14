# DeepSpeech

This uses [Mozilla DeepSpeech](https://github.com/mozilla/DeepSpeech) and works shockingly well even on the Pi. You may want to change the VAD (Voice Activity Detection) parameter down to 2 given the quality of our microphones.

## Setup

```
sudo apt-get install libatlas3-base
pip install -r requirements.txt
sh downloader.sh
```

## Running

```
python deepspeech_demo.py -m deepspeech-0.9.3-models.tflite -s deepspeech-0.9.3-models.scorer
```
