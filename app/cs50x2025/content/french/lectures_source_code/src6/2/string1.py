# Affiche le caractère de la chaîne caractère par caractère

from cs50 import get_string

s = get_string("Entrée : ")
print("Sortie : ", end="")
pour c dans s :
    print(c, end="")
print()