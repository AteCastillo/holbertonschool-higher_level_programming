#!/usr/bin/python3
"""
a function that prints a square
with the character #

"""


def print_square(size):
    """
    size is the size length of the square and must be an interger
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size is float and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
