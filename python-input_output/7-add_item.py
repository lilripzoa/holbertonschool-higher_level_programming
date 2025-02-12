#!/usr/bin/python3
"""Add all arguments to a Python list,
and then save them to a file"""
import sys


def add_item():
    """Add all arguments to a Python list,
    and then save them to a file"""
    with open(filename, 'r', encoding="utf-8") as fic:
        return json.load(fic)
