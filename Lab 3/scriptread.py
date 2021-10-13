import json
import os


with open("script.json") as f:
  _script=json.load(f)
  
line=_script["Romeo"][1]

os.system("flite -voice slt -v "+line)
