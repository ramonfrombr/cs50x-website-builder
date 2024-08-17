# Met une majuscule à la première lettre d’une copie d’une chaîne de caractères

from cs50 import get_string

# Obtenir une chaîne de caractères
s = get_string("s: ")

# Copier la chaîne de caractères
t = s

# Mettre une majuscule à la première lettre de la copie
t = t.capitalize()

# Afficher les chaînes de caractères
print(f"s: {s}")
print(f"t: {t}")