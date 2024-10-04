#!/usr/bin/python3
"""module documentation"""

def load_from_json_file(filename):
    """function that creates a object from a json file"""
    import json
    with open(filename, 'r') as file:
        json_object = json.load(file)
        