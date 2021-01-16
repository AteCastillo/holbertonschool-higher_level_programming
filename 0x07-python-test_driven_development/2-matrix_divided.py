#!/usr/bin/python3
"""
A function that divides a matrix
to an int
"""


def matrix_divided(matrix, div):
    """
    matrix must be int or float
    """
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix \
        (list of lists) of integers/floats")
    if type(matrix) is not int or type(matrix) is not float:
        raise TypeError("matrix must be a matrix \
        (list of lists) of integers/floats")
    if type(div) is not int or type(div) is not float:
        raise TypeError("div must a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    try:
        size = len(matrix[0])
    except:
        raise TypeError("matrix must be a matrix \
        (list of lists) of integers/floats")
    for row in matrix:
        if len(row) == size:
            size = len(row)
        else:
            raise TypeError("Each row of the matrix must have the same size")

    new_matrix = []
    for row in matrix:
        newrow = []
    for value in row:
        new_row.append(round(value/div),2)
    new.append(newrow)

    return new_matrix
