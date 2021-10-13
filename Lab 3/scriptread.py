import json
import os

with open("script.json") as f:
  _script=json.load(f)
  
os.system("flite -voice slt -v 'Which part will you play?'")
comp_part=input("Device's part: ")

while True:
  num=int(input("Line: "))
  line=_script[comp_part][num]
  os.system("flite -voice slt -v "+line)
