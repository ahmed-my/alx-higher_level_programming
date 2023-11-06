#!/usr/bin/python3
"""Define MyList class that inherits from list class"""


class MyList(list):
    """public instance method that prints in sorted order."""

    def print_sorted(self):
        """Print the list in sorted ascending order."""
        print(sorted(self))
