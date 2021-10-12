import json


with open(script.json) as f:
  _script=json.load(f)
  
line=_script["Romeo"][0]

return line
