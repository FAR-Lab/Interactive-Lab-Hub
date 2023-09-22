#https://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)
#from: https://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)#Festival_Text_to_Speech


#!/bin/bash
# say() { local IFS=+;/usr/bin/mplayer -ao alsa -really-quiet -noconsolecontrols "http://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&q=$*&tl=en"; }
# say $*
# say "Please tell me your zip code"
# echo  "Please tell me your zip code"
echo "Please tell me your phone number" | festival --tts
python inquiry.py -m en