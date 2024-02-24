# Agrega detección de errores

import sys

if len(sys.argv) < 2:
    print("Demasiados pocos argumentos")
elif len(sys.argv) > 2:
    print("Demasiados argumentos")
else:
    print("Hola, mi nombre es", sys.argv[1])