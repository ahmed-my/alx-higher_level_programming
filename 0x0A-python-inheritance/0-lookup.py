#!/usr/bin/python3
"""Defines an object attribute lookup function."""


def lookup(obj):
    """Return the list of available attributes and method."""
    return (dir(obj))
