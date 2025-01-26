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
    """ Divide a matrix by a number div """
    list_error = "matrix must be a matrix (list of lists) of integers/floats"
    len_error = "Each row of the matrix must have the same size"
    div_int_error = "div must be a number"
    div_zero_error = "division by zero"
    new_matrix = []
    new_list = []
    if not matrix:
        raise TypeError(list_error)
    if type(div) is not int and type(div) is not float:
        raise TypeError(div_int_error)
    if div == 0:
        raise ZeroDivisionError(div_zero_error)
    longitud = len(matrix[0])
    for lista in matrix:
        if type(lista) is not list:
            raise TypeError(list_error)
        if len(lista) != longitud:
            raise TypeError(len_error)
        for item in lista:
            if type(item) is not int and type(item) is not float:
                raise TypeError(list_error)
            num = item / div
            new_list.append(round(num, 2))
        new_matrix.append(new_list)
        new_list = []
    return new_matrix
