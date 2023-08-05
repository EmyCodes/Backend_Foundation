#!/usr/bin/python3
"""function that finds the biggest integer of a list."""


def max_integer(my_list=[]):
    """function that finds the biggest integer of a list."""
    if len(my_list) == 0:
        return None
    else:
        new_list = my_list.sort()
        return new_list[-1]
