#!/usr/bin/python3
"""Add all arguments to a Python list,
and then save them to a file"""
import sys


def add_item():
    """Add all arguments to a Python list,
    and then save them to a file"""
    try:
        my_list = load_from_json_file("add_item.json")
    except:
        my_list = []
    for i in range(1, len(sys.argv)):
        my_list.append(sys.argv[i])
    save_to_json_file(my_list, "add_item.json")
