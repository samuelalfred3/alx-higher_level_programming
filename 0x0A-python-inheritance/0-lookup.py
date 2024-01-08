#!/usr/bin/python3
"""
This module contains the function lookup.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        A list of the names of the available attributes and methods of `obj`.
    """
    return dir(obj)


class MyClass1(object):
    """
    An empty class for demonstration purposes.
    """
    pass


class MyClass2(object):
    """
    A class with one attribute and one method for demonstration purposes.
    """
    my_attr1 = 3

    def my_meth(self):
        """
        A method that does nothing.
        """
        pass


if __name__ == "__main__":
    print(lookup(MyClass1))
    print(lookup(MyClass2))
    print(lookup(int))
