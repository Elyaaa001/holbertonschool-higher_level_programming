#!/usr/bin/python3
"""checks object"""


def inherits_from(obj, a_class):
    """body"""
    return isinstance(obj, a_class) and type(obj) is not a_class
