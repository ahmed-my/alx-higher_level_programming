#!/usr/bin/python3
"""MyList class that inherits list class"""


class MyList(list):
    """public instance method that prints in sorted order."""

    def print_sorted(self):
        """Print the list in sorted ascending order."""
        print(sorted(self))
