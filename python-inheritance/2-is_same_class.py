#!/usr/bin/python3

"""Module that return true if
object is exactly an instance of the specified class"""


def is_same_class(obj, a_class):
    """Return true if object is exactly an instance of the specified class"""
    return type(obj) == a_class
