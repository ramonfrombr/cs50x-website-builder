# Implémente un répertoire téléphonique

import sys

personnes = {
    "EMMA": "617-555-0100",
    "RODRIGO": "617-555-0101",
    "BRIAN": "617-555-0102",
    "DAVID": "617-555-0103"
}

# Chercher EMMA
if "EMMA" in personnes:
    print(f"Trouvé {personnes['EMMA']}")
    sys.exit(0)
print("Pas trouvé")
sys.exit(1)