#!/usr/bin/python3
"""
This module defines a base class for geometric shapes.
"""


class BaseGeometry:
    """ BaseGeometry class empty """

    def area(self):
        """ raise an exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates value is an integer """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
