# Imprime un caracter de cadena tras caracter

from cs50 import get_string

s = get_string("Input: ")
print("Output: ", end="")
for c in s:
    print(c, end="")
print()