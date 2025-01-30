#!/usr/bin/python3

"""A class square that defines a square"""


class Square:
    """Class square"""

    def __init__(self, size=0):
        """Initialization"""
        self.size = size

    @property
    def size(self):
        """Getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size with validation"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate area of the square"""
        return self.__size ** 2
