#!/usr/bin/python3

"""Append a string to a file"""


def append_write(filename="", text=""):
    """Append a string to a file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
