import json
import os

with open("script.json") as f:
  _script=json.load(f)
  
os.system("flite -voice slt -v 'Which part will you play?'")
comp_part=input("Device's part: ")

os.system("flite -voice slt -v 'Would you like to start or should I?'")
_start=int(input("Who starts? 0 for User, 1 for Device: "))
if _start==0: os.system("flite -voice slt -v 'Begin when you are ready'")
if _start==1: os.system("flite -voice slt -v 'Which line should I start with?'")

while True:
  num=int(input("Line: "))
  line=_script[comp_part][num]
  os.system("flite -voice slt -v "+line)
