# Conditions et opérateurs relationnels

from cs50 import get_int

# Invite l'utilisateur à entrer x
x = get_int("x: ")

# Invite l'utilisateur à entrer y
y = get_int("y: ")

# Comparaison de x et y
if x < y:
    print("x est inférieur à y")
elif x > y:
    print("x est supérieur à y")
else:
    print("x est égal à y")