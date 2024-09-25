#!/usr/bin/python3
"""checks object for instance"""

def is_kind_of_class(obj, a_class):
    """body"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
