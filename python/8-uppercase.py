#!/usr/bin/python3
"""function that prints a string in uppercase
followed by a new line"""


def uppercase(str):
    """function that prints a string in uppercase
    followed by a new line."""
    for i in str:
        # if (ord(i) >= 97) and (ord(i) <= 122):
        if (i >= 'a') and (i <= 'z'):
            ascii_diff = 97 - 65
            converted_i = ord(i) - ascii_diff
            print(converted_i)
            convert_back = chr(converted_i)
            # print(convert_back, end="")
    print()
