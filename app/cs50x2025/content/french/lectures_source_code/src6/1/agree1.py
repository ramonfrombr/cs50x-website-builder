# Opérateurs logiques, avec des listes

from cs50 import get_string

# Demander à l'utilisateur d'être d'accord
s = get_string("Etes-vous d'accord ?\n")

# Vérifier si l'utilsateur est d'accord
if s.lower() in ["y", "yes"]:
    print("D'accord.")
elif s.lower() in ["n", "no"]:
    print("Pas d'accord.")