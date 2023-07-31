#!/usr/bin/python3
"""function that prints the numbers from 1 to 100
separated by a space"""


def fizzbuzz():
    """function that prints the numbers from 1 to 100
    separated by a space"""
    for i in range(1, 101):
        """Looping through"""
        if i % (3 * 5) == 0:
            print("{}".format("FizzBuzz"), end=' ')
        elif i % 3 == 0:
            print("{}".format("Fizz"), end=' ')
        elif i % 5 == 0:
            print("{}".format("Buzz"), end=' ')
        else:
            print(i, end=' ')
