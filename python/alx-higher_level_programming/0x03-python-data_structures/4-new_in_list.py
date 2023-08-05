#!/usr/bin/python3
"""
function that replaces an element in a list at a
specific position without modifying the original list (like in C).
"""


def new_in_list(my_list, idx, element):
    """function that replaces an element in a list at a
    specific position without modifying the original list (like in C)
    """
    if (idx < 0) or (idx >= len(my_list)):
        return my_list
    else:
        new_list = my_list[:]
        # or
        # new_list = my_list.copy()
        new_list[idx] = element
        return new_list
