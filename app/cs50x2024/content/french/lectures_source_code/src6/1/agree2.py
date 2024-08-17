# Opérateurs logiques, utilisant des expressions régulières

import re
from cs50 import get_string

# Invite l'utilisateur à répondre
s = get_string("Es-tu d'accord ?\n")

# Vérifier si d'accord
if re.search("^y(es)?$", s, re.IGNORECASE):
    print("D'accord.")
elif re.search("^no?$", s, re.IGNORECASE):
    print("Pas d'accord.")