#!/usr/bin/python3
"""
Module for the Base class.
"""
class Base:
    """
    Base class for managing id attribute.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor for Base class.

        Args:
            id (int): Optional id to be assigned. If None, increments __nb_objects.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
