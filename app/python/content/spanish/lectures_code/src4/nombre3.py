# Demuestra sys.exit

import sys

if len(sys.argv) < 2:
    sys.exit("Muy pocos argumentos")
elif len(sys.argv) > 2:
    sys.exit("Demasiados argumentos")

print("hola, mi nombre es", sys.argv[1])