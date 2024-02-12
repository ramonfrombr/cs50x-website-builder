# Demuestra IndexError

import sys

try:
    print("Hola, mi nombre es", sys.argv[1])
except IndexError:
    print("Argumentos insuficientes")