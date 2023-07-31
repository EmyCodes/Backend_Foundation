#!/usr/bin/python3
"""function that prints the last digit of a number."""


def print_last_digit(number):
    """function that prints the last digit of a number."""
    # Make number absolute
    number = abs(number)
    if (number % (3*5)) = 0:
        number = number % (3*5)
    elif number % 3 == 0:
        number = number % 3
    elif number % 5 == 0:
        number = number % 5
    else:
        continue
    return number
