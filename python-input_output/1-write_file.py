#!/usr/bin/python3
"""module"""


def write_file(filename="", text=""):
    """writes a string to a UTF-8 text file"""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
