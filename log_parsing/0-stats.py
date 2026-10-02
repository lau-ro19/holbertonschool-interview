#!/usr/bin/python3
"""
Log parsing module that reads stdin line by line and computes metrics:
- Total file size
- Number of lines by status code (200, 301, 400, 401, 403, 404, 405, 500)
Prints statistics every 10 lines and upon keyboard interruption.
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
    """Affiche la taille totale et le nombre d'occurrences par code de statut."""
    print("File size: {}".format(total_file_size))
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))


if __name__ == "__main__":
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()

            # Vérification basique du format (au moins 7 éléments)
            if len(parts) >= 7:
                try:
                    file_size = int(parts[-1])
                    status_code = int(parts[-2])

                    total_file_size += file_size

                    if status_code in valid_status_codes:
                        status_counts[status_code] += 1
                except ValueError:
                    # Ignore les lignes où le statut ou la taille ne sont pas des entiers
                    pass

            # Affichage toutes les 10 lignes
            if line_count % 10 == 0:
                print_statistics()

    except KeyboardInterrupt:
        # Gestion de l'interruption clavier (CTRL + C)
        print_statistics()
        raise
