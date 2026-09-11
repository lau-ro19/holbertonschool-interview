#!/usr/bin/python3
"""Module for pascal_triangle method."""


def pascal_triangle(n):
    """Return a list of lists of integers representing Pascal's triangle."""
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]
        row = [1]

        for j in range(len(prev_row) - 1):
            row.append(prev_row[j] + prev_row[j + 1])

        row.append(1)
        triangle.append(row)

    return triangle
