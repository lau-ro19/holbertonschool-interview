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

    # Masques pour les bits de poids fort
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for num in data:
        # On ne garde que les 8 bits de poids faible
        byte = num & 0xFF

        if n_bytes == 0:
            # Compter le nombre de bits à 1 au début de l'octet
            mask = 1 << 7
            while (byte & mask):
                n_bytes += 1
                mask >>= 1

            # 1 octet (ASCII normal) -> n_bytes == 0
            if n_bytes == 0:
                continue

            # Un caractère UTF-8 valide fait entre 2 et 4 octets.
            # S'il commence par 1 seul bit à 1 (10xxxxxx) ou plus de 4 bits à 1, c'est invalide.
            if n_bytes == 1 or n_bytes > 4:
                return False

            n_bytes -= 1
        else:
            # Pour les octets de continuation, ils doivent commencer par '10' (mask1 actif, mask2 inactif)
            if not (byte & mask1 and not (byte & mask2)):
                return False
            n_bytes -= 1

    return n_bytes == 0
