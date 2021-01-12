#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """what are these for? who knows"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
    """getter width"""
        return self.__width

    @width.setter
    def width(self, value):
    """ setter width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
    """getter height"""
        return self.__height

    @height.setter
    def height(self, value):
    """ setter height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
    """return the rectangle's area"""
        return self.__width * self.__height

    def perimeter(self):
    """return the rectangle's perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)
