# Se termine par une valeur explicite, importation d'argv et sortie

from sys import argv, exit

if len(argv) != 2:
    print("argument de ligne de commande manquant")
    exit(1)
print(f"bonjour, {argv[1]}")
exit(0)