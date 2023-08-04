#!/usr/bin/python3
"""
Program imports all functions from the file
calculator_1.py and handles basic operations.
"""


if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div

    operators = [+, -, *, /]
    if len(argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        break
    else:
        if argv[2] not in operator:
            print("Unknown operator. 
                    Available operators: +, -, * and /")
        else:
            a = int(len(argv[1]))
            b = int(len(argv[3]))

            if argv[2] == '+':
                print("{} + {} = {}".format(a, b, add(a, b)))
            elif argv[2] == '-':
                print("{} + {} = {}".format(a, b, sub(a, b)))
            elif argv[2] == '/':
                print("{} + {} = {}".format(a, b, div(a, b)))
            elif argv[2] == '*':
                print("{} + {} = {}".format(a, b, mul(a, b)))
