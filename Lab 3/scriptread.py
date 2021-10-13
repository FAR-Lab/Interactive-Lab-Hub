import json
import os

with open("script.json") as f:
  _script=json.load(f)

while True:
  num=int(input("Line: "))
  line=_script["Romeo"][num]
  os.system("flite -voice slt -v "+line)
