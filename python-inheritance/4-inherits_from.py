#!/usr/bin/python3
"""
This module contains the function is_same_class.
"""


def inherits_from(obj, a_class):
    """checks if an object inherited from a class
    """
    if not isinstance(a_class, type):
        raise TypeError("a_class must be of type 'type'")
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
