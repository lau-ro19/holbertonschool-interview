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
            if (byte & mask1) == 0:
                continue
            elif (byte & (mask1 | mask2 | (1 << 5))) == (mask1 | mask2 | (1 << 5)):
                n_bytes = 3
            elif (byte & (mask1 | mask2 | (1 << 5))) == (mask1 | mask2):
                n_bytes = 2
            elif (byte & (mask1 | mask2)) == mask1:
                n_bytes = 1
            else:
                return False
        else:
            if not (byte & mask1 and not (byte & mask2)):
                return False
            n_bytes -= 1

    return n_bytes == 0
