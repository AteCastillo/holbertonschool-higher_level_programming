#!/usr/bin/python3
"""
Rectangle class
"""


class Rectangle:
    """what are these for? who knows"""
    number_of_instances = 0
    print_symbol = '#'

    @classmethod
    def square(cls, size=0):
        """return a new instance with width = height = size"""
        width = size
        height = size
        return cls(width, height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """static method"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    def __init__(self, width=0, height=0):
        """Initializes the rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """ delete my balls """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """getter for the private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the private instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for the private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the private instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
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

    def __str__(self):
        """print rectangle"""
        my_rectangle = ""
        if self.__width == 0 or self.__height == 0:
            return my_rectangle
        for s in range(self.__height):
            my_rectangle += str(self.print_symbol)
            for t in range(self.__width - 1):
                my_rectangle += str(self.print_symbol)
            if s < self.__height - 1:
                my_rectangle += "\n"
        return my_rectangle

    def __repr__(self):
        """returns a string representation of the rectangle for reproduction"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
