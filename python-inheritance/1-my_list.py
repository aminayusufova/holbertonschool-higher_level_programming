#!/usr/bin/python3
"""
This module defines an extended version
of the list class called MyList.
MyList includes an additional method to
print the list in ascending order.
"""


class MyList(list):
    """
    An extended version of the list class with an additional method.
    """
    def print_sorted(self):
        """
        Prints the list in ascending order.
        """
        copy = self[:]
        copy.sort()
        print(copy)
