#!/usr/bin/python3
"""
Module for inherits_from function.
"""


def inherits_from(obj, a_class):
    """
    Check if obj is an instance of a class that inherited (directly or indirectly)
    from the specified class.

    Args:
        obj (object): The object to check.
        a_class (class): The class to compare with.

    Returns:
        bool: True if obj is an instance of a class that inherited from a_class;
              False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class


if __name__ == "__main__":
    a = True

    if inherits_from(a, int):
        print("{} inherited from class {}".format(a, int.__name__))
    if inherits_from(a, bool):
        print("{} inherited from class {}".format(a, bool.__name__))
    if inherits_from(a, object):
        print("{} inherited from class {}".format(a, object.__name__))
