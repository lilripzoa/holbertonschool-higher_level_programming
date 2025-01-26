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
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    
    print(f"My name is {first_name} {last_name}")
    