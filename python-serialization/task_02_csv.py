#!/usr/bin/python3
""" CSV module
"""
import csv
import json

python import csv import json


def convert_csv_to_json(csv_file):
    """ Convert CSV to JSON
    """
    with open(csv_file, mode='r') as file:
        csv_reader = csv.DictReader(file)
        data = [row for row in csv_reader]
    with open('data.json', mode='w') as file:
        json.dump(data, file)
    return data