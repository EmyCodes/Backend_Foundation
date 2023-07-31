#!/usr/bin/python3
"""program that prints the ASCII alphabet,
in reverse order, alternating lowercase and uppercase 
(z in lowercase and Y in uppercase) ,
not followed by a new line."""


def reverse_ascii_alpha():
    """Function Reverses ASCII alphabets
    except 'z' and 'Y' in uppercase and lowercase respectively"""
    start = 'A'
    for i in range(97, 122):
        if (ord(start) >= 65) and (ord(start) <= 90):
            print(chr(i), end="")
    #        if (ord(start) >= 95) and (ord(start) <= 122):
    #            reverse_ = (chr(i))
    # return reverse_

reverse_ascii_alpha()
