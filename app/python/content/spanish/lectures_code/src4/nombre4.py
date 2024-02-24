# Demuestra rebanada de lista

import sys

if len(sys.argv) < 2:
    sys.exit("Argumentos insuficientes")

for arg in sys.argv[1:]:
    print("hola, mi nombre es", arg)