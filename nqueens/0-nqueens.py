#!/usr/bin/python3
"""
Solution to the N queens puzzle using backtracking.
"""

import sys


def print_usage_and_exit():
    """Prints usage message and exits with status 1."""
    print("Usage: nqueens N")
    sys.exit(1)


def solve_nqueens():
    """Main logic to handle arguments and solve N queens problem."""
    if len(sys.argv) != 2:
        print_usage_and_exit()

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    def backtrack(row, queens):
        if row == n:
            solutions.append([[r, c] for r, c in enumerate(queens)])
            return
        for col in range(n):
            if all(
                col != c and
                abs(col - c) != row - r
                for r, c in enumerate(queens)
            ):
                queens.append(col)
                backtrack(row + 1, queens)
                queens.pop()

    solutions = []
    backtrack(0, [])

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    solve_nqueens()
