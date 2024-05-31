#!/usr/bin/python3
"""
This module contains the lookup function that returns
a list of an object's attributes and methods.
"""


def lookup(obj):
    """returns all objects in an objects dictionary
        -> as a list
    """
    return dir(obj)
