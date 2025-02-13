#!/usr/bin/python3
"""
Loads an object from a text file containing JSON data.
"""


import sys
import os.path
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

args = sys.argv[1:]

filename = "add_item.json"

try:
    my_list = load_from_json_file(filename)

except FileNotFoundError:
    my_list = []

my_list.extend(args)
save_to_json_file(my_list, filename)