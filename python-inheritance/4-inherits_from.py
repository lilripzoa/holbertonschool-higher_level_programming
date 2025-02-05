#!/usr/bin/python3

"""Module that return true if
object is an instance of,
or if the object is an instance"""


def inherits_from(obj, a_class):
    """Function that return true if
    object is an instance of,
    or if the object is an instance"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
