# Sortie avec une valeur explicite, importation de sys

import sys

if len(sys.argv) != 2:
    sys.exit("Argument en ligne de commande manquant")
print(f"Bonjour, {sys.argv[1]}")
sys.exit(0)