#!/usr/bin/python3
"""function that prints all integers of a list, in reverse order"""


def print_reversed_list_integer(my_list=[]):
    """
    function that prints all integers of a list, in reverse order.
    """
    for i in range(len(my_list) - 1, -1, -1):
        print("{:d}".format(my_list[i]))
    # Or
    # my_list.reverse()
    # for i in my_list:
    #    print("{:d}".format(i))
