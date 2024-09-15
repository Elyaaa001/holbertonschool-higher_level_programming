#!/usr/bin/python3


def add_integer(a, b=98):
 
    listo = [int, float]
    if type(a) not in listo:
        raise TypeError("a must be an integer")
    if type(b) not in listo:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
