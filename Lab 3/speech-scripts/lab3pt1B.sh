#from: https://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)#Festival_Text_to_Speech

echo "Hello user! Can you please tell me how many pets you have?" | festival --tts 

python3 /home/gilbertoe.ruiz/Interactive-Lab-Hub/Lab\ 3/speech-scripts/test_microphone.py -m en -f /home/gilbertoe.ruiz/Interactive-Lab-Hub/Lab\ 3/speech-scripts/lab3pt1B.txt

python3 /home/gilbertoe.ruiz/Interactive-Lab-Hub/Lab\ 3/speech-scripts/format_partial.py
