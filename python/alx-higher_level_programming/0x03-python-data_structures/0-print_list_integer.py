#!/usr/bin/python3
"""Function prints all integers of a list"""


def print_list_integer(my_list=[]):
    """Function prints all integers of a list"""
    for i in my_list:
        print("{:d}".format(i))
    # or

    for i in range(0, len(my_list):
        print("{:d}".format(my_list[i]))
