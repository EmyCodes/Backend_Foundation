#!/usr/bin/python3
import json

#json string
jsonStr = '{"rollno":25, "name":"Raghu", "mark": {"science":87, "math":34}}'

#parse/load json string into json object
jsonObj = json.loads(jsonStr)

#access inner nodes
x = jsonObj["mark"]["science"]
print(x)

