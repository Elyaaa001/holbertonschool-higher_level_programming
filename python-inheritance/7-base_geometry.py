#!/usr/bin/python3
"""create a class"""


class BaseGeometry:
    """new classs"""
    def area(self):
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """"fuvction"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
