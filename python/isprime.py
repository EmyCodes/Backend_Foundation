#!/usr/bin/env python3

def isprime(n: int) -> str:
    """This function detcts prime number"""
    if (n % n == 0) and (n % 2 != 1):
        return "{} is prime".format(n)
    else:
        return "{} is not prime".format(n)


if __name__ == "__main__":
    from sys import argv

    isprime(argv[1])
