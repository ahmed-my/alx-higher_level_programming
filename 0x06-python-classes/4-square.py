#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """square module."""

    def __init__(self, size=0):
        """Initialize instance of square.
        Args:
            size (int): The size of the new square."""
        self.size = size

    @property
    def size(self):
        """Get/set the size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """ get the value of the sqaure """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        area = self.__size * self.__size
        return (area)
