# Opérateurs logiques

de cs50 importer get_string

# Inviter l'utilisateur à accepter
s = get_string("Acceptez-vous ?\n")

# Vérifier s'il accepte
si s == "O" ou s == "o":
    imprimer("Accepté.")
sinon si s == "N" ou s == "n":
    imprimer("Non accepté.")