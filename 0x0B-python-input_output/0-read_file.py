#!/usr/bin/python3
"""
Module for reading a file
"""


def read_file(filename=""):
    """
    Function that reads a text file (UTF8) and prints it to stdout
    Args:
        filename (str): the file name to read
    """
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end="")
