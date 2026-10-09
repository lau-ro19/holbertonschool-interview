#!/usr/bin/python3
"""
Module to validate if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    :param data: list of integers representing bytes
    :return: True if valid UTF-8, else False
    """
    n_bytes = 0

    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for num in data:
        byte = num & 0xFF

        if n_bytes == 0:
            mask = 1 << 7
            while (byte & mask):
                n_bytes += 1
                mask >>= 1

            if n_bytes == 0:
                continue

            if n_bytes == 1 or n_bytes > 4:
                return False

            n_bytes -= 1
        else:
            is_continuation = (
                (byte & mask1) and not (byte & mask2)
            )
            if not is_continuation:
                return False
            n_bytes -= 1

    return n_bytes == 0
