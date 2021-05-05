# experimentsSTT

Some notes about the relative performance of DeepSpeech 0.4.1 vs. Vosk 0.3.10


`$time python test_words.py record.wav` (where test_words has digits in library, and record.wav is 5 second file)

"text" : "one three four five six seven eight nine [unk] seven"

real	0m9.739s

user	0m9.762s

sys	0m0.309s

`time python test_simple.py record.wav` (where test_simple is open-ended recognitioni, and record.wav is 5 second file)

"text" : "when the four five six seven eight nine ten eleven"

real	0m19.454s

user	0m19.411s

sys	0m0.370s


`$ time ./deepspeech_demo.sh record.wav`

on hou three four five thicks eve an eight nine teny leven

Inference took 96.329s for 5.000s audio file.

real	1m37.270s

user	1m44.394s



sys	0m0.516s
