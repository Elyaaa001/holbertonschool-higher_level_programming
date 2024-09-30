#!/usr/bin/python3
"""Module that reads a file and prints its content."""

def read_file(filename=""):
    """Function that reads a UTF-8 text file and prints its content."""
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        print(content, end="")
