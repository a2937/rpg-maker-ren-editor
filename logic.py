import json
import re

def transform(jsonString):
  output = "" 
  if jsonString != "":
    jsonArray = json.loads(jsonString)
    output += "autoplayBgm" + ":" + str(jsonArray["autoplayBgm"]).lower() + "\n"
    output += "autoplayBgs" + ":" + str(jsonArray["autoplayBgs"]).lower() + "\n"
  return output.strip()

def restore(myString):
  normal = ""
  if myString.strip() == "":
    return '{}'; 
  dataPattern = re.compile(r'([\w]+)\s*:\s*([\w\d]+)')
  rows = myString.strip().split("\n")
  normal += "{"
  for i in range(rows.len):
    normal += '"' + dataPattern.match(rows[i])[0] + '":' + dataPattern.match(rows[i])[0]; 
  return normal