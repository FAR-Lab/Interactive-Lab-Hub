#arecord -f cd -r 16000 -d 5 -t wav recorded.wav && sox recorded.wav recorded_mono.wav remix 1,2

espeak -ven+f2 -k5 -s150 --stdout  "What is your adress and zip code?" | aplay
arecord -D hw:2,0 -f cd -c1 -r 16000 -d 5 -t wav recorded_mono.wav
