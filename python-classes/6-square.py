#!/usr/bin/python3
"""
This module defines the Square class.
"""


class Square:
    """Square Class

    A Square Class

    """

    def __init__(self, size=0, position=(0, 0)):
        """__init__

        The __init__ method initializes the size and position of the square.

        Attributes:
            size (:obj:`int`, optional): The size of the square.
            position (:obj:`tuple`, optional): The position of the square.

        Raises:
            TypeError: If `size` type is not `int`.
            ValueError: If `size` is less than `0`.
            TypeError: If `position` is not a tuple of 2 positive integers.

        """

        if type(size) is not int:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        if not self.__check_tuple(position) or not self.__check_indexes(position) \
           or not self.__check_integers(position) or not self.__check_values(position):
            raise TypeError('position must be a tuple of 2 positive integers')

        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        """__init__

        The size setter method updates the size value of the square.

        Attributes:
            size (:obj:`int`): The new size of the square.

        Raises:
            TypeError: If `size` type is not `int`.
            ValueError: If `size` is less than `0`.

        """

        if type(size) is not int:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if not self.__check_tuple(position) or not self.__check_indexes(position) \
           or not self.__check_integers(position) or not self.__check_values(position):
            raise TypeError('position must be a tuple of 2 positive integers')

        self.__position = position

    def __check_tuple(self, position):
        return type(position) is tuple

    def __check_indexes(self, position):
        return len(position) == 2

    def __check_integers(self, position):
        return type(position[0]) is int and type(position[1]) is int

    def __check_values(self, position):
        return position[0] >= 0 and position[1] >= 0

    def area(self):
        """Returns the current square area

        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the # character

        """
        if self.__size == 0:
            print()
            return None

        if self.__position[1] > 0:
            for _ in range(self.__position[1]):
                print()

        for j in range(1, self.area() + 1):
            if j % self.__size == 1:
                print('{:>{w}}'.format('#', w=self.__position[0] + 1), end='')
            else:
                print('#', end='')

            if j % self.__size == 0 and j > 0:
                print()
