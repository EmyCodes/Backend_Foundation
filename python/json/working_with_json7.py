#!/usr/bin/python3
import json

jsonStr = '[{"rollno":1, "name":"Prasanth"}, {"rollno":2, "name":"Raghu"}]'

jsonObj = json.loads(jsonStr)

print(jsonObj[0])
print(jsonObj[1])

