#!/usr/bin/python3
"""
eturns a list of lists of integers
representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """
    eturns a list of lists of integers
    representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []
    res = []
    temp = []
    for x in range(n):
        row = []
        for y in range(x + 1):
            if x == 0 or y == 0 or x == y:
                row.append(1)
            else:
                row.append(temp[y] + temp[y - 1])
        temp = row
        res.append(row)
    return res
