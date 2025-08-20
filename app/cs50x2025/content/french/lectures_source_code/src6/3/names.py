# Implémente une recherche linéaire pour les noms

import sys

# Une liste de noms
names = ["EMMA", "RODRIGO", "BRIAN", "DAVID"]

# Recherche d'EMMA
if "EMMA" in names:
    print("Trouvé")
    sys.exit(0)
print("Non trouvé")
sys.exit(1)