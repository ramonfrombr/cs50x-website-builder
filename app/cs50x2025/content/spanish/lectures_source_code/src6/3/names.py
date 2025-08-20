# Implementa la búsqueda lineal de nombres

import sys

# Una lista de nombres
names = ["EMMA", "RODRIGO", "BRIAN", "DAVID"]

# Busca el nombre EMMA
if "EMMA" in names:
    print("Found")
    sys.exit(0)
print("Not found")
sys.exit(1)