#!/usr/bin/python3
"""Module to calculate the fewest operations
needed to result in n characters.
"""


def minOperations(n):
    """Calculate the fewest number of operations
    to reach exactly n 'H' characters.

    Args:
        n (int): The target number of characters.

    Returns:
        int: The minimum number of operations, or 0 if impossible.
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
