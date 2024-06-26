#!/usr/bin/python3
"""
This module defines a Square class that inherits from Rectangle.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square shape class, super class is BaseGeometry, then Rectangle
    """
    def __init__(self, size):
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size
