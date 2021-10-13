import json
import os


with open("script.json") as f:
  _script=json.load(f)
  
line=_script["Romeo"][0]

os.system("flite -voice slt -v 'here is a test of some words'")
