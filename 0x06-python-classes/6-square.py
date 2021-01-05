#!/usr/bin/python3
"""defining a new class"""


class Square:
    """New Class"""
    def __init__(self, size=0, position=(0, 0)):
        """Function to instantiation with size"""
        self.__size = size
        self.__position = position  
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Returns the area of a square"""
        return self.__size ** 2

    @property
    def size(self):
        """to retrieve size"""
        return self.__size

    @size.setter
    def size(self, value):
        """to change size"""
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        """to retrieve position"""
        return self.__position

    @position.setter
    def position(self, value):
        if len(self.__position) != 2 or value < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """to print the square"""
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                for i in range(self.__size):
                    print("#", end="")
                print("")
