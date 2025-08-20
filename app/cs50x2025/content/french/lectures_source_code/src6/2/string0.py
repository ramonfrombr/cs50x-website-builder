# Affiche une chaîne caractère par caractère, en indexant la chaîne

from cs50 import get_string

s = get_string("Entrée :  ")
print("Sortie : ", end="")
for i in range(len(s)):
    print(s[i], end="")
print()