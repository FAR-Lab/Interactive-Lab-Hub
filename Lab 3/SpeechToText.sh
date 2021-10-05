echo "Please tell me your bank account password" | festival --tts

arecord -D hw:2,0 -f cd -c1 -r 48000 -d 5 -t wav recorded_answer.wav
python3 test_numbers.py recorded_answer.wav
