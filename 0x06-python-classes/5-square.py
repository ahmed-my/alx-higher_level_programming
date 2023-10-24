#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """ square module."""

    def __init__(self, size):
        """Initialize instance of a square.
        Args:
            size (int): The size of square."""
        self.size = size

    @property
    def size(self):
        """Get/set the size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """ value set for the square class """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        area = self.__size * self.__size
        return (area)

    def my_print(self):
        """Print the # character."""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
