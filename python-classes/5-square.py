#!/usr/bin/python3

"""This module defines a class Square."""


class Square:
    """
    An class that defines a square.
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)
    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for i in range(0, self.__size):
                print("#" * self.__size)
