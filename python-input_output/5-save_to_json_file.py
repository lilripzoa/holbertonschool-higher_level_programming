#!/usr/bin/python3
import json


def save_to_json_file(my_obj, filename):
    """Save Object to a file
    Args:
        my_obj: The object to be saved.
        filename: The name of the file to save the object to.
    returns:
        None
    """
    with open(filename, 'w', encoding="utf-8") as fic:
        json.dump(my_obj, fic)
