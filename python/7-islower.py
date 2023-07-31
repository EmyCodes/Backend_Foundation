#!/usr/bin/python3
"""function that checks for lowercase character. """


def islower(c):
    """function that checks for lowercase character."""
    if (ord(c) >= 97) and (ord(c) <= 122):
    # if (c >= 'a') and (c <= 'z'):
        return True
    else:
        return False
