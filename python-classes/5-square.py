#!/usr/bin/python3
"""Module for creating a class that defines a square."""
class Square:
    """Represent a square."""

    def __init__(self, size=0):
        self.size = size

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
        return self.__size * self.__size

    def my_print(self):
        if self.size == 0:
            print()
        else:
            for _ in range(self.size):
                print('#' * self.size)
