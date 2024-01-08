#!/usr/bin/python3
"""
Module for Square class.
"""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """
    A class representing a square.

    Attributes:
    - __size (int): The size of the square.
    """

    def __init__(self, size):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Returns a string representation of the square."""
        return "[Square] {}/{}".format(self.__size, self.__size)


if __name__ == "__main__":
    s = Square(13)

    print(s)
    print(s.area())
