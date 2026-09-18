#!/usr/bin/python3
"""Module to solve the lockboxes puzzle using graph traversal (DFS/BFS)."""


def canUnlockAll(boxes):
    """Determine if all the boxes can be opened.

    Args:
        boxes (list of list of int): A list where each index represents a box
        containing keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes:
        return False

    n = len(boxes)
    unlocked = set([0])
    stack = [0]

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if 0 <= key < n and key not in unlocked:
                unlocked.add(key)
                stack.append(key)

    return len(unlocked) == n
