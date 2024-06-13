#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix: List[List[int]]) -> None:
    """
    Rotate 2D Matrix

    Args:
        matrix (List[List[int]]): The 2D matrix to be rotated.

    Returns:
        None
    """

    matrix.reverse()
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
