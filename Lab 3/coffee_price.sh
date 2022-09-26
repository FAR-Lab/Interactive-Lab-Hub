# Speak the question prompt
espeak -ven+f2 -k5 -s150 --stdout "How much was that coffee?" | aplay

# Record the response
arecord -D hw:2,0 -f cd -c1 -r 44100 -d 5 -t wav recorded_mono.wav

# Analyze using test_words.py
python3 test_words.py recorded_mono.wav
