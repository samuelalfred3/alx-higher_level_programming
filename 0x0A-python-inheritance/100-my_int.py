#!/usr/bin/python3
"""
Module for MyInt class.
"""


class MyInt(int):
    """
    A class representing a rebel integer.

    MyInt has == and != operators inverted.

    Methods:
    - __eq__(self, other): Overrides the == operator.
    - __ne__(self, other): Overrides the != operator.
    """

    def __eq__(self, other):
        """Overrides the == operator."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Overrides the != operator."""
        return super().__eq__(other)


if __name__ == "__main__":
    my_i = MyInt(3)
    print(my_i)
    print(my_i == 3)
    print(my_i != 3)
