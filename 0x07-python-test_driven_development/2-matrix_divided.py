#!/usr/bin/python3
"""
A function that divides a matrix
to an int
"""


def matrix_divided(matrix, div):
    """
    matrix must be int or float
    """
    if type(matrix) is not int or type(matrix) is not float:
        raise TypeError("matrix must be a matrix \
        (list of lists) of integers/floats")
    for in in matrix:
