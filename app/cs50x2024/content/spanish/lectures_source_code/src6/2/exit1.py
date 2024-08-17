# Sale con un valor explícito, importando sys

import sys

if len(sys.argv) != 2:
    sys.exit("argumento de línea de comandos faltante")
print(f"hola, {sys.argv[1]}")
sys.exit(0)