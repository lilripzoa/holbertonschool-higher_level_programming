#!/usr/bin/python3

"""A square class that defines a square"""


class Square:
    """A class square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialization"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter pour position"""
        if not (isinstance(value, tuple) and len(value) == 2 and all(
          isinstance(x, int) and x >= 0 for x in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Print the square using '#' with the given position"""
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__position[1]):
                print(" ")  # Print vertical offset
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
