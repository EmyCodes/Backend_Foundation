#!/usr/bin/python3
"""
Program imports all functions from the file
calculator_1.py and handles basic operations.
"""


if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, div, mul

    operators = ['+', '-', '*', '/']

    if len(argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
    else:
        if argv[2] not in operators:
            print("Unknown operator. \
Available operators: +, -, * and /")

        a = int(argv[1])
        b = int(argv[3])

        if argv[2] == '+':
            print("{} + {} = {}".format(a, b, add(a, b)))
        elif argv[2] == '-':
            print("{} - {} = {}".format(a, b, sub(a, b)))
        elif argv[2] == '/':
            print("{} / {} = {}".format(a, b, div(a, b)))
        elif argv[2] == '*':
            print("{} * {} = {}".format(a, b, mul(a, b)))
        else:
            pass
