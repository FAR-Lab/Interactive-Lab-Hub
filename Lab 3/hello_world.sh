# Testing out speech synthesis
espeak -ven+f2 -k5 -s150 --stdout "Hello world! I am now speaking in full sentences" | aplay