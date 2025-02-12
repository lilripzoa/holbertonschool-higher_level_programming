#!/usr/bin/pyhton3
import json
"""Save Object to a file"""


def save_to_json_file(my_obj, filename):
    """Save Object to a file
    Args:
        my_obj: The object to be saved.
        filename: The name of the file to save the object to.
    returns:
        None
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
