#!/usr/bin/env python3

from typing import Union, List, Tuple, Dict, Any

""" Duck typing - first part """


class Shape:
    """ Shape class """
    def area(self):
        raise Exception("area() is not implemented")

    def perimeter(self):
        raise Exception("perimeter() is not implemented")


class Circle(Shape):
    """ Circle class """
    def __init__(self, radius: Union[int, float]):
        self.__radius = radius

    def area(self):
        """ Area of a circle """
        return 3.14159265359 * (self.__radius ** 2)

    def perimeter(self):
        """ Perimeter of a circle """
        return 2 * 3.14159265359 * self.__radius

    def __str__(self):
        """ String representation of a circle """
        return "[Circle] {}/{}".format(self.__radius, self.__radius)


class Square(Shape):
    """ Square class """
    def __init__(self, size: Union[int, float]):
        self.__size = size

    def area(self):
        """ Area of a square """
        return self.__size ** 2

    def perimeter(self):
        """ Perimeter of a square """
        return 4 * self.__size

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)


class shape_info:
    """ Shape info class """
    def __init__(self, shape: Shape):
        print(shape)
        print("Area:", shape.area())
        print("Perimeter:", shape.perimeter())


class Rectangle(Shape):
    """ Rectangle class """
    def __init__(self, width: Union[int, float], height: Union[int, float]):
        self.__width = width
        self.__height = height

    def area(self):
        """ Area of a rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ Perimeter of a rectangle """
        return 2 * (self.__width + self.__height)

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
