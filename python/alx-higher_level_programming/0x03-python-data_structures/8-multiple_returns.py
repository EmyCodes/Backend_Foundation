#!/usr/bin/python3
"""
function that returns a tuple with the length of a string and its first character.
"""


def multiple_returns(sentence):
    """"function that returns a tuple with the length
    of a string and its first character. """
    if len(sentence) == 0:
        return None
    else:
        return len(sentence), sentence[0]
