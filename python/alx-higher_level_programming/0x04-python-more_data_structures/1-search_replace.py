#!/usr/bin/python3
"""
function that replaces all occurrences
of an element by another in a new list.
"""


def search_replace(my_list, search, replace):
    """
    function that replaces all occurrences
    of an element by another in a new list.
    """
    new_list = my_list[:]
    # new_list = my_list.copy()
    for value in new_list:
        if search == value:
            value = replace
            print(value)

