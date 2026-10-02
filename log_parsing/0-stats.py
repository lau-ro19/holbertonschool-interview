#!/usr/bin/python3
"""
Log parsing module that reads stdin line by line and computes metrics:
- Total file size
- Number of status code occurrences
Prints statistics every 10 lines, upon keyboard interruption, and at the end.
"""

import sys

# Initialisation des variables globales pour les métriques
total_file_size = 0
status_counts = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}
valid_status_codes = set(status_counts.keys())


def print_statistics():
    """Affiche la taille totale et les codes de statut."""
    print("File size: {}".format(total_file_size))
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))


if __name__ == "__main__":
    line_count = 0
    printed_at_end = False

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()

            if len(parts) >= 2:
                try:
                    # Le dernier élément est toujours la taille du fichier
                    file_size = int(parts[-1])
                    total_file_size += file_size
                except ValueError:
                    pass

                try:
                    # L'avant-dernier élément est le code de statut
                    status_code = int(parts[-2])
                    if status_code in valid_status_codes:
                        status_counts[status_code] += 1
                except ValueError:
                    pass

            # Affichage toutes les 10 lignes
            if line_count % 10 == 0:
                print_statistics()
                printed_at_end = True
            else:
                printed_at_end = False

        # Affichage final à la fin de la lecture du flux
        if not printed_at_end:
            print_statistics()

    except KeyboardInterrupt:
        # Gestion de l'interruption clavier (CTRL + C)
        print_statistics()
        raise
