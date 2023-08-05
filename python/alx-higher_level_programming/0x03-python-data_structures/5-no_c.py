#!/usr/bin/python3
"""
function that removes all characters c and C from a string.
"""


def no_c(my_string):
    """
    function that removes all characters c and C from a string.
    """
    if ("C" in my_string) or ("c" in my_string):
        my_string.strip("C").strip("c")
        return my_string
    else:
        return my_string
