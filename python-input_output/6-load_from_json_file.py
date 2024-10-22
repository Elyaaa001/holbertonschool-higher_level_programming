#!/usr/bin/python3
"""module documentation"""

import json


def load_from_json_file(filename):
   
    
    with open(filename, 'r') as file:
        return json.load(file)
