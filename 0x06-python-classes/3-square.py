#!/usr/bin/python3
"""defining a new class"""


class Square:
    """New Class"""
    def __init__(self, size=0):
        """Function to instantiation with size"""
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Returns the area of a square"""
        return self.__size ** 2
