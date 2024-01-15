#!/usr/bin/python3
"""
Module for the Square class.
"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """
    Square class, inherits from Rectangle.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor for Square class.

        Args:
            size (int): Size of the square.
            x (int): X-coordinate of the square's position.
            y (int): Y-coordinate of the square's position.
            id (int): Optional id to be assigned.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update the attributes of the Square.

        Args:
            *args: Variable number of arguments in the order (id, size, x, y).
            **kwargs: Variable number of keyword arguments.
        """
        if args:
            attributes = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
            str: Formatted string.
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
