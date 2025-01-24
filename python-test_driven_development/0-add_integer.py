#!/usr/bin/python3

def add_integer(a, b=98):
"""
    Adds two integers (or floats).
    
    Parameters:
    a (int, float): The first number to add.
    b (int, float, optional): The second number to add. Defaults to 98.
    
    Returns:
    int: The sum of a and b, returned as an integer.
    
    Raises:
    TypeError: If a or b are not integers or floats.
    
    Example:
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
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
