#!/usr/bin/python3
"""Function"""


if __name__ == "__main__":
    from add_0 import add

    def add(a, b):
        """Function"""
        a = 1
        b = 2
        print("{} + {} = {}".format(a, b, add(a, b)))
