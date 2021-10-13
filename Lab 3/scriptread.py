import json
import subprocess


with open("script.json") as f:
  _script=json.load(f)
  
line=_script["Romeo"][0]

subprocess.run("flite -voice slt -v "+line)
