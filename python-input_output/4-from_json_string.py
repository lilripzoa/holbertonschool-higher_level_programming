#!/usr/bin/python3
"""From JSON string to Object"""
import json


def from_json_string(my_str):
    """From JSON string to Object
    Args:
        my_str: The JSON string to convert to object.
    Returns:
        object: The Python object represented by the JSON string.
    """
    return json.loads(my_str)
