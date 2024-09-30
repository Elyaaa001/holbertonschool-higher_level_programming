#!/usr/bin/python3
"""module that reads file"""
def read_file(filename=""):
"""func"""

with open("filename.txt", "r") as file:
    content = file.read()
