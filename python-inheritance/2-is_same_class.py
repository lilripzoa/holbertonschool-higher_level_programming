#!/usr/bin/python3

"""Module that return true if
object is exactly an instance of the specified class"""


def is_same_class(obj, a_class):
    """Function that return true if
    object is exactly an instance of the specified class"""
    return type(obj) is a_class
