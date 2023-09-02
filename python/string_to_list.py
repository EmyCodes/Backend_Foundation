#!/usr/bin/python3
"""
This script converts string to list whose elements are in lowercase
"""

from sys import argv, exit

if len(argv) == 3:
    string = argv[2]
    string = string.lower()
    new_string = []
    for char in string:
        new_string.append(char)
    print(new_string)
elif len(argv) == 2:
    string = argv[1]
    string = string.lower()
    new_string = []
    for char in string:
        new_string.append(char)
    print(new_string)
else:
    exit(1)
