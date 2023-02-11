#!/usr/bin/python3
import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
y = re.findall("Portugal", txt)
print(x)
print(y)

