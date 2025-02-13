#!/usr/bin/env python3
""" Basic serialization task 0
"""

import json


def serialize_and_save_to_file(data, filename):
    """ Serializes data to a file
    data: data to serialize
    filename: file to save data
    """
    with open(filename, 'w', encoding='utf-8') as fic:
        json.dump(data, fic)


def load_and_deserialize(filename):
    """ Deserializes data from a file
    filename: file to load data
    """
    with open(filename, 'r', encoding='utf-8') as fic:
        return json.load(fic)