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
    if not isinstance(matrix, list) or len(matrix) == 0 or not matrix[0]:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")

    for row in matrix:
        if len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        for x in row:
            if type(x) is not int and type(x) is not float:
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")

    len_rows = []
    for row in matrix:
        len_rows.append(len(row))
    if not all(elem == len_rows[0] for elem in len_rows):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(x / div, 2) for x in row] for row in matrix]

    return new_matrix
