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
    for index in range(len(new_list)):
        if new_list[index] == search:
            new_list[index] = replace
    # return new_list
    # if search in new_list:
    #    search = replace
    return new_list
