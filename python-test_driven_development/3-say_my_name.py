#!/usr/bin/python3
"""
    Write a function that prints My name is <first name> <last name>
    Prototype: def say_my_name(first_name, last_name="")
    first_name and last_name must be strings
    Return: nothing
"""

def say_my_name(first_name, last_name=""):
    """
    Function that prints a string with the first name and last name
    Args:
        first_name: string
        last_name: string
    Returns:
        nothing
    Raises:
        TypeError: If first_name or last_name is not a string
    """
    str_error = "first_name must be a string or last_name must be a string"
    if type(first_name) is not str or type(last_name) is not str:
        raise TypeError(str_error)
    print("My name is", first_name, last_name)
    