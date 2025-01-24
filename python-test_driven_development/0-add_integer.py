#!/usr/bin/python3

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
"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
