#!/usr/bin/python3
"""function that prints the last digit of a number."""


def print_last_digit(number):
    """function that prints the last digit of a number."""
    # Make number absolute
    number = abs(number) % 10
    print(number, end="")
    return number
