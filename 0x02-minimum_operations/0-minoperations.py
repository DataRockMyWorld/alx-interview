#!/usr/bin/python3
"""
Minimum Operations Challenge
"""


def minOperations(n: int) -> int:
    """
    Returns the minimum number of operations
    needed to reach n
    """
    if n <= 1:
        return 0
    operations = 0
    current_length = n
    # Start from the largest factor and work down to 2
    for i in range(2, n + 1):
        while current_length % i == 0:
            # Find the smallest operation to reach to `current_length`
            operations += i
            current_length //= i
    return operations
