#!/usr/bin/python3

"""
    this module provides a function `matrix_divided`
    to divide all elements of a matrix.

    the function has two parameters, `matrix` and `div`,
    and returns a new matrix with all elements divided by div.
    If matrix is not a list of lists of integers or floats,
    a `TypeError` will be raised.
    If matrix contains rows of different sizes, a `TypeError` will be raised.
    If div is not an integer or float, a `TypeError` will be raised.
    If div is 0, a `ZeroDivisionError` will be raised.

    exemple:
    >>> matrix = [
    ...     [1, 2, 3],
    ...     [4, 5, 6]
    ... ]
    >>> print(matrix_divided(matrix, 3))
    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
    >>> print(matrix)
    [[1, 2, 3], [4, 5, 6]]

    try:
    ...     print(matrix_divided(matrix, 0))
    ... except Exception as e:
    ...     print(e)
    division by zero

    trace:
    >>> matrix_divided(1, 2)
    Traceback (most recent call last):
        ...
    TypeError: matrix must be a matrix (list of lists) of integers/floats
    >>> matrix_divided([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2)
    Traceback (most recent call last):
        ...
    TypeError: Each row of the matrix must have the same size
    >>> matrix_divided([[1, 2, 3], [4, 5, 6]], 'a')
    Traceback (most recent call last):
        ...
    TypeError: div must be a number
    >>> matrix_divided([[1, 2, 3], [4, 5, 6]], 0)
    Traceback (most recent call last):
        ...
    ZeroDivisionError: division by zero
"""


def matrix_divided(matrix, div):
    """
    Function that divides all elements of a matrix.
    Args:
        matrix: list of lists of integers or floats
        div: integer or float
    Returns:
        A new matrix with all elements divided by div
    Raises:
        TypeError: If matrix is not a list of lists of integers or floats
        TypeError: If matrix contains rows of different sizes
        TypeError: If div is not an integer or float
        ZeroDivisionError: If div is 0
    """

    errorMessage = "matrix must be a matrix (list of lists) of integers/floats"
    if not matrix:
        raise TypeError(errorMessage)
    if not isinstance(matrix, list):
        raise TypeError(errorMessage)
    for lists in matrix:
        if not isinstance(lists, list):
            raise TypeError(errorMessage)
        for item in lists:
            if not isinstance(item, int) and not isinstance(item, float):
                raise TypeError(errorMessage)
    for lists in matrix:
        if len(lists) == 0:
            raise TypeError(errorMessage)
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if not all(len(lists) == len(matrix[0]) for lists in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(item / div, 2) for item in lists] for lists in matrix]
