#!/usr/bin/python3

"""
This module provides a function `add_integer` to add two integers or floats.

The function has two parameters, `a` and `b`,
and returns their sum as an integer.
If either `a` or `b` is not an integer or float, a `TypeError` will be raised.

Examples:
>>> add_integer(1, 2)
3
>>> add_integer(100, -2)
98
>>> add_integer(2)
100
>>> add_integer(100.3, -2)
98
>>> add_integer(4, "School")
Traceback (most recent call last):
    ...
TypeError: b must be an integer
"""


def add_integer(a, b=98):

    """
    Add two integers
    parameters: a, b (integers) or (floats)
    a is the first number to add
    b is the second number to add, his default value is 98
    return: the sum of a and b.
    errors: if a or b is not an integer or a float, raise a TypeError.

    test:
    >>> add_integer(1, 2)
    3
    >>> add_integer(100, -2)
    98
    >>> add_integer(2)
    100
    >>> add_integer(100.3, -2)
    98
    >>> add_integer(4, "School")
    traceback (most recent call last):
        ...
    TypeError: b must be an integer
        >>> add_integer(float('nan'), 2)
    Traceback (most recent call last):
        ...
    TypeError: a or b must be a valid number
    >>> add_integer(2, float('nan'))
    Traceback (most recent call last):
        ...
    TypeError: a or b must be a valid number
    """
    
    if type(a) not in [int, float] or a != a:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float] or b != b:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
