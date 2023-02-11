#!/usr/bin/python3
import json

#json string
jsonStr = '{"rollno":25, "name": "Raghu", "class":7,"section":"B"}'

#parse/load jsons string into object
jsonObj = json.loads(jsonStr)

#access
print(jsonObj["rollno"])
print(jsonObj["name"])
print(jsonObj["class"])
print(jsonObj["section"])

