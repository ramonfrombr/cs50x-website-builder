# Implementa una agenda telefónica

import sys

personas = {
    "EMMA": "617-555-0100",
    "RODRIGO": "617-555-0101",
    "BRIAN": "617-555-0102",
    "DAVID": "617-555-0103"
}

# Buscar a EMMA
if "EMMA" in personas:
    print(f"Encontrado {personas['EMMA']}")
    sys.exit(0)
print("No encontrado")
sys.exit(1)