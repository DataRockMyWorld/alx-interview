#!/usr/bin/python3

"""
This program develops a function that returns a list of lists of
integers representing
Returns an empty list if n <= 0
You can assume n will be always an integer
"""


def pascal_triangle(n):
    """Pascals triangle algorithm"""
    if n <= 0:
        return []
    elif n == 1:
        return [[1]]
    elif n == 2:
        return [[1], [1, 1]]
    else:
        triangle = [[1], [1, 1]]
        for i in range(2, n):
            row = [1]
            for j in range(1, i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            row.append(1)
            triangle.append(row)
        return triangle
