#!/usr/bin/python3
import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position: ", x.start())

