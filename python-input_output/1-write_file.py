#!/usr/bin/python3

"""Write a string to a file and return
the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Write a string to a file and return
    the number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
