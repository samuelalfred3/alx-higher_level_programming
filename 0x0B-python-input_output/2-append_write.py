#!/usr/bin/python3
"""
This is the "2-append_write" module.
The 2-append_write module supplies one function, append_write().
"""

def append_write(filename="", text=""):
    """
    Append a string at the end of a text file (UTF8) and return the number of characters added.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
