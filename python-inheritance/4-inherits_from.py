#!/usr/bin/python3
"""checks object"""


def inherits_from(obj, a_class):
    """body"""
    if isinstance(obj, a_class) and type(obj) is a_class:
        return True
    else:
        return False
