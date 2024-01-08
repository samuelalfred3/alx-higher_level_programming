#!/usr/bin/python3
"""
Module for BaseGeometry class.
"""


class BaseGeometry:
    """
    A class representing base geometry.

    Public instance method:
    - def area(self): Raises an Exception with the message "area() is not implemented".
    """

    def area(self):
        """Raises an Exception with the message "area() is not implemented"."""
        raise Exception("area() is not implemented")


if __name__ == "__main__":
    bg = BaseGeometry()

    try:
        print(bg.area())
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
