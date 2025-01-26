#!/usr/bin/python3

"""
     Write a function that divides all elements of a matrix.

    Prototype: def matrix_divided(matrix, div):
    matrix must be a list of lists of integers or floats,
    otherwise raise a TypeError exception with the message
    matrix must be a matrix (list of lists)
    of integers/floats

    Each row of the matrix must be of the same size,
    otherwise raise a TypeError exception
    with the message Each row of the matrix must have
    the same size

    div must be a number (integer or float),
    otherwise raise a TypeError exception
    with the message div must be a number

    div can’t be equal to 0, otherwise raise a
    ZeroDivisionError exception
    with the message division by zero

    All elements of the matrix should be divided by div,
    rounded to 2 decimal places
    Returns a new matrix
    You are not allowed to import any module
"""


def matrix_divided(matrix, div):
    """
    Function that divides all elements of a matrix
    """
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError
    ("matrix must be a matrix (list of lists) of integers/floats")
    if not all(type(row) is list for row in matrix):
        raise TypeError
    ("matrix must be a matrix (list of lists) of integers/floats")
    if not all(type(num) in [int, float] for row in matrix for num in row):
        raise TypeError
    ("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError
    ("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(num / div, 2) for num in row] for row in matrix]
