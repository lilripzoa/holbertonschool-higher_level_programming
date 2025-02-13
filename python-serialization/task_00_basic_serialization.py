#!/usr/bin/env python3
""" Basic serialization task 0
"""

import json


def serialize_and_save_to_file(data, filename):
    """ Serializes data to a file
    data: data to serialize
    filename: file to save data
    """
    with open(filename, 'w') as f:
        f.write(data)

def load_and_deserialize(filename):
    """ Deserializes data from a file
    filename: file to load data
    """
    with open(filename, 'r') as f:
        return json.load(f)