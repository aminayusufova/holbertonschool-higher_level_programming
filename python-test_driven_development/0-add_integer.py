#!/usr/bin/python3
"""
This is a module-level docstring.
"""
def add_integer(a, b=98):
     """
    Adds two integers and returns the result.
    
    Args:
        a (int or float): The first number.
        b (int or float): The second number, defaults to 98.
    
    Returns:
        int: The sum of the two numbers, with floats cast to integers before addition.
    
    Raises:
        TypeError: If either of a or b are not integers or floats.
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return (a + b)
